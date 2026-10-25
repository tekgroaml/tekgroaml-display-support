# Raspberry Pi Setup: 6.2-inch Touch Display Timing Profile

Customer lookup name: **6.2-inch 420 × 960 strip touchscreen** (verified input mode; native panel specification unconfirmed).

| Reported driver field | Original → repair |
| --- | --- |
| EDID label / identifier bytes | LTM / ZL480; `328d5e04` |
| EDID structure | 256 bytes, one extension |
| Input mode | 420 × 960 → unchanged |
| Pixel clock | 28MHz → 32.4MHz |
| Refresh | Approximately 51.851852Hz → 60Hz |
| H front / sync / back | 50 / 20 / 50, unchanged |
| V front / sync / back | 16 / 4 / 20, unchanged |
| Repair script filename | `6.2inch-420x960-60hz-ltm-zl480.sh` |

The formal ID requires tool 2.3.0 or later; the old ID `ltm-420x960-60` remains an alias for existing scripts/settings. The driver label is not a confirmed physical part number.

## Confirm the product first

This guide covers a seller-confirmed HDMI-video/USB-touch variant matching the tested sample. Tested host: Raspberry Pi 4 Model B, Raspberry Pi OS Bookworm Desktop 64-bit, labwc/Wayland.

The sample was stable with a **420 × 960 input signal at 60Hz** after correcting its pixel clock. Its manufacturer part number has not been established. `LTM ZL480` is an EDID/controller name, not a reliable panel model. Confirm your SKU and revision with the seller before using this profile.

**A non-touch sample reporting the same EDID continued flickering with this correction. It is not a supported success case.** Screen size, EDID name and even a complete EDID match cannot distinguish these variants. Do not describe this profile as a universal fix. A 360 × 960 trial also failed on the tested touch sample.

## Connections

Connect HDMI for video and a data-capable USB cable to the host for touch. Follow the display's own power label and wiring diagram. A USB cable connected only to a charger does not send touch data to the host.

Brightness pulsing may require a separate power comparison. A Raspberry Pi showing no undervoltage record does not establish that the display's own supply is stable. Use only a supply compatible with the display's rated specifications.

## Port numbers and tool version

| Number | Commands | Linux connector | Board connector |
| --- | --- | --- | --- |
| 1 | `--port 1` / `--screen 1` | HDMI-A-1 | HDMI0, next to USB-C power |
| 2 | `--port 2` / `--screen 2` | HDMI-A-2 | HDMI1 |

Obtain version **2.3.0 or a later release that retains this profile name** from [TEKGROAML Pi Display Tools](https://github.com/tekgroaml/tekgroaml-pi-display-tools), and follow its installation guide. Older installations without the `pi-setting` manager need the new package's `sudo bash scripts/install.sh` entry point for the first upgrade.

```bash
screen-config --version
screen-config profiles
screen-config list
screen-config modes --port 1
```

The examples below use port 1. If connected to port 2, replace both `--port 1` and `--screen 1` with 2.

## Why the timing correction is different from auto-detection

The sample's original preferred timing is 420 × 960, 28MHz pixel clock and totals of 540 × 1000, giving approximately 51.85Hz. `auto` selects that original preferred mode again. `set` only selects modes already exposed by the system.

The profile keeps the resolution, sync polarities and porches unchanged, and changes only the pixel clock to **32.4MHz**, producing **60Hz**. This is a host-side EDID override, not a display or touch-controller firmware update.

## Apply temporarily first

Save work in graphical applications and keep SSH available. Applying the profile restarts the desktop, closes graphical windows and can briefly blank every connected display.

Only after confirming the product variant with the seller:

```bash
screen-test stop
screen-config apply --port 1 --profile 6.2inch-420x960-60hz-ltm-zl480 --confirm-profile
screen-config list
```

`--confirm-profile` acknowledges these product limitations; it does not bypass EDID checks. Unknown controller IDs, names, structures or timing descriptors are rejected. A successful command confirms host-side output, not that the physical panel is operating correctly.

This command has no `--save`, so it does not add a persistent startup setting. **There is no automatic countdown rollback in this command.** Restore manually if the result is worse. A reboot clears a temporary override, but a previously saved profile may be reapplied; use the restore command below to remove it.

## Verify the physical display

Check the complete image, edges, brightness stability and touch accuracy:

```bash
screen-test white --screen 1
screen-test pattern --screen 1
screen-test touch --screen 1
screen-test tap-cycle --screen 1
screen-test stop
```

`tap-cycle` starts black; each finger press advances to white, red, then black. `touch` provides targets and movement trails. The display timing profile does not repair a missing USB data connection or incorrect touch mapping. If touch operates another monitor, confirm the USB-to-HDMI cable pairing with support.

## Save only after a successful test

After confirming a stable image on the correct product variant:

```bash
screen-config apply --port 1 --profile 6.2inch-420x960-60hz-ltm-zl480 --confirm-profile --save
```

The saved entry includes the port, EDID identity, profile and acknowledgment. Test login, reboot and cold startup separately. Another device reporting the exact same EDID can still match; clear the old profile before swapping physical displays. Software cannot infer an absent manufacturer part number.

## Restore or change displays

```bash
screen-test stop
screen-config auto --port 1 --save
```

This clears the program-managed override and saved entry for that port, then returns to the original preferred timing. The original flicker may return because the original approximately 51.85Hz mode is restored.

If brightness still pulses or the image is incomplete, stop changing timings blindly. Send support your SKU, controller label, current mode, power connections and a short video. The non-touch sample needs separate diagnosis; this profile is not a verified remedy for it.

[Back to this product's support page](../README.md)
