# 4.0-inch 720×720 touchscreen

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

## The screen stays black or the picture flickers

**What you may see:** the display is powered and HDMI is connected, but there is no picture, or the picture appears and flickers.

1. Check the screen's rated power supply and HDMI cable; test one screen first.
2. Inspect the detected screen, then try the matching compatibility profile:

   ```bash
   screen-config list
   screen-config apply --port 1 --profile 4.0inch-720x720-60hz-wks-lontium-semi
   screen-test pattern --screen 1
   ```

   Save open desktop files first: applying the profile may restart the desktop. This command has no automatic timeout rollback. If the tool says the screen does not match, stop and contact support rather than force it.
3. Check that the picture is stable and all four edges are visible. If it passes, save:

   ```bash
   screen-config apply --port 1 --profile 4.0inch-720x720-60hz-wks-lontium-semi --save
   ```

This timing correction worked on the tested sample. If you need to undo it and the screen information can be read, run `screen-config auto --port 1 --save`; the original symptom may return.

## Touch does nothing, operates the other screen, or misses buttons

1. Connect a USB **data** cable to the touch socket; HDMI alone does not carry touch.
2. Open the target test:

   ```bash
   screen-test touch --screen 1 --shape rect
   ```

3. Tap all five targets and slide a finger. Targets should turn green and the trail should follow the finger on the same screen.
4. If another screen responds, use the [USB/HDMI pairing steps](../_shared/README.md#2-touch-does-not-respond-or-reaches-the-wrong-position). Different screen models can report the same controller name.

If the trail is on the correct screen but remains offset, contact support with a photo and `screen-config list`; do not apply the 6.2-inch cut-panel correction to this square screen.

## The test image disappears after changing cables

Restart the test window:

```bash
screen-test stop
screen-test pattern --screen 1
```

If the desktop is also absent, check screen power/connection and that the graphical desktop is logged in.

</details>

## Technical details and test records

<details>
<summary>Show product data, repair details and validation limits</summary>

#### Product information

| Field | Recorded information |
| --- | --- |
| Customer lookup name | 4.0-inch 720×720 touchscreen |
| Form and connections | Square; HDMI video + USB touch. Initial 5.08-inch identification was corrected to 4.0 inches. |
| Validation status | Timing fix and touch verified on the sample. |
| Environment | Raspberry Pi 4B; Raspberry Pi OS Bookworm Desktop 64-bit; labwc/Wayland |
| SKU / ASIN / panel part number / PCB revision | Not established; match the actual item before using a repair |

#### 1. No picture or flicker: verified EDID timing repair

| Timing | Reported | Corrected |
| --- | --- | --- |
| EDID name / vendor-product bytes / size | WKS / Lontium Semi; `5d734600`; 128 bytes | Identity retained |
| Active pixels | 720×720 | 720×720 |
| Pixel clock | 35MHz | 38.54MHz |
| Refresh | 54.492349Hz | 60.003861Hz (nominal 60Hz) |
| Horizontal front / sync / back | 46 / 5 / 41 | 46 / 6 / 40 |
| Horizontal / vertical totals | 812 / 791 | Unchanged |
| Vertical front / sync / back | 50 / 5 / 16 | Unchanged |
| Sync polarity | +H / +V | Unchanged |

The original odd horizontal sync width was rejected on the tested Pi. Making sync even allowed a picture, but clock correction was also needed to remove flicker. This is a host-side EDID override, not a monitor firmware flash.

Install the [display tools](https://github.com/tekgroaml/tekgroaml-pi-display-tools) first. Canonical profile names need 2.3.0+, rectangular touch layout needs 2.3.2+. Commands below select connector 1; replace 1 with 2 for connector 2. Save desktop work first: applying an override may restart the graphical session on both outputs. There is no automatic timeout rollback for `apply`.

```bash
screen-config list
screen-config profiles
screen-config apply --port 1 --profile 4.0inch-720x720-60hz-wks-lontium-semi
screen-test pattern --screen 1
screen-test touch --screen 1 --shape rect
```

Only after checking the physical screen, save:

```bash
screen-config apply --port 1 --profile 4.0inch-720x720-60hz-wks-lontium-semi --save
```

Rollback, when EDID/DDC reads work:

```bash
screen-config auto --port 1 --save
```

Rollback removes this tool's override and saved setting for that port; the original problem may return. Profile alias: `lontium-720`. Wrapper: `scripts/profiles/4.0inch-720x720-60hz-wks-lontium-semi.sh` in the tools repository. A profile mismatch must be investigated, not bypassed.

#### 2. Touch missing, wrong screen, or offset

The tested touch controller reported `wch.cn USB2IIC_CTP_CONTROL`, VID/PID `1a86:e5e3`; this identity is not guaranteed for every batch. HDMI alone carries no touch input. Follow the [shared touch procedure](../_shared/README.md#2-touch-does-not-respond-or-reaches-the-wrong-position), including single-screen checks, identical controller names, same-model and mixed-model dual screens, USB/HDMI cable pairing, and reversed pairs. No cut-panel offset is appropriate for this square sample.

#### 3. Cut-panel compensation

Not observed or required for this product. Do not apply the 6.2-inch offset.

#### Acceptance and limits

Manual sample timing correction and touch operation were confirmed. Validate four borders, five targets, continuous strokes and stability on the actual item. Cold boot, sleep/wake, hot-plug, other batches and other platforms are not fully qualified by these records.

[Product index](../README.md) · [All tested scenarios](../_shared/README.md)

</details>

[Product index](../README.md) · [Shared troubleshooting](../_shared/README.md)
