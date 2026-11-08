# Instructions for AI contributors

These instructions apply throughout this repository. Follow the user's current instructions when they override repository guidance.

## Read before writing

Before creating, editing or reviewing buyer-facing documentation, read and apply the writing requirements:

- English: [docs/WRITING-GUIDELINES.md](docs/WRITING-GUIDELINES.md)
- 简体中文: [docs/文档书写要求.md](docs/文档书写要求.md)

The two files describe the same requirements. Read at least one in full and consult the other when checking bilingual consistency. Do not rely on this short entry as a substitute for the full requirements. If a required file cannot be read, report that limitation instead of claiming compliance.

For product pages, also consult the [naming policy](product-support/NAMING.md) and the [English template](product-support/DEVICE-TEMPLATE.md) / [Chinese template](product-support/DEVICE-TEMPLATE.zh-CN.md). For publishing, consult [PUBLISHING.md](PUBLISHING.md).

## Essentials to preserve

- Write short, natural seller-to-buyer instructions: visible symptom, simple action, expected result, then what to do if it still fails.
- Check connections first. For cable-movement blackouts/flicker, wait briefly, reconnect, then compare cables. For touch faults, first check that the USB power/touch data cable reaches the same host sending HDMI video.
- Put Windows built-in actions before optional Raspberry Pi commands. Never imply Pi scripts work on Windows.
- Put scripts and technical explanations later, using expandable sections where appropriate. Keep applicability limits beside the actions.
- Default buyer pages to English `README.md`, with separate Chinese `README.zh-CN.md` and reciprocal language links. Update both together, preserving equivalent meaning and validation status.
- Sort product indexes by ascending screen size. Identify products by size, advertised resolution and touch capability; mark unknowns explicitly.
- Distinguish confirmed results, unverified ideas and unresolved failures. Do not promise a cure or generalize app-only compensation to the whole desktop, Windows or other batches.
- Do not publish credentials, personal paths, customer data or unsanitized device backups.
- Use English Git commit messages. Do not infer authorization to publish merely from this file; follow the current user's authorized scope.

## Validate the change

Check local Markdown links, bilingual navigation/content, product ordering and `git diff --check`. For attached code, perform relevant syntax/behavior checks and describe any physical-device checks still outstanding. Do not change live displays or flash firmware merely to edit documentation.

## 中文入口

本文件适用于仓库全部目录。修改买家文档前，必须先完整阅读上述中英文写作要求中的至少一份；核对双语一致性时参考另一份。核心顺序为“现象 → 简单操作 → 判断结果 → 未解决怎么办”，脚本和专业原理后置。中英文同步、尺寸升序、英文commit，已验证与未验证明确区分。当前用户的明确要求优先于本仓库规范。
