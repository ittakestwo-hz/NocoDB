# 总体规划

在您的协作下，IT 管理团队进行了一项较为详尽的研究，识别出了一些约束条件，并制定了迁移到选定的开源系统 Debian 的计划。

一个重要的约束条件是，会计部门使用特定的软件，这些软件仅能在 Microsoft Windows™ 上运行。而实验室则使用运行在 OS X™ 上的计算机辅助设计软件。

![Falcot Corp 网络概览](https://www.debian.org/doc/manuals/debian-handbook/images.en/case-study.png)

**图 2.1. Falcot Corp 网络概览**

向 Debian 迁移将是渐进的；作为一家小型企业，资源有限，不能一夜之间改变一切。

首先，IT 员工必须接受 Debian 管理的培训。然后，服务器将开始转换，首先是网络基础设施（路由器、防火墙等），接着是用户服务（文件共享、Web、SMTP 等）。随后，办公室电脑将逐步迁移到 Debian，每个部门将在新系统部署过程中进行内部培训。