# 多架构相关的变化

为了使多架构真正有用并可用，库文件需要重新打包并移动到特定架构的目录中，这样就可以并行安装多个副本（针对不同架构）。这些更新后的软件包包含“`Multi-Arch: same`”头字段，告诉软件包管理系统该软件包的不同架构可以安全地共同安装（并且这些软件包只能满足相同架构软件包的依赖关系）。自从 Debian 7 Wheezy 引入多架构以来，最重要的库文件已经完成了转换，但仍有许多库文件可能永远不会转换，除非有人专门请求（例如通过提交 bug 报告）。

```
$ dpkg -s gcc-9-base
dpkg-query: error: --status needs a valid package name but 'gcc-9-base' is not: ambiguous package name 'gcc-9-base' with more than one installed instance

Use --help for help about querying packages.
$ dpkg -s gcc-9-base:amd64 gcc-9-base:armhf | grep ^Multi
Multi-Arch: same
Multi-Arch: same
$ dpkg -L libgcc-s1:amd64 |grep .so
/lib/x86_64-linux-gnu/libgcc_s.so.1
$ dpkg -S /usr/share/doc/gcc-9-base/copyright
gcc-9-base:amd64, gcc-9-base:armhf: /usr/share/doc/gcc-9-base/copyright
```

值得注意的是，带有“`Multi-Arch: same`”标签的软件包必须通过架构标识来限定其名称，以确保唯一可识别。它们还可以与其他相同软件包的实例共享文件；`dpkg` 确保共享时所有软件包的文件字节完全一致。最后但同样重要的是，所有实例的软件包必须具有相同的版本，因此它们必须一起升级。

多架构支持还带来了一些有趣的挑战，尤其是在依赖关系的处理方式上。满足依赖关系要求要么是一个标记为“`Multi-Arch: foreign`”的软件包，要么是一个其架构与声明该依赖关系的软件包架构匹配的软件包（在这个依赖解析过程中，架构无关的软件包被假定与主机架构相同）。依赖关系还可以通过使用 `_package_:any` 语法进行放宽，以允许任何架构的软件包来满足该依赖，但外部架构的软件包只有在标记为“`Multi-Arch: allowed`”时，才能满足这种依赖。