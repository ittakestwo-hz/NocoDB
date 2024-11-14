# 接管一个现有的 Debian 服务器

要有效地接管一个已经运行 Debian 的服务器的维护工作，可以通过以下几个步骤来分析当前的系统。

首先检查文件 `/etc/debian_version`，该文件通常包含已安装 Debian 系统的版本号（它是 _base-files_ 包的一部分）。如果文件中显示的是 `_codename_/sid`，这意味着系统是通过来自开发分支（如 testing 或 unstable）的软件包更新的。

`apt-show-versions` 程序（来自 Debian 的同名包）可以检查已安装的包列表，并识别可用的版本。`aptitude` 也可以执行类似任务，尽管方式不如 `apt-show-versions` 系统化。

查看 `/etc/apt/sources.list` 文件（及 `/etc/apt/sources.list.d/` 目录）可以帮助确定已安装的 Debian 软件包的来源。如果源列表中出现许多未知的来源，管理员可能需要选择完全重新安装计算机系统，以确保与 Debian 提供的软件包的最佳兼容性。

`sources.list` 文件通常是一个很好的指示器：大多数管理员至少会在文件中保留曾使用过的 APT 源列表（即使是注释掉的）。但需要注意的是，曾经使用的源可能已被删除，而且有些通过互联网下载的随机软件包可能是通过 `dpkg` 命令手动安装的。在这种情况下，机器表面看起来像是一个“标准”的 Debian 系统，但实际上它可能已经安装了外部软件包。因此，您需要注意任何能够揭示外部包存在的迹象（如 `deb` 文件出现在不寻常的目录中，包版本号带有特殊后缀，指示它来自 Debian 项目以外的来源，例如 `ubuntu` 或 `lmde` 等）。

同样，分析 `/usr/local/` 目录的内容也很有价值，因为该目录用于存放手动编译和安装的程序。列出以这种方式安装的软件可以提供有用的信息，尤其是在问及为什么没有使用相应的 Debian 包时。

**_快速查看_ cruft/cruft-ng, debsums 和 apt-show-versions**

`cruft` 和 `cruft-ng` 包可以列出所有不属于任何包的文件。它们带有一些过滤器（有效性和更新频率各不相同），以避免报告一些合法的文件（例如由 Debian 包生成的文件，或者未由 `dpkg` 管理的生成配置文件等）。

请注意，**不要盲目删除** `cruft` 和 `cruft-ng` 列出的所有文件！

`debsums` 包允许检查由软件包安装的每个文件的 MD5 哈希值是否与参考哈希值匹配，帮助识别哪些文件可能已被更改（参见 [_提示_ 查找更改的文件](https://www.debian.org/doc/manuals/debian-handbook/sect.how-to-migrate.en.htmlsect.dist-upgrade.en.html#sidebar.debsums)）。请注意，创建的文件（例如由 Debian 包生成的文件或未由 `dpkg` 管理的生成配置文件等）不在此检查范围内。

`apt-show-versions` 包提供了一个工具，用于检查没有软件包源的已安装软件包，并帮助确定第三方软件包（参见 [第 6.7.3.1 节，“从 Debian 存档中删除的包”](https://www.debian.org/doc/manuals/debian-handbook/sect.how-to-migrate.en.htmlsect.dist-upgrade.en.html#sect.apt-show-versions)）。