# Product FAQ directory

**English** | [简体中文](README.zh-CN.md)

Updated / 更新：2026-11-08。

Find an item by size, advertised resolution and touch capability. Each product has separate English and Chinese pages; English is the default. The 6.2-inch product uses 360×960 visible pixels; 420×960 is its HDMI input, not its customer lookup resolution. Unknown touch status is explicitly marked.

| Product | Recorded status |
| --- | --- |
| [2.8-inch 480×480, touch status unconfirmed](2.8inch-480x480-touch-unconfirmed/README.md) | Both reported black; one EDID readable, the other failed DDC reads. Unresolved. |
| [3.4-inch 800×800 touchscreen](3.4inch-800x800-touch/README.md) | 800×800 at 60Hz visually confirmed stable; exact timing dump not retained. |
| [4.0-inch 720×720 touchscreen](4.0inch-720x720-touch/README.md) | Timing fix and touch verified on the sample. |
| [6.2-inch 360×960 cut-panel touchscreen](6.2inch-360x960-touch/README.md) | Visible-window and touch compensation confirmed in a temporary application. |
| [6.2-inch 360×960 cut panel, non-touch](6.2inch-360x960-nontouch/README.md) | Brightness pulsing unresolved; touch-sample compensation not validated here. |

## Three issue categories

1. No picture / flicker: a known EDID or timing fix applies only to matched samples; power, cable and DDC faults need separate checks.
2. Touch missing / wrong display / offset: verify USB data, fixed cable pairing, unique input names and coordinate mapping.
3. Cut panels: distinguish input resolution from the visible window and pair display compensation with touch compensation.

[Shared procedures and all tested scenarios](_shared/README.md) · [Naming policy](NAMING.md) · [New product template](DEVICE-TEMPLATE.md)

## Historical entries

`6.2inch-420x960-touch` and `6.2inch-420x960-nontouch` retain old links and direct readers to the new 360×960 pages. They are not extra products. The historical repair profile ID remains unchanged and does not implement cut-window compensation.

[Archived 2026-10-24 720 setup package](4inch-720x720-RaspberryPi-support-20261024/raspberry-pi-720-touchscreen-setup/QUICK_START_EN.md) is for legacy support; do not enable it alongside the modern tool. Earlier 480×480 screens with unconfirmed size are not invented as additional SKUs; the initial 5.08-inch claim was corrected to 4.0 inches.

[Support home](../README.md)
