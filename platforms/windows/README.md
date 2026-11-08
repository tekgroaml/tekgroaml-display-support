# Windows: quick checks for picture and touch

**English** | [简体中文](README.zh-CN.md)

Start here before installing drivers or running scripts. These are things to try in Windows 10/11; menu names can vary. A successful Raspberry Pi test does not guarantee the same result on Windows.

## The screen goes black or flickers when I touch a cable

1. Keep the cables still and wait about 10–15 seconds.
2. If the picture does not return, unplug and firmly reconnect HDMI and USB power. Check the computer end too.
3. Try another cable. Test one screen at a time and use the screen's specified power connection.

If a slight movement repeatedly causes the problem, replace the cable first. It is not a reason to start changing display firmware.

## A two-panel kit appears as one display, or cannot show separate content

One logical display can be normal for two panels driven by one HDMI board. A hardware-copy board sends one picture to both; an SBS board sends half a double-width picture to each. Windows Duplicate/Extend changes host outputs, not the board's internal mapping.

1. Check the product instructions for same/different content and whether one or two HDMI cables are used.
2. Select only an actually offered input matching the board. Do not force 960×480 onto a 480×480 board. A normal full-screen window does not guarantee two complete SBS panel views.
3. For one dark panel, wait, reconnect HDMI/USB power and compare cables and rated supplies first. A complete screenshot does not prove both panels received the signal.

[Provisional dual-screen records](../../product-support/_unconfirmed/README.md) contain Pi-side evidence, not a Windows driver or completed Windows acceptance. Approximately 71.295Hz is a particular advertised input, not a universal target. Do not force Windows rates to pass a Pi demo check.

## It still has no picture, flickers, or looks the wrong size

1. Right-click the desktop → **Display settings** → **Identify**. Select the small screen.
2. Choose the resolution listed for your product, if Windows offers it. Do not copy another screen's settings.
3. For separate screens, choose **Extend these displays**. Duplicate mode can limit the available picture sizes.
4. Open **Advanced display**, select the same screen, and try 60Hz **only if it is offered**. If unavailable or worse, return to the previous setting. Confirm a change only when the picture looks correct; Windows normally offers a brief chance to keep or revert display changes.
5. If the whole screen is visible but text is too large, adjust **Scale**. Scale changes text/app size; it does not restore pixels cut off by the screen hardware.

If Windows cannot detect the screen, recheck power and HDMI and try a known-good port/cable or another computer. If detected but still black, contact us with a photo and the selected resolution/refresh rate.

## The picture works, but touch does nothing

The touch model's supplied USB power/touch cable also carries touch data. Connect it to **the same computer that sends the HDMI picture**, not only to a wall charger. Use a USB data cable, not a charging-only cable. A non-touch model will not respond to finger taps.

Try another USB port directly on the computer, temporarily bypass a hub, and reconnect USB. Open **Device Manager → Human Interface Devices** and look for a touchscreen entry such as **HID-compliant touch screen**. If disabled, enable it. If missing or showing a warning, try the data cable/port first, then ask support before installing a third-party driver. Do not disable unrelated input devices.

## Touch controls the other screen

1. Check that both cables from each screen go to the intended computer. Test one screen and its USB touch cable at a time.
2. Reconnect both. Use **Identify** in Display settings to confirm which display is which.
3. Search Start for **Calibrate the screen for pen or touch input**. In **Tablet PC Settings**, choose **Setup** (Touch input if asked).
4. Follow the prompt: touch the requested screen. If the prompt appears on a non-touch screen, press Enter to move it to the next screen. Finish and test both screens.

Try **Setup** before calibration; it assigns the touch input to a display. Availability depends on Windows and the controller. If the option is absent or both still act on one screen, send us a photo of the cable connections and a Device Manager screenshot. The Raspberry Pi USB-mapping script does not configure Windows.

## Touch is on the right screen, but the point misses my finger

First confirm the display resolution, orientation and touch-screen assignment above. If a previous Windows calibration was applied, use **Reset** in Tablet PC Settings if available, then test again. On a normal rectangular touchscreen, **Calibrate** may help if offered. A round panel may hide the calibration corners; do not complete a calibration by guessing invisible points.

For the 6.2-inch cut panel, fix the visible picture area before attempting calibration. A calibration alone cannot reveal missing picture content. [See the cut-panel product FAQ](../../product-support/6.2inch-360x960-touch/README.md).

## A side of the 6.2-inch picture is missing

The measured touch sample displays only part of the incoming picture. The Raspberry Pi application workaround is documented, but a whole-desktop Windows workaround has **not** been validated. Do not expect a different resolution, 60Hz or Windows touch calibration alone to fix the missing area. Send a full-screen photo and a screenshot of **Advanced display** so support can check your sample.

## Do I need the scripts?

The `screen-config`, `screen-test` and Python cut-panel demo in these support pages are for **Raspberry Pi OS with the documented desktop setup**. They are not Windows programs. Windows users should start with the steps above and contact support if the problem remains.

[Choose your product](../../product-support/README.md) · [Support home](../../README.md)
