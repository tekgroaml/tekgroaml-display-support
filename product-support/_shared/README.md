# Shared troubleshooting and tested scenarios

**English** | [简体中文](README.zh-CN.md)

## Before changing settings

- **Black or flickering after moving a cable?** Leave it still and wait about 10–15 seconds. If it does not recover, unplug and firmly reconnect HDMI and USB power; try another cable if movement keeps causing it.
- **No touch, or touch on another screen?** For a touch model, plug its USB power/touch data cable into the **same computer that sends the picture**, not just a charger. Check each screen's HDMI and USB as a pair. A charging-only cable cannot carry touch.
- **Using Windows?** Start with the [Windows picture and touch steps](../../platforms/windows/README.md). The Raspberry Pi commands in this repository do not run on Windows.

## One HDMI drives two panels: check the input design

One logical monitor can be normal. A hardware-copy board duplicates one picture; an SBS board splits a double-width picture. These sessions used 480×480 for hardware copy and 960×480 for different-content SBS, but that is not a universal dual-screen specification. [Choose the sample record](../_unconfirmed/README.md); size and touch options remain unconfirmed.

For one dark panel, check cables, power and the board first. A complete two-region screenshot does not rule out a physical fault. If a demo stops after changing boards, inspect input/layout compatibility instead of applying another product's timing profile or forcing 60Hz.

## Optional Raspberry Pi commands and support records

<details>
<summary>Show technical steps for Raspberry Pi (not Windows)</summary>

Updated 2026-11-08. Use the [product index](../README.md) first. Procedures apply to the tested Pi 4B / Bookworm Desktop 64-bit / labwc environment; they are not a universal driver package. Tools: [TEKGROAML Pi Display Tools](https://github.com/tekgroaml/tekgroaml-pi-display-tools). Install the tools and dependencies before running commands. Use 2.3.2+ for `--shape rect`; the cut-panel demo lives in this support repository, not in stock `screen-test`.

| Public number | Linux connector | Board label | USB cable label after confirmed pairing |
| --- | --- | --- | --- |
| 1 | HDMI-A-1 | HDMI 0 | USB-TOUCH-1 |
| 2 | HDMI-A-2 | HDMI 1 | USB-TOUCH-2 |

Numbers identify connectors, not desktop left/right order or another OS's display numbering. Examples select screen 1; change to 2 where needed. Run rendering tests as the logged-in desktop user over SSH, without sudo. Display configuration commands request root as needed. HDMI carries video; USB data carries touch; power requirements come from the item specification.

## 1. No picture, flicker, or an EDID read error

For the 4.0-inch square and an earlier 6.2-inch touch sample, EDID/timing correction addressed documented symptoms. **Not every black screen or flicker is an EDID problem.** The non-touch strip's brightness pulsing and the 2.8-inch black screens remain unresolved.

1. Confirm the exact product, rated power, backlight and connectors. Test one display and known-good cables first. A Pi undervoltage flag does not measure the voltage at the screen.
2. Inspect connection, enabled state, current mode, EDID override and available modes:

   ```bash
   screen-config list
   screen-config modes --port 1
   ```

3. Select an advertised mode only if it matches the product. `set` cannot add missing timings. `auto` selects the preferred advertised mode after validating EDID; an incorrect EDID can select an incorrect mode.
4. Use a documented compatibility profile only for the corresponding verified controller/timing. EDID names such as ZL 480, EDID physical millimetres and serial strings do not establish panel dimensions, SKU or chip model.
5. Verify the physical screen, not only CLI output or screenshots:

   ```bash
   screen-test white --screen 1
   screen-test pattern --screen 1
   screen-test cycle --screen 1 --interval 5
   screen-test stop
   ```

White tests illumination; pattern tests borders and geometry; cycle runs black/white/red. Observe brightness and all four borders. Do not save until the actual result passes. Most normal profile commands have no timed rollback and may restart the graphical session; keep SSH access and save open work first.

`[Errno 121] Remote I/O error` was reproduced on a direct EDID/DDC read. HDMI hot-plug detection can still say connected while EDID is unreadable. Recheck screen power, HDMI contacts, cable/adapters and another host. A 1024×768 fallback is not evidence of a 1024×768 panel. Do not force a random EDID to hide the read error. `auto --save` is not a guaranteed recovery command when DDC fails.

If a complete system screenshot differs from the physical picture, investigate downstream cropping/windowing; a screenshot cannot measure the visible glass. Use the cut-panel product procedure if its measured geometry matches.

## 2. Touch does not respond or reaches the wrong position

| Symptom | Action and observed result |
| --- | --- |
| HDMI picture but no touch | Check a USB **data** cable and the correct touch socket. A power-only cable does not provide input. |
| No visible feedback | `screen-test cycle` changes colors by time; it is not a touch test. Use `touch`, which shows targets and trails. The test later gained mouse/emulated input handling as some setups did not deliver native touch; test with a finger to distinguish it from a real mouse. |
| Both touchscreens control one output | Same-model **and different-model** panels may use identical-name controllers without unique serials. Identify each by physical taps and bind USB paths separately. This was confirmed corrected in the debugging session. |
| Exactly reversed screens | Swap the two confirmed source-device arguments, reconfigure and retest. One initial pairing was reversed; exchanging the pairs corrected it. |
| One touch + one non-touch screen | Map the sole touch controller only to its own display. This was confirmed corrected. The two-device setup script requires two actual touch controllers; do not use it for this case. |
| Correct output, position offset everywhere | Check rotation, scale, old calibration and panel/display alignment before adding calibration. |
| Right targets close, left targets increasingly offset on the cut strip | Use the measured cut-panel canvas and touch transform together; a constant translation is insufficient. |
| Touchscreen not connected, but targets requested | Targets can still be displayed; absence of touch hardware does not suppress video. |

### On-screen tests

```bash
screen-test touch --screen 1 --shape rect
screen-test touch --screen 2 --shape round
screen-test tap-cycle --screen 1
screen-test status
screen-test stop
```

`rect` uses center/corner targets; `round` uses center/cardinal targets. Layout selection does not calibrate input. `tap-cycle` advances black → white → red on a new press; holding/dragging does not continuously advance. Outputs change independently. Targets and trails are better for coordinate checks. A 5/5 pass is only a five-point sample, not full calibration or multitouch qualification.

### Confirm two USB/HDMI pairs

1. Tap only physical screen 1 and record its source controller; repeat for screen 2. Do not infer pairing from `eventN`, USB topology numbers or enumeration order. With the relay active, it exclusively grabs mapped physical sources; monitoring those raw nodes can show no events. Observe the corresponding virtual node or deliberately stop the relay during controlled identification.
2. From the display-tools source directory, with `python3-evdev` installed, use confirmed original devices. `eventN`, `eventM` and `YOUR_DESKTOP_USER` are placeholders, not commands to copy unchanged:

   ```bash
   sudo python3 scripts/configure-touch-map.py \
     --screen1-device /dev/input/eventN \
     --screen2-device /dev/input/eventM \
     --user YOUR_DESKTOP_USER
   ```

3. The program stores USB-path associations in `/etc/pi-setting/touch-map.json`, creates uniquely named virtual devices and labwc output mappings, and enables `pi-setting-touch.service`. Version 2.3.1+ also creates `/dev/input/USB-TOUCH-1` and `/dev/input/USB-TOUCH-2` through udev rules. Existing internal virtual names `PiSetting Touch HDMI0/1` map to public outputs 1/2; they do not change public numbering.
4. Reload labwc from the desktop user's SSH session **only after confirming this user has one compositor session**:

   ```bash
   pgrep -a -u "$(id -u)" -x labwc
   pkill -HUP -u "$(id -u)" -x labwc
   screen-test touch
   ```

   If there is more than one session, target the verified PID instead. Check service/logs with `systemctl status pi-setting-touch.service` and `journalctl -b -u pi-setting-touch.service --no-pager`.
5. Label paired HDMI and USB cables, and keep the same host USB sockets/hub topology. USB path `1.1` does not inherently mean HDMI 1. Re-identify after swapping sockets, hubs, controller types or screen assignments. Pairing/name persistence exists; the cut-screen coordinate correction is a separate application-only experiment.

The setup script backs up the previous map and labwc config; current versions also back up their naming rule. To undo, restore the matching backups, restart the relay and reload labwc; restore/reload udev rules too if labels changed. Stopping the relay (`sudo systemctl disable --now pi-setting-touch.service`) releases raw devices but can bring back old generic mapping conflicts. Do not restore another customer's paths.

## 3. Test UI absent after hot-plug, logout, or SSH reconnect

A hot-swap case reported `touch` active with no application error, yet a screenshot showed only the desktop. Restarting the test process restored the grid:

```bash
screen-test stop
screen-test pattern --screen 1
```

This is a verified recovery step for that session, not a published automatic hot-plug fix. Non-touch screens can display patterns and targets. If no Wayland session exists, log into the graphical desktop; SSH login alone does not start it. Restarting the display manager closes graphical applications and should not be the first generic step. An SSH `Broken pipe` means the remote terminal connection was lost; inspect network/power/reboot state separately. Keepalive can reduce idle disconnects, not repair physical display faults.

## 4. A two-panel demo stops after a board change or rejects the mode

The 2026-11-01 sessions recorded distinct inputs: 960×480 at ~62.825Hz for two 480 SBS panels; 480×480 at ~62.811Hz for hardware copy; and ~71.295Hz on a later round copy board. Do not assume these connections identify one SKU. Labels such as DELL U 2410 in EDID do not establish size or manufacturer.

The later ~62.811/~71.295Hz compatibility changes updated layout acceptance in the separate [app repository](https://github.com/tekgroaml/lvgl-embedded-gui-demos). They did not change HDMI timings or screen firmware and did not create screen-config repair profiles. App v0.10.2 includes four script families. Follow its full upgrade instructions: stop the old version, copy the complete project, and use the logged-in desktop user over SSH without sudo.

| Content / shape | Script | Input recorded |
| --- | --- | --- |
| Same / round | ./demos/same/round/demo | 480×480 clone, observed ~62.811 or 71.295Hz |
| Same / square | ./demos/same/square/demo | 480×480 clone, observed ~62.811Hz |
| Different / round | ./demos/different/round/demo | 960×480 SBS, observed ~62.825Hz |
| Different / square | ./demos/different/square/demo | 960×480 SBS, observed ~62.825Hz |

See the [four sample entries](../_unconfirmed/README.md) for complete commands and physical acceptance limits. Same-content scripts default to clone; explicit --signal sbs selects double-width software duplication. The square same-content SBS layout does not accept~62.825Hz, so do not transfer the square different-content profile's acceptance to it.

A disconnected or changed output can end the app. After reconnecting power/video stably and logging into the desktop, stop the old instance and check/start the matching script. Automatic restart is not established. Normal stop closes the app; there is no timing change, timed rollback or reset of system settings made by other tools. Legacy command adapters do not replace a full upgrade.

All demos use simulated data and no sound. No touch interaction does not mean a non-touch product. Pi 4B has no onboard speaker; a device named Built-in Audio is an output, not proof of a screen speaker. An unsuccessful HDMI audio trial did not establish its cause or prove a faulty/speakerless display.

## Test coverage record

| Scenario | Recorded conclusion |
| --- | --- |
| 4.0-inch 720-square rejected/odd timing and flicker | Manual timing repair passed; repeat batch/boot qualification |
| 3.4-inch 800-round after a 720-square | Native advertised mode selection restored stable picture |
| Same-model dual touch / identical controllers | Separate USB-path relays and output mappings passed |
| Different-model dual touch / identical controllers | Same method; physical identification required |
| Incorrect USB/HDMI pairing | Swapping confirmed pairs passed |
| One touch + one non-touch | Sole controller bound back to its output; passed |
| Color cycle / touch targets / press-to-change color | Implemented; distinguish temporal color test from position validation |
| Rectangular target layout | Implemented in 2.3.2; does not calibrate |
| Hot-plug leaves state active but overlay absent | Stop/start restored the test; automatic recovery not established |
| 6.2 touch original timing vs 60Hz | Earlier flicker improved; crop remained |
| 6.2 non-touch brightness pulsing | Unresolved; independent supply comparison outstanding |
| Cut strip with 360-input and porch experiments | Did not establish a complete picture |
| Cut strip with rightmost 360-column content window | Customer confirmed complete visible image |
| Cut strip with matching touch scaling | Customer confirmed accurate sampled touch; app-only |
| 2.8-inch pair, black / one DDC read failure | Unresolved; later SSH timeout prevented further confirmation |
| 480×480 units before 2.8-inch identification | Resolution observed, size/touch not conclusively associated; not promoted to another product |
| Round SBS 960×480 at ~62.825Hz | Buyer confirmed complete, different flight pictures and changing data |
| Square SBS with one dark panel | Buyer confirmed both returned after reconnecting; cable/power cause not isolated |
| Mixing 480×480 clone with 960×480 SBS | Match the actual input/layout; not an EDID repair |
| Square copy at ~62.811Hz | v 0.10.1 accepted input and looped; physical result pending |
| Round copy at ~71.295Hz | v0.10.2 accepted preferred input, frames advanced; physical result pending |
| New dual kits: touch / Windows | Seller confirmed non-touch; Windows remains unverified |

The early 5.08-inch claim was corrected to 4.0 inches, not treated as a separate tested SKU. No firmware-encryption determination, firmware dump or reflash was completed. Dual-panel apps were subsequently implemented and checked on the Pi. Round SBS flight and square SBS reconnection have buyer-confirmed physical results; same-content physical completeness remains unconfirmed. This does not qualify every scene or batch.

[Product index](../README.md) · [Support home](../../README.md)

</details>

Product clarification: the current dual-screen kits are non-touch. Touch models are available in the 2.1-inch and 2.8-inch single-screen ranges; availability alone is not touch acceptance or a size assignment for the dual kits.
