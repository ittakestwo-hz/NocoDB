# Debian 开发者

Debian 开发者有着各种不同的职责，作为正式项目成员，他们对项目的方向具有很大的影响力。通常，一个 Debian 开发者至少负责一个软件包，但根据他们的时间和兴趣，他们可以自由参与多个团队和项目，从而承担更多的责任。

→ [Debian 开发者页面](https://www.debian.org/devel/people)  
→ [Debian 组织介绍](https://www.debian.org/intro/organization)  
→ [Debian 团队列表](https://wiki.debian.org/Teams)

## 开发者数据库
Debian 拥有一个包含所有注册开发者的数据库，记录了相关信息（地址、电话、地理坐标等）。其中一些信息（如名字、姓氏、国家、项目中的用户名、IRC 用户名、GnuPG 密钥等）是公开的，并可在网上查看。

→ [Debian 开发者数据库](https://db.debian.org/)  
这些地理坐标可以生成一张全球开发者分布图。Debian 是一个真正的国际项目：其开发者遍布所有大洲，尽管大多数位于“西方国家”。

### Debian 开发者的全球分布

图 1.1：Debian 开发者的全球分布

软件包维护是一个相对有条理的活动，通常有详细的文档，甚至有明确的规定。实际上，它必须遵循 Debian 政策中规定的所有标准。幸运的是，有许多工具可以帮助维护者的工作。因此，开发者可以将更多精力集中在软件包的具体细节和更复杂的任务上，如修复 bug。

→ [Debian 政策文档](https://www.debian.org/doc/debian-policy/)

## 软件包维护——开发者的工作
维护一个软件包首先意味着“打包”一个软件。具体来说，就是定义安装方式，以确保安装后软件能够正常运行，并符合 Debian 项目为自己设定的规则。这个过程的结果保存在一个 .deb 文件中。软件的有效安装仅需提取这个压缩档案并执行其中的安装前或安装后脚本。

在这个初步阶段之后，维护周期真正开始：准备更新以跟进最新版本的 Debian 政策，修复用户报告的 bug，以及包括新的“上游”版本，该程序本身仍在持续开发。例如，在初次打包时，一个程序的版本是 1.2.3。经过几个月的开发，原作者发布了一个新的稳定版本，版本号为 1.4.0。此时，Debian 软件包维护者应更新软件包，以便用户能够享受到最新的稳定版本。

Debian 政策是 Debian 项目的核心要素之一，确保软件包的质量和发行版的完全互操作性。正是由于这个政策，Debian 即使在其庞大规模下，仍然能够保持一致性。该政策并非一成不变，而是通过 Debian 开发者在 debian-policy@lists.debian.org 邮件列表上的提案不断发展。所有相关方一致同意的修改会由一个小组维护者接受并应用到文档中，他们不负编辑责任，仅负责将开发者达成共识的修改内容纳入文本。您可以通过错误追踪系统阅读当前的修正提案：

→ [Debian 政策提案](https://bugs.debian.org/debian-policy)

### 社区——政策编辑流程
任何人都可以通过提交一个严重性为“愿望清单”的 bug 报告来提议修改 Debian 政策。随后，开始的流程在 [Debian 政策文档](https://www.debian.org/doc/debian-policy/ap-process.html) 中有详细记录。如果确认问题需要通过在 Debian 政策中创建新规则来解决，讨论将在 debian-policy@lists.debian.org 邮件列表上展开，直到达成共识并提出提案。接着，会有人起草修订案并提交审批（以补丁的形式进行审查）。一旦另外两位开发者批准该修订案反映了之前讨论达成的共识（即他们“支持”该修订案），该提案即可由一名 debian-policy 包维护者将其纳入官方文档。如果流程在任何阶段失败，维护者会关闭该 bug，将提案标记为“拒绝”。

### Debian 政策——文档
每个软件包的文档存储在 `/usr/share/doc/package/` 目录中。该目录通常包含一个 README.Debian 文件，描述了软件包维护者对 Debian 进行的特定调整。因此，在进行配置之前，阅读这个文件是明智的，以便借鉴他们的经验。还会有一个 changelog.Debian.gz 文件，描述了 Debian 维护者对版本更新的修改。这不应与 changelog.gz 文件（或类似文件）混淆，后者描述的是上游开发者所做的更改。版权文件中包括了作者和软件所采用的许可证信息。最后，还可能有一个名为 NEWS.Debian.gz 的文件，允许 Debian 开发者传达有关更新的重要信息；如果安装了 apt-listchanges，这些信息会自动显示。其他文件则是软件本身特有的。我们特别要指出的是 examples 子目录，通常包含配置文件的示例。

Debian 政策提供了有关打包的技术方面的详细指导。项目的庞大规模也带来了组织上的问题；这些问题由 Debian 宪法（Debian Constitution）处理，它规定了项目的结构和决策流程。换句话说，它建立了一个正式的治理系统。

这部宪法定义了一系列角色和职位，并规定了每个职位的责任和权力。特别值得注意的是，Debian 开发者始终拥有最终决策权，通过“全体决议”投票的方式进行决策，重要的修改（如影响基础文件的修改）需要经过三分之二（75%）的合格多数票才能通过。然而，开发者每年选举一位“领导者”，代表他们参加会议，并确保各团队之间的内部协调。这一选举通常是一次激烈的讨论过程。Debian 项目领导者（DPL）的角色并未在任何文档中明确定义：该职位的候选人通常会提出自己对该职位的定义。实际上，领导者的职能包括作为媒体代表，协调“内部”团队，并在项目中提供总体指导，开发者们可以与领导者产生共鸣：DPL 的意见通常被大多数项目成员默认为正确。

具体来说，领导者拥有实际权力；他们的投票可以解决平局；他们可以做出任何其他人不具备权力做出的决定，并且可以委派部分职责。

自项目开始以来，它分别由 Ian Murdock、Bruce Perens、Ian Jackson、Wichert Akkerman、Ben Collins、Bdale Garbee、Martin Michlmayr、Branden Robinson、Anthony Towns、Sam Hocevar、Steve McIntyre、Stefano Zacchiroli、Lucas Nussbaum、Neill McGovern、Mehdi Dogguy、Chris Lamb、Sam Hartman 和 Jonathan Carter 领导。

宪法还定义了一个“技术委员会”，该委员会的核心职责是在开发者未达成一致时做出技术决定。否则，委员会将扮演顾问角色，为未能做出决策的开发者提供帮助。需要注意的是，他们只有在相关方的邀请下才会介入。

最后，宪法定义了“项目秘书”的职位，负责组织与各种选举和全体决议相关的投票。

“全体决议”（GR）程序在宪法中有详细的说明，从初步讨论到最终投票计数。这个过程最有趣的方面在于，实际投票时，开发者需要对不同选项进行排序，选举结果通过 Condorcet 方法（更具体地说，是 Schulze 方法）决定。详细内容请参见：

→ [Debian 宪法](https://www.debian.org/devel/constitution)

### 文化——火药桶话题：激烈争论
“火药桶”话题指的是激烈的辩论，通常最终会导致人们相互攻击，因为双方的理性辩论已经耗尽。某些话题比其他话题更容易引发激烈争论（例如，选择文本编辑器，"你喜欢 vi 还是 emacs?" 是一个经典话题）。这些问题通常会引发快速的电子邮件交换，因为每个人都对这些问题有意见，而且这些问题本身非常个人化。

通常，这类讨论不会带来什么有用的结果；普遍的建议是避免参与此类辩论，或许快速浏览其中的内容，因为完整阅读会非常耗时。

尽管宪法建立了某种形式的民主，实际情况却完全不同：Debian 自然遵循自由软件的“行动主义”（do-ocracy）规则：谁做事，谁决定如何做。很多时间可能会浪费在讨论解决问题的不同方式上；最终被采纳的解决方案将是第一个既可行又令人满意的方案——它来自一个有能力的人投入的时间。

这也是获得认可的唯一途径：做一些有用

的事情，展示自己的能力。许多 Debian 的“行政”团队通过联名推荐成员，更青睐那些已经有效贡献并证明自己能力的志愿者。由于这些团队的工作是公开的，新贡献者可以观察并开始帮助，而不需要任何特殊的优待。这也是 Debian 常被描述为“功绩主义”的原因。

### 文化——功绩主义：知识的统治
功绩主义是一种政府形式，其中权力由最具功绩的人行使。对于 Debian 来说，功绩是一种衡量能力的标准，通过其他项目成员观察过去的行动来评估一个人的能力（前项目领导者 Stefano Zacchiroli 提到的“行动主义”，即“权力属于那些做事的人”）。他们的存在本身就证明了一定程度的能力；他们的成就通常是自由软件，源代码公开，同行可以轻松审查，以评估其质量。

这种有效的运作方法确保了“关键” Debian 团队的贡献者的质量。虽然这种方法并不完美，但偶尔也会有不接受这种操作方式的人。接受加入团队的开发者选择看似有些随意，甚至有时会觉得不公平。此外，并非每个人对团队所期望的服务有相同的定义。对一些人来说，等待 8 天才加入一个新的 Debian 软件包是不可接受的，而另一些人则可以耐心地等待 3 周，没有问题。因此，常常有来自不满者的投诉，抱怨一些团队的“服务质量”。

### 社区——新维护者的融入
负责接纳新开发者的团队是最常被批评的团队之一。必须承认，随着时间的推移，Debian 项目对所接纳的开发者要求越来越高。有些人可能会觉得不公平，但我们必须承认，在一个拥有超过 1,000 人的社区中，确保 Debian 为其用户生产的每一件事的质量和完整性已经变得更加困难。

此外，接纳过程通常由一个小团队——Debian 账户管理员（Debian Account Managers）进行审查。因此，他们在是否接纳一个志愿者成为 Debian 开发者社区的一员时，通常暴露于批评之下。在实践中，有时他们必须推迟接受一个人，直到他们对项目的运作有更多了解。当然，在成为正式开发者之前，任何人都可以通过获得现有开发者的赞助来为 Debian 做出贡献。