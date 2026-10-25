#!/bin/bash
set -u
printf '%s\n' '=== MODEL AND OS ==='
tr -d '\0' </proc/device-tree/model
printf '\n'
cat /etc/os-release
uname -r
printf '%s\n' '=== HDMI ==='
for connector in /sys/class/drm/card*-HDMI-A-*; do
    [ -d "$connector" ] || continue
    echo "$connector"
    cat "$connector/status" "$connector/modes"
    if [ -r "$connector/edid" ]; then base64 -w0 "$connector/edid"; printf '\n'; fi
done
printf '%s\n' '=== USB ==='
lsusb
printf '%s\n' '=== INPUT ==='
sed -n '/^N: Name=/p; /^H: Handlers=/p' /proc/bus/input/devices
printf '%s\n' '=== POWER ==='
vcgencmd get_throttled
printf '%s\n' '=== SERVICE ==='
systemctl --no-pager status square720-display.service
journalctl -b -u square720-display.service --no-pager -n 30
