# TEKGROAML Display Support

**English** | [简体中文](README.zh-CN.md)

**Download the complete bilingual FAQ:** [PDF - English first, Chinese follows](output/pdf/tekgroaml-display-support-faq.pdf). Includes the home-page introduction, Windows checks, product FAQs and dual-screen examples, with a clickable GitHub home link on the cover.

Find your screen by **size – resolution – touch capability** in the [product FAQ directory](product-support/README.md). Each current product has a separate English FAQ and Chinese FAQ with reciprocal language links. Updated 2026-11-08.

Start with the symptom you can observe: **no picture or flicker**, **touch missing or inaccurate**, or **part of the image missing**. Open your product below for steps to try. Technical data is available at the end of each FAQ.

## Before changing settings

- **Black or flickering after moving a cable?** Leave it still and wait about 10–15 seconds. If it does not recover, unplug and firmly reconnect HDMI and USB power; try another cable if movement keeps causing it.
- **No touch, or touch on another screen?** For a touch model, plug its USB power/touch data cable into the **same computer that sends the picture**, not just a charger. Check each screen's HDMI and USB as a pair. A charging-only cable cannot carry touch.
- **Using Windows?** Start with the [Windows picture and touch steps](platforms/windows/README.md). The Raspberry Pi commands in this repository do not run on Windows.

**Product options:** the current dual-screen kits are non-touch. The 2.1-inch and 2.8-inch single-screen ranges include touch models. Both single-screen touch models are confirmed 480×480; model-specific acceptance is still pending. The older 2.8-inch black-screen pair has not been matched to a confirmed touch/non-touch SKU.

| Product | English FAQ | 中文FAQ |
| --- | --- | --- |
| 2.1-inch 480×480 single-screen touchscreen | [English](product-support/2.1inch-480x480-touch/README.md) | [中文](product-support/2.1inch-480x480-touch/README.zh-CN.md) |
| 2.1-inch dual-screen, 480×480 each, non-touch | [English](product-support/2.1inch-480x480-dual-nontouch/README.md) | [中文](product-support/2.1inch-480x480-dual-nontouch/README.zh-CN.md) |
| 2.8-inch 480×480 single-screen touchscreen | [English](product-support/2.8inch-480x480-touch/README.md) | [中文](product-support/2.8inch-480x480-touch/README.zh-CN.md) |
| 2.8-inch dual-screen, 480×480 each, non-touch | [English](product-support/2.8inch-480x480-dual-nontouch/README.md) | [中文](product-support/2.8inch-480x480-dual-nontouch/README.zh-CN.md) |
| 2.8-inch 480×480 historical test pair (exact variant pending) | [English](product-support/2.8inch-480x480-touch-unconfirmed/README.md) | [中文](product-support/2.8inch-480x480-touch-unconfirmed/README.zh-CN.md) |
| 3.4-inch 800×800 touchscreen | [English](product-support/3.4inch-800x800-touch/README.md) | [中文](product-support/3.4inch-800x800-touch/README.zh-CN.md) |
| 4.0-inch 720×720 touchscreen | [English](product-support/4.0inch-720x720-touch/README.md) | [中文](product-support/4.0inch-720x720-touch/README.zh-CN.md) |
| 6.2-inch 360×960 cut-panel touchscreen | [English](product-support/6.2inch-360x960-touch/README.md) | [中文](product-support/6.2inch-360x960-touch/README.zh-CN.md) |
| 6.2-inch 360×960 cut panel, non-touch | [English](product-support/6.2inch-360x960-nontouch/README.md) | [中文](product-support/6.2inch-360x960-nontouch/README.zh-CN.md) |

## Dual-screen uses and picture distribution

**For these one-HDMI kits, same content repeats the full picture on both panels; different content uses a left/right picture prepared by the app, with one part on each panel.** Copying suits repeated information and symmetry; splitting suits instruments and primary/secondary dashboards. “Mirroring” here preserves reading orientation rather than reversing text.

[Round/square use cases, board-flow diagrams and demo entrypoints](product-support/_shared/dual-screen/README.md). One HDMI kit may correctly appear as one monitor. Hardware-copy single-picture input and SBS double-width input are not interchangeable.

## Non-touch dual-screen records with size unconfirmed

[Choose shape and same/different content](product-support/_unconfirmed/README.md): round SBS, square SBS, round hardware-copy and square hardware-copy kits. Added issues cover one dark panel, demos stopping after a swap, mixing 480×480 and 960×480 inputs, and apps rejecting observed ~62.811/~71.295Hz rates.

These are provisional connection records, not identified new SKUs. They stay outside the inch-sorted table and are not assigned to the 2.8-inch product. Windows and Pi steps are separate. Refresh compatibility changed app acceptance only, not screen timings.

## Non-touch dual-screen kit list

Sizes are still being matched to the kits; all four configurations below are non-touch.

| Kit | FAQ |
| --- | --- |
| Round dual-screen / same content / non-touch | [English](product-support/_unconfirmed/480x480-round-dual-clone-nontouch/README.md) | [中文](product-support/_unconfirmed/480x480-round-dual-clone-nontouch/README.zh-CN.md) |
| Round dual-screen / different content / non-touch | [English](product-support/_unconfirmed/480x480-round-dual-sbs-nontouch/README.md) | [中文](product-support/_unconfirmed/480x480-round-dual-sbs-nontouch/README.zh-CN.md) |
| Square dual-screen / same content / non-touch | [English](product-support/_unconfirmed/480x480-square-dual-clone-nontouch/README.md) | [中文](product-support/_unconfirmed/480x480-square-dual-clone-nontouch/README.zh-CN.md) |
| Square dual-screen / different content / non-touch | [English](product-support/_unconfirmed/480x480-square-dual-sbs-nontouch/README.md) | [中文](product-support/_unconfirmed/480x480-square-dual-sbs-nontouch/README.zh-CN.md) |

## Prefer to let AI help?

If you use GPT or Claude, download this guide, the matching display tools and any demo you want to try. Then tell your AI what you want: **make a wish, and let AI help with the steps.** With access to the project files and your computer or Raspberry Pi, a capable AI assistant can help inspect settings, run tests and set up a supported demo.

- [Product guides and FAQs](https://github.com/tekgroaml/tekgroaml-display-support)
- [Display configuration and test tools](https://github.com/tekgroaml/tekgroaml-pi-display-tools)
- [Round-screen Home Assistant kiosk demo](https://github.com/tekgroaml/round-screen-homeassistant-kiosk)

For example, tell it:

> Please read these repositories first. I have a [size/resolution/touch option] screen connected to [Windows / Raspberry Pi]. I want to [fix the picture / test touch / run a demo]. Check the connections and supported options first, then help me step by step. Keep a way to restore settings when making changes.

Tell the AI your screen model, how HDMI and USB are connected, and what you see. If it can only chat, it can guide you through the steps; running commands requires a tool-enabled assistant with access you grant. Physical connection or hardware faults may still need hands-on checks or our support. Raspberry Pi scripts are not Windows programs.

The product pages cover no picture/flicker, touch issues and cut-panel compensation, including verified results and unresolved cases. EDID input modes are separated from physical visible resolution. Unknown specifications are marked rather than inferred from controller names.

- [Shared procedures and all tested scenarios](product-support/_shared/README.md)
- [General touchscreen customer FAQ](touchscreen/customer/Touchscreen-Customer-FAQ-EN.md)
- [Seller support materials](touchscreen/README.md)
- [Display tools and installation](https://github.com/tekgroaml/tekgroaml-pi-display-tools)
- [Publishing notes](PUBLISHING.md)

The cut-panel workaround is currently application-level; it does not claim whole-desktop or boot-time compensation. Historical product/package links are retained under the product directory. Documentation can be downloaded independently of the tools repository.

- [Maintainers: Writing requirements for buyer-facing FAQs](docs/WRITING-GUIDELINES.md)

## For AI contributors

Start with [AGENTS.md](AGENTS.md). Before editing FAQs, read the full [English writing requirements](docs/WRITING-GUIDELINES.md) or [Chinese writing requirements](docs/文档书写要求.md), and keep both buyer languages consistent. [CLAUDE.md](CLAUDE.md) provides a Claude Code entry to the same instructions. Automatic discovery depends on the AI tool; if it does not load repository instructions, ask it explicitly to read `AGENTS.md` first. An ordinary chat cannot read local files unless you provide them or grant tools access.
