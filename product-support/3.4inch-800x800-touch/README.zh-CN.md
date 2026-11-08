# 3.4英寸800×800触摸屏

[English](README.md) | **简体中文**

适用于3.4英寸800×800圆形触摸屏。测试时选择圆屏靶点，避免将测试点放在玻璃看不到的四角。

以下命令在安装[显示工具](https://github.com/tekgroaml/tekgroaml-pi-display-tools)后的树莓派中执行，矩形触摸测试需2.3.2+。示例为接口1（`HDMI-A-1`，板上HDMI0），接口2（板上HDMI1）替换数字。测试命令使用桌面用户，不加sudo。

## 换上圆屏后没画面，或画面显示不对

换屏后，接口可能仍沿用上一块屏幕的模式。

1. 检查供电和HDMI，再查看可用模式：

   ```bash
   screen-config list
   screen-config modes --port 1
   ```

2. **仅当列表存在约60Hz的800×800时**，选择该模式并打开测试：

   ```bash
   screen-config set --port 1 --mode 800x800@60
   screen-test pattern --screen 1
   ```

3. 实体画面稳定后保存：

   ```bash
   screen-config set --port 1 --mode 800x800@60 --save
   ```

样机选择800×800、60Hz后画面稳定。若没有该模式，向支持提供上述list和modes结果，不套用方屏或长条屏档；这些命令没有自动恢复倒计时。

## 触摸无反应，或另一块屏幕在响应

接上USB数据线后执行：

```bash
screen-test touch --screen 1 --shape round
```

点击五个编号圆点并滑动。若响应跑到另一块屏幕，逐根识别USB触摸线并按[配对流程](../_shared/README.zh-CN.md#二触摸无响应串屏与偏移)操作；已测环境中双触摸问题由此解决。

## 截图里的四角在屏幕上看不到

圆形玻璃不能显示800×800方形截图的四角。应用按钮应放在可见圆内，触摸测试选择`--shape round`。如果圆形本身缺了一部分或中心内容被截，拍照联系支持；不要套用长条屏的60列偏移。

## 重新插线后测试窗口消失

```bash
screen-test stop
screen-test touch --screen 1 --shape round
```

## 详细原因、产品参数与测试记录

<details>
<summary>展开产品参数、修复原理与验证范围</summary>

#### 产品基本信息

| 字段 | 记录 |
| --- | --- |
| 客户识别名 | 3.4英寸800×800触摸屏 |
| 形状与连接 | 圆形；HDMI视频＋USB触摸。 |
| 验证状态 | 800×800、60Hz实体画面稳定；完整原始时序未留存。 |
| 测试环境 | 树莓派4B；Raspberry Pi OS Bookworm Desktop 64位；labwc/Wayland |
| SKU／ASIN／面板料号／PCB版本 | 尚未取得，使用方案前核对实物 |

#### 一、无画面或模式不匹配

换屏后旧输出仍是720×720；切换到本屏800×800、60Hz后，用户确认实体画面稳定。未留存完整原始EDID、像素时钟、前后沿及控制器身份，不套用720方屏或6.2长条屏的配置。

安装工具后先核对当前接口，以下以接口2为例：

```bash
screen-config list
screen-config modes --port 2
```

仅当模式列表中包含约60Hz的800×800时执行：

```bash
screen-config set --port 2 --mode 800x800@60
screen-test pattern --screen 2
screen-test touch --screen 2 --shape round
```

`set`只选择已上报模式，不会生成缺失模式。若列表没有该模式，先收集EDID和完整时序。实物验证通过后才保存：

```bash
screen-config set --port 2 --mode 800x800@60 --save
```

DDC正常时，可用`screen-config auto --port 2 --save`清除该选择并恢复上报首选模式。这些命令没有自动倒计时恢复。

#### 二、触摸映射

调试中也覆盖了双触摸屏：最初都响应同一屏，分别生成虚拟设备名并确认USB路径与输出对应后，用户确认各自响应且位置正常。按[通用流程](../_shared/README.zh-CN.md#二触摸无响应串屏与偏移)操作。未归档每块样机完整的USB／EDID对应表，必须在本机点击识别。选择圆屏布局，靶点位于圆形可见区；方形系统截图中的四角并非圆屏物理可见区域。

#### 三、切割补偿

本款未验证水平60列补偿。圆形遮罩与6.2英寸长条屏裁切是不同问题。

#### 验收边界

调试中确认画面稳定，并最终确认双屏触摸定位正确；干净系统的完整时序复现、重启持久化与其他批次仍需验证。

[产品目录](../README.zh-CN.md) · [全部场景](../_shared/README.zh-CN.md)

</details>

[产品目录](../README.zh-CN.md) · [通用排障](../_shared/README.zh-CN.md)
