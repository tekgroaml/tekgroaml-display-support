#!/usr/bin/env python3
"""Build the English-only buyer FAQ from repository Markdown. Needs reportlab.

Usage: python3 scripts/build-faq-pdf.py --font /path/to/CJK-font.ttf
Use a font licensed for PDF embedding; font files are not distributed here.
"""
import argparse
from datetime import date
from html import escape
from pathlib import Path
import re
import subprocess
from urllib.parse import quote

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                               Spacer, Table, TableStyle, PageBreak)
from reportlab.platypus.tableofcontents import TableOfContents

ROOT = Path(__file__).resolve().parents[1]
HOME = 'https://github.com/tekgroaml/tekgroaml-display-support'
PRODUCTS = [
 '2.1inch-480x480-touch', '2.1inch-480x480-dual-nontouch',
 '2.8inch-480x480-touch', '2.8inch-480x480-dual-nontouch',
 '2.8inch-480x480-touch-unconfirmed', '3.4inch-800x800-touch',
 '4.0inch-720x720-touch', '6.2inch-360x960-touch', '6.2inch-360x960-nontouch']


def online(path, target=''):
    if target.startswith(('https://', 'http://', 'mailto:')):
        return target
    relative, _, anchor = target.partition('#')
    dest = ((path.parent / relative).resolve() if relative else path.resolve())
    suffix = quote(dest.relative_to(ROOT).as_posix(), safe='/')
    return HOME + '/blob/main/' + suffix + ('#' + quote(anchor) if anchor else '')


def inline(text, path):
    text = text.replace('–', '-').replace('—', '-').replace('\u2011', '-')
    pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)|\*\*([^*]+)\*\*|`([^`]+)`')
    chunks = []
    last = 0
    for m in pattern.finditer(text):
        chunks.append(escape(text[last:m.start()]))
        if m[1] is not None:
            chunks.append(f'<a href="{escape(online(path,m[2]),quote=True)}" color="#126D8C">{escape(m[1])}</a>')
        elif m[3] is not None:
            chunks.append('<b>'+escape(m[3])+'</b>')
        else:
            chunks.append(escape(m[4]))
        last = m.end()
    chunks.append(escape(text[last:]))
    return ''.join(chunks)


def buyer_text(path):
    """Exclude maintainer policy and heavy technical records, retain buyer/Pi steps."""
    text = path.read_text()
    for marker in ('## Technical details and test records', '## 详细原因、产品参数与测试记录',
                   '## Product data, explanation and validation', '## 产品数据、原理与验证',
                   '## For AI contributors', '## 给维护文档的AI',
                   '## How does the driver board process one picture?', '## 驱动板如何处理一张图？'):
        text = text.split(marker)[0]
    if path.parent == ROOT:
        text = '\n'.join(line for line in text.splitlines()
                         if not any(x in line for x in ('Maintainers:', '维护者：', 'Seller support materials', '卖家支持资料', 'Publishing notes', '发布说明')))
    # The English export keeps online Chinese pages but removes language-switch links.
    text = re.sub(r'\|\s*\[中文\]\([^)]+\)\s*(?=\||$)', '', text, flags=re.M)
    text = text.replace('| Product | English FAQ | 中文FAQ |', '| Product | English FAQ |')
    text = re.sub(r'^\| --- \| --- \| --- \|$', '| --- | --- |', text, flags=re.M) if path.parent == ROOT else text
    # Do not include large technical diagrams or formulas ahead of buyer guidance.
    text = re.sub(r'```mermaid.*?```', '', text, flags=re.S)
    return text


class FAQDoc(BaseDocTemplate):
    def afterFlowable(self, flowable):
        if hasattr(flowable, 'section_key'):
            key = flowable.section_key
            self.canv.bookmarkPage(key)
            title = flowable.getPlainText()
            self.canv.addOutlineEntry(title, key, level=0)
            self.notify('TOCEntry', (0, title, self.page, key))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--font', required=True, type=Path)
    parser.add_argument('--output', type=Path, default=ROOT/'output/pdf/tekgroaml-display-support-faq.pdf')
    parser.add_argument('--date', default=date.today().isoformat())
    args = parser.parse_args()
    pdfmetrics.registerFont(TTFont('FAQ', str(args.font)))
    pdfmetrics.registerFontFamily('FAQ', normal='FAQ', bold='FAQ', italic='FAQ', boldItalic='FAQ')
    W = 174*mm
    styles = {
      'body': ParagraphStyle('Body', fontName='FAQ', fontSize=9.1, leading=14, spaceAfter=5,
                             textColor=colors.HexColor('#263D49'), wordWrap='CJK'),
      'small': ParagraphStyle('Small', fontName='FAQ', fontSize=7.7, leading=11.5, spaceAfter=4,wordWrap='CJK'),
      'h1': ParagraphStyle('Section',fontName='FAQ',fontSize=19,leading=25,spaceAfter=10,textColor=colors.HexColor('#12374D'),keepWithNext=True,wordWrap='CJK'),
      'h2': ParagraphStyle('Question',fontName='FAQ',fontSize=12.2,leading=18,spaceBefore=10,spaceAfter=5,textColor=colors.HexColor('#126D8C'),keepWithNext=True,wordWrap='CJK'),
      'h3': ParagraphStyle('Sub',fontName='FAQ',fontSize=10,leading=15,spaceBefore=6,spaceAfter=4,keepWithNext=True,wordWrap='CJK'),
      'code': ParagraphStyle('Code',fontName='FAQ',fontSize=7.8,leading=11,backColor=colors.HexColor('#F0F5F7'),borderPadding=6,spaceBefore=4,spaceAfter=8,wordWrap='CJK'),
      'title': ParagraphStyle('Cover',fontName='FAQ',fontSize=28,leading=36,spaceAfter=12,textColor=colors.HexColor('#12374D'),wordWrap='CJK'),
    }
    def para(t, style='body'): return Paragraph(t, styles[style])
    def markdown(path, section_key):
        text=buyer_text(path)
        lines=text.splitlines(); out=[]; i=0
        while i<len(lines):
            line=lines[i].strip()
            if not line or line in ('<details>','</details>') or line.startswith('<summary>'):
                i+=1;continue
            if line.startswith('**English** |') or line.startswith('[English]('):
                i+=1;continue
            if line.startswith('```'):
                block=[];i+=1
                while i<len(lines) and not lines[i].strip().startswith('```'):
                    block.append(lines[i]);i+=1
                # Keep literal command lines distinct and wrap long examples visibly.
                out.append(para('<br/>'.join(escape(x) for x in block),'code'));i+=1;continue
            if line.startswith('|'):
                rows=[]
                while i<len(lines) and lines[i].strip().startswith('|'):
                    cells=[x.strip() for x in lines[i].strip().strip('|').split('|')]
                    if not all(re.fullmatch(r'[:\- ]+',x or '-') for x in cells):rows.append(cells)
                    i+=1
                if rows:
                    n=max(map(len,rows));data=[]
                    for row in rows:
                        row += ['']*(n-len(row))
                        data.append([para(inline(c,path),'small') for c in row])
                    widths=([W*.45,W*.275,W*.275] if n==3 else [W*.35,W*.65] if n==2 else [W/n]*n)
                    tab=Table(data,colWidths=widths,repeatRows=1,hAlign='LEFT')
                    tab.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#DEEDF2')),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F7FAFB')]),('GRID',(0,0),(-1,-1),.35,colors.HexColor('#C6D8E0')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]))
                    out.extend([tab,Spacer(1,7)])
                continue
            h=re.match(r'^(#{1,5})\s+(.+)',line)
            if h:
                level=len(h[1]);obj=para(inline(h[2],path),'h1' if level==1 else 'h2' if level==2 else 'h3')
                if level==1:obj.section_key=section_key
                out.append(obj);i+=1;continue
            if line.startswith(('- ', '> ')) or re.match(r'^\d+\. ',line):
                prefix='• ' if line.startswith('- ') else ''
                content=line[2:] if line.startswith(('- ','> ')) else line
                out.append(para(prefix+inline(content,path)));i+=1;continue
            block=[line];i+=1
            while i<len(lines) and lines[i].strip() and not re.match(r'^(#|\||```|<|[-]>? |>|\d+\. )',lines[i].strip()):
                block.append(lines[i].strip());i+=1
            out.append(para(inline(' '.join(block),path)))
        return out
    args.output.parent.mkdir(parents=True,exist_ok=True)
    try: rev=subprocess.check_output(['git','rev-parse','--short','HEAD'],cwd=ROOT,text=True).strip()
    except subprocess.SubprocessError:rev='unknown'
    def footer(c,d):
        c.saveState();c.setStrokeColor(colors.HexColor('#CBDDE4'));c.line(18*mm,14*mm,192*mm,14*mm)
        c.setFont('FAQ',7);c.setFillColor(colors.HexColor('#55717F'))
        c.drawString(18*mm,9*mm,'TEKGROAML • Buyer FAQ')
        c.drawRightString(192*mm,9*mm,str(d.page))
        c.linkURL(HOME,(18*mm,6*mm,112*mm,13*mm),relative=0);c.restoreState()
    doc=FAQDoc(str(args.output),pagesize=A4,leftMargin=18*mm,rightMargin=18*mm,topMargin=17*mm,bottomMargin=19*mm,title='TEKGROAML Display Support - Complete Buyer FAQ',author='TEKGROAML')
    doc.addPageTemplates(PageTemplate(id='normal',frames=Frame(doc.leftMargin,doc.bottomMargin,doc.width,doc.height,id='content',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0),onPage=footer))
    story=[Spacer(1,20*mm),para('TEKGROAML<br/>Display Support','title'),
           para('Complete Buyer FAQ','h1'),para('English edition','h2'),Spacer(1,8*mm),
           para('Latest guides','h2'),para(f'<a href="{HOME}" color="#126D8C">{HOME}</a>'),
           para('Click the address above to visit our GitHub home page.'),Spacer(1,7*mm),
           para('Connection checks • Windows • Product FAQs • Dual-screen demos'),Spacer(1,10*mm),
           para(f'Document date: {escape(args.date)}<br/>Source snapshot: {escape(rev)}','small'),
           para('This English buyer edition collects the home-page introduction, Windows guide, and product troubleshooting steps. Detailed experiment records and evidence remain linked online. No new hardware testing is implied.','small'),
           PageBreak(),para('Contents','h1')]
    toc=TableOfContents();toc.levelStyles=[ParagraphStyle('TOC',fontName='FAQ',fontSize=9.3,leading=14,spaceBefore=3,wordWrap='CJK')];story.extend([toc,PageBreak()])
    for lang in ('en',):
        name='README.md' if lang=='en' else 'README.zh-CN.md'
        paths=[ROOT/name,ROOT/'platforms/windows'/name]
        paths += [ROOT/'product-support'/p/name for p in PRODUCTS]
        paths += [ROOT/'product-support/_shared/dual-screen'/name]
        for index,path in enumerate(paths):
            story.extend(markdown(path,f'{lang}-{index}'))
            story.append(para(f'<a href="{online(path)}" color="#126D8C">'+('Open the current online page' if lang=='en' else '打开此页的最新在线文档')+'</a>','small'))
            story.append(PageBreak())
    story.pop()
    doc.multiBuild(story)
    print(args.output)

if __name__=='__main__':main()
