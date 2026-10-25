#!/bin/bash
set -euo pipefail
if [ "${EUID}" -ne 0 ]; then
    echo "Run: sudo bash install.sh" >&2
    exit 1
fi
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
model="$(tr -d '\0' </proc/device-tree/model)"
case "$model" in
    "Raspberry Pi 4 Model B"*) ;;
    *) echo "This support package has only been validated for Raspberry Pi 4 Model B." >&2; exit 1 ;;
esac
. /etc/os-release
if [ "${VERSION_CODENAME:-}" != "bookworm" ] || [ "$(getconf LONG_BIT)" != "64" ]; then
    echo "Validated platform: Raspberry Pi OS Bookworm Desktop, 64-bit. Contact the seller for other systems." >&2
    exit 1
fi
command -v python3 >/dev/null
# No installation is made unless the connected display matches the tested profile.
python3 "$SCRIPT_DIR/display_compat.py" --check
install -d -m 755 /usr/local/lib/square720
install -m 644 "$SCRIPT_DIR/display_compat.py" /usr/local/lib/square720/display_compat.py
install -m 644 "$SCRIPT_DIR/square720-display.service" /etc/systemd/system/square720-display.service
systemctl daemon-reload
systemctl enable square720-display.service
echo "Installed. Leave the display connected and run: sudo reboot"
echo "Touch uses a separate USB DATA connection; this package configures video timing."
