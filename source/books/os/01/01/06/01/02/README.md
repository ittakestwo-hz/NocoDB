# 从 USB 闪存启动

由于大多数计算机都能够从 USB 设备启动，您也可以通过 USB 闪存驱动器安装 Debian（这实际上就是一个小型的闪存磁盘）。

安装手册解释了如何创建一个包含 `debian-installer` 的 USB 闪存驱动器。这个过程非常简单，因为 i386 和 amd64 架构的 ISO 镜像是混合镜像，可以从 CD-ROM 或 USB 闪存驱动器启动。

您首先需要确定 USB 闪存驱动器的设备名称（例如：`/dev/sdb`）；最简单的方法是使用 `dmesg` 命令查看内核输出的消息。然后，您需要使用以下命令将之前下载的 ISO 镜像（例如，`debian-11.0.0-amd64-netinst.iso`）复制到 USB 驱动器上：  
```
cat debian-11.0.0-amd64-netinst.iso >/dev/sdb; sync
```  
此命令需要管理员权限，因为它直接访问 USB 驱动器并会完全清除其内容。

更详细的说明可以在安装手册中找到。手册中还描述了一种准备 USB 闪存驱动器的替代方法，这种方法更复杂，但可以让您自定义安装程序的默认选项（例如内核命令行中的选项）。

→ [https://www.debian.org/releases/stable/amd64/ch04s03](https://www.debian.org/releases/stable/amd64/ch04s03)