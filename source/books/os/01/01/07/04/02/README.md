# 软件包删除

使用 `dpkg` 命令并加上 `-r` 或 `--remove` 选项，后跟软件包名称，可以删除该软件包。然而，这种删除并不完全：所有的配置文件、维护脚本、日志文件（系统日志）以及软件包处理的其他用户数据仍然保留。这样，通过卸载程序可以轻松禁用它，并且仍然可以快速重新安装并保留相同的配置。如果要完全删除与软件包相关的所有内容，可以使用 `-P` 或 `--purge` 选项，后跟软件包名称。

**示例 5.4：删除和清除 debian-cd 软件包**

```
# dpkg -r debian-cd
(Reading database ... 228705 files and directories currently installed.)
Removing debian-cd (3.1.35) ...
# dpkg -P debian-cd
(Reading database ... 228049 files and directories currently installed.)
Purging configuration files for debian-cd (3.1.35) ...
```