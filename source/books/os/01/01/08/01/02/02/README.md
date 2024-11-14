# 稳定版更新

稳定版更新并不涉及安全性，但被认为足够重要，因此会在下一个稳定点发布之前推送给用户。

这个仓库通常包含那些在发布前未能修复的、或是后续更新引入的关键性和严重性错误的修复。根据紧急程度，它也可能包含一些需要随着时间推移而更新的软件包，例如 SpamAssassin 的垃圾邮件检测规则、ClamAV 的病毒数据库、所有时区的夏令时规则（tzdata）、Firefox 的 ESR 版本（firefox-esr），或像 `debian-archive-keyring` 这样的加密密钥环。

实际上，这个仓库是 `proposed-updates` 仓库的一个子集，由 [稳定版发布经理](https://www.debian.org/doc/manuals/debian-handbook/apt.en.htmlsect.release-lifecycle.en.html#srm-team) 精心筛选。所有更新都会在 [debian-stable-announce@lists.debian.org](mailto:debian-stable-announce@lists.debian.org) 邮件列表中发布（[归档](https://lists.debian.org/debian-stable-announce/)），并且这些更新最终都会包含在下一个稳定点发布中。