# 语法

`/etc/apt/sources.list` 文件中的每一行都代表一个包源（仓库），并由至少三个部分组成，部分之间用空格分隔。有关文件格式和接受的条目组成的完整描述，请参见 `sources.list(5)`。

**示例 6.1. `/etc/apt/sources.list` 中的示例条目格式**

```
deb url distribution component1 component2 component3 [..] componentX
deb-src url distribution component1 component2 component3 [..] componentX
```

第一字段表示源类型：

- `deb`：二进制包源（仓库）
- `deb-src`：源包源（仓库）

第二字段给出源的基本 URL。结合 `Packages.xz` 文件中列出的文件名，它必须提供一个完整且有效的 URL。这个 URL 可以是一个 Debian 镜像，或者是由第三方设置的任何其他软件包存档。URL 可以以 `file://` 开头，表示本地源，安装在系统的文件层次结构中；可以以 `http://` 或 `https://` 开头，表示通过 Web 服务器访问的源；也可以以 `ftp://` 或 `ftps://` 开头，表示通过 FTP 服务器提供的源。URL 还可以以 `cdrom:` 开头，表示基于 CD-ROM/DVD/Blu-ray 光盘的安装，尽管这种方式不太常见，因为基于网络的安装方法更加普遍。还支持像 `ssh://` 或 `tor+http(s)://` 这样的方式，这些方法要么在 `sources.list(5)` 中描述，要么在相应的 `apt-transport-_method_` 包的文档中有说明。

最后一个字段的语法取决于仓库的结构。在最简单的情况下，您可以仅指定所需源的子目录（必须以斜杠结尾）。这通常是一个简单的“`./`”，表示没有子目录。软件包就直接位于指定的 URL 中。但在最常见的情况下，仓库的结构类似于 Debian 镜像，包含多个发行版，每个发行版有多个组件。在这种情况下，您需要通过其“代号”来命名所选的发行版——请参见边栏 [_社区_ Bruce Perens，一个有争议的领袖](https://www.debian.org/doc/manuals/debian-handbook/apt.en.htmlsect.foundation-documents.en.html#sidebar.bruce-perens) —— 或通过相应的“套件”（`oldoldstable`、`oldstable`、`stable`、`testing`、`unstable`）来命名发行版，然后启用相关组件。典型的 Debian 镜像提供 `main`、`contrib` 和 `non-free` 组件。

**_词汇_ `main`、`contrib` 和 `non-free` 存档**

Debian 使用三个组件来根据每个作品的许可证来区分软件包。`main` 包含所有完全符合 [Debian 自由软件指南](https://www.debian.org/doc/manuals/debian-handbook/apt.en.htmlsect.foundation-documents.en.html#sect.dfsg) 的软件包。

`non-free` 组件不同，因为它包含不完全符合这些原则的软件，但仍然可以不受限制地分发。这个存档并不是 Debian 的官方部分，它为需要这些程序的用户提供服务，尤其是那些现在还需要硬件固件的用户。然而，Debian 总是推荐优先使用自由软件。这个组件的存在对 Richard M. Stallman 来说是一个相当大的问题，也让自由软件基金会无法向用户推荐 Debian。

`contrib`（贡献）是一个开源软件集合，无法在没有一些非自由元素的情况下运行——这些元素可以是来自 `non-free` 部分的软件，或者是如游戏 ROM、游戏机 BIOS 等非自由文件——或者一些在 Debian `main` 存档中完全没有的元素。`contrib` 组件还包括需要专有元素编译的自由软件。最初，OpenOffice.org 办公软件套件就需要一个专有的 Java 环境。

**_提示_ `/etc/apt/sources.list.d/` 中的文件**

如果引用了许多包源，将它们分割成多个文件可能会很有用。每个部分会存储在 `/etc/apt/sources.list.d/_filename_.list` 中（请参见边栏 [_基础知识_ 以 `.d` 结尾的目录](https://www.debian.org/doc/manuals/debian-handbook/apt.en.htmlsect.apt-get.en.html#sidebar.directory.d)）。

`cdrom` 条目描述了您拥有的 CD/DVD-ROM。与其他条目不同，CD-ROM 并不总是可用的，因为它必须插入驱动器并且一次只能读取一张光盘。由于这些原因，这些源以略有不同的方式进行管理，并需要使用 `apt-cdrom` 程序添加，通常使用 `add` 参数。然后，`apt-cdrom` 会要求将光盘插入驱动器，并浏览其内容查找 `Packages` 文件。它会使用这些文件来更新可用软件包的数据库（这个操作通常由 `apt update` 命令完成）。从那时起，如果需要其中一个软件包，APT 就会要求插入光盘。