# Debian 自由软件指南

这份参考文档定义了哪些软件“足够自由”可以被包含在 Debian 中。如果一个程序的许可符合这些原则，它就可以被包含在 Debian 的主分支中；反之，如果允许自由分发，它也可以出现在非自由分支中。非自由分支并不是 Debian 的官方组成部分；它是为用户提供的附加服务。有关 Debian 存档不同部分的详细说明，请参见旁白 [_词汇_ “main”、 “contrib” 和 “non-free” 存档](https://www.debian.org/doc/manuals/debian-handbook/sect.foundation-documents.en.htmlapt.en.html#sidebar.sections)。

这份文档不仅是 Debian 的选择标准，它还成为了自由软件领域的权威文件，并且为“开源定义”奠定了基础。从历史角度来看，它也可以视为“自由软件”概念的最早正式定义之一。

GNU 通用公共许可证（GPL）、BSD 许可证和艺术许可证是符合本文所列 9 项原则的传统自由许可证的例子。以下是文档的原文，发布于 Debian 网站上。

→ [https://www.debian.org/social_contract.html#guidelines](https://www.debian.org/social_contract.html#guidelines)

1. **自由再分发**
Debian 组件的许可证不得限制任何一方将软件作为包含来自多个来源的程序的集成软件包出售或赠送。许可证不得要求为此类销售支付版权费或其他费用。
2. **源代码**
程序必须包含源代码，并且必须允许以源代码和编译后的形式进行分发。
3. **衍生作品**
许可证必须允许修改和衍生作品，并且必须允许在与原始软件许可证相同的条件下分发这些作品。
4. **作者源代码的完整性**
许可证可以仅在允许与源代码一起分发“补丁文件”以便在构建时修改程序时，限制修改版源代码的分发。许可证必须明确允许分发由修改后的源代码构建的软件。许可证还可以要求衍生作品使用与原始软件不同的名称或版本号（_这是一个折衷方案。Debian 团队鼓励所有作者不要限制文件（无论是源代码还是二进制文件）被修改_）。
5. **不得歧视任何个人或团体**
许可证不得歧视任何个人或团体。
6. **不得歧视特定的领域**
许可证不得限制任何人在特定领域使用该程序。例如，许可证不能限制程序在商业中使用，也不能限制其用于基因研究。
7. **分发许可证**
许可证赋予程序的权利必须适用于所有重新分发该程序的人，而无需这些人执行额外的许可证。
8. **许可证不得专门针对 Debian**
许可证赋予程序的权利不得依赖于程序是 Debian 系统的一部分。如果程序从 Debian 中提取并且不依赖于 Debian 分发，但仍然符合该程序许可证的条款，那么重新分发该程序的所有方应该享有与 Debian 系统关联的相同权利。
9. **许可证不得污染其他软件**
- 许可证不得对与被许可软件一起分发的其他软件施加限制。例如，许可证不得要求与被许可软件一起分发的所有其他程序都必须是自由软件。
- **_基础知识_ 版权反制（Copyleft）**
    - 版权反制（Copyleft）是一种使用版权来保证作品及其衍生作品自由的原则，而不是像专有软件那样限制使用者的权利。它也是对“版权”（Copyright）一词的文字游戏。Richard Stallman 在他的朋友喜欢打趣时发现了这个概念，朋友在给他的信封上写道：“copyleft: 所有权利反转”。版权反制要求在分发原始或修改版本的作品时，保留所有初始自由。因此，如果一个程序是基于采用版权反制发布的程序代码衍生的，就不能以专有软件的形式进行分发。
    - 最著名的版权反制许可证家族当然是 GNU 通用公共许可证（GPL）及其衍生版本，GNU 较小通用公共许可证（LGPL）和 GNU 自由文档许可证（GFDL）。不幸的是，版权反制许可证通常是彼此不兼容的。因此，最好只使用其中一个。
10. **示例许可证**
- “GPL”、“BSD” 和 “艺术” 许可证是我们认为的“自由”许可证的例子。
- **_基础知识_ 自由许可证**
    - GNU GPL、BSD 许可证和艺术许可证都符合 Debian 自由软件指南，尽管它们非常不同。
    - GNU GPL（由自由软件基金会（FSF）使用并推广）是最常见的许可证。它的主要特点是，它同样适用于任何重新分发的衍生作品：任何包含或使用 GPL 代码的程序只能根据 GPL 条款进行分发。因此，它禁止将代码重新用于专有应用程序中。这为使用与 GPL 不兼容的自由软件的代码带来了严重问题。因此，有时无法将在另一自由软件许可证下发布的程序与一个在 GPL 许可证下发布的库链接。另一方面，这种许可证在美国法律中非常稳固：FSF 的律师参与了其草拟，并且曾多次迫使违反者与 FSF 达成和解，而无需诉诸法院。

→ [https://www.gnu.org/copyleft/gpl.html](https://www.gnu.org/copyleft/gpl.html)

BSD 许可证则限制最少：允许一切，包括在专有应用程序中使用修改过的 BSD 代码。

→ [https://www.opensource.org/licenses/bsd-license.php](https://www.opensource.org/licenses/bsd-license.php)

最后，艺术许可证在这两者之间达成了折衷：允许将代码集成到专有应用程序中，但任何修改必须公开。

→ [https://www.opensource.org/licenses/artistic-license-2.0.php](https://www.opensource.org/licenses/artistic-license-2.0.php)

这些许可证的完整文本可以在任何 Debian 系统的 `/usr/share/common-licenses/` 目录下找到（对于 BSD 是更新版的 3-Clause 许可证）。

**_社区_ Bruce Perens，一位有争议的领导者**

Bruce Perens 是 Debian 项目的第二任领导人，仅次于 Ian Murdock。他的动态和权威主义方法曾引发了许多争议。然而，他仍然是 Debian 的重要贡献者，特别是对 Debian 自由软件指南（DFSG）的编辑贡献，原始构想来自 Ean Schuessler。此后，Bruce 基于此提出了著名的“开源定义”，并移除了所有与 Debian 相关的内容。

→ [https://opensource.org/](https://opensource.org/)

Bruce 离开项目时颇为感性，但他依然与 Debian 保持着紧密联系，并继续在政治和经济领域推广这一发行版。他仍偶尔出现在邮件列表上，提供建议并提出支持 Debian 的最新举措。

最后一个趣事是，正是 Bruce 提出了 Debian 各个版本的“代号”（1.1 — Rex，1.2 — Buzz，1.3 — Bo，2.0 — Hamm，2.1 — Slink，2.2 — Potato，3.0 — Woody，3.1 — Sarge，4.0 — Etch，5.0 — Lenny，6.0 — Squeeze，7 — Wheezy，8 — Jessie，9 — Stretch，10 — Buster，11 — Bullseye，12（尚未发布）— Bookworm，Unstable — Sid）。

这些名字来源于《玩具总动员》中的角色。此动画电影完全由计算机图形制作，由 Pixar 工作室制作，而 Bruce 当时正是 Pixar 的员工。

Sid 这个名字具有特殊的象征意义，因为它将永远与“不稳定”分支联系在一起。在电影中，Sid 是一个总是破坏玩具的邻家孩子——所以要小心不要接近“不稳定”分支。Sid 也可以解释为“Still In Development（仍在开发中）”的缩写。