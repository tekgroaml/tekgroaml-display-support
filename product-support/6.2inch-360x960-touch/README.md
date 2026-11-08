# 6.2-inch 360×960 cut-panel touchscreen

**English** | [简体中文](README.zh-CN.md)

Please check the size, resolution and touch option on your order. Start with the simple checks below; no commands are needed.

## The screen goes black or flickers after a cable is moved

- Leave the cables still and wait about 10–15 seconds for the picture to return.
- If it stays black, unplug and firmly reconnect HDMI and the USB power connection. Check both ends.
- Try another cable and test one screen at a time. Use the power supply specified for your screen.

If this happens every time a cable moves, try replacing that cable. If the screen never lights up, follow the same connection checks first.

## Touch does nothing or controls another screen

- Connect the screen's **USB power/touch cable to the same computer that is sending the picture**. A wall charger can power the screen but cannot send your touches to the computer.
- Use a USB data cable. A charging-only cable may light the screen without making touch work.
- With two screens, check each screen's HDMI and USB cable as a pair. Try one screen with its USB cable first, then reconnect the other.


## What can I try in Windows?

Right-click the desktop and open **Display settings**. Select this screen, use its listed resolution and choose **Extend these displays** if you want separate screens. For flicker, open **Advanced display** and try 60Hz only if it is available for that screen.

If touch still goes to the wrong screen, search Windows for **Calibrate the screen for pen or touch input**. Open it, choose **Setup**, and follow the prompts to identify the touchscreen. Check the USB connection first.

[Windows steps with more detail](../../platforms/windows/README.md). The commands in the optional Raspberry Pi section below do **not** run on Windows.

## The left side is cut off, or left-side touches miss buttons

This cut-glass sample needs a special picture layout. Changing Windows resolution alone has not been shown to fix it. Please send us a photo showing all four screen edges.

On Raspberry Pi, we confirmed a workaround inside a test app: the full picture became visible and touch lined up. It does not automatically fix Windows, the whole desktop or every app. The optional Raspberry Pi section below explains how to try it.

## Optional: Raspberry Pi instructions

<details>
<summary>Show Raspberry Pi commands (not for Windows)</summary>

Commands below run on the Raspberry Pi after installing the [display tools](https://github.com/tekgroaml/tekgroaml-pi-display-tools). Use version 2.3.2+ for rectangular touch tests. Examples select connector 1 (`HDMI-A-1`, board HDMI0); replace 1 with 2 for connector 2 (board HDMI1). Run screen tests as the desktop user, without sudo.

## The left side is missing: text, buttons or targets are cut off

**What you may see:** right-side content looks complete, but the left border and left-side buttons are missing. Changing resolution alone may not help.

Try the included compensated test application:

1. Install display tools 2.3.2+ and download this support repository. Close any older temporary test window first.
2. From the **support repository root**, inspect the connected screen:

   ```bash
   screen-config list
   screen-test stop
   ```

3. If the selected output is already **420×960, normal rotation, scale 1**, run:

   ```bash
   python3 product-support/6.2inch-360x960-touch/scripts/6.2inch-360x960-touch-window-demo.py --screen 1
   ```

4. Check that all four white borders and all five numbered circles are visible. Tap and slide to check touch alignment. Press Ctrl+C in the launching terminal to close the demo.

A prior temporary application using this method showed complete content and accurate touch on the sample. The included program reproduces that method and has had a launch/screenshot check; its new five-point UI still needs its own physical acceptance check. If the command rejects your output mode or the borders remain clipped, send a photo and `screen-config list` to support. Do not save an unverified profile or guess a new resolution.

**Scope:** compensation is inside this application only. The ordinary desktop, browser and stock `screen-test` are not automatically compensated. Applications intended for this screen need the same visible-area layout.

## Buttons on the right are close, but left-side touches land too far left

First check that touch reaches this physical screen rather than another one; use the [pairing guide](../_shared/README.md#2-touch-does-not-respond-or-reaches-the-wrong-position) if necessary. Then use the compensated demo above: it corrects the visible content and touch position together.

Tap the center and all four corner targets. A target should turn green and the white touch mark should follow your finger. If the input has already been calibrated elsewhere, do not apply the correction twice. Ordinary `screen-test touch --shape rect` changes target layout but does not include this cut-panel correction.

## The picture flickers, even though content is visible

1. Check rated screen power and cables first.
2. If support confirms this sample matches the known touch-strip profile, try the timing correction below. Save desktop work first: applying it may restart the desktop, and it has no timed rollback.

   ```bash
   screen-config apply --port 1 --profile 6.2inch-420x960-60hz-ltm-zl480 --confirm-profile
   screen-test pattern --screen 1
   ```

3. Inspect stability separately from image completeness. A 60Hz test improved flicker on an earlier touch sample, **but it did not fix the missing left edge**.

The successful cut-window and touch test used approximately 51.85Hz. The combined 60Hz-plus-compensation configuration still needs physical verification. Do not add `--save` on the strength of a stable picture alone.

</details>

## Technical details and test records

<details>
<summary>Show product data, repair details and validation limits</summary>

#### Product information

| Field | Recorded information |
| --- | --- |
| Customer lookup name | 6.2-inch 360×960 cut-panel touchscreen |
| Form and connections | Strip-shaped cut glass. Advertised/visible resolution 360×960; HDMI input 420×960. |
| Validation status | Visible-window and touch compensation confirmed in a temporary application. |
| Environment | Raspberry Pi 4B; Raspberry Pi OS Bookworm Desktop 64-bit; labwc/Wayland |
| SKU / ASIN / panel part number / PCB revision | Not established; match the actual item before using a repair |

#### Reported data and visible area

| Item | Evidence |
| --- | --- |
| Advertised / visible area | 360×960; supplier confirmed cut glass; customer confirmed a complete image with compensation |
| HDMI EDID | LTM / ZL480; vendor/product bytes `328d5e04`; 256 bytes |
| Original preferred input | 420×960; 28MHz; 51.851852Hz |
| Original horizontal front / sync / back | 50 / 20 / 50; total 540 |
| Original vertical front / sync / back | 16 / 4 / 20; total 1000; +H/+V |
| Tested visible input coordinates | x = 60…419, y = 0…959; left 60 input columns are not visible |
| Touch device observed in this setup | wch.cn USB2IIC_CTP_CONTROL; `1a86:e5e3`; raw X/Y range 0…4096 |
| Main-chip photograph | Appears to read Lontium LT8619C; exact suffix/revision unconfirmed; ZL480 is an EDID name, not a verified chip or panel model |

The ruler/photo plus complete-image test support this input-coordinate window on the sample. They do not determine the uncut glass resolution, internal scan architecture or firmware encryption. No firmware was read or written.

#### 1. Flicker / no picture: timing is one separate issue

An earlier touch sample stopped flickering at 420×960, 32.4MHz, exactly 60Hz. This corrects the input clock, **not the cut-panel window**. Later border tests showed left cropping still present. Earlier claims that 60Hz alone restored a complete image are superseded by this finding.

With tools 2.3.0+, after checking sample identity, connector and power, this existing profile can test timing (connector 1 shown):

```bash
screen-config list
screen-config apply --port 1 --profile 6.2inch-420x960-60hz-ltm-zl480 --confirm-profile
screen-test pattern --screen 1
```

The profile's historical name uses input width 420. It does not rename the physical product to 420 pixels, and it does not implement compensation. Applying it may restart the desktop; save open work. There is no timed rollback. Do not add `--save` until timing stability, the visible window and the intended application have each been checked. Restore the original preferred mode with `screen-config auto --port 1 --save` only when DDC reads work; original flicker may return.

The successful visible-window/touch trial on 2026-11-08 used the original approximately 51.85Hz input. **Combined 60Hz + window compensation + touch compensation has not yet been physically confirmed.**

#### 2. Touch offset: scale and offset together

Once a complete 360-wide image was placed in the visible window, right targets were close but left targets had a larger leftward error. A center tap arrived near desktop x=209, while the drawn visible center was x=240.

For this test's unrotated, scale-1, 420×960 window, the trial correction was:

```text
screen_x = 60 + received_window_x × 360 / 420
screen_y = received_window_y
```

The customer confirmed accurate touch after this correction. Inside a 360-wide application canvas placed at x=60, use:

```text
canvas_x = received_window_x × 360 / 420
canvas_y = received_window_y
```

These formulas use desktop/window pixel coordinates, not raw 0…4096 controller units. Do not apply them a second time to an already calibrated input device. Correct output routing first; the shared USB relay changes names/routing, not calibration. Other controllers, rotations, desktop scales and output geometry require fresh measurements.

#### 3. Cut-panel display compensation: reproduce the verified approach

Keep the 420×960 HDMI canvas. Reserve x=0…59 as unused black pixels. Lay out the **entire application** in a 360×960 logical canvas and draw it with an x offset of 60. Do not simply shift a full 420-wide UI: its right 60 columns would then be clipped.

| Test | Result |
| --- | --- |
| 420×960 at original ~51.85Hz | Left side missing |
| 420×960 at 60Hz | Left crop remained |
| 360×960 at 60Hz / 28.8MHz | Crop remained; extra right-side line observed |
| 420×960 at 60Hz, front/sync/back 80/20/20 | Left crop essentially unchanged |
| Alternative 20/20/80 porch trial | Applied, but a clear customer result was not retained; not a validated fix |
| 420-wide input; content only at x=60…419 | Customer confirmed complete content |
| Same visible window plus X touch scale/offset | Customer confirmed accurate touch |

##### Included application demo

[scripts/6.2inch-360x960-touch-window-demo.py](scripts/6.2inch-360x960-touch-window-demo.py) packages the tested application-level idea for reproduction. It requires the installed display tools 2.3.2+, their GTK dependencies and a running labwc/Wayland desktop. This newly packaged file is not itself a released `screen-config` profile or a system calibration utility.

From this FAQ repository root, as the desktop user over SSH (no sudo):

```bash
screen-config list
screen-test stop
python3 product-support/6.2inch-360x960-touch/scripts/6.2inch-360x960-touch-window-demo.py --screen 1
```

The selected output must already be 420×960, unrotated, at scale 1. The program does not change timing, EDID, USB pairing or system calibration. It shows a 360-wide test UI at x=60 and corrects touch only inside this window. Five targets turn green on hits; slide to inspect the corrected trail. Inspect all four white borders. Use `--raw-touch` to compare without touch correction, and `--left 0 --width 420 --raw-touch` to view the full uncompensated input canvas. The default 60/360 geometry is specific to the measured sample, not every cut screen.

Stop with Ctrl+C in the launching SSH terminal. No service or boot setting is installed. Old temporary experiments must be closed first; an older overlay can hide this one. Exit the old foreground program with Ctrl+C, or use its recorded PID to terminate only that program.

##### What is and is not fixed

Confirmed on the original temporary program: complete visible content and accurate sampled touch. Not yet implemented/qualified: an entire 360-wide desktop, arbitrary third-party application placement, compositor-wide calibration, startup persistence, reconnects, cold boot, all edge points, multitouch or other batches. Stock `screen-test touch --shape rect` only changes layout; it does not know this crop. Other applications must implement the same logical canvas/input transform, or a separately tested compositor solution is needed. No firmware modification is needed for this application-level workaround.

[Product index](../README.md) · [Shared touch and multi-screen procedures](../_shared/README.md)

#### Evidence and packaged-demo check

- [Application screenshot](evidence/application-window-screenshot.png): full 420×960 captured input, with content inside the rightmost 360 columns. The black 60-column strip is deliberately outside the visible window.
- The packaged demo was launched on the connected Pi at 420×960 / 51.852001Hz on 2026-11-08; screenshot confirmed its border and five targets lie inside x=60…419. Its new five-point UI has not received a separate physical touch acceptance pass; the prior temporary program supplied the user-confirmed display/touch result.
- [Physical pixel-ruler photograph](evidence/physical-pixel-ruler.png): customer-provided evidence used to identify the visible window.

</details>

[Product index](../README.md) · [Shared troubleshooting](../_shared/README.md)
