# 启动并启动安装程序

一旦BIOS开始从CD或DVD-ROM启动，Isolinux引导程序菜单会出现。在此阶段，Linux内核尚未加载；此菜单允许您选择要启动的内核，并输入可能在启动过程中传递给内核的参数。

对于标准安装，您只需选择“安装”或“图形安装”（使用箭头键），然后按**Enter**键启动安装过程的其余部分。如果DVD-ROM是“Multi-arch”磁盘，并且机器具有Intel或AMD 64位处理器，这些菜单选项将启用安装64位版本（_amd64_），并且32位版本的安装仍然可以在专用子菜单中选择（“32位安装选项”）。如果您的处理器是32位的，则没有选择的余地，菜单项将安装32位版本（_i386_）。

**_进一步了解_ 32位还是64位？**

32位和64位系统的根本区别在于内存地址的大小。理论上，32位系统不能使用超过4GB的RAM（2<sup>32</sup>字节）。实际上，可以通过使用`686-pae`内核变体来绕过这一限制，只要处理器支持PAE（物理地址扩展）功能。然而，使用该变体会显著影响系统性能。因此，在内存较大的服务器上使用64位模式是有用的。

对于办公电脑（性能差异只有几个百分点时几乎可以忽略不计），您需要记住，一些专有程序没有64位版本。技术上可以让它们在64位系统上运行，但您必须安装所有必要库的32位版本（参见[第5.4.5节，“多架构支持”](https://www.debian.org/doc/manuals/debian-handbook/sect.installation-steps.en.htmlsect.manipulating-packages-with-dpkg.en.html#sect.multi-arch)），有时还需要使用`setarch`或`linux32`（在util-linux包中）来欺骗应用程序，使其认为系统是32位的。

**_实践中_ 与现有Windows系统并存安装**

如果计算机已经运行Windows，安装Debian时并不需要删除现有系统。您可以将两个系统安装在不同的磁盘或分区上，启动计算机时选择要启动的系统。这种配置通常称为“双重启动”，Debian安装系统可以为您设置它。这是在安装的硬盘分区阶段以及设置引导加载程序时完成的（参见侧边栏[_实践中_ 缩小Windows分区](https://www.debian.org/doc/manuals/debian-handbook/sect.installation-steps.en.htmlsect.installation-steps.en.html#sidebar.shrinking-partition) 和[_注意_ 引导加载程序和双重启动](https://www.debian.org/doc/manuals/debian-handbook/sect.installation-steps.en.htmlsect.installation-steps.en.html#sidebar.bootloader-dual-boot)）.

如果您已经有一个正常工作的Windows系统，甚至可以避免使用CD-ROM；Debian提供了一个Windows程序，可以下载轻量级的Debian安装程序并将其安装到硬盘上。然后，您只需重新启动计算机并选择正常的Windows启动或启动安装程序。您还可以在一个专门的网页上找到该程序，网址相当明确……

→ [https://deb.debian.org/debian/tools/win32-loader/stable/](https://deb.debian.org/debian/tools/win32-loader/stable/)

→ [https://people.debian.org/~rmh/goodbye-microsoft/](https://people.debian.org/~rmh/goodbye-microsoft/)

**_基础知识_ 引导加载程序**

引导加载程序是一个低级程序，负责在BIOS将控制权交给操作系统后引导Linux内核。为了完成这个任务，它必须能够定位磁盘上要引导的Linux内核。在i386和amd64架构中，两个最常用的程序是LILO（较旧的程序）和GRUB（其现代替代品）。Isolinux和Syslinux是常用于从可移动介质引导的替代方案。

每个菜单项隐藏了一个特定的引导命令行，您可以按需要配置该命令行，方法是在确认菜单项并启动之前按**TAB**键。 “帮助”菜单项会显示旧的命令行界面，按**F1**到**F10**键可以显示不同的帮助页面，详细说明在命令行提示符下可以使用的各种选项。除非在非常特定的情况下，否则您很少需要使用此选项。

“专家”模式（可在“高级选项”菜单中访问）详细列出了安装过程中所有可能的选项，并允许在各个步骤之间导航，而不必让它们自动按顺序进行。请注意，这种非常冗长的模式可能会令人困惑，因为它提供了大量的配置选择。

“救援”模式，同样可以在“高级选项”菜单中访问，允许您恢复损坏的系统或修复引导加载程序。在显示安装程序的前几个屏幕后，它将允许您进入所选文件系统的shell提示符，以执行任何必要的操作，或者重新安装引导加载程序。

→ [https://www.debian.org/releases/stable/amd64/ch08s06.en.html](https://www.debian.org/releases/stable/amd64/ch08s06.en.html)

![Boot screen](https://www.debian.org/doc/manuals/debian-handbook/images.en/inst-boot.png)

**图 4.1 引导屏幕**

一旦启动，安装程序会引导您逐步完成整个过程。本节将详细介绍这些步骤。我们将跟随一个从amd64 DVD-ROM（更具体地说，是Bullseye的RC3版本的安装程序）进行的安装过程；_netinst_ 安装以及安装程序的最终发布版本可能会略有不同。我们还将讨论图形模式下的安装，但与“经典”（文本模式）安装的唯一区别在于视觉外观。