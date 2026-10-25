# 产品专项支持资料

本目录收纳具体产品的兼容配置与实测记录，不作为所有屏幕通用的驱动或修复方案。

## 按产品查找

| 客户识别名称 | 状态 | 正式修复脚本 |
| --- | --- | --- |
| [4.0英寸 720×720 方形触摸屏](4.0inch-720x720-touch/README.md) | 已验证样机修正参数 | `4.0inch-720x720-60hz-wks-lontium-semi.sh` |
| [6.2英寸 420×960 长条触摸屏](6.2inch-420x960-touch/README.md) | 已验证触摸样机输入模式，厂家原生规格待核对 | `6.2inch-420x960-60hz-ltm-zl480.sh` |
| [6.2英寸 420×960 长条非触摸屏](6.2inch-420x960-nontouch/README.md) | 亮度闪动问题待解决 | 无已验证脚本 |

每个条目按“基本信息 → 驱动上报数据 → 简述问题 → 修复数据 → 修复脚本 → 验收限制”组织。客户先核对尺寸、分辨率及触摸类型，再核对驱动数据。命名细则见[规范](NAMING.md)，新增产品参考[模板](DEVICE-TEMPLATE.md)。

## 6.2英寸 420×960 长条触摸屏

- [产品支持索引与适用限制](6.2inch-420x960-touch/README.md)
- [中文使用与闪烁处理](6.2inch-420x960-touch/customer/使用与闪烁处理-CN.md)
- [English setup and flicker guide](6.2inch-420x960-touch/customer/Setup-and-Flicker-EN.md)
- [卖家验证与批次验收](6.2inch-420x960-touch/seller/适用范围与验收-CN.md)

需要工具2.3.0的`6.2inch-420x960-60hz-ltm-zl480`档并显式确认；仅在已确认触摸样机上有成功结果。非触摸样机同参仍异常，不按EDID相同就宣布适用。厂家正式型号与原生分辨率仍待核对。

## 历史资料：4.0英寸 720×720 专项支持包

优先查看[新版统一产品条目](4.0inch-720x720-touch/README.md)。以下为2026-10-24旧包，原始文件名和程序保留供历史支持；不要与新版统一工具重复启用。

- [中文安装说明](4inch-720x720-RaspberryPi-support-20261024/raspberry-pi-720-touchscreen-setup/QUICK_START_CN.md)
- [English setup guide](4inch-720x720-RaspberryPi-support-20261024/raspberry-pi-720-touchscreen-setup/QUICK_START_EN.md)
- [卖家交付说明](4inch-720x720-RaspberryPi-support-20261024/SELLER_NOTES_CN.md)
- [验证记录](4inch-720x720-RaspberryPi-support-20261024/VALIDATION.txt)
- [客户配置包ZIP](4inch-720x720-RaspberryPi-support-20261024/4inch-720x720-RaspberryPi-customer-support.zip)

该配置包处理已知720×720显示时序，不能作为通用触摸映射工具。触摸无响应及双屏串屏请先查看[触摸屏FAQ](../touchscreen/README.md)。

[返回FAQ总目录](../README.md)
