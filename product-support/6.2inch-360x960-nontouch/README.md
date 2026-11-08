# 6.2-inch 360×960 cut panel, non-touch

**English** | [简体中文](README.zh-CN.md)

Please check the size, resolution and touch option on your order. Start with the simple checks below; no commands are needed.

## The screen goes black or flickers after a cable is moved

- Leave the cables still and wait about 10–15 seconds for the picture to return.
- If it stays black, unplug and firmly reconnect HDMI and the USB power connection. Check both ends.
- Try another cable and test one screen at a time. Use the power supply specified for your screen.

If this happens every time a cable moves, try replacing that cable. If the screen never lights up, follow the same connection checks first.

## Tapping the screen does nothing

This is the non-touch version, so that is expected. If a second touchscreen controls this screen, check that the other screen's HDMI and USB cables go to the same computer, then set its touch screen in Windows as described below.

## What can I try in Windows?

Right-click the desktop and open **Display settings**. Select this screen, use its listed resolution and choose **Extend these displays** if you want separate screens. For flicker, open **Advanced display** and try 60Hz only if it is available for that screen.

[Windows steps with more detail](../../platforms/windows/README.md). The commands in the optional Raspberry Pi section below do **not** run on Windows.

## The screen keeps getting brighter and darker, or an edge is missing

Please send us a short video and your power connection details. The tested non-touch sample still had this issue after a 60Hz trial; we do not have a confirmed software fix for it. The touch version’s cut-screen workaround has not been confirmed for this version.

## Optional: Raspberry Pi instructions

<details>
<summary>Show Raspberry Pi commands (not for Windows)</summary>

Commands below run on the Raspberry Pi after installing the [display tools](https://github.com/tekgroaml/tekgroaml-pi-display-tools). Use version 2.3.2+ for rectangular touch tests. Examples select connector 1 (`HDMI-A-1`, board HDMI0); replace 1 with 2 for connector 2 (board HDMI1). Run screen tests as the desktop user, without sudo.

## Brightness repeatedly gets lighter and darker

**What you may see:** the picture stays in place, but the backlight or overall brightness pulses.

1. Test one screen with its rated supply. Compare a known-good power cable and suitable independent supply, following the product's power specification.
2. Check and compare the HDMI cable and a known-good host.
3. Display white and a grid so changes are easier to observe:

   ```bash
   screen-config list
   screen-test white --screen 1
   screen-test pattern --screen 1
   ```

If it persists, send support a short video, supply details and `screen-config list`. A 60Hz timing test did **not** solve this sample, so there is no verified profile to recommend. Do not apply the touch-model profile just because the screen name matches.

## The left edge is missing or the image is cropped

Use `screen-test pattern --screen 1` and photograph all four screen edges. The touch version required a special visible-area layout, but its exact offset has **not** been measured or confirmed for this non-touch version. Contact support to measure your sample before adopting that layout.

## Touch targets appear, but tapping does nothing

This is expected: the non-touch version has no touch input. Use color and geometry tests instead:

```bash
screen-test cycle --screen 1 --interval 5
screen-test pattern --screen 1
```

If another attached touchscreen controls this screen, follow the [mixed-screen pairing procedure](../_shared/README.md#2-touch-does-not-respond-or-reaches-the-wrong-position); map that touchscreen only to its own display.

## The picture disappears after reconnecting

```bash
screen-test stop
screen-test pattern --screen 1
```

If it remains black, check power, backlight and screen detection before trying timing changes. Report any `Remote I/O error` to support with the connection details.

</details>

## Technical details and test records

<details>
<summary>Show product data, repair details and validation limits</summary>

#### Product information

| Field | Recorded information |
| --- | --- |
| Customer lookup name | 6.2-inch 360×960 cut panel, non-touch |
| Form and connections | Non-touch counterpart described as the same 6.2-inch screen. Visible-window geometry has not been measured on this sample. |
| Validation status | Brightness pulsing unresolved; touch-sample compensation not validated here. |
| Environment | Raspberry Pi 4B; Raspberry Pi OS Bookworm Desktop 64-bit; labwc/Wayland |
| SKU / ASIN / panel part number / PCB revision | Not established; match the actual item before using a repair |

#### Recorded driver data

This sample reported the same LTM / ZL480 EDID family as the touch strip: 256 bytes, `328d5e04`, 420×960 at 28MHz / approximately 51.85Hz. A second DTD reported 480×480 at 18.72MHz. Matching EDID alone cannot distinguish the touch and non-touch products or confirm native glass dimensions. The 360×960 lookup follows the supplied product description; a separate ruler measurement on this unit is still required.

#### 1. Brightness pulsing / no picture

The sample displayed a positionally stable image with brightness alternating light/dark. A 420×960, 32.4MHz, 60Hz test did not solve it. The screen was powered from a Pi USB port. No Pi undervoltage flag was reported, but that does not prove stable power at the screen connector. An independent supply/cable comparison was not completed.

There is **no validated repair profile for this non-touch sample**. Do not use the touch-only 6.2 profile merely because EDID matches. Check the rated screen supply, substitute a known-good cable/supply, test one screen at a time, and compare with a known-good host. If EDID/DDC fails, repair that connection before automatic mode selection. See [shared display checks](../_shared/README.md#1-no-picture-flicker-or-an-edid-read-error).

#### 2. Touch response

Not applicable: this product has no touch input. A different screen's finger input must not reach this output. This mixed touch/non-touch case was corrected by mapping the single touch controller only to its own output, after which the customer confirmed correct position. Do not blindly deploy a two-touch mapping when only one controller exists. Display-only tests such as `screen-test pattern --screen 2` work without touch hardware.

#### 3. Cut-panel window

The x=60, width=360 compensation was confirmed on the touch sample only. The non-touch sample needs its own ruler/photo and border checks before applying that geometry. The missing touch layer does not prove identical panel firmware or scan alignment. No complete-image or 60Hz cure is claimed here.

[Product index](../README.md) · [All scenarios](../_shared/README.md)

</details>

[Product index](../README.md) · [Shared troubleshooting](../_shared/README.md)
