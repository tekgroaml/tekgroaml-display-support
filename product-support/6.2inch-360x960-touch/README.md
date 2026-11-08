# 6.2-inch 360×960 cut-panel touchscreen

**English** | [简体中文](README.zh-CN.md)

## Product information

| Field | Recorded information |
| --- | --- |
| Customer lookup name | 6.2-inch 360×960 cut-panel touchscreen |
| Form and connections | Strip-shaped cut glass. Advertised/visible resolution 360×960; HDMI input 420×960. |
| Validation status | Visible-window and touch compensation confirmed in a temporary application. |
| Environment | Raspberry Pi 4B; Raspberry Pi OS Bookworm Desktop 64-bit; labwc/Wayland |
| SKU / ASIN / panel part number / PCB revision | Not established; match the actual item before using a repair |

## Reported data and visible area

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

## 1. Flicker / no picture: timing is one separate issue

An earlier touch sample stopped flickering at 420×960, 32.4MHz, exactly 60Hz. This corrects the input clock, **not the cut-panel window**. Later border tests showed left cropping still present. Earlier claims that 60Hz alone restored a complete image are superseded by this finding.

With tools 2.3.0+, after checking sample identity, connector and power, this existing profile can test timing (connector 1 shown):

```bash
screen-config list
screen-config apply --port 1 --profile 6.2inch-420x960-60hz-ltm-zl480 --confirm-profile
screen-test pattern --screen 1
```

The profile's historical name uses input width 420. It does not rename the physical product to 420 pixels, and it does not implement compensation. Applying it may restart the desktop; save open work. There is no timed rollback. Do not add `--save` until timing stability, the visible window and the intended application have each been checked. Restore the original preferred mode with `screen-config auto --port 1 --save` only when DDC reads work; original flicker may return.

The successful visible-window/touch trial on 2026-11-08 used the original approximately 51.85Hz input. **Combined 60Hz + window compensation + touch compensation has not yet been physically confirmed.**

## 2. Touch offset: scale and offset together

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

## 3. Cut-panel display compensation: reproduce the verified approach

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

### Included application demo

[scripts/6.2inch-360x960-touch-window-demo.py](scripts/6.2inch-360x960-touch-window-demo.py) packages the tested application-level idea for reproduction. It requires the installed display tools 2.3.2+, their GTK dependencies and a running labwc/Wayland desktop. This newly packaged file is not itself a released `screen-config` profile or a system calibration utility.

From this FAQ repository root, as the desktop user over SSH (no sudo):

```bash
screen-config list
screen-test stop
python3 product-support/6.2inch-360x960-touch/scripts/6.2inch-360x960-touch-window-demo.py --screen 1
```

The selected output must already be 420×960, unrotated, at scale 1. The program does not change timing, EDID, USB pairing or system calibration. It shows a 360-wide test UI at x=60 and corrects touch only inside this window. Five targets turn green on hits; slide to inspect the corrected trail. Inspect all four white borders. Use `--raw-touch` to compare without touch correction, and `--left 0 --width 420 --raw-touch` to view the full uncompensated input canvas. The default 60/360 geometry is specific to the measured sample, not every cut screen.

Stop with Ctrl+C in the launching SSH terminal. No service or boot setting is installed. Old temporary experiments must be closed first; an older overlay can hide this one. Exit the old foreground program with Ctrl+C, or use its recorded PID to terminate only that program.

### What is and is not fixed

Confirmed on the original temporary program: complete visible content and accurate sampled touch. Not yet implemented/qualified: an entire 360-wide desktop, arbitrary third-party application placement, compositor-wide calibration, startup persistence, reconnects, cold boot, all edge points, multitouch or other batches. Stock `screen-test touch --shape rect` only changes layout; it does not know this crop. Other applications must implement the same logical canvas/input transform, or a separately tested compositor solution is needed. No firmware modification is needed for this application-level workaround.

[Product index](../README.md) · [Shared touch and multi-screen procedures](../_shared/README.md)

## Evidence and packaged-demo check

- [Application screenshot](evidence/application-window-screenshot.png): full 420×960 captured input, with content inside the rightmost 360 columns. The black 60-column strip is deliberately outside the visible window.
- The packaged demo was launched on the connected Pi at 420×960 / 51.852001Hz on 2026-11-08; screenshot confirmed its border and five targets lie inside x=60…419. Its new five-point UI has not received a separate physical touch acceptance pass; the prior temporary program supplied the user-confirmed display/touch result.
- [Physical pixel-ruler photograph](evidence/physical-pixel-ruler.png): customer-provided evidence used to identify the visible window.
