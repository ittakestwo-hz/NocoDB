# 报告 Bug

在 Debian 中，提交 Bug 的基本工具是 Debian Bug Tracking System（Debian BTS），这是项目中广泛使用的系统。公开部分（即网页界面）允许用户查看所有报告的 Bug，并提供按各种标准排序显示 Bug 列表的选项，例如：受影响的软件包、严重性、状态、报告者地址、负责维护该软件包的维护者地址、标签等。此外，还可以浏览与每个 Bug 相关的所有讨论的完整历史记录。

在其背后，Debian BTS 基于电子邮件：它存储的所有信息都来自参与者发送的邮件。任何发送到 `[12345@bugs.debian.org](mailto:12345@bugs.debian.org)` 的邮件都会被分配到 Bug 编号 12345 的历史记录中。经过授权的人员可以通过向 `[12345-done@bugs.debian.org](mailto:12345-done@bugs.debian.org)` 发送邮件来“关闭”一个 Bug，邮件中应描述关闭该 Bug 的理由（当问题解决或不再相关时，Bug 会被关闭）。报告新 Bug 的方法是按照特定格式发送邮件到 `[submit@bugs.debian.org](mailto:submit@bugs.debian.org)`，该格式会标明相关的软件包。地址 `[control@bugs.debian.org](mailto:control@bugs.debian.org)` 允许编辑与 Bug 相关的所有“元信息”。

Debian BTS 还具有其他功能，例如使用标签来标记 Bug。更多信息，请参见

→ [https://www.debian.org/Bugs/](https://www.debian.org/Bugs/)

**_词汇_** Bug 的严重性

Bug 的严重性正式地为报告的问题分配一个严重程度。实际上，并不是所有 Bug 的重要性相同；例如，手册页中的拼写错误与服务器软件中的安全漏洞是不可同日而语的。