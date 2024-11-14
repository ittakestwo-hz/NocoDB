# 安装 Debian

在了解了当前服务器的所有必要信息后，我们可以关闭服务器并开始在其上安装 Debian。

为了选择合适的版本，我们需要了解计算机的架构。如果是较新的 PC，通常是 amd64 架构（旧的 PC 通常使用 i386 架构）。在其他情况下，我们可以根据之前使用的系统来缩小选择范围。

[表 3.1](https://www.debian.org/doc/manuals/debian-handbook/sect.how-to-migrate.en.htmlsect.how-to-migrate.en.html#tab-corresp) 并不打算详尽列出所有可能的架构，但可能会有所帮助。请注意，它列出了在当前稳定版本中不再受支持的 Debian 架构。在任何情况下，计算机的原始文档是获取此信息的最可靠来源。

**表 3.1. 操作系统与架构对应关系**

| 操作系统 | 架构 |
| --- | --- |
| DEC Unix (OSF/1) | alpha, mipsel |
| HP Unix | ia64, hppa |
| IBM AIX | powerpc |
| Irix | mips |
| OS X | amd64, powerpc, i386 |
| z/OS, MVS | s390x, s390 |
| Solaris, SunOS | sparc, i386, m68k |
| Ultrix | mips |
| VMS | alpha |
| Windows 95/98/ME | i386 |
| Windows NT/2000 | i386, alpha, ia64, mipsel |
| Windows XP / Windows Server 2008 | i386, amd64, ia64 |
| Windows RT | armel, armhf, arm64 |
| Windows Vista / Windows 7-8-10 | i386, amd64 |

**_硬件_ 64 位 PC 与 32 位 PC**

大多数现代计算机配备 64 位 Intel 或 AMD 处理器，并且与较旧的 32 位处理器兼容，因此为 "i386" 架构编译的软件也可以运行。然而，这种兼容模式并不能充分发挥这些新处理器的能力。这就是为什么 Debian 提供 "amd64" 架构的原因，它适用于最新的 AMD 处理器以及 Intel 的 "em64t" 处理器（包括大多数 Core 系列），这两者在硬件架构上非常相似。