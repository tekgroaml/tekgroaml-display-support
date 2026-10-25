#!/usr/bin/python3
"""Display timing compatibility helper for the tested WKS/Lontium 720x720 board.

Matches manufacturer/product and known detailed timing; preserves unit-specific
serial/date fields. It does not write to the monitor firmware or boot config.
"""
import argparse
from pathlib import Path
import time

HEADER = bytes.fromhex('00ffffffffffff00')
VENDOR_PRODUCT = bytes.fromhex('5d734600')
ORIGINAL_DTD = bytes.fromhex('ac0dd05c20d047202e05250cd0d02200001e')
OLD_FIXED_DTD = bytes.fromhex('ac0dd05c20d047202e06250cd0d02200001e')
FIXED_DTD = bytes.fromhex('0e0fd05c20d047202e06250cd0d02200001e')


def compatible_edid(data):
    """Return a corrected EDID for this known board, otherwise None."""
    if len(data) != 128 or data[:8] != HEADER or sum(data) % 256:
        return None
    if data[8:12] != VENDOR_PRODUCT or data[126] != 0:
        return None
    names = [data[i+5:i+18].rstrip(b' \n\x00')
             for i in (54, 72, 90, 108)
             if data[i:i+5] == b'\x00\x00\x00\xfc\x00']
    if b'Lontium Semi' not in names:
        return None
    if data[54:72] not in (ORIGINAL_DTD, OLD_FIXED_DTD, FIXED_DTD):
        return None
    result = bytearray(data)
    result[54:72] = FIXED_DTD
    result[127] = (-sum(result[:127])) % 256
    return bytes(result)


def connectors(timeout=15):
    for attempt in range(timeout):
        found = sorted(Path('/sys/class/drm').glob('card*-HDMI-A-*'))
        if found:
            return found
        time.sleep(1)
    return []


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true',
                        help='identify a supported attached board without changing anything')
    args = parser.parse_args()
    matched = 0
    changed = 0
    for connector in connectors():
        if (connector/'status').read_text().strip() != 'connected':
            continue
        data = (connector/'edid').read_bytes()
        fixed = compatible_edid(data)
        if fixed is None:
            print(f'{connector.name}: EDID not in this tested profile; left unchanged.', flush=True)
            continue
        matched += 1
        if args.check:
            print(f'{connector.name}: supported 720x720 display detected.', flush=True)
            continue
        if fixed == data:
            print(f'{connector.name}: 720x720 / 60.004 Hz profile already active.', flush=True)
            continue
        card, port = connector.name.split('-', 1)
        override = Path('/sys/kernel/debug/dri')/card.removeprefix('card')/port/'edid_override'
        if not override.is_file():
            raise RuntimeError(f'DRM debugfs override unavailable: {override}')
        backups = Path('/var/lib/square720')
        backups.mkdir(parents=True, exist_ok=True, mode=0o755)
        saved = backups/(connector.name+'-original.edid')
        if not saved.exists():
            saved.write_bytes(data)
        override.write_bytes(fixed)
        try:
            (connector/'status').write_text('detect\n')
            if '720x720' not in (connector/'modes').read_text().splitlines():
                raise RuntimeError('720x720 was not accepted by the HDMI driver')
        except Exception:
            override.write_bytes(b'reset')
            (connector/'status').write_text('detect\n')
            raise
        changed += 1
        print(f'{connector.name}: enabled Pi 4-compatible 720x720 timing at 60.004 Hz.', flush=True)
    if not matched:
        print('No display matching the tested board was found. Check the HDMI connection or contact the seller.', flush=True)
    elif not args.check and not changed:
        print('No further display changes required.', flush=True)
    # A missing/different display is normal at boot, but blocks installation.
    return 2 if args.check and not matched else 0


if __name__ == '__main__':
    raise SystemExit(main())
