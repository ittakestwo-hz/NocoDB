# 开发团队与跨领域团队

与行政团队不同，开发团队相对开放，甚至对外部贡献者也开放。尽管 Debian 项目并不以创建软件为宗旨，但项目确实需要一些特定的程序来实现其目标。当然，这些程序都是在自由软件许可证下开发的，采用了自由软件领域中其他地方已经验证过的方法。

Debian 自身开发的软件不多，但有些程序已经扮演了重要角色，并且它们的知名度超出了项目的范围。典型的例子包括 `dpkg`（Debian 包管理程序，它实际上是 Debian PacKaGe 的缩写，通常读作 “dee-package”）和 `apt`（一个自动安装任何 Debian 包及其依赖项的工具，能够在升级后保证系统的一致性，apt 是 Advanced Package Tool 的缩写）。然而，这些程序的开发团队相对较小，因为要全面理解这类程序的运作，需要相当高的编程技能。

最重要的团队可能是 Debian 安装程序 `debian-installer` 团队，自 2001 年以来，该程序完成了极为重要的工作。需要大量的贡献者，因为写出一个能够在十几种不同架构上安装 Debian 的程序是非常困难的。每种架构都有自己的启动机制和启动加载程序。所有这些工作都在 `[debian-boot@lists.debian.org](mailto:debian-boot@lists.debian.org)` 邮件列表中进行协调，由 Cyril Brulebois 领导。

→ [https://www.debian.org/devel/debian-installer/](https://www.debian.org/devel/debian-installer/)

→ [https://joeyh.name/blog/entry/d-i_retrospective/](https://joeyh.name/blog/entry/d-i_retrospective/)

相对较小的 `debian-cd` 程序团队有着更加谦逊的目标。许多“小”贡献者负责自己的架构，因为主开发者无法掌握所有的细节，也不知道如何精确地从 CD-ROM 启动安装程序。