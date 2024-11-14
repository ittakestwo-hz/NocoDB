# 配置时钟

如果网络可用，系统的内部时钟会通过 NTP 服务器进行一次性更新。这样，日志的时间戳在首次启动时就会是正确的。为了确保时间随着时间的推移持续准确，需要在初始安装后设置 NTP 守护进程（请参见[第 8.9.2 节，“时间同步”](https://www.debian.org/doc/manuals/debian-handbook/sect.installation-steps.en.htmlsect.config-misc.en.html#sect.time-synchronization)）。