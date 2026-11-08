# 2.8-inch 480×480, touch status unconfirmed

**English** | [简体中文](README.zh-CN.md)

For the 2.8-inch square 480×480 samples. Check your order to confirm whether your item has touch; that option was not established for the tested pair. The black-screen investigation is still open.

Commands below run on the Raspberry Pi after installing the [display tools](https://github.com/tekgroaml/tekgroaml-pi-display-tools). Use version 2.3.2+ for rectangular touch tests. Examples select connector 1 (`HDMI-A-1`, board HDMI0); replace 1 with 2 for connector 2 (board HDMI1). Run screen tests as the desktop user, without sudo.

## The screen stays black after HDMI and power are connected

1. Leave only one screen connected. Check the rated supply, the power indicator and whether the backlight glows.
2. Power down the screen, reseat HDMI, then power it back on. Compare a known-good cable and another host.
3. Inspect what the Pi detects:

   ```bash
   screen-config list
   screen-config modes --port 1
   ```

4. Only if screen information is readable and 480×480 at about 60Hz is listed, try:

   ```bash
   screen-config set --port 1 --mode 480x480@60
   screen-test white --screen 1
   screen-test pattern --screen 1
   ```

These are troubleshooting steps, **not a confirmed cure**. One tested screen was already outputting 480×480 at 60Hz and still appeared black. If it remains black, send a photo of the connections and indicators, supply details and the command output to support. Do not use the 720-square or 6.2-strip profile.

## The command shows “Remote I/O error”

The Pi could not read the display information on the tested connection, even though HDMI was detected. Recheck screen power, HDMI seating and cables. `screen-config auto` depends on that read and cannot repair the physical link. A reported 1024×768 fallback is not your panel's resolution. Contact support if the error persists after cable/power checks.

## The screen displays a picture, but finger taps do nothing

Confirm your order is for the touch version, then check the USB data connection. If it has touch, follow the [touch checklist](../_shared/README.md#2-touch-does-not-respond-or-reaches-the-wrong-position). A non-touch version will not react to a finger. No calibration or cut-panel offset has been verified for these samples.

## Technical details and test records

<details>
<summary>Show product data, repair details and validation limits</summary>

#### Product information

| Field | Recorded information |
| --- | --- |
| Customer lookup name | 2.8-inch 480×480, touch status unconfirmed |
| Form and connections | Two nominally identical square samples; touch capability was not established. |
| Validation status | Both reported black; one EDID readable, the other failed DDC reads. Unresolved. |
| Environment | Raspberry Pi 4B; Raspberry Pi OS Bookworm Desktop 64-bit; labwc/Wayland |
| SKU / ASIN / panel part number / PCB revision | Not established; match the actual item before using a repair |

#### Recorded data

| Sample path | Observed state |
| --- | --- |
| Connector 1 at the time of testing | Valid 256-byte EDID; LTM / ZL480; `328d5e04`; both recorded DTDs 480×480, 18.72MHz, 60Hz; output enabled at 480×480 |
| Connector 2 at the time of testing | HDMI connection detected, but zero-byte kernel EDID; direct DDC returned `[Errno 121] Remote I/O error`; fallback output 1024×768 |

These are observations of that wiring session, not permanent properties of HDMI ports 1 and 2. Both physical screens were reported black. Touch capability, controller identity, exact panel part number, polarity and full timing were not established.

#### 1. Black screens / Remote I/O error

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

#### 2. Touch

Not yet confirmed whether these samples support touch. Inspect the actual SKU and USB input devices before treating it as either a touch or non-touch model. If confirmed, use the [shared touch guide](../_shared/README.md#2-touch-does-not-respond-or-reaches-the-wrong-position) and rename the product directory with the verified touch status; no product-specific calibration is available.

#### 3. Cut-panel compensation

Not measured or validated for these square samples. Do not apply the 6.2-inch window/coordinate offset.

[Product index](../README.md) · [All scenarios](../_shared/README.md)

</details>

[Product index](../README.md) · [Shared troubleshooting](../_shared/README.md)
