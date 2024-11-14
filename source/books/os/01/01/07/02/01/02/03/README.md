# 校验和、配置文件列表等

除了前面提到的维护脚本和控制数据之外，Debian 包的 `control.tar.gz` 存档中还可能包含其他一些有用的文件。

首先，`md5sums` 文件包含该包所有文件的 MD5 校验和。它的主要优点是可以让 `dpkg --verify`（我们将在[第14.3.4.1节，“使用 `dpkg --verify` 审计包”](https://www.debian.org/doc/manuals/debian-handbook/sect.package-meta-information.en.htmlsect.supervision.en.html#sect.dpkg-verify) 中学习）和 `debsums`（来自同名包；参见[第14.3.4.2节，“审计包：`debsums` 及其局限性”](https://www.debian.org/doc/manuals/debian-handbook/sect.package-meta-information.en.htmlsect.supervision.en.html#sect.debsums)）检查这些文件自安装以来是否被修改。需要注意的是，如果该文件不存在（这可能是某些较旧软件包的情况），`dpkg` 会在安装时动态生成该文件，并像其他控制文件一样将其存储在 `dpkg` 数据库中。

`conffiles` 文件列出了必须作为配置文件处理的软件包文件（另见 `deb-conffiles(5)`）。配置文件可以由管理员修改，而 `dpkg` 会在软件包更新过程中尽量保留这些修改。

实际上，在这种情况下，`dpkg` 会尽可能智能地处理：如果标准配置文件在两个版本之间没有变化，它将什么也不做。然而，如果文件发生了变化，它将尝试更新该文件。有两种可能的情况：要么管理员没有修改该配置文件，`dpkg` 会自动安装新版本；要么文件已被修改，`dpkg` 会询问管理员希望使用哪个版本（是保留修改过的旧版本，还是使用软件包提供的新版本）。为了帮助做出这个决定，`dpkg` 提供了一个“`diff`”显示差异，展示两个版本之间的不同。如果用户选择保留旧版本，新版本将以 `.dpkg-dist` 后缀存储在同一位置。如果用户选择新版本，旧版本将以 `.dpkg-old` 后缀保留。另一种可用的操作是暂时中断 `dpkg`，让用户编辑文件并尝试恢复相关修改（之前通过 `diff` 标识）。

**_进一步阅读_ 强制 `dpkg` 提问配置文件问题**

`--force-confask` 选项要求 `dpkg` 显示配置文件相关的问题，即使在通常不需要提问的情况下也是如此。因此，当重新安装包时，`dpkg` 会重新询问所有由管理员修改或删除的配置文件。这对于重新安装原始配置文件非常方便，尤其是在配置文件已被删除且没有其他副本可用的情况下：普通的重新安装是行不通的，因为 `dpkg` 将删除视为一种合法修改形式，因此不会安装所需的配置文件。

参见侧边栏 [**进一步阅读** 避免配置文件提问](https://www.debian.org/doc/manuals/debian-handbook/sect.package-meta-information.en.htmlsect.package-meta-information.en.html#sidebar.questions-conffiles)，了解如何在 `APT` 中使用这些选项。

**_进一步阅读_ 避免配置文件提问**

`dpkg` 会处理配置文件更新，但在此过程中，通常会中断操作并要求管理员提供输入。对于希望以非交互方式进行更新的人来说，这种情况不太愉快。这就是为什么 `dpkg` 提供了一些选项，使系统可以根据相同的逻辑自动响应：`--force-confold` 会保留文件的旧版本；`--force-confnew` 会使用文件的新版本（即使文件没有被管理员修改，通常这些选择会产生预期的效果）。添加 `--force-confdef` 选项会告诉 `dpkg` 在可能的情况下自己决定（换句话说，当原始配置文件未被触及时），并且只在其他情况下使用 `--force-confnew` 或 `--force-confold`。

这些选项适用于 `dpkg`，并在 `dpkg(1)` 或 `dpkg --force-help` 中有详细解释，但大多数情况下管理员将直接使用 `aptitude` 或 `apt` 程序。因此，了解如何将这些选项传递给 `dpkg` 命令非常重要（它们的命令行接口非常相似）。

```
# apt -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" full-upgrade
```

这些选项也可以直接存储在 `apt` 的配置文件中。为此，只需在 `/etc/apt/apt.conf.d/local` 文件中写入以下内容：

```
Dpkg::Options {
  "--force-confdef";
  "--force-confold";
}
```

在配置文件中包括这些选项意味着它们也会在图形界面（如 `aptitude`）中使用。

`control` 存档中还经常包含其他文件，如 `triggers`、`shlibs` 或 `symbols`。这些文件在 `deb-triggers(5)`、`deb-shlibs(5)` 和 `deb-symbols(5)` 中有详细描述。

触发器（Triggers）被引入以减少在软件包安装过程中重复的事件，比如文件注册或目录/数据库更新任务。软件包可以定义自己的触发器或激活已定义的触发器。更全面的文档可以在 [`/usr/share/doc/dpkg/triggers.txt.gz`](https://git.dpkg.org/cgit/dpkg/dpkg.git/tree/doc/triggers.txt) 中找到。

`shlibs` 系统是声明共享库依赖关系的较旧、更简单的替代方案，而 `symbols` 系统则跟踪库中符号的变化及其引入时间。