# TEKGROAML 显示屏支持中心

[English](README.md) | **简体中文**

按**尺寸－分辨率－是否触摸**进入[产品FAQ目录](product-support/README.zh-CN.md)。每款独立提供英文、中文，互有语言切换链接；默认入口英文。更新：2026-11-08。

先从你看到的现象开始：**黑屏或闪烁**、**触摸没反应或不准**、**画面显示不完整**。进入对应产品后先看处理步骤，详细参数在各FAQ末尾。

## 先别急着改设置

- **碰线后黑屏或闪烁？**先别动线，等约10～15秒；没恢复就拔下HDMI和USB供电线重新插紧。每次碰线都发生，优先换线。
- **触摸没反应，或跑到另一屏？**触摸款的USB供电／触摸数据线要插到**正在输出画面的同一台电脑或树莓派上**，不是只插充电头。每块屏的HDMI与USB成组核对，纯充电线不能传触摸。
- **用Windows？**先看[Windows画面及触摸操作](platforms/windows/README.zh-CN.md)，本仓库的树莓派命令不能在Windows运行。

**产品选项已确认：**当前双屏套装都不带触摸；2.1英寸和2.8英寸单屏系列均有触摸型号。2.1英寸的分辨率及专属测试结果尚未记录；有触摸型号不等于已完成触摸验收。此前2.8英寸黑屏双屏记录尚未与具体触摸／非触摸SKU对应。

| 产品 | 中文FAQ | English FAQ |
| --- | --- | --- |
| 2.1英寸单屏触摸款（分辨率待补充） | [中文](product-support/2.1inch-resolution-unconfirmed-touch/README.zh-CN.md) | [English](product-support/2.1inch-resolution-unconfirmed-touch/README.md) |
| 2.1英寸双屏，每屏480×480，非触摸 | [中文](product-support/2.1inch-480x480-dual-nontouch/README.zh-CN.md) | [English](product-support/2.1inch-480x480-dual-nontouch/README.md) |
| 2.8英寸单屏触摸款（分辨率待补充） | [中文](product-support/2.8inch-resolution-unconfirmed-touch/README.zh-CN.md) | [English](product-support/2.8inch-resolution-unconfirmed-touch/README.md) |
| 2.8英寸双屏，每屏480×480，非触摸 | [中文](product-support/2.8inch-480x480-dual-nontouch/README.zh-CN.md) | [English](product-support/2.8inch-480x480-dual-nontouch/README.md) |
| 2.8英寸480×480历史双屏记录（具体款式待核对） | [中文](product-support/2.8inch-480x480-touch-unconfirmed/README.zh-CN.md) | [English](product-support/2.8inch-480x480-touch-unconfirmed/README.md) |
| 3.4英寸800×800触摸屏 | [中文](product-support/3.4inch-800x800-touch/README.zh-CN.md) | [English](product-support/3.4inch-800x800-touch/README.md) |
| 4.0英寸720×720触摸屏 | [中文](product-support/4.0inch-720x720-touch/README.zh-CN.md) | [English](product-support/4.0inch-720x720-touch/README.md) |
| 6.2英寸360×960切割触摸屏 | [中文](product-support/6.2inch-360x960-touch/README.zh-CN.md) | [English](product-support/6.2inch-360x960-touch/README.md) |
| 6.2英寸360×960切割非触摸屏 | [中文](product-support/6.2inch-360x960-nontouch/README.zh-CN.md) | [English](product-support/6.2inch-360x960-nontouch/README.md) |

## 非触摸双屏套装（尺寸待核对）

[按形状与同显／异显查看](product-support/_unconfirmed/README.zh-CN.md)：圆形异显、方形异显、圆形同显、方形同显。新增问题包括只有一块显示、换屏后演示停止、480×480与960×480输入混用，以及应用未接受实际上报的约62.811／71.295Hz。

这些是待核对的连接样本，不是已确认的新SKU，不插入上方按英寸升序的产品表，也不归到2.8英寸款。Windows与树莓派分别说明；刷新率兼容更新只改变应用接受范围，没有改屏幕时序。

## 非触摸双屏套装列表

各套装尺寸仍待对应，以下四种配置均已确认不带触摸。

| 套装 | FAQ |
| --- | --- |
| 圆形双屏／同显／非触摸 | [中文](product-support/_unconfirmed/480x480-round-dual-clone-nontouch/README.zh-CN.md) | [English](product-support/_unconfirmed/480x480-round-dual-clone-nontouch/README.md) |
| 圆形双屏／异显／非触摸 | [中文](product-support/_unconfirmed/480x480-round-dual-sbs-nontouch/README.zh-CN.md) | [English](product-support/_unconfirmed/480x480-round-dual-sbs-nontouch/README.md) |
| 方形双屏／同显／非触摸 | [中文](product-support/_unconfirmed/480x480-square-dual-clone-nontouch/README.zh-CN.md) | [English](product-support/_unconfirmed/480x480-square-dual-clone-nontouch/README.md) |
| 方形双屏／异显／非触摸 | [中文](product-support/_unconfirmed/480x480-square-dual-sbs-nontouch/README.zh-CN.md) | [English](product-support/_unconfirmed/480x480-square-dual-sbs-nontouch/README.md) |

## 会用 GPT 或 Claude？让 AI 帮你一起搞定

把这份文档、配套测试工具，以及想体验的场景仓库下载下来，交给你常用的 AI。接下来，**把你想做的事告诉它，向 AI“许愿”就好**。如果 AI 能读取项目并操作你的电脑或树莓派，它就可以帮你检查设置、执行测试、部署支持的演示场景。

- [产品文档与FAQ](https://github.com/tekgroaml/tekgroaml-display-support)
- [屏幕配置与测试工具](https://github.com/tekgroaml/tekgroaml-pi-display-tools)
- [圆屏 Home Assistant 场景演示](https://github.com/tekgroaml/round-screen-homeassistant-kiosk)

可以直接这样说：

> 请先阅读这些仓库。我有一块[尺寸／分辨率／是否触摸]屏幕，连接的是[Windows电脑／树莓派]。我想[修好显示／测试触摸／运行某个演示]。请先检查接线和支持范围，再一步步帮我完成；修改设置时保留恢复方法。

告诉它屏幕型号、HDMI和USB怎么接，以及现在看到的现象。普通聊天AI可以指导你操作；直接执行命令需要使用带操作工具的AI，并由你提供访问权限。接线或硬件故障仍可能需要你动手检查，或联系我们协助。树莓派脚本不能直接在Windows运行。

各产品包含黑屏／闪烁、触摸问题及切割屏补偿三类内容，并区分已验证与未解决问题。输入分辨率与物理可见区域分开记录，未知规格不通过控制器名称推断。

- [通用流程与全部测试场景](product-support/_shared/README.zh-CN.md)
- [通用客户触摸FAQ](touchscreen/customer/触摸屏-客户常见问题-CN.md)
- [卖家支持资料](touchscreen/README.md)
- [配套程序与安装](https://github.com/tekgroaml/tekgroaml-pi-display-tools)
- [发布说明](PUBLISHING.md)

切割屏目前是应用内补偿，未宣称整个桌面或开机自动补偿。历史产品及配置包链接保留在产品目录中，文档可独立下载。

- [维护者：面向买家的FAQ文档书写要求](docs/文档书写要求.md)

## 给维护文档的AI

仓库入口为[AGENTS.md](AGENTS.md)。修改FAQ前先完整阅读[英文书写要求](docs/WRITING-GUIDELINES.md)或[中文书写要求](docs/文档书写要求.md)，并保持买家中英文内容一致。[CLAUDE.md](CLAUDE.md)为Claude Code提供同一规范的入口。是否自动发现取决于AI工具；未自动加载时，明确要求它先读取`AGENTS.md`。普通聊天无法自行访问本机文件，需要提供文件或开放工具访问。
