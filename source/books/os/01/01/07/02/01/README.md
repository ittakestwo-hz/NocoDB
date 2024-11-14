# 描述：`control` 文件

这个文件使用类似于电子邮件头部的结构（如 [RFC 2822](https://www.debian.org/doc/manuals/debian-handbook/sect.package-meta-information.en.htmlsect.package-meta-information.en.html#sidebar.rfc) 所定义），并在 Debian 政策和手册页 `deb-control(5)` 和 `deb822(5)` 中有详细描述。

→ [https://www.debian.org/doc/debian-policy/ch-controlfields.html](https://www.debian.org/doc/debian-policy/ch-controlfields.html)

例如，`apt` 的 `control` 文件如下所示：

```
$ apt-cache show apt
Package: apt
Version: 2.2.4
Installed-Size: 4337
Maintainer: APT Development Team <deity@lists.debian.org>
Architecture: amd64
Replaces: apt-transport-https (<< 1.5~alpha4~), apt-utils (<< 1.3~exp2~)
Provides: apt-transport-https (= 2.2.4)
Depends: adduser, gpgv | gpgv2 | gpgv1, libapt-pkg6.0 (>= 2.2.4), debian-archive-keyring, libc6 (>= 2.15), libgcc-s1 (>= 3.0), libgnutls30 (>= 3.7.0), libseccomp2 (>= 2.4.2), libstdc++6 (>= 9), libsystemd0
Recommends: ca-certificates
Suggests: apt-doc, aptitude | synaptic | wajig, dpkg-dev (>= 1.17.2), gnupg | gnupg2 | gnupg1, powermgmt-base
Breaks: apt-transport-https (<< 1.5~alpha4~), apt-utils (<< 1.3~exp2~), aptitude (<< 0.8.10)
Description-en: commandline package manager
 This package provides commandline tools for searching and
 managing as well as querying information about packages
 as a low-level access to all features of the libapt-pkg library.
 .
 These include:
  * apt-get for retrieval of packages and information about them
    from authenticated sources and for installation, upgrade and
    removal of packages together with their dependencies
  * apt-cache for querying available information about installed
    as well as installable packages
  * apt-cdrom to use removable media as a source for packages
  * apt-config as an interface to the configuration settings
  * apt-key as an interface to manage authentication keys
Description-md5: 9fb97a88cb7383934ef963352b53b4a7
Tag: admin::package-management, devel::lang:ruby, hardware::storage,
 hardware::storage:cd, implemented-in::c++, implemented-in::perl,
 implemented-in::ruby, interface::commandline, network::client,
 protocol::ftp, protocol::http, protocol::ipv6, role::program,
 scope::application, scope::utility, suite::debian, use::downloading,
 use::organizing, use::playing, use::searching, works-with-format::html,
 works-with::audio, works-with::software:package, works-with::text
Section: admin
Priority: required
Filename: pool/main/a/apt/apt_2.2.4_amd64.deb
Size: 1491328
MD5sum: 24d53e8dd75095640a167f40476c0442
SHA256: 75f07c4965ff0813f26623a1164e162538f5e94defba6961347527ed71bc4f3d
```

让我们仔细看看前面命令列出的某些字段的用途。

**_基础知识回顾_ RFC — 互联网标准**

RFC 是“Request For Comments”（征求意见书）的缩写。RFC 通常是描述将成为互联网标准的技术文档。在这些标准成为正式标准并被冻结之前，它们会提交给公众审阅（因此得名）。IETF（互联网工程任务组）决定这些文档的状态演变（提议标准、草案标准或正式标准）。

RFC 2026 定义了互联网协议标准化的过程。

→ [http://www.faqs.org/rfcs/rfc2026.html](http://www.faqs.org/rfcs/rfc2026.html)