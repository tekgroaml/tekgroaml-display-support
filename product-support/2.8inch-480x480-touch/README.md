# 2.8-inch 480×480 single-screen touchscreen

**English** | [简体中文](README.zh-CN.md)

The seller confirmed that the 2.8-inch single-screen range has a touch model. Check the touch option and resolution on your order. The seller confirmed a 480×480 resolution. Model-specific touch acceptance is still pending; resolution confirmation alone is not a completed test. This is separate from the non-touch dual-screen kits.

## The screen goes black or flickers after moving a cable

Wait about 10–15 seconds without moving the cables. If the picture does not return, reconnect HDMI and USB power firmly at both ends. Try another cable if it happens repeatedly, and follow the product's power requirements.

## Touch does nothing

Connect the USB power/touch **data** cable to the same computer or Pi sending the HDMI picture. A wall charger or charging-only cable cannot carry touch input to the host.

## Touch operates another screen

Test this screen with its HDMI and USB cable first. If it still reaches another display on Windows, follow the [Windows touch setup steps](../../platforms/windows/README.md). These checks are general guidance, not a completed product-specific acceptance test.

## Optional Raspberry Pi steps

Install the [display tools](https://github.com/tekgroaml/tekgroaml-pi-display-tools) and log into the graphical desktop first. These commands do not run on Windows. Use connector 2 instead of 1 if connected there:

```bash
screen-config list
screen-config modes --port 1
```

Share the listed resolution, a product-label photo and any remaining symptom with support. No specific timing override or calibration is confirmed for this entry; do not apply another product's profile.

[Product directory](../README.md)
