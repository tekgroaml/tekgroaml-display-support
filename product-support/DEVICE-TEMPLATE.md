# Buyer product FAQ template (for maintainers)

**English** | [简体中文](DEVICE-TEMPLATE.zh-CN.md)

Read the [writing requirements](../docs/WRITING-GUIDELINES.md) first. This is a template, not an executable repair guide. Create English `README.md` and Chinese `README.zh-CN.md` in the product directory after replacing and verifying every placeholder.

## Buyer-page structure

```markdown
# Size + advertised resolution + touch option

**English** | [简体中文](README.zh-CN.md)

One sentence identifying the product and asking the buyer to check their order.

## A symptom the buyer can see

One sentence saying when it happens and what appears.

1. Start with waiting, reconnecting and checking the host/USB cable.
2. Then offer built-in OS settings; separate Windows from Raspberry Pi.
3. Explain what a successful result looks like.

If unresolved: request the necessary photo, wiring and computer details.

## Optional: Raspberry Pi instructions

<details>
<summary>Show Raspberry Pi steps (not Windows)</summary>

Give platform/version, execution location, effects, verified commands and recovery.

</details>

## Technical details and test records

<details>
<summary>Show product data, explanation and validation limits</summary>

Complete the technical fields below; keep them out of the page opening.

</details>
```

For cable-movement blackouts, wait briefly before reconnecting. For touch faults, first check that the USB power/touch data cable reaches the same host sending video. Follow the writing requirements; do not fill a template with guessed commands.

## Technical information checklist

| Area | Record |
| --- | --- |
| Product | Size, advertised/visible/native/input resolutions separately; shape and touch; confirmed SKU/ASIN/part/revision or unknown |
| Environment | Host, OS, desktop and tool version actually tested |
| Reported data | EDID name/identity/length/checksum, preferred mode, pixel clock, complete timings/polarity; touch USB name/VID/PID if applicable |
| Symptom/cause | Exact visible issue and trigger; distinguish confirmed cause from hypothesis |
| Repair | Before/after values and evidence; host-only vs monitor firmware changes |
| Script | Existing profile/filename and alias, version, temporary/save/recovery steps, unsupported variants |
| Cut panel | Measured visible window, logical canvas and input transform; app/global/boot scope separately |
| Acceptance | Physical picture, borders, colors, sampled touch, restart, cold boot, other batches; mark untested/unresolved |

Include no invented product fields, commands or promises. Cover no-picture/flicker, touch response and cut-panel cases only as applicable. A five-point pass is not full-screen or multitouch qualification.

[Naming policy](NAMING.md) · [Product directory](README.md) · [Writing requirements](../docs/WRITING-GUIDELINES.md)
