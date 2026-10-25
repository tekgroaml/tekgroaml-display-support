# TEKGROAML Display Support / 显示屏支持中心

GitHub仓库：[tekgroaml-display-support](https://github.com/tekgroaml/tekgroaml-display-support)。按主题和使用对象整理客户文档、支持人员资料及产品专项配置。此仓库可以单独下载，不依赖电脑上另一个项目的目录位置。

| 分类 | 内容 | 入口 |
| --- | --- | --- |
| 触摸屏客户指南 | 中英文常见问题：触摸无响应、相同/不同型号多屏、串屏与偏移 | [触摸屏目录](touchscreen/README.md) |
| 触摸屏卖家支持 | 排障SOP、客服回复和商品说明模板 | [卖家资料](touchscreen/seller/触摸屏-卖家排障SOP-CN.md) |
| 产品专项支持 | 4英寸720×720、6.2英寸长条触摸样机的配置与限制 | [产品支持目录](product-support/README.md) |

```text
FAQ/
├── README.md
├── touchscreen/
│   ├── README.md
│   ├── customer/
│   │   ├── 触摸屏-客户常见问题-CN.md
│   │   └── Touchscreen-Customer-FAQ-EN.md
│   └── seller/
│       ├── 触摸屏-卖家排障SOP-CN.md
│       └── 触摸屏-客服回复与商品说明-CN-EN.md
└── product-support/
    ├── README.md
    ├── 6.2inch-420x960-touch/
    │   ├── README.md
    │   ├── customer/
    │   └── seller/
    └── 4inch-720x720-RaspberryPi-support-20261024/
        ├── SELLER_NOTES_CN.md
        ├── VALIDATION.txt
        ├── 4inch-720x720-RaspberryPi-customer-support.zip
        └── raspberry-pi-720-touchscreen-setup/
```

程序代码、安装卸载脚本及工具命令说明位于[TEKGROAML Pi Display Tools](https://github.com/tekgroaml/tekgroaml-pi-display-tools)。

新增FAQ请放入对应主题目录；客户说明放在`customer`，内部排障资料放在`seller`，某一SKU专用配置放在`product-support`。

## Related tool / 配套工具

显示配置、颜色测试和触摸测试工具：[TEKGROAML Pi Display Tools](https://github.com/tekgroaml/tekgroaml-pi-display-tools)。本仓库可独立下载；维护信息见[发布说明](PUBLISHING.md)。

English customers: start with the [Touchscreen FAQ](touchscreen/customer/Touchscreen-Customer-FAQ-EN.md). Product-specific setup packages are under [product-support](product-support/README.md).
