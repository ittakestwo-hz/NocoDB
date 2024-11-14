# 启用多架构支持

`dpkg` 的多架构支持允许用户定义可以安装在当前系统上的“外部架构”。这可以通过 `dpkg --add-architecture` 来实现，如下例所示。对应的 `dpkg --remove-architecture` 用于删除对某个外部架构的支持，但只有在该架构下没有剩余的软件包时才能使用。

```
# dpkg --print-architecture
amd64
# dpkg --print-foreign-architectures
# dpkg -i gcc-9-base_9.3.0-22_armhf.deb
dpkg: error processing archive gcc-9-base_9.3.0-22_armhf.deb (--install):
 package architecture (armhf) does not match system (amd64)
Errors were encountered while processing:
 gcc-9-base_9.3.0-22_armhf.deb
# dpkg --add-architecture armhf
# dpkg --add-architecture armel
# dpkg --print-foreign-architectures
armhf
armel
# dpkg -i gcc-9-base_9.3.0-22_armhf.deb
(Reading database ... 456367 files and directories currently installed.)
Preparing to unpack gcc-9-base_9.3.0-22_armhf.deb ...
Unpacking gcc-9-base:armhf (9.3.0-22) ...
Setting up gcc-9-base:armhf (9.3.0-22) ...
# dpkg --remove-architecture armhf
dpkg: error: cannot remove architecture 'armhf' currently in use by the database
# dpkg --remove-architecture armel
# dpkg --print-foreign-architectures
armhf
```

**_注意_ APT 的多架构支持**

APT 会自动检测 `dpkg` 是否已配置为支持外部架构，并在更新过程中开始下载相应的 `Packages` 文件。

然后，可以使用 `apt install _package_:_architecture_` 来安装外部架构的软件包。

**_实践中_ 在 amd64 系统上使用专有的 i386 二进制文件**

多架构有多种使用场景，但最常见的包括：在 64 位系统（amd64）上执行（有时是专有的）32 位二进制文件（i386），以及为与主机架构不同的平台或架构交叉编译软件的可能性。