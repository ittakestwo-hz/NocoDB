# 对用户的承诺

该项目还有一份“社会契约”。那么，作为一个仅仅专注于开发操作系统的项目，为什么会有这样一份文件呢？其实很简单：Debian 为用户工作，因此，也就间接为社会服务。这份契约总结了该项目所作出的承诺。让我们更详细地了解这些承诺：

1. **Debian 将始终保持 100% 免费**
- 这是第一个原则。Debian 是并将永远是完全由自由软件组成的。此外，Debian 项目内部的所有软件开发工作也将保持自由。
- **_视角_ 超越软件**
    - Debian 社会契约的第一个版本写道：“Debian 将始终保持 100% 免费 _软件_”。而在 2004 年 4 月批准的 1.1 版中，去掉了最后一个单词“软件”，这表明 Debian 的目标是实现自由，不仅仅是在软件方面，而是包括文档和 Debian 在操作系统中所提供的任何其他元素。
    - 这个变化本意只是编辑上的调整，但实际上产生了许多后果，特别是在去除了一些有问题的文档方面。此外，随着固件在驱动程序中的使用日益增加，问题也随之而来：许多固件并不免费，但它们是硬件正常运行所必需的。
2. **我们将回馈自由软件社区**
- Debian 项目对其集成到分发版中的每个作品所做的任何改进，都会反馈给该作品的作者（即“上游”）。通常，Debian 会与社区合作，而不是孤立工作。
- **_社区_ 上游作者，还是 Debian 开发者？**
    - “上游作者”是指作品的作者或开发者，他们负责编写和开发该作品。而 “Debian 开发者” 通常使用现有的作品，将其制作成 Debian 软件包 - 在这种情况下，“Debian 维护者”这个术语更为准确。
    - 实际上，这两个角色之间可以有交集：Debian 维护者可能会编写一个补丁，使得所有使用该作品的用户受益。一般来说，Debian 鼓励负责 Debian 软件包的人也参与“上游”开发（他们因此成为贡献者，而不只是程序的普通用户）。或者，Debian 开发者也可以创建工具或文档，像是 Debian 分发版的包装帮助工具（例如 _debhelper_）或集成框架（例如 _ca-certificates_），并成为这些创作的“上游作者”。
3. **我们不会隐藏问题**
- Debian 并不完美，每天都会有新的问题需要修复。Debian 会保持其所有的 bug 报告数据库始终公开，任何人提交的在线报告都会立即对其他人可见。
4. **我们的优先事项是我们的用户和自由软件**
- 这一承诺较难定义。Debian 在做出决策时会有所偏向，抛弃那些容易的解决方案，以避免影响用户体验，转而选择更加优雅、尽管实现起来更困难的解决方案。这意味着要优先考虑用户和自由软件的利益。
5. **不符合自由软件标准的作品**
- Debian 接受并理解用户可能会想要使用一些非自由的软件。这就是为什么该项目允许在其基础设施中使用和分发可以安全再分发的非自由软件 Debian 包。

**_社区_ 支持还是反对非自由部分？**

- 保持一个用于容纳非自由软件的结构（即“non-free”部分，详见旁白 [_词汇_ “main”、 “contrib” 和 “non-free” 存档](https://www.debian.org/doc/manuals/debian-handbook/sect.foundation-documents.en.htmlapt.en.html#sidebar.sections)）在 Debian 社区中经常成为辩论的主题。
- 反对者认为这会使人远离自由软件的替代品，违背了只为自由软件事业服务的原则。支持者则明确表示，大多数非自由软件包是“几乎自由的”，只是由于一个或两个烦人的限制（最常见的是禁止商业使用）。通过将这些作品分发到非自由分支，我们间接向作者解释，如果他们能将许可调整为符合主分支的标准，他们的作品将更为广泛传播和使用。因此，他们被礼貌地邀请修改许可，以达到这一目的。
- 在 2004 年首次尝试并未成功后，彻底移除非自由部分不太可能重新上议程，尤其是因为其中包含了许多有用的文档，这些文档只是因为不符合主分支的新要求而被移除。尤其是某些 GNU 项目发布的软件文档（如 Emacs 和 Make）。许多现代系统还需要所谓的“固件”，这些小型二进制文件是运行特定硬件所必需的，其中许多文件也只能在非自由部分找到。
- 非自由部分的继续存在偶尔与自由软件基金会发生摩擦，也是其拒绝正式推荐 Debian 作为操作系统的主要原因。