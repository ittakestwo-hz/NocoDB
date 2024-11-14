# 为什么选择 lxml？

## 座右铭

"尽享刺激，无需陌生"

解释这个座右铭：

"使用 libxml2 编程就像是被一个陌生的异国人热情拥抱。它似乎拥有实现你最疯狂梦想的潜力，但你脑海中总有一个声音在警告你，可能会以最糟糕的方式遭遇挫败。"（[马克·皮尔格林的引用](https://web.archive.org/web/20110902041836/http://diveintomark.org/archives/2004/02/18/libxml2)）

马克·皮尔格林特别描述了 Python 程序员在使用 libxml2 时的体验。libxml2 的默认 Python 绑定非常快、充满刺激和强大，但你的代码可能会以一种非常糟糕的方式崩溃，而这种崩溃其实在编写 Python 代码时完全不应担心。lxml 将 libxml2 的强大功能与 Python 的易用性相结合。

## 目标

C 库 [libxml2](http://www.xmlsoft.org/) 和 [libxslt](http://xmlsoft.org/XSLT) 具有巨大的优势：

- 符合标准的 XML 支持。
- 支持（损坏的）HTML。
- 功能全面。
- 由 XML 专家积极维护。
- 快！快！非常快！

这些库已经提供了 Python 绑定，但这些 Python 绑定模仿了 C 级接口，导致了一些问题：

- 非常底层且 C 风格（不符合 Python 风格）。
- 文档不充分且庞大，容易迷失。
- API 中使用 UTF-8，而不是 Python 的 Unicode 字符串。
- 容易导致 Python 崩溃（segfault）。
- 需要手动内存管理！

lxml 是一个新的 Python 绑定，完全独立于这些现有的 Python 绑定，绑定到 libxml2 和 libxslt。它的目标是：

- Python 风格的 API。
- 有文档支持。
- 在 API 中使用 Python 的 Unicode 字符串。
- 安全（没有崩溃）。
- 无需手动内存管理！

lxml 旨在通过尽可能遵循 [ElementTree API](http://effbot.org/zone/element-index.htm) 提供一个 Python 风格的 API。我们尽量避免发明过多新的 API，或让你学习新东西——XML 已经够复杂了。