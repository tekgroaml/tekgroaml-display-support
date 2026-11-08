# Non-touch dual-screen records awaiting size identification

**English** | [简体中文](README.zh-CN.md)

These are provisional support records, not four newly identified SKUs. Each panel was used with a 480×480 layout, but size, advertised/native resolution, SKU and board revision are not confirmed; all four dual-screen configurations are confirmed non-touch. They are kept outside the size-sorted catalog until those details are matched to an order or product label. Do not merge them into the 2.8-inch product by resolution alone.

| Shape / display relationship | Input observed in the session | Symptoms and guide |
| --- | --- | --- |
| Round / different content | One 960×480 signal, approximately 62.825Hz | [Blank after swapping; choosing the two-region app](480x480-round-dual-sbs-nontouch/README.md) |
| Square / different content | One 960×480 signal, approximately 62.825Hz | [Only one panel displayed; both returned after reconnecting](480x480-square-dual-sbs-nontouch/README.md) |
| Round / same content | One 480×480 signal; approximately 62.811Hz on an earlier connection, 71.295Hz on a later one | [App rejects the new board's input; no forced 60Hz](480x480-round-dual-clone-nontouch/README.md) |
| Square / same content | One 480×480 signal, approximately 62.811Hz | [Desktop works but app rejects refresh rate](480x480-square-dual-clone-nontouch/README.md) |

## Is the input one picture or two side-by-side regions?

A **hardware-copy (clone) board** receives one picture and sends it to both panels. An **SBS board** receives a double-width picture and sends half to each panel. Both can use one HDMI cable and appear as one logical monitor. An SBS app can repeat its image to show the same content, but this does not make a hardware-copy board accept a double-width signal.

The observed rates above identify connection records, not recommended target rates or proven glass specifications. Do not change clocks or firmware to make an app's layout check pass. Check connections first, then the actual signal and matching app version.

The seller confirmed that the current dual-screen kits are non-touch. The 2.1-inch and 2.8-inch single-screen ranges have touch models; this does not establish the size of each dual-screen record. Do not assign a kit to either size without confirmation.

## How these entries will become product pages

Match the per-panel inch size, advertised resolution, order/SKU and board revision; preserve the confirmed non-touch option. Move each record into the verified size-based product directory, preserve links, and distinguish batches that differ. Earlier and later round same-content connections are not assumed to be the same board. Historical no-picture and touch records for other products remain separate.

Original tests: 2026-11-01. Documentation: 2026-11-08. Round different-content physical flight output and the square different-content reconnect result were buyer-confirmed. Other same-content evidence is app launch/runtime evidence, not a new physical acceptance. Windows, cold boot and other batches remain unverified for these kits.

[All products](../README.md) · [Shared troubleshooting](../_shared/README.md)

The seller has now confirmed two non-touch dual-screen sizes: [2.1-inch](../2.1inch-480x480-dual-nontouch/README.md) and [2.8-inch](../2.8inch-480x480-dual-nontouch/README.md), both 480×480 **per panel**. The remaining uncertainty is which earlier shape/layout record belongs to which size/board, not whether these two sizes exist. The single-screen touch variants are separate.
