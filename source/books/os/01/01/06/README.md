# 第 4 章：安装

要使用 Debian，您需要将其安装到一台计算机上；这个任务由 _debian-installer_ 程序来完成。一次正确的安装涉及许多操作。本章将按时间顺序回顾这些步骤。

**_回归基础_ 附录中的补习课程**

当您熟悉计算机的工作原理时，安装过程总是更简单。如果您不熟悉，请在阅读本章之前快速浏览一下 [附录 B, _简短补习课程_](https://www.debian.org/doc/manuals/debian-handbook/installation.en.htmlshort-remedial-course.en.html)。

Bullseye 的安装程序基于 `debian-installer`。它的模块化设计使其能够适应不同的场景，并能够随着变化而演进。尽管需要支持大量架构，但该安装程序对初学者非常友好，因为它在每个阶段都会为用户提供帮助。自动硬件检测、引导分区和图形用户界面解决了 Debian 初期新手所面临的绝大多数问题。

安装需要 256 MB 的内存（RAM）和至少 2 GB 的硬盘空间。所有 Falcot 计算机都符合这些标准。然而，需注意，这些数据适用于安装一个非常精简的系统，没有图形桌面。对于一个基本的办公室桌面工作站，建议至少 2 GB 的内存和 10 GB 的硬盘空间。

**_警告_ 从 Buster 升级**

如果您的计算机上已经安装了 Debian Bullseye，本章就不适合您了！与其他发行版不同，Debian 允许您在不重新安装系统的情况下，从一个版本升级到下一个版本。重新安装不仅是多余的，甚至可能是危险的，因为它可能会删除已经安装的程序。

升级过程将在 [第 6.7 节，“从一个稳定版本升级到下一个稳定版本”](https://www.debian.org/doc/manuals/debian-handbook/installation.en.htmlsect.dist-upgrade.en.html) 中描述。

直接从更旧的 Debian 系统进行升级是不被支持的。在这种情况下，您需要逐步更新到紧跟您当前 Debian 版本的稳定版本，然后依此类推。以往版本的本书将帮助您处理此问题。