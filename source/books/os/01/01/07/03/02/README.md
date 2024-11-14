# 在 Debian 中的使用

源代码包是 Debian 中一切的基础。所有 Debian 软件包都来自一个源代码包，每个 Debian 软件包中的修改都是源代码包中相应修改的结果。Debian 维护者与源代码包进行工作，但他们知道这些操作对二进制包的影响。因此，他们的工作成果体现在 Debian 提供的源代码包中：你可以轻松地回到这些源代码包，所有内容都源于这些包。[第 15 章，_创建一个 Debian 软件包_](https://www.debian.org/doc/manuals/debian-handbook/sect.source-package-structure.en.htmldebian-packaging.en.html) 包含了一些示例。

当一个新的源代码包版本出现在 Debian 服务器上时，它将被不同架构的计算机网络使用，用于在 Debian 支持的各个架构上进行编译。

→ [https://buildd.debian.org/](https://buildd.debian.org/)

**_深入了解_ 仅源代码上传的维护者上传**

在 Debian 10 Buster 发布后，[发布团队](https://www.debian.org/doc/manuals/debian-handbook/sect.source-package-structure.en.htmlsect.release-lifecycle.en.html#srm-team)宣布将不再接受维护者的二进制包上传，`main` 组件中的所有二进制包必须通过强制的源代码-only 上传自动构建。虽然 `contrib` 和 `non-free` 组件仍然允许二进制包上传，但我们不会详细讨论这种情况，因为它应该仅作为例外。