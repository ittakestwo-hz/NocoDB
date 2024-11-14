# 稳定版回溯包

`stable-backports` 仓库托管着“软件包回溯”（Package Backports）。这个术语指的是一些较新的软件包，它们被重新编译以适应较旧的发行版，通常是为了稳定版（Stable）。

当发行版稍微过时时，许多软件项目发布了新版本，这些版本未被集成到当前的稳定版中，因为稳定版只会修改以解决最关键的问题，例如安全问题。由于测试版（Testing）和不稳定版（Unstable）可能更具风险，软件包维护者有时会自愿提供一些较新软件应用程序的回溯包，用于稳定版。这对用户和系统管理员有利，因为它可以将潜在的不稳定性限制在少数几个特定的软件包中。[https://backports.debian.org](https://backports.debian.org) 页面提供了更多信息。

`stable-backports` 中的回溯包只会从测试版中的软件包创建。这确保了所有已安装的回溯包将在下一个稳定版发布时能够升级到相应的稳定版版本。

尽管这个仓库提供了较新版本的软件包，但 `APT` 不会自动安装这些包，除非你明确指示安装（或者之前已经安装过该回溯包的旧版本）：

```
$ sudo apt-get install package/bullseye-backports
$ sudo apt-get install -t bullseye-backports package

```