# 4.0英寸720×720触摸屏

[English](README.md) | **简体中文**

适用于4.0英寸方屏，HDMI传画面、USB传触摸。先核对订单上的尺寸、分辨率及触摸选项。

以下命令在安装[显示工具](https://github.com/tekgroaml/tekgroaml-pi-display-tools)后的树莓派中执行，矩形触摸测试需2.3.2+。示例为接口1（`HDMI-A-1`，板上HDMI0），接口2（板上HDMI1）替换数字。测试命令使用桌面用户，不加sudo。

## 通电后黑屏，或画面一直闪烁

**可能看到的现象：**电源和HDMI已经连接，但没有画面；或有画面但持续闪烁。

1. 检查屏幕额定供电及HDMI线，先只连接一块屏幕。
2. 查看识别结果，再临时应用对应兼容配置：

   ```bash
   screen-config list
   screen-config apply --port 1 --profile 4.0inch-720x720-60hz-wks-lontium-semi
   screen-test pattern --screen 1
   ```

   先保存桌面文件，配置可能重启桌面，命令没有自动倒计时恢复。如果提示产品不匹配，请停止并联系支持，不强制套用。
3. 检查画面是否稳定、四边是否完整，通过后再保存：

   ```bash
   screen-config apply --port 1 --profile 4.0inch-720x720-60hz-wks-lontium-semi --save
   ```

该时序方案已在样机通过。需撤回且屏幕信息能正常读取时，执行`screen-config auto --port 1 --save`；撤回后原症状可能返回。

## 点击无反应、控制了另一块屏，或点不到按钮

1. 用USB**数据线**连接触摸口，HDMI本身没有触摸数据。
2. 打开靶点测试：

   ```bash
   screen-test touch --screen 1 --shape rect
   ```

3. 点击五个靶点并滑动；命中应变绿，轨迹应在同一块屏上跟随手指。
4. 若另一块屏响应，按[USB与HDMI配对流程](../_shared/README.zh-CN.md#二触摸无响应串屏与偏移)重新确认。不同型号也可能上报相同控制器名称。

本屏响应但仍偏移时，提供照片及`screen-config list`结果联系支持；本款方屏不使用6.2切割屏的偏移补偿。

## 换线后测试图案不见了

重启测试窗口：

```bash
screen-test stop
screen-test pattern --screen 1
```

如果连桌面也看不到，继续检查供电、连接，以及是否已登录图形桌面。

## 详细原因、产品参数与测试记录

<details>
<summary>展开产品参数、修复原理与验证范围</summary>

#### 产品基本信息

| 字段 | 记录 |
| --- | --- |
| 客户识别名 | 4.0英寸720×720触摸屏 |
| 形状与连接 | 方形；HDMI视频＋USB触摸。早期5.08英寸的说法已更正为4.0英寸。 |
| 验证状态 | 样机时序修复及触摸已验证。 |
| 测试环境 | 树莓派4B；Raspberry Pi OS Bookworm Desktop 64位；labwc/Wayland |
| SKU／ASIN／面板料号／PCB版本 | 尚未取得，使用方案前核对实物 |

#### 一、黑屏或闪烁：已验证的EDID时序修复

| 参数 | 原始 | 修复后 |
| --- | --- | --- |
| EDID名称／厂商产品字节／长度 | WKS / Lontium Semi；`5d734600`；128字节 | 身份不变 |
| 有效像素 | 720×720 | 720×720 |
| 像素时钟 | 35MHz | 38.54MHz |
| 刷新率 | 54.492349Hz | 60.003861Hz，名义60Hz |
| 水平前沿／同步／后沿 | 46 / 5 / 41 | 46 / 6 / 40 |
| 水平／垂直总长 | 812 / 791 | 不变 |
| 垂直前沿／同步／后沿 | 50 / 5 / 16 | 不变 |
| 同步极性 | +H / +V | 不变 |

原始奇数水平同步宽度在测试树莓派上被拒绝；改偶数后可出图，但仍需修正像素时钟消除闪烁。修改的是树莓派的EDID覆盖，不刷屏幕固件。

先安装[配套工具](https://github.com/tekgroaml/tekgroaml-pi-display-tools)。正式配置名需2.3.0+，矩形触摸布局需2.3.2+。下面以接口1为例，接口2替换数字。先保存桌面工作，应用覆盖可能重启两个输出所在的图形会话；`apply`没有自动倒计时恢复。

```bash
screen-config list
screen-config profiles
screen-config apply --port 1 --profile 4.0inch-720x720-60hz-wks-lontium-semi
screen-test pattern --screen 1
screen-test touch --screen 1 --shape rect
```

实体画面及触摸通过后才保存：

```bash
screen-config apply --port 1 --profile 4.0inch-720x720-60hz-wks-lontium-semi --save
```

EDID/DDC可正常读取时回退：

```bash
screen-config auto --port 1 --save
```

这会清除本工具在该口的覆盖及保存项，原始问题可能再次出现。旧别名为`lontium-720`；工具仓库中的便捷入口为`scripts/profiles/4.0inch-720x720-60hz-wks-lontium-semi.sh`。匹配失败应先核查，不绕过检查。

#### 二、触摸无响应、串屏或偏移

已测控制器为`wch.cn USB2IIC_CTP_CONTROL`、VID/PID `1a86:e5e3`，不保证每批相同。HDMI不传递触摸。按[通用触摸流程](../_shared/README.zh-CN.md#二触摸无响应串屏与偏移)处理单屏、同名控制器、相同／不同型号双屏、USB与HDMI配对及反屏。本款方屏不应使用切割屏偏移。

#### 三、切割补偿

本款未观察到或需要切割补偿，不应用6.2英寸的偏移。

#### 验收边界

手工样机时序修复及触摸已确认。每块实物需检查四边、五点、连续轨迹及稳定性；冷启动、睡眠唤醒、热插拔、其他批次和平台未完成全面验收。

[产品目录](../README.zh-CN.md) · [全部测试场景](../_shared/README.zh-CN.md)

</details>

[产品目录](../README.zh-CN.md) · [通用排障](../_shared/README.zh-CN.md)
