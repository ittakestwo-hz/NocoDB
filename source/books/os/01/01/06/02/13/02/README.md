# 手动分区

手动分区提供了更大的灵活性，允许用户选择每个分区的用途和大小。此外，如果你希望使用软件 RAID，那么这种模式是不可避免的。

**_实践操作_ 缩小 Windows 分区**

为了在现有操作系统（如 Windows 或其他）旁边安装 Debian，你必须确保有一些未被其他系统使用的硬盘空间，以便可以创建用于 Debian 的分区。在大多数情况下，这意味着需要缩小 Windows 分区，并重新利用释放出的空间。

Debian 安装程序在使用手动分区模式时允许进行此操作。你只需选择 Windows 分区，并设置其新大小（对于未加密的 FAT 或 NTFS 分区，这一操作是相同的）。

如果 Windows 使用了 BitLocker 加密的分区，则需要使用 BitLocker 管理工具结合 Windows 磁盘管理工具来调整分区大小。

第一个屏幕会显示可用的磁盘、它们的分区以及任何尚未分配的空闲空间。你可以选择每个显示的项目，按 **Enter** 键后会列出可执行的操作。

你可以通过选择一个磁盘来删除该磁盘上的所有分区。

选择磁盘上的空闲空间后，你可以手动创建一个新分区。你也可以使用引导分区方式来完成这项操作，这对于已有操作系统的磁盘来说是一个有趣的解决方案，但你可能希望按标准方式为 Linux 进行分区。有关引导分区的更多详情，请参阅[第 4.2.13.1 节，“引导分区”](https://www.debian.org/doc/manuals/debian-handbook/sect.installation-steps.en.htmlsect.installation-steps.en.html#sect.install-autopartman-mode)。

![编辑/创建分区](https://www.debian.org/doc/manuals/debian-handbook/sect.installation-steps.en.htmlimages.en/inst-partman-partition.png)

**图 4.11 编辑/创建分区**

**_回归基础_ 挂载点**

挂载点是一个目录树，它将容纳选定分区上的文件系统内容。因此，挂载在 `/home/` 的分区通常用于存储用户数据。

当这个目录被命名为 “`/`” 时，它被称为文件树的 _根_，因此也是将实际托管 Debian 系统的分区的根。

**_回归基础_ 虚拟内存，交换分区**

虚拟内存允许 Linux 内核在缺乏足够内存（RAM）时，通过将一段时间内未使用的 RAM 内容存储到硬盘上的交换分区，从而释放部分内存。它对系统的“挂起”和“休眠”功能也至关重要。

为了模拟额外的内存，Windows 使用一个直接包含在文件系统中的交换文件。而 Linux 则使用一个专门用于此目的的分区，这就是所谓的“交换分区”。不过，Linux 也可以使用交换文件。

在选择分区时，你可以指定如何使用它：

-   格式化并将其包含到文件树中，选择一个挂载点；
-   将其用作交换分区；
-   将其设置为“加密的物理卷”（用于保护某些分区上的数据隐私，详见下文）；
-   将其设置为“LVM 物理卷”（此概念将在本章后续部分详细讨论）；
-   将其用作 RAID 设备（详见本章后续部分）；
-   你也可以选择不使用该分区，从而保持其不变。