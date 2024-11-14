# 与其他软件包管理系统的共存

Debian 包并不是自由软件世界中唯一使用的软件包格式。主要的竞争者是 Red Hat Linux 发行版及其众多衍生版本使用的 RPM 格式。Red Hat 是一个非常流行的商业发行版。因此，第三方提供的软件通常以 RPM 包的形式提供，而不是 Debian 包。

在这种情况下，您应该知道，处理 RPM 包的程序 `rpm` 作为 Debian 包提供，因此可以在 Debian 上使用这种包格式。然而，需要注意的是，最好将这些操作限制为提取包中的信息或验证其完整性。事实上，在 Debian 系统上使用 `rpm` 安装 RPM 包是不合理的，因为 RPM 使用的是独立于本地软件（如 `dpkg`）的数据库。这就是为什么无法确保两个软件包管理系统稳定共存的原因。

另一方面，`alien` 工具可以将 RPM 包转换为 Debian 包，反之亦然。

**_社区倡导采用 `.deb` 格式_**

如果您经常使用 `alien` 程序安装来自某个供应商的 RPM 包，请不要犹豫，写信给他们并友好地表达您对 `.deb` 格式的强烈偏好。请注意，软件包的格式并非一切：一个通过 `alien` 构建的 `.deb` 包，或者为与您使用的 Debian 版本不同的版本（甚至为类似 Ubuntu 的衍生发行版）而准备的包，可能无法提供与专为 Debian Bullseye 开发的软件包相同的质量和集成水平。

```
$ fakeroot alien --to-deb phpMyAdmin-5.1.1-2.fc35.noarch.rpm
[..]
Warning: Skipping conversion of scripts in package phpMyAdmin: postinst
Warning: Use the --scripts parameter to include the scripts.
[..]
phpmyadmin_5.1.1-3_all.deb generated
$ ls -sh phpmyadmin_5.1.1-3_all.deb
  6,0M phpmyadmin_5.1.1-3_all.deb
$ dpkg -c phpmyadmin_5.1.1-3_all.deb
drwxr-xr-x root/root         0 2021-08-09 02:02 ./
drwxr-xr-x root/root         0 2021-08-09 02:02 ./etc/
drwxr-xr-x root/root         0 2021-08-09 02:02 ./etc/httpd/
drwxr-xr-x root/root         0 2021-08-09 02:02 ./etc/httpd/conf.d/
-rw-r--r-- root/root      1181 2021-07-27 09:32 ./etc/httpd/conf.d/phpMyAdmin.conf
drwxr-xr-x root/root         0 2021-08-09 02:02 ./etc/nginx/
drwxr-xr-x root/root         0 2021-08-09 02:02 ./etc/nginx/default.d/
-rw-r--r-- root/root       430 2021-07-27 09:32 ./etc/nginx/default.d/phpMyAdmin.conf
drwxr-x--- root/root         0 2021-08-09 02:02 ./etc/phpMyAdmin/
-rw-r----- root/root      4546 2021-07-27 09:34 ./etc/phpMyAdmin/config.inc.php
drwxr-xr-x root/root         0 2021-08-09 02:02 ./usr/
drwxr-xr-x root/root         0 2021-08-09 02:02 ./usr/share/
drwxr-xr-x root/root         0 2021-08-09 02:02 ./usr/share/doc/
drwxr-xr-x root/root         0 2021-08-09 02:02 ./usr/share/doc/phpMyAdmin/
[..]
$ dpkg -I phpmyadmin_5.1.1-3_all.deb
 new Debian package, version 2.0.
 size 6195324 bytes: control archive=44444 bytes.
     102 bytes,     3 lines      conffiles
     593 bytes,    15 lines      control
  180405 bytes,  1919 lines      md5sums
     448 bytes,    11 lines   *  postinst             #!/bin/sh
 Package: phpmyadmin
 Version: 5.1.1-3
 Architecture: all
 Maintainer: Daniel Leidert <dleidert@debian.org>
 Installed-Size: 40693
 Section: alien
 Priority: extra
 Description: A web interface for MySQL and MariaDB
  phpMyAdmin is a tool written in PHP intended to handle the administration of
  MySQL over the Web. Currently it can create and drop databases,
  create/drop/alter tables, delete/edit/add fields, execute any SQL statement,
  manage keys on fields, manage privileges,export data into various formats and
  is available in 50 languages
  .
  (Converted from a rpm package by alien version 8.95.4.)
```

您会发现这个过程非常简单。然而，您需要知道的是，生成的软件包没有任何依赖关系信息，因为这两种软件包格式中的依赖关系并没有系统化的对应关系。因此，管理员必须手动确保转换后的包能正常工作，这也是为什么尽量避免使用这种方式生成的 Debian 包的原因。幸运的是，Debian 拥有所有发行版中最大的软件下载库，您所需要的软件包很可能已经在其中。

查看 `alien` 命令的手册页，您还会注意到，该程序支持其他软件包格式，特别是 Slackware 发行版使用的格式（它由一个简单的 `tar.gz` 压缩包构成）。

使用 `dpkg` 工具部署的软件的稳定性是 Debian 知名度的重要因素。接下来的章节中将介绍的 APT 工具套件在保留这一优势的同时，减轻了管理员管理软件包状态的负担，这是一个既必要又困难的任务。