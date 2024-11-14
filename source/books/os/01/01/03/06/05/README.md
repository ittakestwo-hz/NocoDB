# 旧稳定版与旧旧稳定版状态

每个稳定版（Stable）的生命周期大约为 5 年，考虑到稳定版通常每 2 年发布一次，因此在任何给定时刻，最多会有 3 个版本受到支持。当一个新的稳定版发布时，前一个版本将成为旧稳定版（Oldstable），再前一个版本则成为旧旧稳定版（Oldoldstable）。

Debian 发行版的长期支持（LTS）是一个近期的举措：个别贡献者和公司联合起来创建了 Debian LTS 团队。那些不再得到 Debian 安全团队支持的旧版本将由这个新团队负责。

Debian 安全团队负责当前稳定版的安全支持，并且也会在旧稳定版中提供安全支持（但仅限于与当前稳定版重叠一年的时间）。这大约意味着每个版本会有三年的支持时间。Debian LTS 团队则负责提供最后（两年）的安全支持，从而确保每个版本至少可以得到 5 年的支持，并且用户可以从版本 N 升级到 N+2，例如，从 Debian 9 Stretch 升级到 Debian 11 Bullseye。

→ [https://wiki.debian.org/LTS](https://wiki.debian.org/LTS)

**_社区_ 支持 LTS 计划的公司**

在 Debian 中，长期支持是一项艰巨的承诺，因为志愿者往往会避免那些不太有趣的工作。而且为 5 年前的软件提供安全支持，对于许多贡献者来说，比打包新的上游版本或开发新特性要无聊得多。

为了实现这个项目，Debian 依赖于长期支持对公司尤为重要的事实，企业愿意共同承担这项安全支持的成本。

该项目始于 2014 年 6 月：一些组织允许他们的员工兼职为 Debian LTS 做贡献，而另一些公司则更愿意通过资金资助该项目，以便让 Debian 贡献者获得报酬来完成他们免费不会做的工作。大多数愿意为 LTS 项目获得报酬的 Debian 贡献者聚集在一起，创建了一个明确的赞助方案，由 Freexian（Raphaël Hertzog 的公司）管理：

→ [https://www.freexian.com/services/debian-lts.html](https://www.freexian.com/services/debian-lts.html)

在 Debian LTS 团队中，志愿者负责自己关心的软件包，而受薪的贡献者则优先处理其赞助商所使用的软件包。

该项目始终在寻找新的赞助商：你的公司是否愿意参与？你是否可以让一名员工兼职为长期支持做贡献？你是否可以为安全支持分配一小部分预算？

→ [https://wiki.debian.org/LTS/Funding](https://wiki.debian.org/LTS/Funding)