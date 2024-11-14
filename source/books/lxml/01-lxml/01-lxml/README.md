# lxml - 使用 Python 处理 XML 和 HTML

lxml 是 Python 中最具功能性且易于使用的 XML 和 HTML 处理库。

## 介绍

lxml XML 工具包是 C 库 [libxml2](http://xmlsoft.org/) 和 [libxslt](http://xmlsoft.org/XSLT/) 的 Pythonic 绑定。它的独特之处在于将这些库的速度和 XML 功能完备性与原生 Python API 的简洁性相结合，兼容且优于著名的 [ElementTree](http://effbot.org/zone/element-index.htm) API。最新版本支持从 3.6 到 3.12 的所有 CPython 版本。有关 lxml 项目背景和目标的更多信息，请参见 [介绍](https://lxml.de/intro.html)。一些常见问题可以在 [FAQ](https://lxml.de/FAQ.html) 中找到。

## 支持该项目

lxml 已从 [Python 包索引](https://pypi.python.org/pypi/lxml) 下载数百万次，并且也直接在许多软件包分发版中提供，例如 Linux 或 macOS。

大多数使用 lxml 的人是因为他们喜欢使用它。你可以通过在博客中分享你使用 lxml 的经验并链接到项目网站，来表达你对它的喜爱。

如果你在工作中使用 lxml，并希望为支持该项目回馈一些自己的利益，可以通过 GitHub Sponsors、Tidelift 或 PayPal 向我们捐款，我们将用这些资金为维护这个伟大的库、修复软件中的 bug、审核和整合代码贡献、改进其功能和文档，或偶尔休息喝杯茶提供支持。请阅读下方的法律声明，谢谢您的支持。

通过 [GitHub Sponsors](https://github.com/users/scoder/sponsorship) 支持 lxml

通过 [Tidelift 订阅](https://tidelift.com/subscription/pkg/pypi-lxml)

或通过 PayPal：

[![Donate to the lxml project](https://lxml.de/paypal_btn_donateCC_LG.png)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=R56JE3VCPDA9N)

请 [联系 Stefan Behnel](http://consulting.behnel.de/) 了解支持 lxml 项目的其他方式，以及有关 lxml 和快速 Python XML 处理的商业咨询、定制和培训。

请注意，我们不接受加密货币捐款。lxml 的许多开发和托管工作是通过碳中和或补偿和低排放的方式进行的。加密货币不符合这一目标。

[AppVeyor](https://www.appveyor.com/) 和 [GitHub Actions](https://docs.github.com/en/actions) 支持 lxml 项目的构建和 CI 服务器。Jetbrains 通过捐赠免费的 [PyCharm IDE](https://www.jetbrains.com/pycharm/) 许可证来支持 lxml 项目。lxml 项目的另一个支持者是 [COLOGNE Webdesign](https://www.colognewebdesign.de/)。

## 文档

本网站的 HTML 文档是正常 [源代码下载](https://lxml.de/index.html#download)的一部分。

-   教程：
    -   [lxml.etree XML 处理教程](https://lxml.de/tutorial.html)
    -   John Shipman 的 [Python XML 处理教程](https://web.archive.org/web/20110108100213/https://infohost.nmt.edu/tcc/help/pubs/pylxml/)
    -   Fredrik Lundh 的 [ElementTree 教程](https://web.archive.org/web/20200720191942/http://effbot.org:80/zone/element.htm)
-   ElementTree：
    -   [ElementTree API](http://effbot.org/zone/element-index.htm#documentation)
    -   lxml.etree 的 [兼容性](https://lxml.de/compatibility.html) 和差异
    -   [ElementTree 性能](https://lxml.de/performance.html) 特性和比较
-   lxml.etree：
    -   [lxml.etree 特定 API](https://lxml.de/api.html) 文档
    -   [生成的 API 文档](https://lxml.de/api/index.html) 作为参考
    -   [解析](https://lxml.de/parsing.html) 和 [验证](https://lxml.de/validation.html) XML
    -   [XPath 和 XSLT](https://lxml.de/xpathxslt.html) 支持
    -   Python [XPath 扩展函数](https://lxml.de/extensions.html) 用于 XPath 和 XSLT
    -   [自定义 XML 元素类](https://lxml.de/element_classes.html) 用于自定义 XML API（参见 [EuroPython 2008 讲座](https://lxml.de/s5/lxml-ep2008.html)）
    -   [SAX 兼容 API](https://lxml.de/sax.html) 用于与其他 XML 工具接口
    -   [C 级 API](https://lxml.de/capi.html) 用于与外部 C/Cython 模块接口
-   lxml.objectify：
    -   [lxml.objectify](https://lxml.de/objectify.html) API 文档
    -   简要比较 [objectify 和 etree](https://lxml.de/FAQ.html#what-is-the-difference-between-lxml-etree-and-lxml-objectify)

lxml.etree 尽可能遵循 [ElementTree](http://effbot.org/zone/element-index.htm) API，并在其基础上构建原生 libxml2 树。如果你是 ElementTree 的新手，可以从 [lxml.etree XML 处理教程](https://lxml.de/tutorial.html) 开始。另见 ElementTree 的 [兼容性](https://lxml.de/compatibility.html) 概述和 [ElementTree 性能](https://lxml.de/performance.html) 页面，比较 lxml 和原版 [ElementTree](http://effbot.org/zone/element-index.htm) 以及 [cElementTree](http://effbot.org/zone/celementtree.htm) 实现。

在 [lxml.etree XML 处理教程](https://lxml.de/tutorial.html) 和 [ElementTree](http://effbot.org/zone/element-index.htm) 文档之后，下一步可以查看 [lxml.etree 特定 API](https://lxml.de/api.html) 文档。它描述了 lxml 如何扩展 ElementTree API，以暴露 libxml2 和 libxslt 特定的 XML 功能，如 [XPath](https://www.w3.org/TR/xpath/)、[Relax NG](https://relaxng.org/)、[XML Schema](https://www.w3.org/XML/Schema)、[XSLT](https://www.w3.org/TR/xslt) 和 [c14n](https://www.w3.org/TR/xml-c14n)（包括 [c14n 2.0](https://www.w3.org/TR/xml-c14n2)）。Python 代码可以通过 [XPath 扩展函数](https://lxml.de/extensions.html) 从 XPath 表达式和 XSLT 样式表中调用。lxml 还提供了一个 [SAX 兼容 API](https://lxml.de/sax.html)，它与标准库中的 SAX 支持一起使用。

除了 ElementTree API，lxml 还提供了一个复杂的 [自定义 XML 元素类](https://lxml.de/element_classes.html) API，这是在 lxml 上编写任意 XML 驱动 API 的简单方法。lxml.etree 还有一个 [C 级 API](https://lxml.de/capi.html)，可以用于在外部 C 模块中高效地扩展 lxml.etree，包括对自定义元素类的快速支持。

## 下载

下载 lxml 最好的方式是访问 [Python 包索引中的 lxml](http://pypi.python.org/pypi/lxml/)（PyPI）。它包含适用于各种平台的源代码。源代码分发包已通过 [此密钥](https://lxml.de/index.htmlpubkey.asc) 签名。

最新版本是 [lxml 5.3.0](https://lxml.de/files/lxml-5.3.0.tgz)，发布于 2024-08-10（[5.3.0 的更新内容](https://lxml.de/changes-5.3.0.html)）。[旧版本](https://lxml.de/index.html##old-versions) 列在下面。

请查看 [安装说明](https://lxml.de/index.htmlinstallation.html)！

本完整网站（包括生成的 API 文档）是源代码分发包的一部分，因此，如果你想离线使用文档，可以下载源代码归档并复制 doc/html 目录。

最新的 [可安装开发源代码](https://github.com/lxml/lxml/archive/master.zip) 可从 GitHub 获取。你也可以通过类似如下的命令直接从 GitHub 获取 lxml 的最新开发版本：

```
git clone https://github.com/lxml/lxml.git lxml
```

你可以通过网页浏览 [源代码仓库](https://github.com/lxml/lxml/) 及其历史。请首先阅读 [如何从源代码构建 lxml](https://lxml.de/index.htmlbuild.html)。你也可以查看开发版的 [最新更改](https://github.com/lxml/lxml/blob/master/CHANGES.txt)，以了解你发现的 bug 是否已修复，或你希望的功能是否已在最新的主干版本中实现。

## 邮件列表

有问题吗？有建议吗？有代码贡献吗？我们有 [邮件列表](https://lxml.de/mailinglist/)。

你也可以在 [邮件列表归档](https://mail.python.org/archives/list/lxml@python.org/) 中搜索过去的问题和讨论。

## 错误跟踪

lxml 使用 [launchpad 错误跟踪器](https://launchpad.net/lxml/)。如果你确信在 lxml 中发现了 bug，请在此处提交错误报告。如果你不确定 lxml 的某些意外行为是否为 bug，请先查看文档，并在 [邮件列表](https://lxml.de/mailinglist/) 中提问。别忘了先 [搜索归档](https://mail.python.org/archives/list/lxml@python.org/)！

## 许可证

lxml 库根据 [BSD 许可证](https://github.com/lxml/lxml/blob/master/doc/licenses/BSD.txt) 发行。libxml2 和 libxslt2 本身根据 [MIT 许可证](https://opensource.org/licenses/mit-license.html) 发行。因此，使用 lxml 进行开发应该没有障碍。

## 旧版本

请访问 lxml 的各个旧版本网站：[5.2](https://lxml.de/5.2/)，[5.1](https://lxml.de/5.1/)，[5.0](https://lxml.de/5.0/)，[4.9](https://lxml.de/4.9/)，[4.8](https://lxml.de/4.8/)，[4.7](https://lxml.de/4.7/)，[4.6](https://lxml.de/4.6/)，[4.5](https://lxml.de/4.5/)，[4.4](https://lxml.de/4.4/)，[4.3](https://lxml.de/4.3/)，[4.2](https://lxml.de/4.2/)，[4.1](https://lxml.de/4.1/)，[4.0](https://lxml.de/4.0/)，[3.8](https://lxml.de/3.8/)，[3.7](https://lxml.de/3.7/)，[3.6](https://lxml.de/3.6/)，[3.5](https://lxml.de/3.5/)，[3.4](https://lxml.de/3.4/)，[3.3](https://lxml.de/3.3/)，[3.2](https://lxml.de/3.2/)，[3.1](https://lxml.de/3.1/)，[3.0](https://lxml.de/3.0/)，[2.3](https://lxml.de/2.3/)，[2.2](https://lxml.de/2.2/)，[2.1](https://lxml.de/2.1/)，[2.0](https://lxml.de/2.0/)，[1.3](https://lxml.de/1.3/)

-   [lxml 5.3.0](https://lxml.de/files/lxml-5.3.0.tgz)，发布于 2024-08-10（[5.3.0 更新内容](https://lxml.de/changes-5.3.0.html)）
-   [lxml 5.2.2](https://lxml.de/files/lxml-5.2.2.tgz)，发布于 2024-05-12（[5.2.2 更新内容](https://lxml.de/changes-5.2.2.html)）
-   [lxml 5.2.1](https://lxml.de/files/lxml-5.2.1.tgz)，发布于 2024-04-02（[5.2.1 更新内容](https://lxml.de/changes-5.2.1.html)）
-   [lxml 5.2.0](https://lxml.de/files/lxml-5.2.0.tgz)，发布于 2024-03-30（[5.2.0 更新内容](https://lxml.de/changes-5.2.0.html)）
-   [lxml 5.1.1](https://lxml.de/files/lxml-5.1.1.tgz)，发布于 2024-03-28（[5.1.1 更新内容](https://lxml.de/changes-5.1.1.html)）
-   [lxml 5.1.0](https://lxml.de/files/lxml-5.1.0.tgz)，发布于 2024-01-05（[5.1.0 更新内容](https://lxml.de/changes-5.1.0.html)）
-   [lxml 5.0.2](https://lxml.de/files/lxml-5.0.2.tgz)，发布于 2024-03-28（[5.0.2 更新内容](https://lxml.de/changes-5.0.2.html)）
-   [lxml 5.0.1](https://lxml.de/files/lxml-5.0.1.tgz)，发布于 2024-01-05（[5.0.1 更新内容](https://lxml.de/changes-5.0.1.html)）
-   [lxml 5.0.0](https://lxml.de/files/lxml-5.0.0.zip)，发布于 2023-12-29（[5.0.0 更新内容](https://lxml.de/changes-5.0.0.html)）
-   [旧版本](https://lxml.de/5.0/##old-versions)

## 项目收入报告

lxml 每月在 PyPI 上的下载量约为 8000 万次。

-   2023 年总项目收入：EUR 2776.56（231.38 欧元/月，2.89 欧元/百万次下载）
    -   Tidelift：EUR 2738.46
    -   Paypal：EUR 38.10
-   2022 年总项目收入：EUR 2566.38（213.87 欧元/月，3.56 欧元/百万次下载）
    -   Tidelift：EUR 2539.38
    -   Paypal：EUR 24.32
-   2021 年总项目收入：EUR 4640.37（386.70 欧元/月）
    -   Tidelift：EUR 4066.66
    -   Paypal：EUR 223.71
    -   其他：EUR 350.00
-   2020 年总项目收入：EUR 6065.86（506.49 欧元/月）
    -   Tidelift：EUR 4064.77
    -   Paypal：EUR 1401.09
    -   其他：EUR 600.00
-   2019 年总项目收入：EUR 717.52（59.79 欧元/月）
    -   Tidelift：EUR 360.30
    -   Paypal：EUR 157.22
    -   其他：EUR 200.00

## 捐赠法律声明

你对 lxml 项目的任何捐赠都是自愿的，并不是支付任何服务、商品或其他优势的费用。通过捐赠给 lxml 项目，你

同意 lxml 的收入将用于开发 lxml 和维护其操作，且有可能用于向开发人员提供报酬（包括薪水、津贴、福利、雇佣等），但 lxml 项目的资金仍由开发人员自主管理。