# 3.4-inch 800×800 touchscreen

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

## Still not working?

Please send a photo or short video, your computer model, and how HDMI and USB are connected. Raspberry Pi users can try the product-specific steps below after the basic checks.

## Optional: Raspberry Pi instructions

<details>
<summary>Show Raspberry Pi commands (not for Windows)</summary>

Commands below run on the Raspberry Pi after installing the [display tools](https://github.com/tekgroaml/tekgroaml-pi-display-tools). Use version 2.3.2+ for rectangular touch tests. Examples select connector 1 (`HDMI-A-1`, board HDMI0); replace 1 with 2 for connector 2 (board HDMI1). Run screen tests as the desktop user, without sudo.

## After connecting the round screen, there is no picture or the picture looks wrong

This can happen when an output still uses the mode selected for a previously connected screen.

1. Check power and HDMI, then inspect the screen's available modes:

   ```bash
   screen-config list
   screen-config modes --port 1
   ```

2. **Only if 800×800 at approximately 60Hz is listed**, select it and display the test:

   ```bash
   screen-config set --port 1 --mode 800x800@60
   screen-test pattern --screen 1
   ```

3. If the physical picture is stable, save that selection:

   ```bash
   screen-config set --port 1 --mode 800x800@60 --save
   ```

The sample displayed a stable picture after selecting 800×800 at 60Hz. If the mode is missing, send `screen-config list` and `screen-config modes --port 1` to support; do not use the square-screen or strip-screen repair profile. These commands do not provide an automatic rollback.

## Touch does not work or controls the other display

Connect the USB data cable, then run:

```bash
screen-test touch --screen 1 --shape round
```

Tap the five numbered circles, then slide. If touches appear on another screen, identify each USB touch cable and follow the [pairing procedure](../_shared/README.md#2-touch-does-not-respond-or-reaches-the-wrong-position). This procedure corrected the dual-touch problem in the tested setup.

## The test screenshot has corners that are not visible on the screen

A round panel cannot show the four corners of a square 800×800 screenshot. Keep application buttons inside the visible circle and use `--shape round` for touch testing. A missing part of the circle or clipped center content is a different problem: send a photo to support. Do not apply the strip panel's 60-column offset.

## The test window disappears after reconnecting

```bash
screen-test stop
screen-test touch --screen 1 --shape round
```

</details>

## Technical details and test records

<details>
<summary>Show product data, repair details and validation limits</summary>

#### Product information

| Field | Recorded information |
| --- | --- |
| Customer lookup name | 3.4-inch 800×800 touchscreen |
| Form and connections | Round; HDMI video + USB touch. |
| Validation status | 800×800 at 60Hz visually confirmed stable; exact timing dump not retained. |
| Environment | Raspberry Pi 4B; Raspberry Pi OS Bookworm Desktop 64-bit; labwc/Wayland |
| SKU / ASIN / panel part number / PCB revision | Not established; match the actual item before using a repair |

#### 1. No picture / wrong mode

The earlier output still used 720×720 after this screen was attached. Switching to the panel's 800×800 at 60Hz produced a stable picture, confirmed on the physical sample. The exact original EDID, pixel clock, porch values and controller identity were not retained; do not copy the 720-square or 6.2-strip EDID profiles.

With display tools installed, inspect the selected connector first (example: connector 2):

```bash
screen-config list
screen-config modes --port 2
```

Only if 800×800 at approximately 60Hz is advertised:

```bash
screen-config set --port 2 --mode 800x800@60
screen-test pattern --screen 2
screen-test touch --screen 2 --shape round
```

`set` only selects advertised modes; it does not manufacture a missing mode. If it is absent, collect the raw timing/EDID before choosing a profile. Save only after physical checks:

```bash
screen-config set --port 2 --mode 800x800@60 --save
```

To remove this saved selection and return to the advertised preferred mode, use `screen-config auto --port 2 --save` when DDC works. No automatic rollback is provided by these commands.

#### 2. Touch mapping

The session also tested two connected touchscreens: input first reached the same screen, then separate virtual device names and confirmed USB-path/output pairing corrected routing and position. Follow the [shared procedure](../_shared/README.md#2-touch-does-not-respond-or-reaches-the-wrong-position). The complete per-unit USB/EDID association was not archived; identify your own controller by taps. Use the round layout so targets remain inside the circular visible area. A square screenshot includes corner pixels that a circular panel cannot physically show.

#### 3. Cut-panel compensation

No rectangular 60-column offset was validated here. The natural circular mask is different from the 6.2-inch strip's horizontal crop.

#### Acceptance and limits

Stable picture and eventual correct dual-screen touch were reported in the debugging session. Reboot persistence, exact timing reproduction from a clean OS, and other batches remain to be qualified.

[Product index](../README.md) · [All tested scenarios](../_shared/README.md)

</details>

[Product index](../README.md) · [Shared troubleshooting](../_shared/README.md)
