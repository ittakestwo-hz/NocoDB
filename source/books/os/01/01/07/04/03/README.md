# 查询 `dpkg` 的数据库和检查 `.deb` 文件

## 回到基础：选项语法

大多数选项都有“长版本”（一个或多个相关单词，前面加上双破折号）和“短版本”（一个字母，通常是长版本单词的首字母，前面加上单破折号）。这种约定非常常见，已经成为 POSIX 标准。

在本节结束之前，我们将研究 `dpkg` 的一些选项，这些选项用于查询内部数据库以获取信息。首先给出长版本选项，然后是相应的短版本（这些选项显然会接受相同的参数），我们列举如下：

- `--listfiles package`（或 `-L`），列出该软件包安装的文件；
- `--search file`（或 `-S`），查找包含该文件的软件包；
- `--status package`（或 `-s`），显示已安装软件包的头部信息；
- `--list`（或 `-l`），显示系统已知的软件包及其安装状态；
- `--contents file.deb`（或 `-c`），列出指定的 Debian 软件包中的文件；
- `--info file.deb`（或 `-I`），显示该 Debian 软件包的头部信息。

## 注意：`dpkg --search` 和合并的 `/usr`

由于多种原因，Debian 默认将一些顶级目录安装为指向 `/usr` 下对应目录的符号链接。例如，`/bin`、`/sbin` 和 `/lib` 现在是分别指向 `/usr/bin`、`/usr/sbin` 和 `/usr/lib` 的符号链接。虽然这种做法带来了好处，但也可能引起一些混淆。例如，当你查询 `dpkg` 查找某个文件所属的软件包时，它只有在你询问原始路径时才能正确返回结果：

```
$ dpkg --search /bin/mount
mount: /bin/mount
$ dpkg --search /usr/bin/mount
dpkg-query: no path found matching pattern /usr/bin/mount
$ dpkg --search /bin/apt
dpkg-query: no path found matching pattern /bin/apt
$ dpkg --search /usr/bin/apt
apt: /usr/bin/apt
```

这个问题目前已经被追踪为 bug #858331。目前也有讨论是否这种方法是适得其反的。
→ [https://bugs.debian.org/858331](https://bugs.debian.org/858331)

## 示例 5.5. 使用 `dpkg` 的各种查询

```
$ dpkg -L base-passwd
/.
/usr
/usr/sbin
/usr/sbin/update-passwd
/usr/share
/usr/share/base-passwd
/usr/share/base-passwd/group.master
/usr/share/base-passwd/passwd.master
/usr/share/doc
/usr/share/doc/base-passwd
/usr/share/doc/base-passwd/README
/usr/share/doc/base-passwd/changelog.gz
/usr/share/doc/base-passwd/copyright
/usr/share/doc/base-passwd/users-and-groups.html
/usr/share/doc/base-passwd/users-and-groups.txt.gz
/usr/share/doc-base
/usr/share/doc-base/users-and-groups
/usr/share/lintian
/usr/share/lintian/overrides
/usr/share/lintian/overrides/base-passwd
/usr/share/man
/usr/share/man/de
/usr/share/man/de/man8
/usr/share/man/de/man8/update-passwd.8.gz
/usr/share/man/es
/usr/share/man/es/man8
/usr/share/man/es/man8/update-passwd.8.gz
/usr/share/man/fr
/usr/share/man/fr/man8
/usr/share/man/fr/man8/update-passwd.8.gz
/usr/share/man/ja
/usr/share/man/ja/man8
/usr/share/man/ja/man8/update-passwd.8.gz
/usr/share/man/man8
/usr/share/man/man8/update-passwd.8.gz
/usr/share/man/pl
/usr/share/man/pl/man8
/usr/share/man/pl/man8/update-passwd.8.gz
/usr/share/man/ru
/usr/share/man/ru/man8
/usr/share/man/ru/man8/update-passwd.8.gz
$ dpkg -S /bin/date
coreutils: /bin/date
$ dpkg -s coreutils
Package: coreutils
Essential: yes
Status: install ok installed
Priority: required
Section: utils
Installed-Size: 17478
Maintainer: Michael Stone <mstone@debian.org>
Architecture: amd64
Multi-Arch: foreign
Source: coreutils (8.32-4)
Version: 8.32-4+b1
Pre-Depends: libacl1 (>= 2.2.23), libattr1 (>= 1:2.4.44), libc6 (>= 2.28), libgmp10, libselinux1 (>= 3.1~)
Description: GNU core utilities
 This package contains the basic file, shell and text manipulation
 utilities which are expected to exist on every operating system.
 .
 Specifically, this package includes:
 arch base64 basename cat chcon chgrp chmod chown chroot cksum comm cp
 csplit cut date dd df dir dircolors dirname du echo env expand expr
 factor false flock fmt fold groups head hostid id install join link ln
 logname ls md5sum mkdir mkfifo mknod mktemp mv nice nl nohup nproc numfmt
 od paste pathchk pinky pr printenv printf ptx pwd readlink realpath rm
 rmdir runcon sha*sum seq shred sleep sort split stat stty sum sync tac
 tail tee test timeout touch tr true truncate tsort tty uname unexpand
 uniq unlink users vdir wc who whoami yes
Homepage: http://gnu.org/software/coreutils
$ dpkg -l 'b*'
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name                       Version       Architecture Description
+++-==========================-==============-============-==================================
un  backupninja                <none>         <none>       (no description available)
un  backuppc                   <none>         <none>       (no description available)
ii  baloo-kf5                  5.78.0-3       amd64        framework for searching and manag>
un  balsa                      <none>         <none>       (no description available)
ii  baobab                     3.38.0-1       amd64        GNOME disk usage analyzer
un  base                       <none>         <none>       (no description available)
un  base-config                <none>         <none>       (no description available)
ii  base-files                 11.1           amd64        Debian base system miscellaneous >
ii  base-passwd                3.5.51         amd64        Debian base system master passwor>
ii  bash                       5.1-2+b1       amd64        GNU Bourne Again SHell
[..]
$ dpkg -c /var/cache/apt/archives/bash_5.1-3+b1_amd64.deb
drwxr-xr-x root/root         0 2021-07-25 20:43 ./
drwxr-xr-x root/root         0 2021-07-25 20:43 ./bin/
-rwxr-xr-x root/root   1234376 2021-07-25 20:43 ./bin/bash
drwxr-xr-x root/root         0 2021-07-25 20:43 ./etc/
-rw-r--r-- root/root      1994 2021-07-25 20:43 ./etc/bash.bashrc
drwxr-xr-x root/root         0 2021-07-25 20:43 ./etc/skel/
-rw-r--r-- root/root       220 2021-07-25 20:43 ./etc/skel/.bash_logout
-rw-r--r-- root/root      3526 2021-07-25 20:43 ./etc/skel/.bashrc
-rw-r--r-- root/root       807 2021-07-25 20:43 ./etc/skel/.profile
drwxr-xr-x root/root         0 2021-07-25 20:43 ./usr/
drwxr-xr-x root/root         0 2021-07-25 20:43 ./usr/bin/
-rwxr-xr-x root/root      6759 2021-07-25 20:43 ./usr/bin/bashbug
-rwxr-xr-x root/root     14648 2021-07-25 20:43 ./usr/bin/clear_console
drwxr-xr-x root/root         0 2021-07-25 20:43 ./usr/share/
drwxr-xr-x root/root         0 2021-07-25 20:43 ./usr/share/doc/
[..]
$ dpkg -I /var/cache/apt/archives/bash_5.1-3+b1_amd64.deb
 new Debian package, version 2.0.
 size 1416600 bytes: control archive=7256 bytes.
      77 bytes,     4 lines      conffiles
    1030 bytes,    27 lines      control
    4511 bytes,    64 lines      md5sums
     603 bytes,    31 lines   *  postinst             #!/bin/bash
     500 bytes,    25 lines   *  postrm               #!/bin/sh
   14536 bytes,    33 lines   *  preinst              
     289 bytes,    22 lines   *  prerm                #!/bin/bash
 Package: bash
 Source: bash (5.1-3)
 Version: 5.1-3+b1
 Architecture: amd64
 Essential: yes
 Maintainer: Matthias Klose <doko@debian.org>
 Installed-Size: 6470
 Pre-Depends: libc6 (>= 2.25), libtinfo6 (>= 6)
 Depends: base-files (>= 2.1.12), debianutils (>= 2.15)
 Recommends: bash-completion (>= 20060301-0)
 Suggests: bash-doc
 Conflicts: bash-completion (<< 20060301-0)
 Replaces: bash-completion (<< 20060301-0), bash-doc (<= 2.05-1)
 Section: shells
 Priority: required
 Multi-Arch: foreign
 Homepage: http://tiswww.case.edu/php/chet/bash/bashtop.html
 Description: GNU Bourne Again SHell
  Bash is an sh-compatible command language interpreter that executes
  commands read from the standard input or from a file.  Bash also
  incorporates useful features from the Korn and C shells (ksh and csh).
  .
  Bash is ultimately intended to be a conformant implementation of the
  IEEE POSIX Shell and Tools specification (IEEE Working Group 1003.2).
  .
  The Programmable Completion Code, by Ian Macdonald, is now found in
  the bash-completion package.
```

## 进一步：版本比较

由于 `dpkg` 是用于处理 Debian 软件包的程序，它也提供了比较版本号的逻辑的参考实现。这就是它提供 `--compare-versions` 选项的原因，该选项可以被外部程序（尤其是由 `dpkg` 本身执行的配置脚本）使用。这个选项需要三个参数：一个版本号、一个比较操作符和第二个版本号。不同的操作符包括：`lt`（严格小于）、`le`（小于或等于）、`eq`（等于）、`ne`（不等于）、`ge`（大于或等于）和 `gt`（严格大于）。如果比较正确，`dpkg` 会返回 0（成功）；否则，会返回非零值（表示失败）。

```
$ dpkg --compare-versions 1.2-3 gt 1.1-4
$ echo $?
0
$ dpkg --compare-versions 1.2-3 lt 1.1-4
$ echo $?
1
$ dpkg --compare-versions 2.6.0pre3-1 lt 2.6.0-1
$ echo $?
1
```

请注意最后一次比较的意外失败：对于 `dpkg`，`pre`（通常表示预发布版本）没有特定的含义，该程序按字母顺序（a < b < c ...）来比较字符。因此，它将“0pre3”视为大于“0”。当我们希望软件包的版本号表示预发布版本时，我们使用波浪号字符“~”：

```
$ dpkg --compare-versions 2.6.0~pre3-1 lt 2.6.0-1
$ echo $?
0
```