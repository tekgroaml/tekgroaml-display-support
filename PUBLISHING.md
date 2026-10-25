# GitHub 发布说明

仓库：[tekgroaml/tekgroaml-display-support](https://github.com/tekgroaml/tekgroaml-display-support)。

建议Description：`Setup guides, FAQs, and troubleshooting for HDMI USB touch displays.`

GitHub账号/组织为`tekgroaml`。仓库同时容纳产品接线、安装、排障和专项支持；本地文件夹名称可以继续使用`FAQ`。

## 目录与独立使用

- `touchscreen/customer/`：中英文客户FAQ。
- `touchscreen/seller/`：维护人员SOP、回复模板和商品说明草稿。公开仓库中这些文件同样可被所有人读取；已检查不含客户凭据、订单资料或个人路径。需要保密的运营资料应另存私有位置，不要误认为目录名能限制访问。
- `product-support/`：产品专项旧包及其验证范围，非通用触摸驱动。
- `README.md`：总导航。

本仓库的相对链接均应指向仓库内部，不能要求客户在同一父目录再放一个本地`pi-setting`项目。配套软件：[tekgroaml-pi-display-tools](https://github.com/tekgroaml/tekgroaml-pi-display-tools)。

## 发布前元数据

README和相关文档已经使用真实的软件仓库链接；更新时请保持两个项目的链接一致。

选择文档及所附代码的授权方式后，再增加相应`LICENSE`和必要版权说明。目前没有替所有者决定许可；文档可读与允许复制修改不是同一个授权声明。

## 已完成的内容检查

- 去除跨仓库的本机相对链接，改为配套仓库名称说明。
- 保留`YOUR_USER`、`YOUR_PI_HOST`等显式占位示例，不填真实账号或网络地址。
- 本机节点、物理USB路径、带日期的实际备份路径不作为客户默认设置。
- 旧产品包的历史备注整理为适用范围与未验证项目，不描述某台开发机仍在运行的状态。
- 对ZIP内容也扫描，不只检查可见Markdown。

首次内容提交保留远程初始化README历史；发布仓库不等于已经通过邮件或消息发送给客户。

## 本次检查结果（2026-10-25）

- 20个仓库文件，以及旧专项ZIP内8个文件均纳入内容检查。
- 23处仓库内链接通过，并在单独复制目录后验证不依赖本地软件项目位置。
- ZIP完整性通过，压缩包各文件与目录中的对应源码/说明一致。
- 未发现检查范围内的个人主目录、真实测试主机IP、已知测试密码、私钥或GitHub访问令牌。
- 保留平台版本、VID/PID和显示模式作为兼容性信息；运行时设备节点及用户名采用占位符。

扫描不能替代对未来新提交的复核。后续加入客户日志、设备备份、截图或新压缩包时，应重新检查其中是否含个人信息。
