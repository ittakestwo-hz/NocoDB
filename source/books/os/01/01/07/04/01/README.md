# 安装软件包

`dpkg` 是用来安装已存在的 Debian 软件包的基本工具（因为它不会下载任何内容）。要进行安装，我们使用其 `-i` 或 `--install` 选项。

**示例 5.2：使用 `dpkg` 安装软件包**

```
# dpkg -i man-db_2.9.4-2_amd64.deb
(Reading database ... 227466 files and directories currently installed.)
Preparing to unpack man-db_2.9.4-2_amd64.deb ...
Unpacking man-db (2.9.4-2) over (2.8.5-2) ...
Setting up man-db (2.9.4-2) ...
Updating database of manual pages ...
man-db.service is a disabled or a static unit not running, not starting it.
Processing triggers for mailcap (3.69) ...
```

我们可以看到 `dpkg` 执行的不同步骤，因此能够确定错误发生的具体位置。安装过程实际上分为两个阶段：首先是解包，然后是配置。

`apt` 工具利用这一点，减少了对 `dpkg` 的调用次数（因为每次调用都很耗时，需要加载数据库到内存中，特别是已安装文件的列表）。

**示例 5.3：分开解包和配置**

```
# dpkg --unpack man-db_2.9.4-2_amd64.deb
(Reading database ... 227466 files and directories currently installed.)
Preparing to unpack man-db_2.9.4-2_amd64.deb ...
Unpacking man-db (2.9.4-2) over (2.9.4-2) ...
Processing triggers for mailcap (3.69) ...
# dpkg --configure man-db
Setting up man-db (2.9.4-2) ...
Updating database of manual pages ...
man-db.service is a disabled or a static unit not running, not starting it.
```

有时，`dpkg` 可能无法安装软件包并返回错误；如果用户指示忽略此错误，`dpkg` 只会发出警告。为此，`dpkg` 提供了不同的 `--force-*` 选项。通过运行 `dpkg --force-help` 命令或查看该命令的文档，可以获得这些选项的完整列表。最常见的错误，是文件冲突。当一个软件包包含一个已由另一个软件包安装的文件时，`dpkg` 会拒绝安装。此时会出现如下错误信息：

```
Unpacking libgdm (from .../libgdm_3.8.3-2_amd64.deb) ...
dpkg: error processing /var/cache/apt/archives/libgdm_3.8.3-2_amd64.deb (--unpack):
 trying to overwrite '/usr/bin/gdmflexiserver', which is also in package gdm3 3.4.1-9
```

在这种情况下，如果你认为替换该文件不会对系统稳定性造成重大风险（通常情况如此），可以使用 `--force-overwrite` 选项，这会告诉 `dpkg` 忽略此错误并覆盖该文件。

虽然 `dpkg` 提供了很多 `--force-*` 选项，但只有 `--force-overwrite` 是可能会经常使用的。这些选项仅在极少数情况下才需要使用，通常在 Debian Stable 中很少遇到。因此，最好尽量避免使用这些选项，以遵循包管理机制所强加的规则。别忘了，这些规则确保了系统的一致性和稳定性。

**_警告_ `--force-*` 选项的谨慎使用**

如果不小心使用了 `--force-*` 选项，可能会导致 APT 系列命令无法正常工作。实际上，其中一些选项允许在不满足依赖关系或发生冲突的情况下安装软件包。结果是系统的依赖关系不一致，APT 命令将拒绝执行任何操作，除非能够将系统恢复到一致的状态（这通常意味着安装缺失的依赖项或移除有问题的软件包）。这通常会导致类似以下的消息，通常出现在忽略了 `rdesktop` 软件包依赖于更高版本的 libc6 时：

```
# apt full-upgrade
[...]
You might want to run 'apt-get -f install' to correct these.
The following packages have unmet dependencies:
  rdesktop: Depends: libc6 (>= 2.5) but 2.3.6.ds1-13etch7 is installed
E: Unmet dependencies. Try using -f.
```

一个勇敢的管理员如果确信他们的分析是正确的，可能会选择忽略依赖关系或冲突，使用相应的 `--force-*` 选项。在这种情况下，如果他们希望继续使用 `apt` 或 `aptitude`，则必须编辑 `/var/lib/dpkg/status` 文件，删除或修改他们选择覆盖的依赖关系或冲突。

这种操作是一种不优雅的解决方案，应该避免使用，除非在最极端的情况下。更合适的解决方案通常是重新编译导致问题的软件包（见 [第 15.1 节，“从源代码重建软件包”](https://www.debian.org/doc/manuals/debian-handbook/sect.manipulating-packages-with-dpkg.en.htmldebian-packaging.en.html#sect.rebuilding-package)）或者使用来自像 `stable-backports` 这样的仓库的更新版本（见 [第 6.1.2.4 节，“稳定回溯”](https://www.debian.org/doc/manuals/debian-handbook/sect.manipulating-packages-with-dpkg.en.htmlapt.en.html#sect.apt-sources.list.stable.backports)）。