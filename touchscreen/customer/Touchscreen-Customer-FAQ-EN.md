# HDMI Touchscreen: Customer FAQ

For displays that use **HDMI for video and USB for touch data**. Follow the wiring diagram, power requirements and supported operating systems for your specific model. A connector that looks the same may have a different function.

## Start with these checks

1. Confirm that the picture is stable. Resolve a black screen, no signal or severe flickering before checking touch accuracy.
2. Connect both the HDMI video cable and the touch USB data cable to the **same computer or Raspberry Pi**.
3. Use a data-capable USB cable. A USB connection only to a wall charger cannot send touch data to the host.
4. For a multi-display issue, first test each display on its own, then reconnect them one at a time.

## Q1. I have a picture, but touch does not work. Why?

Video and touch use separate connections. A working picture confirms video, not the touch USB connection.

Check that you are using the display's correct touch USB port. Try a known working USB data cable and connect directly to the host, temporarily bypassing hubs, docks and extension cables. Power the display according to its own instructions; do not try an unlisted voltage.

## Q2. USB is connected, but touch still does not respond. What should I check?

| What you observe | Next step |
| --- | --- |
| No touch device is detected by the OS | Check the data cable, correct port, USB connection and power |
| A touch device is detected, but nothing happens | Check desktop login, application input support and whether another display responds |
| Touch responds at the wrong position | Confirm the correct display association before checking rotation or calibration |

Changing video resolution alone does not repair a missing USB data connection. Please do not install an unrelated display's driver.

## Q3. How can I test touch directly on the screen?

If the seller's compatible `pi-setting` tool has been installed, run this on the **Raspberry Pi**:

```bash
screen-test touch
```

Tap each of the five numbered targets. A hit turns the target green. Slide your finger to draw a trail. Use `RESET` to clear that screen's test.

```bash
screen-test touch --screen 1
screen-test touch --screen 2
screen-test stop
```

Configuration `--port` and test `--screen` now both use 1/2: 1 selects Linux connector `HDMI-A-1` (board HDMI0), and 2 selects `HDMI-A-2` (board HDMI1), regardless of their left/right desktop arrangement. These numbers may differ from another operating system's display numbers.

Check that each physical screen responds on itself, the marker follows your finger, and movement is reasonably continuous. Hitting five targets is a sample check, not certification of every edge, calibration or multitouch capability.

`command not found` means the support tool is not installed. It does not mean the monitor is defective. Ask the seller for the appropriate package and installation guide.

For a combined color and touch test, the updated tool provides `screen-test tap-cycle`. It starts black; each finger press advances to white, red, then black. There is no timer, and each screen responds independently. The picture stays solid with no labels or markers. This checks whether input can trigger a color change and whether it reaches the intended display; use `screen-test touch` to check coordinate accuracy and movement. A real mouse can also trigger this mode, so use only your finger when testing touch.

## Q4. Why does tapping a solid-color or grid test show no response?

The `black`, `white`, `red`, `cycle` and `pattern` modes test video output. They do not provide interactive touch feedback. Use `screen-test touch`, or exit the test and use an application that accepts touch.

`POINTER / EMULATED TOUCH` means the window received pointer-style input. This may come from touch converted to mouse input, or from a real mouse. Use only your finger when testing. This label is not, by itself, a fault.

## Q5. Two identical displays are connected. Why does touching one operate the other?

Their USB touch controllers may report the same name or have missing/duplicate serial numbers. The OS may not distinguish them correctly. This is a touch-to-display association issue; it does not by itself prove a panel defect.

Test each display individually. Label both HDMI and USB data cables A/B, then reconnect and test one display at a time. Send support a wiring photo and a description such as “touching A operates B.”

Some Raspberry Pi configurations require identifying controllers by their physical USB paths and mapping each to the correct HDMI output. These paths must be confirmed on your own host. Do not copy another host's input-device nodes or USB path values.

## Q6. Can this also happen with different models or screen sizes?

Yes. Different-looking displays may use the same touch controller and report the same USB name. Even devices with distinct names need correct display association.

A difference in size is not enough to conclude that two touchscreens cannot work together. Check each display's native resolution, orientation, desktop layout and touch mapping. Test each individually before combining them. Do not apply one display's resolution or calibration values to every monitor.

If you change displays and the picture itself becomes incorrect, have the host detect the new display before testing touch accuracy.

## Q7. Touch is offset, reversed or rotated. What should I do?

First confirm that input goes to the correct physical display. Then check whether the display orientation matches its installation. Rotating the picture may require a separate touch-coordinate setting.

Tell support if previous calibration or mapping settings are present. Do not copy a calibration matrix intended for a different OS, monitor or desktop layout.

## Q8. Why did touch mapping change after moving a USB cable, HDMI cable or dock?

Some multi-display setups bind a physical USB path to an HDMI output. Changing ports can change that association.

If support previously configured your setup, reconnect the original cable/port pairs first. For a permanent wiring change, confirm and configure each screen-to-touch connection again.

## Q9. SSH works, but the Raspberry Pi test says no desktop session is running.

SSH login and graphical desktop login are separate. The test requires a logged-in graphical desktop. Logging out of that desktop can leave SSH working while removing the session needed to show the test window.

Log back in on the physical screen. On the tested LightDM setup with desktop autologin enabled, support may ask you to run:

```bash
sudo systemctl restart lightdm
```

This closes graphical applications. Save your work first. It is not a universal command for every Linux desktop. Run the test again after the desktop is ready.

## Q10. On Windows, touch operates the wrong monitor. What can I try?

Connect each touch display's video and USB data cables. Temporarily use an extended desktop so that the displays can be identified separately. In **Tablet PC Settings**, look for **Setup** and follow the on-screen display-identification instructions.[1][2]

Touch the appropriate display when prompted. Follow your current system's instructions to skip a non-touch display. Available settings and their location may vary by Windows version, driver and permissions.[1]

Associate touch with the correct display before attempting coordinate calibration. Raspberry Pi Linux scripts do not run as Windows touch drivers. If settings are missing or no touch USB device appears, send support your Windows version and a Device Manager screenshot.

## Q11. Can multiple displays support simultaneous multitouch?

These are different capabilities: each display working individually, multiple fingers on one display, and multiple fingers across several displays at the same time.

Results depend on the controller, OS, drivers, input mode and application. Our tested Raspberry Pi setup confirmed that two screens responded on their own displays at the correct positions. This does not establish simultaneous cross-screen multitouch for every application. Please provide your host OS and software before purchase if this is a requirement.

## Q12. Do I need a separate touch driver?

The USB controller in our tested Raspberry Pi setup was recognized by the OS's built-in driver. No separate manufacturer touch driver was installed for that setup. This is not a guarantee for every product revision and OS.

Video timing, touch drivers and touch-to-display mapping are separate settings. A 720 × 720 video compatibility package is not a universal touch driver.

## Q13. What information should I send support?

Please provide your purchased model, host model, OS version, number of displays, wiring photos and whether each display works individually. State whether the issue is no response, input on another screen, coordinate offset or intermittent disconnection. A short video showing your finger and both screens can help.

Support may request a USB device list or a brief touch-event capture. Do not send Wi-Fi passwords, computer login passwords or SSH passwords.

## Scope and references

The Raspberry Pi instructions are based on the seller's October 25, 2026 sample testing: Raspberry Pi 4 Model B, Raspberry Pi OS Bookworm Desktop 64-bit, labwc/Wayland. Other operating systems and product combinations require their own verification.

[1] [MicroTouch: Touch Setup for Multiple Monitors in Windows](https://help.microtouch.com/calibrating-multiple-monitors-in-windows)

[2] [Microsoft: Using multiple monitors in Windows](https://support.microsoft.com/en-us/windows/hardware/display-graphics/how-to-use-multiple-monitors-in-windows)

[Back to touchscreen documentation](../README.md)
