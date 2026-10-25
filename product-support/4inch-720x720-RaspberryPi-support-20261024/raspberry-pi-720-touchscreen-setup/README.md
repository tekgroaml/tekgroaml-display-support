# 4.0-inch 720x720 Raspberry Pi support package

Start with QUICK_START_EN.md or QUICK_START_CN.md.

Validated profile: Raspberry Pi 4 Model B, Raspberry Pi OS Bookworm Desktop 64-bit, WKS/Lontium 720x720 controller with the known EDID timing. The helper identifies the controller independently of its per-unit serial number, preserves unit-specific fields, changes the horizontal sync width to 6 pixels and pixel clock to 38.54 MHz, and corrects the EDID checksum. The resulting mode is approximately 60.004Hz.

This package uses a Linux DRM runtime EDID override at startup. It does not flash the monitor or edit config.txt/cmdline.txt. The operating system's debugfs override interface must be available. The installer stops on an unrecognized display or an unverified platform.

Files:
- install.sh: validate and install the startup configuration.
- display_compat.py: apply the narrow display compatibility profile.
- square720-display.service: run before the desktop at startup.
- uninstall.sh: remove this package's startup service.
- collect-diagnostics.sh: collect OS, HDMI, USB and service diagnostics.

Touch input requires a separate USB data connection. This package does not install a proprietary touch driver.
