# 二进制软件包的结构

Debian软件包格式的设计使得其内容可以在任何拥有经典命令 `ar`、`tar` 和 `xz`（有时是 `gzip` 或 `bzip2`）的Unix系统上提取。这看似微不足道的特性对软件包的可移植性和灾难恢复非常重要。

例如，假设您不小心删除了 `dpkg` 程序，这样您将无法再安装Debian软件包。由于 `dpkg` 本身就是一个Debian软件包，似乎您的系统就彻底崩溃了……幸运的是，您知道软件包的格式，因此可以[下载](https://www.debian.org/distrib/packages#search_packages) `dpkg` 软件包的 `.deb` 文件并手动安装它（请参见侧边栏 [_TOOLS_ `dpkg`、`APT` 和 `ar`](https://www.debian.org/doc/manuals/debian-handbook/packaging-system.en.htmlpackaging-system.en.html#sidebar.dpkg-apt-ar)）。如果由于某种不幸的情况，`ar`、`tar` 或 `gzip`/`xz`/`bzip2` 等程序之一或多个消失了，您只需要从另一个系统中复制缺失的程序（因为这些程序各自独立运行，无需其他依赖，简单的复制即可）。如果您的系统遭遇了更严重的故障，甚至这些工具都无法工作（也许系统中最深层的库文件丢失了？），您可以尝试使用 `busybox` 的静态版本（包含在 `busybox-static` 包中），它更加自给自足，提供了 `busybox ar`、`busybox tar` 和 `busybox xz` 等子命令。

_如果发生不幸的情况，最好还要有系统的备份（请参见 [第9.10节，“备份”](https://www.debian.org/doc/manuals/debian-handbook/packaging-system.en.htmlsect.backup.en.html)）。_

**_工具_ `dpkg`、`APT` 和 `ar`**

`dpkg` 是处理 `.deb` 文件（二进制软件包）的程序，主要用于提取、分析和解包这些文件。

APT（“高级包管理工具”的缩写）是一组程序，允许对系统进行更高层次的操作：安装或卸载软件包（同时确保依赖关系得到满足）、更新和升级系统、列出可用的软件包等。

至于 `ar` 程序，它由 `binutils` 包提供，允许处理同名的文件：

-   `ar t _archive_` 显示归档文件中包含的文件列表，
-   `ar x _archive_` 将文件从归档中提取到当前工作目录，
-   `ar d _archive_ _file_` 从归档中删除指定的文件，等等。

它的手册页 `ar(1)` 记录了所有其他功能。`ar` 是一个非常基础的工具，Unix管理员通常只在极少数情况下使用它，但管理员通常会使用更为复杂的归档和文件管理程序 `tar`。因此，在误删除 `dpkg` 的情况下，恢复它非常简单。您只需下载Debian软件包并从系统根目录（`/`）中的 `data.tar.xz` 归档中提取内容：

```
# ar x dpkg_1.20.9_amd64.deb
# tar -C / -p -xJf data.tar.xz
```

**_基础知识回顾_ 手册页标注**

对于初学者来说，文献中提到的“ar(1)”可能会感到困惑。这通常是指 `ar` 手册页，位于第1节。

有时这种标注也用于消除歧义，例如区分 `printf` 命令（也可以通过 `printf(1)` 指定）和C语言中的 `printf` 函数（可以通过 `printf(3)` 指定）。

[第7章，“解决问题和查找相关信息”](https://www.debian.org/doc/manuals/debian-handbook/packaging-system.en.htmlsolving-problems.en.html) 更详细地讨论了手册页（参见 [第7.1.1节，“手册页”](https://www.debian.org/doc/manuals/debian-handbook/packaging-system.en.htmlsolving-problems.en.html#sect.manual-pages)）。

查看一个 `.deb` 文件的内容：

```
$ ar t dpkg_1.20.9_amd64.deb
debian-binary
control.tar.gz
data.tar.xz
$ ar x dpkg_1.20.9_amd64.deb
$ ls
control.tar.gz  data.tar.xz  debian-binary  dpkg_1.20.9_amd64.deb
$ tar tJf data.tar.xz | head -n 16
./
./etc/
./etc/alternatives/
./etc/alternatives/README
./etc/cron.daily/
./etc/cron.daily/dpkg
./etc/dpkg/
./etc/dpkg/dpkg.cfg
./etc/dpkg/dpkg.cfg.d/
./etc/logrotate.d/
./etc/logrotate.d/alternatives
./etc/logrotate.d/dpkg
./sbin/
./sbin/start-stop-daemon
./usr/
./usr/bin/
$ tar tJf control.tar.xz
./
./conffiles
./control
./md5sums
./postrm
$ cat debian-binary
2.0
```

正如您所看到的，Debian软件包的 `ar` 归档包含三个文件：

`debian-binary`

这是一个文本文件，简单地指示 `.deb` 文件的软件包格式版本。在Debian Bullseye中，它仍然是版本 2.0。

`control.tar.xz`

这个归档文件包含所有可用的元信息，如软件包的名称和版本，以及一些在安装、卸载前后运行的脚本。一些元信息允许软件包管理工具确定是否可以安装或卸载该软件包，例如根据系统上已经安装的软件包列表，或者检查文件是否已经在本地修改过。

`data.tar.xz`、`data.tar.bz2`、`data.tar.gz`

这个归档包含所有从软件包中提取的文件；可执行文件、库文件、文档等都存储在这里。软件包可能使用不同的压缩格式，因此文件名可能会有所不同，例如 `xz`、`bzip2` 或 `gzip`。