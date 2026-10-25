# Raspberry Pi Setup: 4.0-inch 720 × 720 HDMI Touchscreen

This guide covers the display controller supported by this package. Tested setup: Raspberry Pi 4 Model B with Raspberry Pi OS Bookworm Desktop, 64-bit. Other Raspberry Pi models, operating systems and controller revisions require separate verification.

## 1. Prepare your Raspberry Pi

You need a Raspberry Pi, a microSD card with a working operating system, the correct power supplies, an HDMI cable and a USB cable that supports data transfer. Raspberry Pi 4 uses micro-HDMI; choose the cable to match the actual connector on the display. Micro-HDMI and mini-HDMI are different connectors.

Use a suitable 5.1V/3A USB-C supply for Raspberry Pi 4. Power the display according to its own label and wiring diagram. The Raspberry Pi power specification is not the display power specification.

If your microSD card already has a working OS, you can use it. For a new installation, use Raspberry Pi Imager. This package's tested OS is Bookworm Desktop, 64-bit.

For remote setup, configure your own username, password, Wi-Fi and SSH access when writing the OS, or enable them on the existing installation. Do not assume a default username or password.

## 2. Connect video, touch and power

Shut down and disconnect Raspberry Pi power before changing connections.

| Connection | Purpose |
| --- | --- |
| Raspberry Pi HDMI output → display HDMI input | Video |
| Raspberry Pi USB port → display touch USB port | Touch data; any shared power function depends on the product wiring diagram |
| Display power connection | Follow the display label and wiring diagram |
| Raspberry Pi USB-C power connection | Raspberry Pi power |

An HDMI connection alone does not provide USB touch input. A touch USB cable connected only to a charger also does not send touch data to the Raspberry Pi. Use a data-capable USB cable and the display's correct touch port.

Connect all required cables and power, then start the Raspberry Pi.

## 3. If video and touch work normally

You do not need to install this display compatibility package. Use the native 720 × 720 resolution; the tested working mode is approximately 60Hz. In our tested OS, the touchscreen was automatically recognized by the built-in USB HID/multitouch driver, without installing an additional touch driver.

## 4. If the screen is black, has no signal or flickers

The tested controller required a display timing adjustment on Raspberry Pi 4. Selecting 720 × 720 alone may not be sufficient. Check cables and power first, then use this seller-supplied package. Do not copy configuration values intended for a different display.

If you cannot operate the screen, temporarily use another monitor or connect by SSH from a computer on the same local network.

Extract the entire support folder. To copy it from another computer, open a terminal in the folder's parent directory. Replace YOUR_USER and YOUR_PI_IP with your own Raspberry Pi username and IP address:

```bash
scp -r raspberry-pi-720-touchscreen-setup YOUR_USER@YOUR_PI_IP:~/
ssh YOUR_USER@YOUR_PI_IP
```

On the Raspberry Pi, run:

```bash
cd ~/raspberry-pi-720-touchscreen-setup
sudo bash install.sh
sudo reboot
```

Keep the display connected by HDMI during installation. The installer checks the Raspberry Pi model, OS and display identification. If they do not match the tested profile, send the error to the seller instead of forcing an installation.

After reboot, the matching controller receives a 720 × 720 timing profile at approximately 60Hz. Other displays are left unchanged. The helper runs at startup; reboot after changing displays to repeat detection.

## 5. If touch does not respond

Check the USB touch connection first. Connect the touch USB port to a Raspberry Pi USB port using a data-capable cable. If already connected, try a known working data cable and another Raspberry Pi USB port.

Run:

```bash
lsusb
```

Our tested touch controller appeared as:

```text
1a86:e5e3 QinHeng Electronics USB2IIC_CTP_CONTROL
```

If no touch device appears, check the cable, port and controller connection. Device names may differ between product revisions. If a touch device is present but taps still fail or coordinates are incorrect, send the seller the system information, wiring photos and diagnostic output. This package adjusts display timing; it does not automatically calibrate every touch configuration.

## 6. Diagnostics and removal

From the support folder, run:

```bash
sudo bash collect-diagnostics.sh > ~/square720-diagnostics.txt 2>&1
```

Send the output file to the seller with your Raspberry Pi model, OS version, wiring photos and a description of the issue.

To remove this package:

```bash
sudo bash uninstall.sh
sudo reboot
```

The system will return to reading the display's original identification. A display that needs this compatibility profile may stop showing an image again.
