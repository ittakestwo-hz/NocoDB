# 稳定版用户的仓库

以下是运行 Debian 稳定版的系统的标准 `sources.list` 文件：

**示例 6.2. Debian 稳定版用户的 `/etc/apt/sources.list` 文件**

```
# 安全更新
deb http://security.debian.org/ bullseye-security main contrib non-free
deb-src http://security.debian.org/ bullseye-security main contrib non-free

## Debian 镜像

# 基本仓库
deb https://deb.debian.org/debian bullseye main contrib non-free
deb-src https://deb.debian.org/debian bullseye main contrib non-free

# 稳定版更新
deb https://deb.debian.org/debian bullseye-updates main contrib non-free
deb-src https://deb.debian.org/debian bullseye-updates main contrib non-free

# 稳定版回溯包
deb https://deb.debian.org/debian bullseye-backports main contrib non-free
deb-src https://deb.debian.org/debian bullseye-backports main contrib non-free
```

该文件列出了与 Debian Bullseye 版本（截至本文撰写时的当前稳定版）相关的所有包源。在上述示例中，我们选择明确使用“bullseye”而不是对应的“stable”别名（`stable`、`stable-updates`、`stable-backports`），因为我们不希望在下一个稳定版发布时，基础发行版被不受控制地更改。

大多数软件包将来自“基本仓库”，该仓库包含所有软件包，但更新频率较低（大约每 2 个月进行一次“点更新”）。其他仓库是部分仓库（它们不包含所有软件包），可以托管更新（具有新版本的软件包），APT 可能会安装这些更新。接下来的章节将解释每个仓库的用途和管理规则。

需要注意的是，当某个软件包在多个仓库中都有提供时，将使用 `sources.list` 文件中列出的第一个仓库。因此，非官方源通常会被添加到文件的末尾。

作为附带说明，本节内容大部分也适用于旧稳定版（Oldstable），因为它只是一个较旧的稳定版，并且与当前稳定版并行维护。