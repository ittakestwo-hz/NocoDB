# 商业驱动与社区驱动的发行版

Linux 发行版主要分为两大类：商业发行版和社区驱动发行版。前者由公司开发，通常附带商业支持服务进行销售；后者则按照与自由软件相同的开放开发模式进行开发。

商业发行版通常会更频繁地发布新版本，以便更好地推销更新和相关服务。它们的未来直接与公司商业成功挂钩，许多发行版已经因为公司倒闭或其他原因而消失（如 Caldera Linux、StormLinux、Mandriva Linux 等）。

与此不同，社区驱动的发行版则没有固定的发布周期，而是根据自身的进度发布新版本。就像 Linux 内核一样，只有在新版本稳定后才会发布，而不会提前发布。只要有足够的开发者或第三方公司支持，社区驱动的发行版就能持续生存。

对多种 Linux 发行版的比较，最终促使管理员选择 Debian，主要基于以下几个原因：

-   Debian 是社区驱动的发行版，其开发不受任何商业约束；因此，它的目标本质上是技术性的，这有助于提升产品的整体质量。
    
-   在所有社区驱动的发行版中，Debian 从多个角度来看都具有重要地位：其贡献者数量、可用软件包数量以及连续存在的年数都是领先的。其庞大的社区规模无可争议地证明了其持续性。
    
-   统计数据显示，Debian 每 18 到 24 个月发布一个新版本，并且每个版本的支持周期为 5 年，这一时间表对管理员非常友好。
    
-   对几家法国自由软件服务公司进行的调查显示，所有这些公司都为 Debian 提供技术支持；对于其中的许多公司来说，Debian 还是它们内部使用的首选发行版。潜在的服务提供商的多样性是 Falcot Corp 独立性的重要资产。
    
-   最后，Debian 可用于多种架构，包括针对 OpenPOWER 处理器的 ppc64el 架构；因此，Falcot Corp 的最新 IBM 服务器也可以安装 Debian。
    

**_实践经验_ Debian 长期支持（LTS）**

Debian 长期支持（LTS）项目始于 2014 年，旨在为所有稳定版 Debian 提供 5 年的安全支持。LTS 对于那些拥有大量部署的组织至关重要，因此该项目尽力汇集使用 Debian 的公司资源。

→ [https://wiki.debian.org/LTS](https://wiki.debian.org/LTS)

Falcot Corp 由于规模较小，无法让其 IT 部门的员工参与 LTS 项目，因此公司选择订阅 Freexian 的 Debian LTS 合同并提供财务支持。借助这一支持，Falcot 的管理员知道他们所使用的软件包将优先处理，并且在遇到问题时，他们可以与 LTS 团队直接联系。

→ [https://wiki.debian.org/LTS/Funding](https://wiki.debian.org/LTS/Funding)

→ [https://www.freexian.com/services/debian-lts.html](https://www.freexian.com/services/debian-lts.html)

一旦 Debian 被选定，接下来就需要决定使用哪个版本。我们接下来来看看为什么管理员最终选择了 Debian Bullseye。