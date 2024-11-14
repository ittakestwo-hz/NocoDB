# 安装与升级

在初次安装以及每次升级一个软件包时，`dpkg` 会调用所谓的 _维护脚本_，例如 `prerm` 或 `preinst` 脚本。这些脚本可以在软件包生命周期的不同阶段执行额外的操作。脚本名称前缀为 `new-` 的是来自正在安装或升级到的新版本的脚本；前缀为 `old-` 的是来自正在升级的旧版本的脚本。

在每次调用时，`dpkg` 会将某些参数传递给每个脚本，例如 `upgrade _new-version_`。被调用的脚本可以处理这些参数并执行特定操作，或者如果在该步骤不需要做任何操作，可以忽略这些参数并返回退出码 `0`。实际上，许多软件包在生命周期的每个步骤中都不需要执行操作。因此，一个典型的配置脚本会检查特定的参数，并忽略其他所有参数，隐式地返回退出码 `0`。

以下是在安装（或更新）过程中发生的情况，`_old-version_`、`_new-version_` 和 `_last-version-configured_` 是软件包实际（旧版本和新版本）版本号的占位符：

1. **更新时**，`dpkg` 调用 `old-prerm` 脚本，并传递 `upgrade _new-version_` 作为参数。
2. 更新时，`dpkg` 接着执行 `new-preinst` 脚本，并传递 `upgrade _old-version_` 作为参数；如果是初次安装，它会执行 `new-preinst` 脚本并传递 `install` 作为参数。如果软件包已经安装并已被移除（但未被完全清除，因此保留了配置文件），它还可能将旧版本作为最后一个参数传递。
3. 然后，新的软件包文件会被解包。如果某个文件已存在，它将被替换，但会暂时保留备份副本。
4. 对于更新，`dpkg` 执行 `old-postrm` 脚本，并传递 `upgrade _new-version_` 作为参数。
5. `dpkg` 更新所有内部数据（文件列表、配置脚本等），并移除已替换文件的备份。此时为不可逆的阶段：`dpkg` 不再能访问恢复到先前状态所需的所有元素。
6. `dpkg` 将更新配置文件，如果它无法自动管理此任务，则会请求用户决定。此过程的详细信息可以参考 [第 5.2.3 节，“校验和、配置文件列表等”](https://www.debian.org/doc/manuals/debian-handbook/sect.package-meta-information.en.htmlsect.package-meta-information.en.html#sect.conffiles)。
7. 最后，`dpkg` 会通过执行 `new-postinst` 脚本并传递 `configure _last-version-configured_` 作为参数来配置该软件包。