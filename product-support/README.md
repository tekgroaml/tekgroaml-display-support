# Product FAQ directory

**English** | [简体中文](README.zh-CN.md)

Updated / 更新：2026-11-08。

Find an item by size, advertised resolution and touch capability. Each product has separate English and Chinese pages; English is the default. The 6.2-inch product uses 360×960 visible pixels; 420×960 is its HDMI input, not its customer lookup resolution. Unknown touch status is explicitly marked.

Choose your screen below, then find the symptom that matches what you see. Each FAQ gives steps to try first and keeps technical explanations at the end. Products are sorted by screen size.

## Before changing settings

- **Black or flickering after moving a cable?** Leave it still and wait about 10–15 seconds. If it does not recover, unplug and firmly reconnect HDMI and USB power; try another cable if movement keeps causing it.
- **No touch, or touch on another screen?** For a touch model, plug its USB power/touch data cable into the **same computer that sends the picture**, not just a charger. Check each screen's HDMI and USB as a pair. A charging-only cable cannot carry touch.
- **Using Windows?** Start with the [Windows picture and touch steps](../platforms/windows/README.md). The Raspberry Pi commands in this repository do not run on Windows.

**Product options:** the current dual-screen kits are non-touch. The 2.1-inch and 2.8-inch single-screen ranges include touch models. The 2.1-inch resolution and model-specific test results have not been recorded; an available touch option is not a completed touch test. The older 2.8-inch black-screen pair has not been matched to a confirmed touch/non-touch SKU.

| Product | What you may see |
| --- | --- |
| [2.1-inch single-screen touch model (resolution pending)](2.1inch-resolution-unconfirmed-touch/README.md) | Touch model available; check USB data and screen assignment first. |
| [2.1-inch dual-screen, 480×480 each, non-touch](2.1inch-480x480-dual-nontouch/README.md) | Check connections and same/different-content layout; tapping does nothing. |
| [2.8-inch single-screen touch model (resolution pending)](2.8inch-resolution-unconfirmed-touch/README.md) | Touch model available; check USB data and screen assignment first. |
| [2.8-inch dual-screen, 480×480 each, non-touch](2.8inch-480x480-dual-nontouch/README.md) | Check connections and same/different-content layout; tapping does nothing. |
| [2.8-inch 480×480 historical test pair (exact variant pending)](2.8inch-480x480-touch-unconfirmed/README.md) | Black screen; “Remote I/O error”; touch option needs checking. |
| [3.4-inch 800×800 touchscreen](3.4inch-800x800-touch/README.md) | No picture after swapping screens; wrong image; touch reaches another display. |
| [4.0-inch 720×720 touchscreen](4.0inch-720x720-touch/README.md) | Black screen or flicker; touch missing or on the wrong display. |
| [6.2-inch 360×960 cut-panel touchscreen](6.2inch-360x960-touch/README.md) | Left-side content missing; left touches offset; picture flickers. |
| [6.2-inch 360×960 cut panel, non-touch](6.2inch-360x960-nontouch/README.md) | Brightness pulses; image cropped; finger taps have no response. |

## Dual-screen uses and picture distribution

**For these one-HDMI kits, same content repeats the full picture on both panels; different content uses a left/right picture prepared by the app, with one part on each panel.** Copying suits repeated information and symmetry; splitting suits instruments and primary/secondary dashboards. “Mirroring” here preserves reading orientation rather than reversing text.

[Round/square use cases, board-flow diagrams and demo entrypoints](_shared/dual-screen/README.md). One HDMI kit may correctly appear as one monitor. Hardware-copy single-picture input and SBS double-width input are not interchangeable.

## Non-touch dual-screen records with size unconfirmed

[Choose shape and same/different content](_unconfirmed/README.md): round SBS, square SBS, round hardware-copy and square hardware-copy kits. Added issues cover one dark panel, demos stopping after a swap, mixing 480×480 and 960×480 inputs, and apps rejecting observed ~62.811/~71.295Hz rates.

These are provisional connection records, not identified new SKUs. They stay outside the inch-sorted table and are not assigned to the 2.8-inch product. Windows and Pi steps are separate. Refresh compatibility changed app acceptance only, not screen timings.

## Non-touch dual-screen kit list

Sizes are still being matched to the kits; all four configurations below are non-touch.

| Kit | FAQ |
| --- | --- |
| Round dual-screen / same content / non-touch | [FAQ](_unconfirmed/480x480-round-dual-clone-nontouch/README.md) |
| Round dual-screen / different content / non-touch | [FAQ](_unconfirmed/480x480-round-dual-sbs-nontouch/README.md) |
| Square dual-screen / same content / non-touch | [FAQ](_unconfirmed/480x480-square-dual-clone-nontouch/README.md) |
| Square dual-screen / different content / non-touch | [FAQ](_unconfirmed/480x480-square-dual-sbs-nontouch/README.md) |

## Three issue categories

1. No picture / flicker: a known EDID or timing fix applies only to matched samples; power, cable and DDC faults need separate checks.
2. Touch missing / wrong display / offset: verify USB data, fixed cable pairing, unique input names and coordinate mapping.
3. Cut panels: distinguish input resolution from the visible window and pair display compensation with touch compensation.

[Shared procedures and all tested scenarios](_shared/README.md) · [Naming policy](NAMING.md) · [New product template](DEVICE-TEMPLATE.md)

## Historical entries

`6.2inch-420x960-touch` and `6.2inch-420x960-nontouch` retain old links and direct readers to the new 360×960 pages. They are not extra products. The historical repair profile ID remains unchanged and does not implement cut-window compensation.

[Archived 2026-10-24 720 setup package](4inch-720x720-RaspberryPi-support-20261024/raspberry-pi-720-touchscreen-setup/QUICK_START_EN.md) is for legacy support; do not enable it alongside the modern tool. Earlier 480×480 screens with unconfirmed size are not invented as additional SKUs; the initial 5.08-inch claim was corrected to 4.0 inches.

[Support home](../README.md)
