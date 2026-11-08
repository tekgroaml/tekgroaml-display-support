# Export the complete buyer FAQ as PDF

The buyer download is [output/pdf/tekgroaml-display-support-faq.pdf](../output/pdf/tekgroaml-display-support-faq.pdf). It contains English followed by Chinese, with a linked contents page, PDF bookmarks, current online-page links and the GitHub home address near the beginning.

The PDF is a buyer edition of the home-page introduction, Windows guide, size-sorted product FAQs and dual-screen use cases. Heavy technical records and diagrams remain online through links; it is not a byte-for-byte archive of all repository files.

## Rebuild

Requires Python 3, `reportlab` and a TrueType font with English/Chinese coverage that permits PDF embedding. The font file is supplied locally; it is not bundled in this repository.

```bash
python3 -m pip install reportlab
python3 scripts/build-faq-pdf.py --font /path/to/cjk-font.ttf --date YYYY-MM-DD
```

The path and date are placeholders. Replace the font path with a real file and the date with the actual edition date. Run from the repository root. Output defaults to the stable buyer download path; use `--output` for a different file. The source Git commit is printed on the cover so readers can identify the snapshot.

## Review before publishing

1. Rebuild after changes to the included Markdown pages. Check English and Chinese sections, the visible GitHub URL and its clickable PDF annotation.
2. Render all pages with Poppler and inspect them for cropped text, missing glyphs, broken tables, blank pages and incorrect page breaks.
3. Check the table of contents, PDF bookmarks and links; verify code lines remain legible.
4. Commit the exporter and generated PDF together when publishing a new edition. Do not commit temporary previews or local font files.

PDF generation does not test hardware. Keep unresolved issues and sample-only/app-only limitations intact.

## 中文维护说明

买家总册为一份双语PDF，英文在前、中文在后。首页说明、Windows指南、按尺寸排列的产品FAQ及双屏场景由仓库Markdown生成；技术记录及图解通过在线链接保留，不是仓库全部文件的逐字归档。

更新内容后使用上面的脚本重新生成，传入允许嵌入且覆盖中英文的本机字体及本次实际日期。检查全部页面、目录书签和封面的GitHub链接，再提交脚本与PDF；临时截图、字体文件不入库。生成PDF不等于完成新的实物测试。
