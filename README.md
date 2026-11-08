# TEKGROAML Display Support

**English** | [简体中文](README.zh-CN.md)

Find your screen by **size – resolution – touch capability** in the [product FAQ directory](product-support/README.md). Each current product has a separate English FAQ and Chinese FAQ with reciprocal language links. Updated 2026-11-08.

Start with the symptom you can observe: **no picture or flicker**, **touch missing or inaccurate**, or **part of the image missing**. Open your product below for steps to try. Technical data is available at the end of each FAQ.

## Before changing settings

- **Black or flickering after moving a cable?** Leave it still and wait about 10–15 seconds. If it does not recover, unplug and firmly reconnect HDMI and USB power; try another cable if movement keeps causing it.
- **No touch, or touch on another screen?** For a touch model, plug its USB power/touch data cable into the **same computer that sends the picture**, not just a charger. Check each screen's HDMI and USB as a pair. A charging-only cable cannot carry touch.
- **Using Windows?** Start with the [Windows picture and touch steps](platforms/windows/README.md). The Raspberry Pi commands in this repository do not run on Windows.

| Product | English FAQ | 中文FAQ |
| --- | --- | --- |
| 2.8-inch 480×480, touch status unconfirmed | [English](product-support/2.8inch-480x480-touch-unconfirmed/README.md) | [中文](product-support/2.8inch-480x480-touch-unconfirmed/README.zh-CN.md) |
| 3.4-inch 800×800 touchscreen | [English](product-support/3.4inch-800x800-touch/README.md) | [中文](product-support/3.4inch-800x800-touch/README.zh-CN.md) |
| 4.0-inch 720×720 touchscreen | [English](product-support/4.0inch-720x720-touch/README.md) | [中文](product-support/4.0inch-720x720-touch/README.zh-CN.md) |
| 6.2-inch 360×960 cut-panel touchscreen | [English](product-support/6.2inch-360x960-touch/README.md) | [中文](product-support/6.2inch-360x960-touch/README.zh-CN.md) |
| 6.2-inch 360×960 cut panel, non-touch | [English](product-support/6.2inch-360x960-nontouch/README.md) | [中文](product-support/6.2inch-360x960-nontouch/README.zh-CN.md) |

The product pages cover no picture/flicker, touch issues and cut-panel compensation, including verified results and unresolved cases. EDID input modes are separated from physical visible resolution. Unknown specifications are marked rather than inferred from controller names.

- [Shared procedures and all tested scenarios](product-support/_shared/README.md)
- [General touchscreen customer FAQ](touchscreen/customer/Touchscreen-Customer-FAQ-EN.md)
- [Seller support materials](touchscreen/README.md)
- [Display tools and installation](https://github.com/tekgroaml/tekgroaml-pi-display-tools)
- [Publishing notes](PUBLISHING.md)

The cut-panel workaround is currently application-level; it does not claim whole-desktop or boot-time compensation. Historical product/package links are retained under the product directory. Documentation can be downloaded independently of the tools repository.

- [Maintainers: Writing requirements for buyer-facing FAQs](docs/WRITING-GUIDELINES.md)
