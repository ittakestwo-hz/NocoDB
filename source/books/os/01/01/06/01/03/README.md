# 通过网络启动安装

许多 BIOS 都允许通过网络启动计算机，方法是下载一个内核和一个最小的文件系统镜像。如果计算机没有 CD-ROM 驱动器，或者 BIOS 无法从该介质启动，这种方法（有时称为 PXE 或 TFTP 启动）可以派上大用场。

这种安装方法分为两个步骤。首先，在启动计算机时，BIOS（或网络卡）会发出一个 BOOTP/DHCP 请求来自动获取 IP 地址。当 BOOTP 或 DHCP 服务器返回响应时，它会包括一个文件名以及网络设置。网络配置完成后，客户端计算机会发出一个 TFTP（简易文件传输协议）请求，下载一个事先指定的文件。一旦文件下载完成，它将像引导加载程序一样被执行，从而启动 Debian 安装程序，仿佛它是从硬盘、CD-ROM 或 USB 闪存驱动器运行的一样。

有关此方法的所有详细信息，可以参考安装手册中的“准备 TFTP 网络启动文件”部分。

→ [https://www.debian.org/releases/stable/amd64/ch05s01#boot-tftp-x86](https://www.debian.org/releases/stable/amd64/ch05s01#boot-tftp-x86)

→ [https://www.debian.org/releases/stable/amd64/ch04s05](https://www.debian.org/releases/stable/amd64/ch04s05)