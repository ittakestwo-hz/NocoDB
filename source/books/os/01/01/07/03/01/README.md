# 格式

一个源代码包通常由三个文件组成：`.dsc`、`.orig.tar.gz` 和 `.debian.tar.xz`（或 `.diff.gz`）。这些文件用于从程序的源代码文件（用编程语言编写）创建二进制包（即上面提到的 `.deb` 文件）。

`.dsc`（Debian 源控制）文件是一个简短的文本文件，包含一个 RFC 2822 头部（类似于我们在[第 5.2.1 节，"描述：`control` 文件"](https://www.debian.org/doc/manuals/debian-handbook/sect.source-package-structure.en.htmlsect.package-meta-information.en.html#sect.control)中学到的 `control` 文件），它描述了源代码包并指示了哪些其他文件是其一部分。该文件由维护者签名，保证其真实性。有关更多信息，请参见[第 6.6 节，“检查软件包的真实性”](https://www.debian.org/doc/manuals/debian-handbook/sect.source-package-structure.en.htmlsect.package-authentication.en.html)。

**示例 5.1：`.dsc` 文件**

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA512

Format: 3.0 (quilt)
Source: zim
Binary: zim
Architecture: all
Version: 0.73.5-1
Maintainer: Zim Package Maintainers <zim@packages.debian.org>
Uploaders: Raphaël Hertzog <hertzog@debian.org>
Homepage: https://zim-wiki.org
Standards-Version: 4.5.1
Vcs-Browser: https://salsa.debian.org/debian/zim
Vcs-Git: https://salsa.debian.org/debian/zim.git
Build-Depends: debhelper-compat (= 13), python3, python3-gi, python3-xdg, gir1.2-gtk-3.0, dh-python
Package-List:
 zim deb x11 optional arch=all
Checksums-Sha1:
 80d43d5c1c6a47c695079eb02bc8ad36b84d6e57 2159901 zim_0.73.5.orig.tar.gz
 b1cd86dc4819a80126efbf6ee6eba17a33f451d3 10124 zim_0.73.5-1.debian.tar.xz
Checksums-Sha256:
 a36f15d92c3994c0d55b07f83253b3d8b826beb3714865edbabc14f1cc91d63a 2159901 zim_0.73.5.orig.tar.gz
 6c2db642d9ac1c2440ed08e0cd584006045b342b255f37ffe42bd5459fb5cb76 10124 zim_0.73.5-1.debian.tar.xz
Files:
 fa76ceb8ac7d7354fb0e2bc5607e9faa 2159901 zim_0.73.5.orig.tar.gz
 a0c824d979efb196cde0176d3cb9c719 10124 zim_0.73.5-1.debian.tar.xz

-----BEGIN PGP SIGNATURE-----
Comment: Signed by Raphael Hertzog

iQEzBAEBCgAdFiEE1823g1EQnhJ1LsbSA4gdq+vCmrkFAmAa3ooACgkQA4gdq+vC
mrkq1gf/cs7irmbCSDrADVqsqYBrFJ1FyprE3jiHLNs0OQLryhFj9tzDuilX35VE
HkCfxSaKkzgvQLYtpuw1VBfhOdngTdHO39U6eljkaScnfLWU8Z5n/q+YeedxItoY
X3TtzMexFmb4WJqlylfjbXeqbLdYvsILQ3NVnE48AzkaBQlCC2d9bqecZhWiKfzq
gNxIDVDDhqCXMPe7QCErCBiFPUVpGN7b+6QWN0RxOTLZdj/slRD73rT++VmY+xN1
L8BSLcjXie+ES11MhQNYaLpCv2vqImlZaxkFWvsKBo9ndRFSbE3/RNK479a4KGve
KrdpGUJXy9uLPuAMyn5WphwXJ7OZXQ==
=YFDk
-----END PGP SIGNATURE-----
```

注意，源代码包也有与二进制包完全不同的依赖关系（`Build-Depends`），这些依赖关系指定了构建软件包所需的工具，以及构建二进制包所需的其他组件。

**_注意_ 独立的命名空间**

需要特别注意的是，源代码包和它生成的二进制包之间的名称并没有强制要求必须对应。这个概念很好理解，因为每个源代码包可能生成多个二进制包。这就是为什么 `.dsc` 文件中有 `Source` 和 `Binary` 字段，用来明确指出源代码包的名称，并列出它生成的二进制包的列表。

**_文化_ 为什么要分成多个包**

源代码包（针对某个特定软件）经常会生成多个二进制包。这种拆分的理由是，软件的不同部分可以在不同的上下文中使用。例如，考虑一个共享库，它可能是为了让某个应用程序工作而安装（例如，`libc6`），或者它也可以安装为开发新程序的工具（此时，`libc6-dev` 就是正确的包）。我们在客户端/服务器服务中也能看到类似的逻辑，我们希望将服务器部分安装到一台机器上，将客户端部分安装到其他机器上（例如 `openssh-server` 和 `openssh-client` 就是这种情况）。

同样，文档也通常会提供为一个单独的包：用户可以独立安装它，随时选择删除它以节省磁盘空间。此外，这样也能节省 Debian 镜像站的磁盘空间，因为文档包会在所有架构之间共享，而不是在每个架构的软件包中重复包含文档。

**_视角_ 不同的源代码包格式**

最初，只有一种源代码包格式，即 `1.0` 格式，它将 `.orig.tar.gz` 存档与 `.diff.gz` “debian化”补丁相关联（还有一种变体，它由一个单独的 `.tar.gz` 存档组成，如果没有 `.orig.tar.gz` 可用时，会自动使用这种格式）。

自 Debian 6 Squeeze 以来，Debian 开发者可以选择使用新的格式，这些格式解决了历史格式的许多问题。格式 `3.0 (quilt)` 可以将多个上游归档文件合并到同一个源代码包中：除了常见的 `.orig.tar.gz`，还可以包括补充的 `.orig-_component_.tar.gz` 文件。这对于那些由多个上游组件分发的软件，但又希望只有一个源代码包的情况很有用。还可以使用 `xz` 而非 `gzip` 来压缩这些归档文件，从而节省磁盘空间和网络资源。最后，单一的补丁文件 `.diff.gz` 被 `.debian.tar.xz` 归档所替代，后者包含了构建指令和包维护者提供的上游补丁集合。这些补丁以与 `quilt` 兼容的格式记录，`quilt` 是一个有助于管理一系列补丁的工具。

`.orig.tar.gz` 文件是一个包含原开发者提供的源代码的归档文件。Debian 软件包维护者被要求不要修改此归档文件，以便能够轻松地检查文件的来源和完整性（通过简单的校验和比较）并尊重一些作者的意愿。

`.debian.tar.xz` 文件包含了 Debian 维护者所做的所有修改，特别是添加了一个 `debian` 目录，该目录包含了构建一个或多个 Debian 二进制包所需的执行指令。

**_工具_ 解压源代码包**

如果你有一个源代码包，可以使用 `dpkg-source` 命令（来自 `dpkg-dev` 包）来解压它：

```
$ dpkg-source -x zim_0.73.5-1.dsc
dpkg-source: info: extracting zim in zim-0.73.5
dpkg-source: info: unpacking zim_0.73.5.orig.tar.gz
dpkg-source: info: unpacking zim_0.73.5-1.debian.tar.xz
```

你也可以使用 `apt` 命令来下载并立即解压一个源代码包。不过，这要求 `/etc/apt/sources.list` 文件中包含适当的 `deb-src` 行（更多详细信息，请参见[第 6.1 节，“填写 `sources.list` 文件”](https://www.debian.org/doc/manuals/debian-handbook/sect.source-package-structure.en.htmlapt.en.html#sect.apt-sources.list)）。这些行用于列出源代码包的“源”（即托管源代码包的一组服务器）。

```
$ apt source package

Reading package lists... Done
NOTICE: 'zim' packaging is maintained in the 'Git' version control system at:
https://salsa.debian.org/debian/zim.git
Please use:
git clone https://salsa.debian.org/debian/zim.git
to retrieve the latest (possibly unreleased) updates to the package.
Need to get 2,172 kB of source archives.
Get:1 https://deb.debian.org/debian bullseye/main zim 0.73.5-1 (dsc) [1,580 B]
Get:2 https://deb.debian.org/debian bullseye/main zim 0.73.5-1 (tar) [2,160 kB]
Get:3 https://deb.debian.org/debian bullseye/main zim 0.73.5-1 (diff) [10.1 kB]
Fetched 2,172 kB in 0s (7,176 kB/s)
dpkg-source: info: extracting zim in zim-0.73.5
dpkg-source: info: unpacking zim_0.73.5.orig.tar.gz
dpkg-source: info: unpacking zim_0.73.5-1.debian.tar.xz
```