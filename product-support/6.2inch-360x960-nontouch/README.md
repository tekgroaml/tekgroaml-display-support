# 6.2-inch 360×960 cut panel, non-touch

**English** | [简体中文](README.zh-CN.md)

## Product information

| Field | Recorded information |
| --- | --- |
| Customer lookup name | 6.2-inch 360×960 cut panel, non-touch |
| Form and connections | Non-touch counterpart described as the same 6.2-inch screen. Visible-window geometry has not been measured on this sample. |
| Validation status | Brightness pulsing unresolved; touch-sample compensation not validated here. |
| Environment | Raspberry Pi 4B; Raspberry Pi OS Bookworm Desktop 64-bit; labwc/Wayland |
| SKU / ASIN / panel part number / PCB revision | Not established; match the actual item before using a repair |

## Recorded driver data

This sample reported the same LTM / ZL480 EDID family as the touch strip: 256 bytes, `328d5e04`, 420×960 at 28MHz / approximately 51.85Hz. A second DTD reported 480×480 at 18.72MHz. Matching EDID alone cannot distinguish the touch and non-touch products or confirm native glass dimensions. The 360×960 lookup follows the supplied product description; a separate ruler measurement on this unit is still required.

## 1. Brightness pulsing / no picture

The sample displayed a positionally stable image with brightness alternating light/dark. A 420×960, 32.4MHz, 60Hz test did not solve it. The screen was powered from a Pi USB port. No Pi undervoltage flag was reported, but that does not prove stable power at the screen connector. An independent supply/cable comparison was not completed.

There is **no validated repair profile for this non-touch sample**. Do not use the touch-only 6.2 profile merely because EDID matches. Check the rated screen supply, substitute a known-good cable/supply, test one screen at a time, and compare with a known-good host. If EDID/DDC fails, repair that connection before automatic mode selection. See [shared display checks](../_shared/README.md#1-no-picture-flicker-or-an-edid-read-error).

## 2. Touch response

Not applicable: this product has no touch input. A different screen's finger input must not reach this output. This mixed touch/non-touch case was corrected by mapping the single touch controller only to its own output, after which the customer confirmed correct position. Do not blindly deploy a two-touch mapping when only one controller exists. Display-only tests such as `screen-test pattern --screen 2` work without touch hardware.

## 3. Cut-panel window

The x=60, width=360 compensation was confirmed on the touch sample only. The non-touch sample needs its own ruler/photo and border checks before applying that geometry. The missing touch layer does not prove identical panel firmware or scan alignment. No complete-image or 60Hz cure is claimed here.

[Product index](../README.md) · [All scenarios](../_shared/README.md)
