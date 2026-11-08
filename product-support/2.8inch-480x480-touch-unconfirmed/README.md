# 2.8-inch 480×480, touch status unconfirmed

**English** | [简体中文](README.zh-CN.md)

## Product information

| Field | Recorded information |
| --- | --- |
| Customer lookup name | 2.8-inch 480×480, touch status unconfirmed |
| Form and connections | Two nominally identical square samples; touch capability was not established. |
| Validation status | Both reported black; one EDID readable, the other failed DDC reads. Unresolved. |
| Environment | Raspberry Pi 4B; Raspberry Pi OS Bookworm Desktop 64-bit; labwc/Wayland |
| SKU / ASIN / panel part number / PCB revision | Not established; match the actual item before using a repair |

## Recorded data

| Sample path | Observed state |
| --- | --- |
| Connector 1 at the time of testing | Valid 256-byte EDID; LTM / ZL480; `328d5e04`; both recorded DTDs 480×480, 18.72MHz, 60Hz; output enabled at 480×480 |
| Connector 2 at the time of testing | HDMI connection detected, but zero-byte kernel EDID; direct DDC returned `[Errno 121] Remote I/O error`; fallback output 1024×768 |

These are observations of that wiring session, not permanent properties of HDMI ports 1 and 2. Both physical screens were reported black. Touch capability, controller identity, exact panel part number, polarity and full timing were not established.

## 1. Black screens / Remote I/O error

The readable sample already had the advertised resolution, so resolution mismatch alone cannot explain both black screens. The other sample could not complete the EDID read; `screen-config auto` requires that read and is not a fix for a failing DDC link. During follow-up the SSH connection also timed out; the requested white-screen test was not confirmed executed.

No validated repair is available. Test one screen at a time with rated power, check backlight/power indicators, reseat HDMI with the screen powered down, compare HDMI/data/power cables and a known-good host, then recheck:

```bash
screen-config list
screen-config modes --port 1
```

Only if 480×480 at about 60Hz is advertised and the link is readable:

```bash
screen-config set --port 1 --mode 480x480@60
screen-test white --screen 1
screen-test pattern --screen 1
```

These are diagnostic steps, not an established black-screen cure. No 720-square or 6.2-strip EDID override should be applied to this product. A host without undervoltage flags does not establish adequate power at the panel.

## 2. Touch

Not yet confirmed whether these samples support touch. Inspect the actual SKU and USB input devices before treating it as either a touch or non-touch model. If confirmed, use the [shared touch guide](../_shared/README.md#2-touch-does-not-respond-or-reaches-the-wrong-position) and rename the product directory with the verified touch status; no product-specific calibration is available.

## 3. Cut-panel compensation

Not measured or validated for these square samples. Do not apply the 6.2-inch window/coordinate offset.

[Product index](../README.md) · [All scenarios](../_shared/README.md)
