# 卖家交付说明与实测边界

产品：4.0 英寸方形 HDMI 触摸屏，原生 720×720。日期：2026-10-24。

## 本次实测记录

- 主机：Raspberry Pi 4 Model B Rev 1.5，2GB。
- 系统：Raspberry Pi OS / Debian 12 Bookworm，64 位，桌面为 labwc/Wayland。
- 内核：6.12.25+rpt-rpi-v8。
- 显示识别：WKS / Lontium Semi，manufacturer/product bytes 5d734600。
- 屏幕原始 EDID 只有一个详细时序。水平同步宽度 5 为奇数，树莓派 4 驱动不接受，连接状态为 connected，但模式列表为空，桌面输出禁用。
- 初步修正：水平同步宽度 5→6，水平后沿 41→40，保持总行长 812；此时可显示，但保留原始 35MHz 像素时钟时刷新率约 54.49Hz，用户报告闪烁。
- 后续修正：像素时钟 38.54MHz，保持 720×720、总尺寸 812×791，得到约 60.004Hz。用户先反馈闪烁明显改善，随后连接触摸后确认完全可用。不能据此断言所有闪烁都仅由刷新率引起。
- 最终复核：720×720 / 60.004Hz 已启用；USB 1a86:e5e3，名称 wch.cn USB2IIC_CTP_CONTROL，Linux hid-multitouch 已识别为触摸设备。无需另装触摸驱动。

## 买家必须知道的核心信息

1. HDMI 负责画面，USB 数据连接负责触摸。不能只接 HDMI，也不能把触摸 USB 口只接充电器。
2. 树莓派需要可启动的系统 TF 卡；已有系统无需重复刷机。
3. 本驱动板在本次树莓派 4 + Bookworm 环境需要显示兼容配置。Windows 能正常显示，不代表树莓派会自动接受同一 EDID。
4. 本包用于已知驱动板及已验证平台，不能宣称所有树莓派、所有系统均免配置即插即用。
5. Wi-Fi 和 SSH 是远程配置途径，不是触摸屏正常工作的强制硬件条件。用户也可用临时显示器完成安装。

## 交付物与使用范围

买家可分发 ZIP 包只包含中英文客户说明、显示配置脚本、安装/卸载脚本及诊断工具，不包含本卖家说明。无需向客户提供本次测试使用的账号、密码、网络信息或固定 IP。

买家包使用厂商/产品标识、显示名称和已知详细时序识别驱动板，避免原先仅匹配单块样机完整 EDID 哈希造成其他序列号样机无法安装。未知驱动板会拒绝套用。不同生产批次请复核，不要直接移除匹配保护。

该专项包使用独立服务`square720-display.service`。如果已安装功能相同的其他配置程序，不应重复启用多套时序覆盖；请先核对现有设置及回退方案。

## 发布前需要补齐和验证

- 在商品说明中补上实物接口照片，标出 HDMI、触摸数据口、供电口，以及屏幕实际额定输入电压/电流。当前未取得产品电源铭牌，不编造屏幕电源规格。
- 确认包装内 USB 线可传输数据，明确 HDMI 线两端规格和是否随附电源。
- 用干净的 Bookworm Desktop 64 位 TF 卡完成安装、重启、断电冷启动、USB 触摸和卸载验证。本次样机的运行显示/触摸已验证，但新分发安装包尚未在干净系统上走完安装及冷启动流程。
- 在另一块同批次屏幕上验证，确认序列号差异不会影响安装；新批次变更驱动板或 EDID 时需重新验证。
- 如要宣传支持树莓派 5、Trixie、其他 Linux 系统或屏幕旋转，请分别实测后再更新支持范围。
- 若想实现真正的树莓派免配置即插即用，优先与工厂修正驱动板出厂 EDID：保留 720×720，提供树莓派 4 接受的偶数水平时序及约 60Hz 的一致参数。工厂固件修改属于另外的产品验证工作，本次没有修改屏幕固件。

## 可用于商品页面的说明

中文：支持 HDMI 视频输入和 USB 触摸连接。使用 Raspberry Pi 时，需同时连接 HDMI 视频线与 USB 数据线。已在 Raspberry Pi 4 Model B、Raspberry Pi OS Bookworm Desktop 64 位环境中验证；该环境可能需要安装随附的显示兼容配置。其他型号和系统版本请先咨询支持。

English: HDMI video and USB touch connections. For Raspberry Pi use, connect both the HDMI video cable and a USB data cable. Tested with Raspberry Pi 4 Model B running Raspberry Pi OS Bookworm Desktop, 64-bit. The supplied display compatibility setup may be required. Please contact support for other models or operating systems.

## 本次文件校验结果

专项包通过了时序复现、不同序列号保留、重复执行、错误校验和/非目标型号/未知时序拒绝等逻辑检查，以及Shell脚本语法检查。此旧专项分发包在干净系统上的完整安装、重启、冷启动和卸载仍待验收。以上是历史测试范围，不表示用户设备当前已配置。
