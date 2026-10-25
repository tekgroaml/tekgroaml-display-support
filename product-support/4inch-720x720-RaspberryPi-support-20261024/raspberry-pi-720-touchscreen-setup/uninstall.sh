#!/bin/bash
set -euo pipefail
if [ "${EUID}" -ne 0 ]; then
    echo "Run: sudo bash uninstall.sh" >&2
    exit 1
fi
systemctl disable --now square720-display.service || true
rm -f /etc/systemd/system/square720-display.service
rm -f /usr/local/lib/square720/display_compat.py
rmdir /usr/local/lib/square720 2>/dev/null || true
systemctl daemon-reload
echo "Removed this package's startup service. Run sudo reboot to clear the runtime override."
echo "Saved original EDID files remain in /var/lib/square720."
