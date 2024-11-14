# 配置脚本

除了 `control` 文件，每个 Debian 包的 `control.tar.gz` 压缩包中可能还包含一些脚本，这些脚本在处理包的不同阶段被 `dpkg` 调用。Debian 政策详细描述了可能的情况，指定了调用的脚本及它们接收的参数。这些过程可能很复杂，因为如果其中一个脚本失败，`dpkg` 会尝试通过取消当前的安装或删除操作来恢复到一个满意的状态（只要这是可能的）。

→ [https://www.debian.org/doc/debian-policy/ch-maintainerscripts.html](https://www.debian.org/doc/debian-policy/ch-maintainerscripts.html)

**_深入了解_ `dpkg` 的数据库**

所有已安装软件包的配置脚本都存储在 `/var/lib/dpkg/info/` 目录中，以包名为前缀的文件形式存在。该目录还包含每个包的 `.list` 后缀的文件，其中列出了属于该包的所有文件。

`/var/lib/dpkg/status` 文件包含一系列数据块（格式遵循著名的邮件头 RFC 2822），描述每个软件包的状态。已安装包的 `control` 文件中的信息也会在那里复制。

通常，`preinst` 脚本会在安装包之前执行，`postinst` 紧随其后。类似地，`prerm` 会在包删除之前调用，`postrm` 会在删除之后执行。包的更新相当于删除旧版本并安装新版本。这里无法详细描述所有可能的场景，但我们将讨论两种最常见的情况：安装/更新和删除。

**_注意_ 脚本的符号名称**

本节中描述的过程调用配置脚本时使用了特定的名称，例如 `old-prerm` 或 `new-postinst`。分别是旧版本包中包含的 `prerm` 脚本（更新之前安装的）和新版本包中包含的 `postinst` 脚本（通过更新安装的）。

**_提示_ 状态图**

Manoj Srivastava 和 Margarita Manterola 制作了以下图表，解释了 `dpkg` 如何调用配置脚本。

→ [https://people.debian.org/~srivasta/MaintainerScripts.html](https://people.debian.org/~srivasta/MaintainerScripts.html)

→ [https://www.debian.org/doc/debian-policy/ap-flowcharts.html](https://www.debian.org/doc/debian-policy/ap-flowcharts.html)