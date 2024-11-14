# 使用备用镜像

本章中的 `sources.list` 示例引用了托管在 `deb.debian.org` 上的软件包仓库。这些 URL 会将你重定向到接近你的服务器，这些服务器由内容分发网络（CDN）管理，CDN 的主要作用是将文件的多个副本存储在全球各地，并尽可能快速地将它们提供给用户。与 Debian 合作的 CDN 公司是 Debian 的合作伙伴，免费为 Debian 提供他们的服务。尽管这些服务器并不在 Debian 的直接控制之下，但整个存档通过 GPG 签名进行封装，因此这一点不会成为问题。

→ [https://deb.debian.org/](https://deb.debian.org/)

对 `deb.debian.org` 的性能不满意的挑剔用户可以尝试在官方镜像列表中找到更好的镜像：

→ [https://www.debian.org/mirror/list](https://www.debian.org/mirror/list)

不过，当你不知道哪个镜像最适合你时，这个列表的帮助有限。幸运的是，Debian 维护了形式为 `ftp._country-code_.debian.org`（例如，美国是 `ftp.us.debian.org`，法国是 `ftp.fr.debian.org` 等）的 DNS 记录，涵盖了许多国家，并指向该国境内最好的镜像之一。

作为 `deb.debian.org` 的替代，曾经有 `httpredir.debian.org`。这个服务会根据官方镜像列表（主要使用 GeoIP）识别一个接近你的镜像，并将 APT 的请求重定向到该镜像。然而，由于可靠性问题，这个服务已经被弃用，现在 `httpredir.debian.org` 提供与 `deb.debian.org` 相同的基于 CDN 的服务。