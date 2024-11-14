# 安装额外的软件

安装时选择的配置文件对应了已安装的软件包，但这不一定符合计算机的实际使用需求。因此，你可能需要使用软件包管理工具来优化已安装软件包的选择。如果选择了“Debian 桌面环境”配置文件，常用的两个工具（已经自动安装）是 `apt`（命令行工具）和 `synaptic`（菜单中的“Synaptic 包管理器”）。

为了方便安装一组有机的软件包，Debian 提供了针对特定用途（如邮件服务器、文件服务器等）的“任务”。你已经在安装过程中选择了这些任务，并且可以通过软件包管理工具再次访问它们，比如通过 `aptitude`（任务在一个独立的部分列出）和 `synaptic`（通过菜单 **编辑** → **按任务标记软件包...**）。

Aptitude 是一个全屏文本模式的 APT 界面。它允许用户根据不同类别（已安装的或未安装的包、按任务、按部分等）浏览可用的软件包列表，并查看每个包的所有相关信息（如依赖、冲突、描述等）。每个包可以标记为“安装”（**+** 键）或“删除”（**\-** 键）。一旦你按下 **g** 键（“g”代表“go！”），所有这些操作将同时执行。如果你忘记了某些程序，不用担心；初步安装完成后，你可以再次运行 `aptitude`。

**_提示_ Debian 关心非英语语言使用者**

有几个任务是为了将系统本地化为英语以外的其他语言而设置的。这些任务包括翻译的文档、词典以及其他一些对不同语言用户有用的软件包。如果在安装过程中选择了非英语语言，相关的任务将自动被选中。

当然，你也可以选择不安装任何任务。在这种情况下，你可以使用 `apt` 或 `aptitude` 命令手动安装所需的软件包（这两个命令都可以从命令行访问）。可以使用 `apt-cache search task _keyword_` 命令来查找包。

**_词汇_ 软件包依赖与冲突**

在 Debian 的打包术语中，“依赖”指的是另一个包，是软件包正常运行所必需的。相反，“冲突”指的是无法与另一个软件包并行安装的包。

这些概念在[第 5 章，_打包系统：工具与基本原理_](https://www.debian.org/doc/manuals/debian-handbook/sect.after-first-boot.en.htmlpackaging-system.en.html)中有更详细的讨论。