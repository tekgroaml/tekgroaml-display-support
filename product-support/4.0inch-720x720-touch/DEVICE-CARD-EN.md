# 4.0-inch 720 × 720 Square Touchscreen

## Device information

Customer lookup name: **4.0-inch 720 × 720 square touchscreen**, HDMI video and USB touch. Size was confirmed by the customer; it is not inferred from EDID dimensions. The SKU, manufacturer part number and revision still need seller confirmation.

Tested environment: Raspberry Pi 4 Model B, Raspberry Pi OS Bookworm Desktop 64-bit, labwc/Wayland. This does not establish compatibility with every display of this size.

## Reported driver data

| Field | Original data |
| --- | --- |
| EDID label | WKS / Lontium Semi |
| Manufacturer/product identifier bytes | `5d734600` |
| EDID length | 128 bytes |
| Detailed mode | 720 × 720, 35MHz, approximately 54.492349Hz |
| Horizontal front porch / sync / back porch | 46 / 5 / 41; total 812 |
| Vertical front porch / sync / back porch | 50 / 5 / 16; total 791 |
| Sync polarity | Positive horizontal and vertical |
| Tested USB controller | `wch.cn USB2IIC_CTP_CONTROL`, VID/PID `1a86:e5e3` |

These are matching data, not a claim that the actual panel or controller chip part number has been identified.

## Issue

The original odd horizontal sync width can be rejected by the Pi 4 HDMI driver, leaving no accepted mode. Fixing only that width produced an image but did not establish stable operation.

## Repair data

The verified correction keeps 720 × 720 and totals 812 × 791, changes horizontal sync 5 → 6 and horizontal back porch 41 → 40, and changes the pixel clock 35 → 38.54MHz. The resulting rate is approximately **60.003861Hz**, described as nominal 60Hz in the filename. Vertical timing and sync polarities are preserved.

The repair is on the host. It does not flash monitor firmware. The historical manual sample worked; complete current-script cold-start and cross-revision acceptance remain pending.

## Repair script

Filename: **`4.0inch-720x720-60hz-wks-lontium-semi.sh`**.

Profile ID: `4.0inch-720x720-60hz-wks-lontium-semi`. Legacy alias `lontium-720` remains supported. Install version **2.3.0 or later retaining this ID** from the [tool repository](https://github.com/tekgroaml/tekgroaml-pi-display-tools).

Save graphical work first: profile application may restart the entire desktop. Keep SSH available. For connector 1 (`HDMI-A-1`, board HDMI0):

```bash
screen-config apply --port 1 --profile 4.0inch-720x720-60hz-wks-lontium-semi
screen-test pattern --screen 1
screen-test touch --screen 1
screen-test stop
```

Verify the physical picture and touch before persisting:

```bash
screen-config apply --port 1 --profile 4.0inch-720x720-60hz-wks-lontium-semi --save
```

After installing the application, the source directory also contains this convenience entry point:

```bash
bash scripts/profiles/4.0inch-720x720-60hz-wks-lontium-semi.sh --port 1
```

EDID matching remains mandatory. A successful command is not proof that the physical image is correct. Temporary application has no automatic countdown rollback. To clear the override and saved entry:

```bash
screen-config auto --port 1 --save
```

Original symptoms may return when the original EDID mode is restored. Use number 2 for `HDMI-A-2` (board HDMI1). Obtain rated power and wiring details from the specific product label; do not infer them from this profile name.

[Back to this product](README.md) · [Product index](../README.md)
