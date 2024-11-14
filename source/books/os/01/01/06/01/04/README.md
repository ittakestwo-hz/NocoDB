# 其他安装方法

当需要为大量计算机部署定制化的安装时，我们通常会选择自动化安装而非手动安装。根据具体情况和安装的复杂性，可以使用 FAI（完全自动化安装器，详见[第 12.3.1 节，“完全自动化安装器（FAI）”](https://www.debian.org/doc/manuals/debian-handbook/installation.en.htmlsect.automated-installation.en.html#sect.fai)），甚至可以使用带预种（preseeding）的定制安装 DVD（见[第 12.3.2 节，“预种 Debian 安装器”](https://www.debian.org/doc/manuals/debian-handbook/installation.en.htmlsect.automated-installation.en.html#sect.d-i-preseeding)）。

还需要注意的是，安装程序可以加载并运行 SSH 服务器，因此提供了通过 SSH 会话远程安装 Debian 的能力。发行说明中还描述了如何使用 _grub_ 从现有系统运行安装程序，并完全替换现有系统。