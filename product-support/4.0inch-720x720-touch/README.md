# 4.0-inch 720×720 touchscreen

**English** | [简体中文](README.zh-CN.md)

## Product information

| Field | Recorded information |
| --- | --- |
| Customer lookup name | 4.0-inch 720×720 touchscreen |
| Form and connections | Square; HDMI video + USB touch. Initial 5.08-inch identification was corrected to 4.0 inches. |
| Validation status | Timing fix and touch verified on the sample. |
| Environment | Raspberry Pi 4B; Raspberry Pi OS Bookworm Desktop 64-bit; labwc/Wayland |
| SKU / ASIN / panel part number / PCB revision | Not established; match the actual item before using a repair |

## 1. No picture or flicker: verified EDID timing repair

| Timing | Reported | Corrected |
| --- | --- | --- |
| EDID name / vendor-product bytes / size | WKS / Lontium Semi; `5d734600`; 128 bytes | Identity retained |
| Active pixels | 720×720 | 720×720 |
| Pixel clock | 35MHz | 38.54MHz |
| Refresh | 54.492349Hz | 60.003861Hz (nominal 60Hz) |
| Horizontal front / sync / back | 46 / 5 / 41 | 46 / 6 / 40 |
| Horizontal / vertical totals | 812 / 791 | Unchanged |
| Vertical front / sync / back | 50 / 5 / 16 | Unchanged |
| Sync polarity | +H / +V | Unchanged |

The original odd horizontal sync width was rejected on the tested Pi. Making sync even allowed a picture, but clock correction was also needed to remove flicker. This is a host-side EDID override, not a monitor firmware flash.

Install the [display tools](https://github.com/tekgroaml/tekgroaml-pi-display-tools) first. Canonical profile names need 2.3.0+, rectangular touch layout needs 2.3.2+. Commands below select connector 1; replace 1 with 2 for connector 2. Save desktop work first: applying an override may restart the graphical session on both outputs. There is no automatic timeout rollback for `apply`.

```bash
screen-config list
screen-config profiles
screen-config apply --port 1 --profile 4.0inch-720x720-60hz-wks-lontium-semi
screen-test pattern --screen 1
screen-test touch --screen 1 --shape rect
```

Only after checking the physical screen, save:

```bash
screen-config apply --port 1 --profile 4.0inch-720x720-60hz-wks-lontium-semi --save
```

Rollback, when EDID/DDC reads work:

```bash
screen-config auto --port 1 --save
```

Rollback removes this tool's override and saved setting for that port; the original problem may return. Profile alias: `lontium-720`. Wrapper: `scripts/profiles/4.0inch-720x720-60hz-wks-lontium-semi.sh` in the tools repository. A profile mismatch must be investigated, not bypassed.

## 2. Touch missing, wrong screen, or offset

The tested touch controller reported `wch.cn USB2IIC_CTP_CONTROL`, VID/PID `1a86:e5e3`; this identity is not guaranteed for every batch. HDMI alone carries no touch input. Follow the [shared touch procedure](../_shared/README.md#2-touch-does-not-respond-or-reaches-the-wrong-position), including single-screen checks, identical controller names, same-model and mixed-model dual screens, USB/HDMI cable pairing, and reversed pairs. No cut-panel offset is appropriate for this square sample.

## 3. Cut-panel compensation

Not observed or required for this product. Do not apply the 6.2-inch offset.

## Acceptance and limits

Manual sample timing correction and touch operation were confirmed. Validate four borders, five targets, continuous strokes and stability on the actual item. Cold boot, sleep/wake, hot-plug, other batches and other platforms are not fully qualified by these records.

[Product index](../README.md) · [All tested scenarios](../_shared/README.md)
