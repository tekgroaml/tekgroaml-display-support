# Round dual-screen kit, 480×480 input, same content; non-touch; size unconfirmed

**English** | [简体中文](README.zh-CN.md)

This is a provisional connection record, not an identified SKU. These dual-screen kits are confirmed non-touch. Check your order and each panel's size. The 480×480 description comes from the input/layout record; advertised and native panel specifications are not established. Do not identify it as the existing 2.8-inch product from resolution alone.

## The desktop appears, but the demo stops after swapping the screen

A hardware-copy board needs one square picture, not the double-width picture used by an SBS kit. A different board can also advertise a different refresh rate.

1. Leave the cables still for about 10–15s. If the picture does not return, firmly reconnect HDMI and USB power at the host and board. Use the rated supply; never reseat internal panel ribbon cables while powered.
2. Confirm whether one HDMI board drives both panels, and whether it copies one image or splits left/right content. Two panels do not necessarily mean two host display entries.
3. In Windows, inspect the modes actually offered in [Display settings](../../../platforms/windows/README.md). On the Pi, ensure the graphical desktop is logged in. Hardware-copy and SBS boards require different complete inputs, explained below.
4. Both physical circles should show the same complete image, with the spectrum, light effect or clock moving. A running app alone cannot confirm that both panels received it.

If unresolved, send a photo showing both panels, backlight state, host/OS, supply rating, HDMI/USB connections and board label. Do not repeatedly apply other products' profiles. There is no guaranteed software cure for an unidentified fault.

## Windows shows only one display number. Is one panel missing?

One logical output can be normal when one HDMI board drives two panels. Windows Duplicate/Extend controls host outputs; it cannot automatically change the board's internal copy/split design. Pi programs in this repository are not Windows drivers. Full Windows product acceptance has not been completed for this kit.

## Touch does not work, or an edge is missing

This dual-screen kit is **non-touch**, as confirmed by the seller. Tapping either panel does nothing; this is expected and does not need touch calibration or a USB touch-mapping script. USB power does not add touch capability. The 2.1-inch and 2.8-inch single-screen ranges have touch models; they are separate product options.

No cut-panel window was measured for this kit. Do not apply the 6.2-inch panel's 60-column compensation. Check input, shape and application layout first. Hidden square corners on round glass are not themselves a cut-panel fault.

## Optional: Raspberry Pi checks and demo

<details>
<summary>Show Pi commands (not Windows)</summary>

Tested environment: Pi 4B, Bookworm Desktop 64-bit, labwc/Wayland. Read-only identification uses separately installed version 2.3.2+ of the [display tools](https://github.com/tekgroaml/tekgroaml-pi-display-tools); install them first if commands are absent. Demos come from the independent [dual-display app repository](https://github.com/tekgroaml/lvgl-embedded-gui-demos). Use **v0.10.2 or a later compatible release** for these instructions so the recorded refresh rates are accepted.

Inspect without changing modes:

```bash
screen-config list
screen-config modes --port 1
```

This record used **480×480 at approximately 71.294998Hz**. Inspect other batches independently; do not force this value. Public connector 1/2=Linux HDMI-A-1/2=Pi 4 board HDMI0/1, not the left/right panel. Change 1 to 2 throughout if wired to connector 2.

Follow the app repository's full installation instructions. Stop an old running version using its existing code before updating the complete directory; do not overwrite running programs. `screen-config` and `./app` belong to different projects.

From the complete app directory, over SSH as the same ordinary logged-in desktop user, without sudo:

```bash
cd ~/apps/lvgl-embedded-gui-demos
./app --version
# Stop this project's previous scene; use the owner's stop command for other projects
./app stop --port 1
./demos/same/round/demo check --port 1 --signal clone
./demos/same/round/demo start --port 1 --signal clone
```

If an installed screen-test owns the output, first use `screen-test stop --screen 1`. The showcase is **Music visualization → RGB ambient lighting → desktop clock**, with 3s brand/use-case introductions and 10s effects, 39s loop. It is a demo, not an EDID repair, driver installer or whole-desktop compensation.

Later inspect/stop separately:

```bash
./demos/same/round/demo status --port 1
./demos/same/round/demo logs --port 1 --follow
./demos/same/round/demo stop --port 1
```

These app commands preserve the current input signal, do not restart the desktop or flash firmware, and have no timed rollback. Failure does not create a missing mode. start stays in the background after SSH exits while the desktop remains logged in. Disconnecting/changing modes can end the app; after reconnecting stably, check/start again. Stopping the demo only closes this project's window; it does not undo system settings changed by another tool.

If check rejects geometry/rate, verify clone versus SBS, the actual output and app version. Do not force 60Hz or arbitrary EDID merely to pass the check. With no unique Wayland session, log into the graphical desktop first. `running/ok` is runtime evidence; inspect both physical panels.

</details>

## Product data, explanation and validation

<details>
<summary>Show input data, compatibility changes and evidence</summary>

| Field | Known information |
| --- | --- |
| Size / advertised resolution / native panel resolution | Unconfirmed; not inferred from EDID name or input mode |
| Form / content | Round / same content; two panels on one HDMI |
| Touch option / USB controller / VID/PID | Non-touch, seller confirmed; touch controller and touch acceptance not applicable |
| SKU / ASIN / batch / part number | Unconfirmed; this is not SKU or cross-batch certification |
| Environment / dates | Pi 4B, Bookworm 64-bit, labwc/Wayland; original session 2026-11-01, documentation 2026-11-08 |

| Driver / app data | Record |
| --- | --- |
| Later round-board preferred/current input | 480×480 at 71.294998Hz |
| Later EDID detailed timing | 128-byte EDID; 25.21MHz; calculated 71.295249Hz; complete porch/polarity record not retained here |
| Earlier observed connection | 480×480 at 62.811001Hz; do not assume the same SKU/revision |
| App mapping | single-link-clone; one 480×480 canvas duplicated by the board |
| 0.10.2 clone 480 acceptance | 60 / 62.811001 / 71.295249Hz, tolerance ±0.1Hz; mapping version 1.1.0 |
| Changed by this compatibility update | App/layout acceptance only; no HDMI clock, timing or screen firmware change |

### Confirmed scope

An earlier connection used 480×480 at 62.811001Hz. A later round kit on 2026-11-01 advertised 480×480 at 71.294998Hz as preferred/current. The relationship between the boards/batches is unconfirmed. Version 0.10.2 accepted the later advertised signal and launched the round same-content showcase with advancing frames and running/ok status; no separate buyer confirmation of both physical panels was retained.

### Not established

Size, advertised resolution, actual controller/PCB revision, Windows, cold boot, sleep/wake, long-term stability and other batches lack full acceptance. Missing detailed timings are not guessed. Matching EDID labels/rates do not prove the same product. No dedicated `screen-config apply --profile` repair or assumed-size repair script exists for this record.

An app accepting a layout does not mean screen timings were corrected. This evidence does not support forcing every screen to 60Hz or promising an app update cures black screens.

[Upstream verification](https://github.com/tekgroaml/lvgl-embedded-gui-demos/blob/main/docs/verification.md) · [Upstream v0.10.2 commit](https://github.com/tekgroaml/lvgl-embedded-gui-demos/commit/3d4dd083bc9b07216b5186cd3e8a3188d358d53c)

</details>

[Provisional products](../README.md) · [All products](../../README.md) · [Shared troubleshooting](../../_shared/README.md)
