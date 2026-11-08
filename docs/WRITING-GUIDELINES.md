# Writing requirements for buyer-facing FAQs

**English** | [简体中文](文档书写要求.md)

Use these requirements for the support home, product FAQs, shared troubleshooting and Windows guides. Technical support records can contain detailed data, but should not open a buyer-facing page. Use the [buyer-page template](../product-support/DEVICE-TEMPLATE.md) for new entries.

## 1. Audience and voice

Write for someone who bought a screen and wants to use it. Sound like a helpful seller: brief, natural and direct, with one action or idea per sentence.

- Describe visible symptoms: “the screen stays black,” “the picture flickers,” “the left side is missing,” or “touch controls the other screen.”
- Usually give three to five simple steps per issue. Link or expand special cases rather than mixing several failures into one long explanation.
- Buyers should not need to understand EDID, pixel clocks, porches or coordinate matrices to begin troubleshooting.
- Keep development history and machine-specific session details out of the opening instructions.
- If there is no confirmed fix, say so. Never promise that running a command will definitely solve the issue.

| Avoid opening with | Say instead |
| --- | --- |
| A DDC read failure caused an EDID fallback | The computer detects the screen, but it stays black. Check power and HDMI first. |
| The input device has an incorrect output mapping | Tapping the small screen controls another screen. Check each screen's two cables first. |
| The active window and coordinate scale do not match | The left side is missing and touches miss more toward the left. Try the matching compensated demo. |

## 2. Page order

1. **Confirm the product:** title with size, advertised resolution and touch option; one sentence asking the buyer to check the order.
2. **Describe the symptom:** headings use what the buyer sees, not a protocol name or an assumed diagnosis.
3. **Explain what to try:** wait, reconnect, check power, then built-in OS settings; do not lead with scripts.
4. **Explain a pass:** all borders visible, stable picture, touch on the intended screen, marker following the finger.
5. **If it still fails:** give a next step and request only the necessary photos, wiring and computer details.
6. **Optional Raspberry Pi instructions:** commands come after basic checks and can be collapsed.
7. **Technical details and product data:** end with expandable parameters, formulas, evidence and limits.

Use “what you see → what to do → how to check / what next,” followed by the explanation. Keep necessary applicability limits beside the action, such as “touch model only” or “inside this test app only.”

## 3. First checks to prioritize

### Black screen or flicker after moving a cable

First ask the buyer to leave the cables still and wait about 10–15 seconds. If it does not recover, unplug and firmly reconnect HDMI and USB power at both ends. If movement repeatedly causes the issue, try a replacement cable. Test one screen first and use the power connection specified for the product.

The waiting time is a suggestion, not a guaranteed recovery time. Do not start with resolution changes, firmware flashing or driver installation.

### No touch or touch on the wrong screen

Explain that the touch model's supplied USB power/touch cable also carries data. It must connect to **the same computer or Raspberry Pi that sends the picture**, not only to a wall charger. A charging-only cable does not carry touch.

For two screens, check each HDMI/USB pair and test one screen at a time before reconnecting both. If the wiring is correct but routing remains wrong, explain the OS display-assignment step. Connecting to the same host does not guarantee every routing problem is solved. Do not imply a non-touch model gains touch through USB.

### Cropped picture or offset touch

Check picture completeness and the target screen before calibration. Changing target layout is not calibration. Ordinary scaling, 60Hz or touch calibration does not guarantee recovery of content hidden by a cut panel.

## 4. Separate Windows and Raspberry Pi

| Platform | First steps | Further instructions |
| --- | --- | --- |
| Windows 10/11 | Connections; select the screen in Display settings; matching offered resolution; Extend if needed; try 60Hz only if offered | For wrong-screen touch, use Tablet PC Settings → Setup first; consider Reset/Calibrate only after assigning the correct screen. Options vary by Windows/controller. |
| Raspberry Pi | Connections, power and a logged-in graphical desktop | Then provide the product's `screen-config`, `screen-test` or demo steps with tool version and platform requirements. |

Link to the [English Windows guide](../platforms/windows/README.md) or [Chinese guide](../platforms/windows/README.zh-CN.md). Do not present Raspberry Pi commands as Windows instructions or imply one script configures both. Select only modes/rates actually offered by the system.

Clearly identify unverified platforms. For example, an application workaround tested on the Pi does not establish a Windows whole-desktop fix. Round screens can hide Windows corner calibration targets; do not tell buyers to guess invisible points.

## 5. Three issue categories

| Category | Required distinction |
| --- | --- |
| Black screen / flicker | Connections, power and OS modes first. Attribute to EDID/timing only when supported by evidence; not every case has that cause. |
| Missing touch / wrong screen / offset | USB data connection, host and screen pairing first, then OS settings. Distinguish single, same-model dual, mixed-model dual and touch-plus-non-touch setups. |
| Cut panel | Separate advertised/visible size from input size. Measure before proposing a window or coordinate transform. State whether app-only, global and boot-persistent support exists. |

Mark inapplicable categories briefly; do not invent a problem to fill a section. Matching controller names, EDIDs or sizes do not prove the same panel, firmware or repair applies.

## 6. Product naming and navigation

- Use size – advertised resolution – touch capability for product directories; see the [naming policy](../product-support/NAMING.md). Use `touch-unconfirmed` while that option is genuinely unknown.
- Sort every home/product index by screen size **ascending**, keeping same-size products adjacent.
- Do not infer native glass resolution from the advertised HDMI input mode. Distinguish product specification, visible area and input for cut screens.
- Keep published repair IDs compatible; explain historical names and preserve redirects when product directories move.
- Mark unknown SKU, ASIN, revision and part numbers as unconfirmed rather than inventing them.

## 7. Default English, separate Chinese

Buyer pages use English `README.md` and a separate `README.zh-CN.md`, with reciprocal language links at the top. Do not duplicate full English and Chinese paragraphs in one page.

Keep step order, values, commands, applicability and validation status consistent across both languages. Use natural wording rather than literal translation. Preserve historical addresses or redirect them. Clearly label maintainer requirements/templates so readers do not mistake them for executable customer instructions.

## 8. Commands and technical data come later

Label scripts “Optional: Raspberry Pi instructions,” optionally inside `<details>`. State:

- Matching product/platform, minimum tool version, where to run and whether sudo is needed.
- Connector numbering: public 1/2 = Linux HDMI-A-1/2 = board HDMI0/1.
- Temporary check before saving; desktop-restart effects, whether timed recovery exists, and supported rollback steps.
- What to do if tools are absent, modes missing or identity checks fail. Do not invent commands or automatic repair behavior.
- Whether the file is a demo, released profile or global fix. Use explicit device/path placeholders, not development-machine mappings.

Keep detailed product information, EDID, clocks, sync values, USB identifiers, formulas, images and validation limits at the end. A screenshot verifies host output, not the visible glass or physical touch accuracy. A successful command or launch is not proof of a hardware repair.

## 9. Evidence and acceptance

Separate “physically confirmed,” “launch/screenshot checked,” “unverified” and “unresolved.” Record the date/sample scope; failed experiments must not become recommended fixes.

One sample does not qualify every batch. Do not transfer touch-model results to a non-touch model without testing. When new evidence overturns a claim, correct the buyer-facing conclusion and retain history in details so readers do not encounter contradictory advice.

## 10. Before submitting

- Can a buyer start simple checks without technical knowledge or scripts?
- Do symptoms lead to actions, with necessary limits beside them?
- Are Windows and Pi separated? Are unresolved cases described without promises?
- Are both languages complete, linked and consistent? Are products size-sorted?
- Do commands exist, local links resolve and placeholders look unmistakable?
- Remove personal paths, real passwords, tokens, customer data and unsanitized device backups from public content.
- **Write Git commit messages in English.** Describe the actual change; a documentation update is not a completed hardware repair.

Documentation normally needs content/link review. Attached programs need appropriate syntax, launch or behavior checks, with unfinished physical acceptance clearly recorded.

[Buyer-page template](../product-support/DEVICE-TEMPLATE.md) · [Product naming](../product-support/NAMING.md) · [Publishing notes](../PUBLISHING.md)

## AI repository entry

[AGENTS.md](../AGENTS.md) requires AI contributors to read these full requirements before editing buyer documentation. [CLAUDE.md](../CLAUDE.md) points Claude Code to the same entry. Keep English and Chinese requirements equivalent when updating this policy. Repository discovery is tool-dependent; if not supported, explicitly ask the assistant to read `AGENTS.md`. These files do not give a chat access to local files or grant permission to publish or change hardware.
