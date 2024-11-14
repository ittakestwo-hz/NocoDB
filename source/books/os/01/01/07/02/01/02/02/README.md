# 软件包卸载

卸载软件包的步骤与安装步骤类似。主要的区别在于会调用软件包的卸载脚本：

1. `dpkg` 调用 `prerm` 脚本，并传递 `remove` 参数。
2. `dpkg` 删除软件包的所有文件，但保留配置文件和维护脚本。
3. `dpkg` 执行 `postrm` 脚本，并将 `remove` 作为参数传递。之后，所有维护脚本（除了 `postrm` 脚本）都会被删除。如果用户没有使用“清除”选项，过程到此为止。
4. 如果需要完全清除软件包（使用 `dpkg --purge` 或 `dpkg -P` 命令），配置文件也会被删除，并且某些临时文件（如 `*.dpkg-tmp`、`*.dpkg-old`、`*.dpkg-new`）也会被删除；然后，`dpkg` 会执行 `postrm` 脚本，并传递 `purge` 参数。

---

**_词汇_ 完全清除**

当 Debian 软件包被卸载时，配置文件会被保留，以便于可能的重新安装。同样，守护进程生成的数据（如 LDAP 服务器目录中的内容，或 SQL 服务器数据库中的内容）通常也会被保留。

如果要删除与软件包相关的所有数据，则需要使用命令 `dpkg -P _package_`、`apt-get remove --purge _package_` 或 `aptitude purge _package_` 来“清除”该软件包。

鉴于此类数据删除的决定性特征，执行清除操作时应该谨慎。

上面详细描述的四个脚本由一个 `config` 脚本补充，该脚本由使用 `debconf` 进行配置的包提供。在安装过程中，这个脚本详细定义了 `debconf` 所询问的问题。回答会被记录在 `debconf` 数据库中，供以后参考。该脚本通常会在逐一安装软件包之前由 `apt` 执行，以便将所有问题集中在安装开始时一次性问用户。安装前后脚本可以根据用户的回答来执行相应操作。

**_工具_ `debconf`**

`debconf` 是为了解决 Debian 中的一个常见问题而创建的。所有无法在没有最小配置的情况下运行的 Debian 软件包，以前都需要通过 `postinst` shell 脚本（以及其他类似的脚本）调用 `echo` 和 `read` 命令来向用户提问。这也意味着在大规模安装或更新过程中，用户必须一直坐在电脑前，随时回答可能出现的各种问题。现在，借助 `debconf` 工具，几乎完全消除了这种手动交互。

`debconf` 具有许多有趣的功能：它要求开发者指定用户交互；它允许本地化所有显示给用户的字符串（所有翻译存储在描述交互的 `templates` 文件中）；它有不同的前端来显示问题给用户（文本模式、图形模式、非交互模式）；它还允许创建一个共享响应的中央数据库，以便多个计算机共享相同的配置……但最重要的是，它现在可以在开始长时间的安装或更新过程之前，一次性向用户提出所有问题。用户可以继续做自己的事情，而系统会自动处理安装过程，无需一直盯着屏幕等待问题。