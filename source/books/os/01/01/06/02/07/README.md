# 检测网络硬件

这个自动步骤会尝试识别网络卡并加载相应的模块。如果自动检测失败，您可以手动选择要加载的模块。如果没有任何模块起作用，还可以从可移动设备加载特定模块。这个最后的解决方案通常只有在适当的驱动程序没有包含在标准 Linux 内核中，但可以从其他地方获取时才需要，例如从制造商的网站或固件归档/包中获取。

→ [https://www.debian.org/devel/debian-installer/#firmware_nonfree](https://www.debian.org/devel/debian-installer/#firmware_nonfree)

对于 _netinst_ 安装，必须确保此步骤成功，因为 Debian 软件包需要从网络加载。