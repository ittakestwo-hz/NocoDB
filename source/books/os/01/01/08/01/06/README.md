# Debian 包的缓存代理

当整个网络中的机器配置为使用相同的远程服务器下载相同的更新包时，任何管理员都会知道，设置一个作为网络本地缓存的中间代理是非常有益的（参见侧边栏 [_词汇_ 缓存](https://www.debian.org/doc/manuals/debian-handbook/apt.en.htmlsect.apt-cache.en.html#sidebar.cache)）。

您可以配置 APT 使用一个“标准”代理（有关 APT 配置的详细信息，请参见 [第 6.2.4 节，“配置选项”](https://www.debian.org/doc/manuals/debian-handbook/apt.en.htmlsect.apt-get.en.html#sect.apt-config)，以及代理端的配置，请参见 [第 11.6 节，“HTTP/FTP 代理”](https://www.debian.org/doc/manuals/debian-handbook/apt.en.htmlsect.http-ftp-proxy.en.html)），但 Debian 生态系统提供了更好的解决方案来处理这个问题。本节中介绍的专用软件比普通的代理缓存更智能，因为它们可以依赖 APT 仓库的特定结构（例如，它们知道哪些文件已经过时，因此能够调整文件的缓存时间）。

`apt-cacher` 和 `apt-cacher-ng` 就像普通的代理缓存服务器一样工作。APT 的 `sources.list` 文件保持不变，但 APT 被配置为将它们用作外部请求的代理。

另一方面，`approx` 则充当一个 HTTP 服务器，它“镜像”其顶级 URL 中的任何数量的远程仓库。这些顶级目录与远程仓库的 URL 之间的映射存储在 `/etc/approx/approx.conf` 文件中，如下所示：

```
# <name>   <repository-base-url>
debian     https://deb.debian.org/debian
security   http://security.debian.org/debian-security
```

默认情况下，`approx` 运行在端口 9999 上，通过 systemd 套接字提供服务，用户需要调整其 `sources.list` 文件，以指向本地的 approx 服务器：

```
# 示例 sources.list，指向本地 approx 服务器
deb http://localhost:9999/security bullseye-security main contrib non-free
deb http://localhost:9999/debian   bullseye main contrib non-free
```