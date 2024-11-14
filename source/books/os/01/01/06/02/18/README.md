# 安装 GRUB 启动加载器

启动加载器是由 BIOS 启动的第一个程序。它将 Linux 内核加载到内存中并执行。启动加载器通常提供一个菜单，允许用户选择要加载的内核和/或要启动的操作系统。

**_注意_ 启动加载器与双重启动**

Debian 安装过程中的这一阶段会检测计算机上已经安装的操作系统，并自动在启动菜单中添加相应的条目，但并非所有的安装程序都会这样做。

特别是，如果你在此之后安装（或重新安装）Windows，启动加载器将被擦除。Debian 仍然存在于硬盘上，但将无法通过启动菜单访问（Windows 10 除外，此时可以通过 Windows 恢复控制台访问）。你将需要在 **`rescue`** 模式下启动 Debian 安装系统，以设置一个不那么排他的启动加载器。此操作在安装手册中有详细描述。

→ [https://www.debian.org/releases/stable/amd64/ch08s06](https://www.debian.org/releases/stable/amd64/ch08s06)

默认情况下，GRUB 提供的菜单包含所有已安装的 Linux 内核，以及任何已检测到的操作系统。这就是为什么你应该接受将 GRUB 安装到主引导记录（MBR）中的提议。由于保留旧的内核版本可以确保在最近安装的内核出现故障或与硬件不兼容时仍然可以启动系统，因此通常保留几个旧版本的内核是有意义的。

GRUB 是 Debian 默认安装的启动加载器，凭借其技术优势，它能够支持大多数文件系统，因此在每次安装新内核时无需更新，因为 GRUB 会在启动时读取其配置并找到新内核的确切位置。GRUB 1（现在称为“Grub Legacy”）无法处理所有 LVM 和软件 RAID 的组合；而默认安装的 GRUB 2 更加完整。尽管在某些情况下安装 LILO（另一个启动加载器）可能更为合适，但 Debian 安装程序现在不再支持安装 LILO。

值得注意的是，GRUB 不是单一的启动加载器，而更像是一个适用于不同情况的启动加载器集合。由 GRUB 源包构建的众多二进制包也反映了这一点：`grub-efi-amd64` 用于 64 位 PC 的 UEFI 启动，`grub-efi-ia32` 用于 32 位 PC 的 UEFI 启动，`grub-pc` 用于 PC 的 BIOS 启动，`grub-uboot` 用于 ARM 计算机，等等。

有关 GRUB 配置的更多信息，请参阅[第 8.8.2 节，“GRUB 2 配置”](https://www.debian.org/doc/manuals/debian-handbook/sect.installation-steps.en.htmlsect.config-bootloader.en.html#sect.config-grub)。

**_文化提示_ 安全启动与 shim 启动加载器**

安全启动（Secure Boot）是一项技术，确保你运行的只有操作系统厂商验证过的软件。为了实现这一目标，启动序列中的每个元素都会验证它将执行的下一个软件组件。在最底层，UEFI 固件嵌入了 Microsoft 提供的加密密钥，用于检查启动加载器的签名，以确保其可以安全执行。由于获得微软签名的二进制文件是一个漫长的过程，Debian 决定不直接签署 GRUB。相反，Debian 使用一个中介启动加载器，称为 shim，它几乎不需要更改，其唯一的作用是检查 Debian 提供的 GRUB 签名并执行 GRUB。要在启用安全启动的机器上运行 Debian，必须安装 `shim-signed` 软件包。

在 GRUB 之后，GRUB 会对内核进行类似的签名检查，接着内核也可能检查加载的模块的签名。内核还可能禁止某些操作，以防止破坏系统的完整性。

Debian 10（Buster）是首个支持安全启动的版本。在此之前，你必须在 BIOS 或 UEFI 提供的系统设置屏幕中禁用此功能。