# 网络和进程

`nmap` 工具（与其同名的包）可以快速识别网络中主机托管的 Internet 服务，甚至无需登录该主机。只需在同一网络中的另一台机器上运行以下命令：

```
$ nmap mirwiz
Starting Nmap 7.80 ( https://nmap.org ) at 2021-04-29 14:41 CEST
Nmap scan report for mirwiz (192.168.1.104)
Host is up (0.00062s latency).
Not shown: 992 closed ports
PORT     STATE SERVICE
22/tcp   open  ssh
25/tcp   open  smtp
80/tcp   open  http
111/tcp  open  rpcbind
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
5666/tcp open  nrpe
9999/tcp open  abyss

Nmap done: 1 IP address (1 host up) scanned in 0.06 seconds
```

> **_替代方案_ 使用 `ss` 查找可用服务列表**
> 
> 在 Linux 机器上，`ss -anptu` 命令将显示活动或待处理的 TCP 会话列表，以及正在监听的 UDP 端口。这有助于识别网络上提供的服务。

> **_深入了解_ IPv6**
> 
> 一些网络命令可能同时支持 IPv4（通常是默认协议）或 IPv6，包括 `nmap` 和 `ss` 命令，以及 `route` 或 `ip` 等其他命令。启用 IPv6 的行为通常通过命令行选项 _`-6`_ 实现。

如果服务器是提供 shell 帐户的 Unix 机器，了解进程是否在没有其所有者的情况下在后台执行也非常重要。`ps auxw` 命令将显示所有进程及其所属的用户身份。通过将这些信息与 `who` 或 `w` 命令的输出进行对比（后者列出了已登录的用户），可以识别出潜在的未授权或未声明的后台服务器或程序。查看 `crontab`（列出用户计划的自动任务的表格）通常也能提供关于服务器功能的有趣信息（关于 `cron` 的完整解释，请参见 [第 9.7 节, “使用 `cron` 和 `atd` 安排任务”](https://www.debian.org/doc/manuals/debian-handbook/sect.how-to-migrate.en.htmlsect.task-scheduling-cron-atd.en.html)）。

无论如何，备份服务器数据是至关重要的：这可以在迁移后，当用户报告由于迁移而导致的特定问题时，帮助恢复数据。