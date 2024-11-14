# 与 macOS 机器的集成

macOS 机器提供并能够使用诸如文件服务器和打印机共享等网络服务。这些服务会在本地网络上发布，使得其他机器能够发现并使用它们，无需手动配置，使用 Bonjour 实现的 Zeroconf 协议套件。Debian 包含另一个实现，叫做 Avahi，提供相同的功能。

反向操作方面，Netatalk 守护进程可以用来为网络上的 macOS 机器提供文件服务器。它实现了 AFP 协议（Apple Filing Protocol，现在称为 AppleShare）以及所需的通知，以便服务器能够被 macOS 客户端自动发现。

较旧的 Mac OS 网络（OS X 之前的版本）使用了一个不同的协议，叫做 AppleTalk。对于使用这种协议的环境，Netatalk 也提供了 AppleTalk 协议（实际上，它最初是作为该协议的重新实现）。它确保文件服务器和打印队列的正常运行，以及时间服务器（时钟同步）。它的路由功能允许与 AppleTalk 网络的互联。