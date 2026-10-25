# 客服回复与商品说明模板

使用前将产品接口名称、实际供电要求及支持系统替换为对应SKU的信息。以下模板可按客户现象选择，不需要一次全部发送。

## 1. 有画面但触摸无响应

**中文**

这款屏幕使用HDMI传输画面、USB传输触摸数据。请确认屏幕的触摸USB口通过支持数据传输的USB线连接到同一台电脑/树莓派，而不是只接充电器。若已连接，请先换一条确认能传数据的线，直接接主机USB口测试。方便的话，请提供屏幕型号、主机系统及接线照片，我们可以据此确认下一步。

**English**

This display uses HDMI for video and USB for touch data. Please connect the display's touch USB port to the same computer or Raspberry Pi using a data-capable USB cable. A connection only to a wall charger will not send touch input. If it is already connected, please try a known working data cable directly into the host. Please share the display model, host OS and a wiring photo so we can check the next step.

## 2. 相同型号多屏串屏

**中文**

两块相同型号屏幕的触摸控制器可能报告相同名称，主机需要把每个触摸设备分别关联到对应显示器。请先分别单独测试两块屏幕，再同时接回。随后只点A屏一次、再只点B屏一次，观察是哪块屏幕响应。请把这个结果及两条USB数据线的接线位置发给我们，以便提供适用的映射设置。

**English**

Identical displays may report the same USB touch-controller name. The host may need each controller associated with its own display. Please test each display individually first, then reconnect both. Touch only Screen A, then only Screen B, and note which display responds. Please share the result and the USB cable connections so we can provide the appropriate mapping instructions.

## 3. 不同型号屏幕一起用时触摸异常

**中文**

不同型号屏幕也可能使用相同的触摸控制器。我们需要分别检查各屏幕的显示模式、触摸设备与显示器关联，以及旋转方向。请告诉我们每块屏幕的型号、分辨率、单独使用是否正常，以及点击后是无响应、偏移还是落到另一块屏幕。请暂时不要给所有屏幕套用同一个校准参数。

**English**

Different display models can still use the same touch controller. We need to check each display's video mode, touch-to-display association and orientation. Please provide each model and resolution, whether it works on its own, and whether touch is unresponsive, offset or operating another screen. Please avoid applying the same calibration values to every display.

## 4. 操作验证

**中文**

如果已安装我们为您系统提供的`pi-setting`工具，请运行`screen-test touch`。用手指点击五个编号靶点，命中后应变绿；滑动时轨迹应跟随手指。请确认每块屏幕只在自己被触摸时响应。如果不确定，请录一段能同时看到手指与两块屏幕的短视频。

**English**

If our compatible `pi-setting` tool has been installed, run `screen-test touch`. Tap the five numbered targets with your finger; successful hits turn green. Slide your finger to check that the trail follows it. Each display should respond only to touches on that physical screen. A short video showing your finger and both displays can help us check any mismatch.

## 5. 修复后的使用提醒

**中文**

已按当前USB接口与HDMI连接关系完成触摸映射。请给两组线贴上A/B标签，并保持这组插口配对。以后更换USB口、Hub或HDMI配对后，如果触摸位置变化，需要重新确认映射。请按实际测试结果确认重启后是否也正常。

**English**

Touch mapping has been configured for the current USB and HDMI connections. Please label the cable pairs A/B and keep the same port pairing. Moving a USB connection, changing a hub or swapping HDMI connections may require the mapping to be checked again. Please also confirm operation after restarting the host.

仅在实际完成客户映射后发送这条回复；不能在尚未验证时直接声称已修复。

## 6. 商品详情页可用说明

**中文**

HDMI视频输入＋USB触摸连接。使用触摸功能时，需要将触摸USB口通过支持数据传输的USB线连接到主机。多触摸屏环境可能需要在操作系统中分别设置触摸与显示器的关联。系统兼容性、多点触控及具体线材配置请以本型号说明为准。

**English**

HDMI video input with USB touch connection. Touch operation requires a data-capable USB cable between the touch USB port and the host. Multi-touchscreen setups may require separate touch-to-display association in the operating system. Please check this model's specifications for supported systems, multitouch capability and included cables.

这段话未承诺电源或线缆随附，也没有将全部系统、多屏多点功能描述为已验证。发布前由运营补上该SKU实际接口图、额定供电、随附配件及已测系统清单。

## 7. 问题收集表

```text
购买型号 / Purchased model:
主机型号 / Host model:
操作系统及版本 / OS and version:
屏幕数量 / Number of displays:
各屏幕型号与分辨率 / Each display's model and resolution:
单独连接时是否正常 / Does each work on its own?:
画面是否稳定 / Is the picture stable?:
触摸问题 / Touch issue: no response / wrong display / offset / intermittent
最近是否换口、换屏或旋转 / Recent port, display or orientation changes:
附接线照片或短视频 / Wiring photo or short video:
```

不向客户索取Wi-Fi、系统登录或SSH密码。故障描述和诊断输出足以开展第一轮排查。

[返回触摸屏资料目录](../README.md)
