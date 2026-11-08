# 2.8-inch dual-screen kit, 480×480 per screen, non-touch

**English** | [简体中文](README.zh-CN.md)

The seller confirmed this 2.8-inch dual-screen option has **two 480×480 panels and no touch**. Check your order for round/square shape and same/different-content options. These options use different layouts; their exact mapping to the earlier test boards has not been established.

## One or both screens stay black or flicker after a cable is moved

Wait about 10–15 seconds, then firmly reconnect HDMI and USB power if the picture does not return. Test with known-good cables and the specified supply. Do not reseat internal panel ribbons while powered. Send a photo showing both screens and the board label if it still fails.

## Windows shows one display number, but there are two panels

This can be normal when one driver board feeds both panels from one HDMI cable. **480×480 is each panel's resolution.** A same-content board can receive one 480×480 picture; a side-by-side different-content board can receive a combined 960×480 picture. Check the actual modes offered for your board; do not force one input for every kit.

## Tapping either screen does nothing

This kit is non-touch. USB power does not add touch support. The 2.8-inch single-screen range also has touch models, sold as a separate option.

## Which applications suit same or different content?

**For these one-HDMI kits, same content repeats the full picture on both panels; different content uses a left/right picture prepared by the app, with one part on each panel.** “Mirroring” here duplicates the picture in the same reading orientation; it does not reverse text horizontally.

| Content / shape | Applications | Two-panel arrangement |
| --- | --- | --- |
| Same / round | Music visualization, RGB ambience, desktop clock | Identical spectrum/light/time for symmetry or opposite viewers |
| Same / square | Retail offers, meeting-room status, parcel pickup | The same product/room/parcel information on both sides of a counter |
| Different / round | Flight, automotive instruments, PC monitoring | Left attitude/right airspeed; speed/engine; CPU/GPU |
| Different / square | Smart home, PC case, industrial equipment | Left environment/right energy; CPU/cooling; pump/trends |

Choose the shape and option on your order. This table does not mean every combination is sold or physically tested at this size. Existing Pi showcases use simulated data; the music demo is silent. Real prices, calendars, shipments, weather and device data are not connected automatically.

Each showcase introduces brand/use case for 3s, then runs effects for 10s; three chapters loop in 39s. Same-content introductions/effects match on both panels. Different-content introductions show brand/use case on separate panels, followed by different effects. See [use cases and board diagrams](../_shared/dual-screen/README.md) for the full explanation and script entrypoints.

## Which demo should I use?

Choose the matching shape and same/different-content layout. These links describe earlier connection tests, **not proof that every shape/layout has been tested at this size**:

- [Round / same content](../_unconfirmed/480x480-round-dual-clone-nontouch/README.md)
- [Round / different content](../_unconfirmed/480x480-round-dual-sbs-nontouch/README.md)
- [Square / same content](../_unconfirmed/480x480-square-dual-clone-nontouch/README.md)
- [Square / different content](../_unconfirmed/480x480-square-dual-sbs-nontouch/README.md)

Start with the [Windows checks](../../platforms/windows/README.md) when using a PC. Raspberry Pi commands in the linked demo pages are not Windows programs. No size-specific timing correction, universal 60Hz setting or touch calibration is claimed here.

## How does the board distribute one picture to two panels?

<details>
<summary>Show hardware copying and side-by-side splitting</summary>

“Driver” here means the hardware board and its firmware driving both panels, not a Windows driver you must install.

- **Different-content board (SBS):** the host/app prepares one combined left-A/right-B image. The board sends the left half to panel 1 and the right half to panel 2. For two 480×480 panels, a matching input example is 960×480. The app lays out both views beforehand; the board does not redesign an ordinary page into two complete interfaces.
- **Same-content board (hardware clone):** the host supplies complete A, and the board copies it to both panels. Each shows complete A in the normal reading orientation. Example input: 480×480, without a horizontal flip.
- **SBS software duplication:** the app prepares `[A | A]` in a double-width image, then the SBS board splits it. Both panels match, but still require double-width input rather than the single input used by a hardware-copy board.

One HDMI kit may occupy one OS monitor entry. Windows Duplicate/Extend controls host outputs, not the board's internal mapping. Use board documentation and actually offered modes; do not force all kits to 960×480 or 60Hz. Software duplication does not mean a copy board can be converted to different content.

[Picture-flow diagrams, use cases and Pi commands](../_shared/dual-screen/README.md). These explanations do not replace per-size, board or batch acceptance.

</details>

## Confirmed information and remaining details

Seller-confirmed: 2.8 inches per panel, two panels, 480×480 per panel, non-touch. Pending: order/SKU, board revision, shape/layout assignment and per-size physical acceptance. Observed refresh rates belong to the linked connection records; they are not new recommended product specifications.

[Product index](../README.md)
