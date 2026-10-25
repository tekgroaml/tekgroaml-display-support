# 4.0英寸 720×720 方形触摸屏

## 产品基本信息

| 字段 | 内容 |
| --- | --- |
| 客户识别名 | **4.0英寸 720×720 方形触摸屏** |
| 尺寸 | 4.0英寸，依据用户确认的实物信息；购买SKU仍需核对 |
| 分辨率/触摸 | 720×720，USB触摸 |
| SKU/ASIN/厂家料号/批次 | 尚未取得，需按卖家商品资料核对 |
| 测试环境 | Raspberry Pi 4 Model B，Bookworm Desktop 64位，labwc/Wayland |

## 驱动上报数据

| 字段 | 原始数据 |
| --- | --- |
| EDID厂商/名称 | `WKS / Lontium Semi` |
| 厂商/产品标识字节 | `5d734600` |
| EDID长度 | 128字节 |
| 第一详细时序 | 720×720，35MHz，约54.492349Hz |
| 水平前沿/同步/后沿 | 46 / 5 / 41，水平总长812 |
| 垂直前沿/同步/后沿 | 50 / 5 / 16，垂直总长791 |
| 同步极性 | 水平正、垂直正 |
| 触摸控制器 | 本次测试为`wch.cn USB2IIC_CTP_CONTROL`，VID/PID `1a86:e5e3` |

这些名称和标识是兼容核对数据，不是对真实芯片或面板料号的认证；不发布单台样机的序列号。

## 简述问题

树莓派4拒绝原始奇数水平同步时序，可能出现HDMI已连接却没有可用模式、黑屏。只把水平同步改为偶数后可以显示，但仍观察到闪烁。

## 修复数据

| 参数 | 原始 | 修复后 |
| --- | --- | --- |
| 有效分辨率 | 720×720 | 720×720，保持不变 |
| 水平同步宽度 | 5 | 6 |
| 水平后沿 | 41 | 40 |
| 水平总长 | 812 | 812，保持不变 |
| 像素时钟 | 35MHz | 38.54MHz |
| 实际刷新率 | 约54.492349Hz | 约60.003861Hz（名义60Hz） |

垂直时序与同步极性不变。修复发生在树莓派侧，不刷显示器固件。手工样机最终确认可用；新版统一脚本的冷启动和跨批次验收仍需完成。

## 修复脚本

正式文件名：**`4.0inch-720x720-60hz-wks-lontium-semi.sh`**。

正式配置ID：`4.0inch-720x720-60hz-wks-lontium-semi`。旧名`lontium-720`继续兼容，已有保存项无需手动改名。

从[工具仓库](https://github.com/tekgroaml/tekgroaml-pi-display-tools)安装2.3.0或更新的适用版本。新命名需2.3.0；旧版使用其支持的旧名称。当前接口统一为1/2，与Linux的`HDMI-A-1/2`一致；板子HDMI0对应1，HDMI1对应2。

先保存图形应用文件并保持SSH连接；应用EDID覆盖可能重启桌面、关闭所有屏幕上的图形窗口。以接口1为例：

```bash
screen-config profiles
screen-config list
screen-config apply --port 1 --profile 4.0inch-720x720-60hz-wks-lontium-semi
screen-test pattern --screen 1
screen-test touch --screen 1
screen-test stop
```

先临时应用，实体显示和触摸正常后再保存：

```bash
screen-config apply --port 1 --profile 4.0inch-720x720-60hz-wks-lontium-semi --save
```

如果从代码目录使用同名脚本入口（仍需先安装应用）：

```bash
bash scripts/profiles/4.0inch-720x720-60hz-wks-lontium-semi.sh --port 1
```

不匹配的EDID会被拒绝。命令成功不等于实体画面已经验证。临时测试没有自动倒计时恢复，需手工恢复：

```bash
screen-config auto --port 1 --save
```

恢复会清除本程序覆盖和该口保存项，原始黑屏/闪烁可能再次出现。另一接口请把命令数字改成2。

## 安装与验收资料

- [English device card and repair instructions](DEVICE-CARD-EN.md)
- [中文通用安装说明](https://github.com/tekgroaml/tekgroaml-pi-display-tools/blob/main/docs/02-%E4%B8%8A%E4%BC%A0%E5%AE%89%E8%A3%85%E4%B8%8E%E4%BD%BF%E7%94%A8.md)
- [命名规范](../NAMING.md)
- [旧专项包与历史记录](../4inch-720x720-RaspberryPi-support-20261024/SELLER_NOTES_CN.md)：保留供历史支持使用，不要与统一工具重复启用。

额定电源、清晰接线图、SKU/料号和新批次测试结果应由卖家补齐。发布兼容范围时不要把一台样机成功推广为所有4.0英寸屏幕通用。

[返回产品目录](../README.md)
