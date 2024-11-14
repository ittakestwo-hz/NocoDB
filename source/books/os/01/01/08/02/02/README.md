# 安装与删除

使用 APT，软件包可以通过 `apt install _package_` 和 `apt remove _package_` 命令分别被添加或从系统中删除。在这两种情况下，APT 会自动安装必要的依赖包，或删除依赖于正在被删除的包的其他软件包。`apt purge _package_` 命令会进行完全卸载，包括删除配置文件。

**_提示_ 多次安装相同的软件包列表**

在多台计算机上系统地安装相同的软件包列表可能非常有用。这可以通过以下简单步骤完成。

首先，获取作为“模型”的计算机上已安装的软件包列表。

```
$ dpkg --get-selections >pkg-list
```

`pkg-list` 文件中将包含已安装的软件包列表。接下来，将 `pkg-list` 文件转移到你想要更新的计算机上，并使用以下命令：

```
## Update dpkg's database of known packages
# avail=`mktemp`
# apt-cache dumpavail > "$avail"
# dpkg --merge-avail "$avail"
# rm -f "$avail"
## Update dpkg's selections
# dpkg --set-selections < pkg-list
## Ask apt-get to install the selected packages
# apt-get dselect-upgrade
```

第一组命令记录了 dpkg 数据库中的可用软件包列表。然后，`dpkg --set-selections` 恢复你希望安装的软件包选择，最后 `apt-get` 执行所需的操作！`aptitude` 没有这个命令。

**_提示_ 同时删除和安装软件包**

可以要求 `apt`（或 `apt-get`，或 `aptitude`）在同一命令行中安装某些软件包并删除其他软件包，只需在包名后添加后缀。在 `apt install` 命令中，删除包时在包名后添加“`-`”。在 `apt remove` 命令中，安装包时在包名后添加“`+`”。

以下示例展示了两种不同的方式来安装 _package1_ 并删除 _package2_。

```
# apt install package1 package2-
```

```
# apt remove package1+ package2
```

这也可以用来排除本来会被安装的包，例如，由于自动安装 `Recommends` 包而需要安装的包。通常，依赖解析器会将这些信息作为提示来寻找替代方案。

**_提示_ `apt --reinstall` 和 `aptitude reinstall`**

系统在删除或修改软件包文件后，有时可能会损坏。恢复这些文件最简单的方法是重新安装受影响的软件包。不幸的是，包管理系统认为该软件包已经安装，并会礼貌地拒绝重新安装它；为了避免这种情况，可以使用 `apt` 和 `apt-get` 命令的 `--reinstall` 选项。以下命令即使软件包已经存在，也会重新安装 postfix：

```
# apt --reinstall install postfix
```

`aptitude` 命令行略有不同，但可以通过 `aptitude reinstall postfix` 实现相同的结果。

`dpkg` 不会出现这个问题，但管理员通常很少直接使用它。

小心！使用 `apt --reinstall` 恢复在攻击中修改的包，肯定无法恢复系统到原来的状态。[第 14.7 节，“处理被攻击的机器”](https://www.debian.org/doc/manuals/debian-handbook/sect.apt-get.en.htmlsect.dealing-with-compromised-machine.en.html) 详细说明了处理被攻破系统时需要采取的步骤。

这些命令不会恢复配置文件。但是，正如你在 [第 5.2.3 节，“校验和、配置文件列表等”](https://www.debian.org/doc/manuals/debian-handbook/sect.apt-get.en.htmlsect.package-meta-information.en.html#sect.conffiles)（也请参见边栏 [_进一步了解_ 强制 dpkg 提问配置文件](https://www.debian.org/doc/manuals/debian-handbook/sect.apt-get.en.htmlsect.package-meta-information.en.html#sidebar.questions-conffiles-bis)）中学到的，你可以使用以下命令被提示安装未修改版本，甚至恢复已删除的配置文件。

```
# apt --reinstall -o Dpkg::Options::="--force-confask,confmiss" install package
```

有些软件包不会随包一起提供 `/etc` 目录下的配置文件。相反，它们在安装过程中会通过复制骨架文件或通过脚本写入配置文件。例如，`/etc/inputrc` 文件是 `/usr/share/readline/inputrc` 的一个副本。在这种情况下，上述命令将不起作用。

如果 `sources.list` 文件提到了多个发行版，你可以指定要安装的软件包版本。可以通过 `apt install _package_=_version_` 请求特定的版本号，但通常更推荐指明它的发行版（Stable、Testing 或 Unstable）——通过 `apt install _package_/_distribution_`。通过此命令，可以回退到软件包的旧版本（例如，如果你知道它运行良好），前提是该版本仍然可以在 `sources.list` 文件中引用的源中找到。否则，可以使用 `snapshot.debian.org` 存档来帮助恢复（请参见边栏 [_进一步了解_ 旧版本软件包：`snapshot.debian.org` 和 `archive.debian.org`](https://www.debian.org/doc/manuals/debian-handbook/sect.apt-get.en.htmlapt.en.html#sidebar.snapshot.debian.org)）。

**示例 6.4. 安装 Unstable 版本的 spamassassin**

```
# apt install spamassassin/unstable
```

如果你要安装的软件包以简单的 `.deb` 文件形式提供，并且没有关联的包仓库，仍然可以使用 APT 来安装它及其依赖项（前提是这些依赖项在配置的仓库中可用）。只需使用以下简单命令：`apt install ./_path-to-the-package.deb_`。前面的 `./` 非常重要，它明确表示我们引用的是文件名而不是仓库中可用的软件包名称。

**_进一步了解_ `.deb` 文件的缓存**

APT 会将每个下载的 `.deb` 文件的副本保存在 `/var/cache/apt/archives/` 目录中。如果更新频繁，这个目录可能会迅速占用大量磁盘空间，存放每个软件包的多个版本；因此，应该定期清理。可以使用两个命令：`apt-get clean` 完全清空目录；`apt-get autoclean` 只会删除那些已经无法下载的软件包（因为它们已从 Debian 镜像站消失），因此这些包明显是无用的（配置参数 `APT::Clean-Installed` 可以防止删除当前已安装的 `.deb` 文件）。