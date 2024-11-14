# 测试版/不稳定版用户的仓库

以下是一个运行 Debian 测试版（Testing）或不稳定版（Unstable）系统的标准 `sources.list` 文件：

**示例 6.3. Debian 测试版/不稳定版用户的 `/etc/apt/sources.list` 文件**

```
# 不稳定版
deb https://deb.debian.org/debian unstable main contrib non-free
deb-src https://deb.debian.org/debian unstable main contrib non-free

# 测试版
deb https://deb.debian.org/debian testing main contrib non-free
deb-src https://deb.debian.org/debian testing main contrib non-free

# 测试版安全更新
deb http://security.debian.org/ testing-security main contrib non-free
deb-src http://security.debian.org/ testing-security main contrib non-free

# 稳定版
deb https://deb.debian.org/debian stable main contrib non-free
deb-src https://deb.debian.org/debian stable main contrib non-free

# 稳定版安全更新
deb http://security.debian.org/ stable-security main contrib non-free
deb-src http://security.debian.org/ stable-security main contrib non-free
```

**_注意_ 安全仓库布局**

从 Debian 11 Bullseye 开始，提供安全更新的仓库的代号已从 `_codename_/updates` 更名为 `_codename_-security`，以避免与 `_codename_-updates` 混淆（请参阅[第 6.1.2.2 节，“稳定版更新”](https://www.debian.org/doc/manuals/debian-handbook/apt.en.htmlapt.en.html#sect.apt-sources.list.stable.updates)）。

→ [https://www.debian.org/releases/bullseye/amd64/release-notes/ch-information.en.html#security-archive](https://www.debian.org/releases/bullseye/amd64/release-notes/ch-information.en.html#security-archive)

使用此 `sources.list` 文件，APT 将从不稳定版（Unstable）套件安装软件包。如果不希望这样，可以使用 `APT::Default-Release` 设置（参见[第 6.2.3 节，“系统升级”](https://www.debian.org/doc/manuals/debian-handbook/apt.en.htmlsect.apt-get.en.html#sect.apt-upgrade)），指示 APT 从另一个套件（在这种情况下通常是测试版）选择软件包。

尽管一个仓库通常就足够了，但包括所有这些仓库是有好处的。测试版用户会感激当测试版中的某个包存在恼人的 bug 时，可以从不稳定版中挑选一个修复包。另一方面，不稳定版用户如果遇到意外的回归问题，也可以将软件包降级到其（假定已修复的）测试版版本。

包含稳定版的做法较为有争议，但它通常可以提供一些在开发版本中已被删除的包。此外，它还确保你能获得自上次稳定版发布以来未修改的包的最新更新。