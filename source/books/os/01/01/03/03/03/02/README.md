# 行政团队

大多数行政团队相对封闭，通常通过协作的方式招募新成员。加入其中最好的方式是智能地协助现有成员，展示你理解他们的目标和工作方法。

_ftpmasters_ 团队负责 Debian 包的官方存档。他们维护一个程序，该程序接收开发者发送的包，并在经过一些检查后将其自动存储在参考服务器（ftp-master.debian.org）上。

他们还必须验证所有新包的许可证，以确保 Debian 可以分发这些包，然后才将它们纳入现有包的库中。当开发者希望移除一个包时，他们会通过 bug 跟踪系统和 _ftp.debian.org_ “伪包”联系该团队。

**_词汇_ 伪包，一个监控工具**

最初设计用于将 bug 报告与 Debian 包关联的 bug 跟踪系统，已经证明它对于管理其他事务非常实用：列出需要解决的问题或需要管理的任务，而这些任务与特定的 Debian 包无关。通过“伪包”，某些团队可以在不将真实包与团队关联的情况下使用 bug 跟踪系统。任何人都可以报告需要处理的问题。例如，BTS 有一个 _ftp.debian.org_ 条目，用于报告和跟踪官方包存档的问题，或仅仅请求移除某个包。同样，_www.debian.org_ 伪包用于报告 Debian 网站的错误，_lists.debian.org_ 则汇集了有关邮件列表的所有问题。

**_工具_ GitLab，Git 仓库托管及更多功能**

Debian 使用名为 salsa.debian.org 的 GitLab 实例来托管 Git 包管理仓库；但这个软件提供的功能远不止简单的托管，Debian 的贡献者已经迅速利用其持续集成功能（每次推送时运行测试，甚至构建包）。Debian 的贡献者还受益于更加清晰的贡献工作流程，这得益于广泛理解的合并请求过程（类似 GitHub 的拉取请求）。

GitLab 替代了 FusionForge（曾在 alioth.debian.org 上运行），用于协作包维护。这个服务由 Alexander Wirt、Bastian Blank 和 Jörg Jaspert 管理。

→ [https://salsa.debian.org/](https://salsa.debian.org/)

→ [https://wiki.debian.org/Salsa/Doc](https://wiki.debian.org/Salsa/Doc)

_Debian 系统管理员_（DSA）团队（[debian-admin@lists.debian.org](mailto:debian-admin@lists.debian.org)）负责项目中许多服务器的系统管理。团队确保所有基础服务（DNS、Web、电子邮件、shell 等）的最佳运行，安装 Debian 开发者请求的软件，并在安全方面采取所有必要的预防措施。

→ [https://dsa.debian.org](https://dsa.debian.org)

**_工具_ Debian 包追踪器**

这是 Raphaël 的创作之一。其基本理念是将有关某个包的尽可能多的信息集中在一个页面上。这样，用户可以快速查看一个程序的状态，确定需要完成的任务，并提供帮助。因此，这个页面汇总了所有 bug 统计信息、各发行版中的可用版本、包在 Testing 发行版中的进展、描述和 debconf 模板的翻译状态、是否有新的上游版本、与 Debian 政策最新版本不符的通知、维护者信息以及该维护者希望包括的任何其他信息。

→ [https://tracker.debian.org/](https://tracker.debian.org/)

该网页界面还配有一个电子邮件订阅服务，自动将以下选定信息发送到列表中：bug 和相关讨论、新版本在 Debian 服务器上的可用性、可供校对的新翻译等。

高级用户可以密切关注这些信息，甚至在充分理解系统运作方式后贡献自己的力量。

另一个网页界面，被称为 _Debian 开发者包概述_（DDPO），为每个开发者提供了一个概览，显示其负责的所有 Debian 包的状态。

→ [https://qa.debian.org/developer.php](https://qa.debian.org/developer.php)

这两个网站是由负责 Debian 质量保证的团队（即 Debian QA）开发和管理的工具。

_listmasters_ 团队负责管理邮件列表的电子邮件服务器。他们创建新的列表，处理退信（投递失败通知），并维护垃圾邮件过滤器（即未经请求的大量邮件）。

**_文化_ 邮件列表上的流量：一些数据**

邮件列表无疑是一个项目活动的最佳见证，因为它记录了发生的所有事情。以下是关于我们邮件列表的统计数据（截至 2021 年 4 月）：Debian 主机大约有 325 个列表，总订阅人数超过 295,000。每天有 396,000 封电子邮件被投递。

每个特定服务都有自己的管理团队，通常由安装了该服务的志愿者组成（他们也经常自己编写相关工具）。这适用于 bug 跟踪系统（BTS）、包追踪器、salsa.debian.org（GitLab 服务器，参见旁边的 [_工具_ GitLab，Git 仓库托管及更多功能](https://www.debian.org/doc/manuals/debian-handbook/sect.debian-internals.en.htmlsect.debian-internals.en.html#sidebar.gitlab)）、qa.debian.org 上的服务、lintian.debian.org、buildd.debian.org、cdimage.debian.org 等等。