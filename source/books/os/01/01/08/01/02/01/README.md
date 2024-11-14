# 安全更新

Debian 非常重视安全性。Debian 中已知的软件漏洞会在 [安全漏洞跟踪器](https://security-tracker.debian.org) 中进行跟踪，并通常会在合理的时间内得到修复。安全更新并不托管在常规的 Debian 镜像网络中，而是托管在 `security.debian.org` 上，这是一个由 [Debian 系统管理员团队](https://www.debian.org/doc/manuals/debian-handbook/apt.en.htmlsect.debian-internals.en.html#dsa-team) 维护的小型服务器集群。这个存档包含由 Debian 安全团队和/或软件包维护者为稳定版和旧稳定版（Oldstable）发行版准备的安全更新。

该服务器也可以托管测试版（Testing）的安全更新，但这种情况并不常见，因为这些更新通常会通过来自不稳定版（Unstable）的常规更新流进入该版本。

对于严重问题，安全团队会发布 `Debian 安全公告`（DSA），并在发布安全更新时通过 [debian-security-announce@lists.debian.org](mailto:debian-security-announce@lists.debian.org) 邮件列表进行通知（[归档](https://lists.debian.org/debian-security-announce/)）。