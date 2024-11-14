# 基准测试和速度

lxml.etree 是一个非常快速的 XML 库。它的大部分速度来自于 libxml2，例如解析器、序列化器以及 XPath 引擎。lxml 的其他部分则是专门为高层操作中的高性能编写的，例如树迭代器。

另一方面，lxml 的简洁性有时掩盖了比 API 所暗示的更为昂贵的内部操作。如果您没有意识到这些情况，lxml 的表现可能不会如您预期。在 Python 世界中，一个常见的例子是 Python 的 list 类型。新用户常常期望它是一个链表，而实际上它是作为一个数组实现的，这导致常见操作的复杂度完全不同。

类似地，libxml2 的树模型比 lxml 的 ElementTree API 映射到 Python 空间的模型更复杂，因此某些操作可能表现出意外的性能。放心，大多数 lxml 用户在实际使用中不会注意到这一点，因为 lxml 在绝对数值上非常快。它对于大多数应用来说足够快，因此 lxml 对于您的应用可能处于“足够快”和“最佳选择”之间。可以阅读一些来自[满意用户](http://article.gmane.org/gmane.comp.python.lxml.devel/3246)和[开发者讨论](http://permalink.gmane.org/gmane.comp.python.lxml.devel/3250)，看看我们是什么意思。

本文描述了 lxml.etree（简称 'lxe'）的优势，提供了一些性能陷阱的提示，并将其整体性能与 Fredrik Lundh 的原始 [ElementTree](http://effbot.org/zone/element-index.htm)（ET）和 [cElementTree](http://effbot.org/zone/celementtree.htm)（cET）库进行了比较。cElementTree 库是原始 ElementTree 的一个快速 C 实现。

## 一般说明

首先要说的是：让一个类似 DOM 的 C 库模拟 ElementTree API 是有开销的。与 ElementTree 不同，lxml 必须在请求时动态生成树节点的 Python 表示，而 libxml2 的内部树结构导致比 ElementTree 更简单的自顶向下结构更高的维护开销。这意味着：代码越多在 Python 中运行，您就越无法受益于 lxml 和 libxml2 的速度。然而，值得注意的是，这对于大多数性能关键的 Python 应用程序来说都是正确的。没有人会在纯 Python 中实现傅里叶变换，当你可以使用 NumPy 时。

因此，优势在于 lxml 提供了强大的工具，如树迭代器、XPath 和 XSLT，它们可以以 C 的速度处理复杂操作。lxml 中的 Python 风格 API 使得它们非常灵活，大多数应用程序都可以轻松受益于这些工具。

## 如何读取时间数据

此处的陈述由 (微)基准脚本 [bench_etree.py](https://github.com/lxml/lxml/blob/master/benchmark/bench_etree.py)、[bench_xpath.py](https://github.com/lxml/lxml/blob/master/benchmark/bench_xpath.py) 和 [bench_objectify.py](https://github.com/lxml/lxml/blob/master/benchmark/bench_objectify.py) 支持，这些脚本随 lxml 源代码分发一起提供。它们与 lxml 本身共享相同的 BSD 许可证，lxml 项目希望将它们推广为所有 ElementTree 实现的通用基准测试套件。添加新的基准非常容易，您只需编写小的测试方法，因此，如果您为 API 的特定部分编写了性能测试，请考虑将其发送到 lxml 邮件列表。

下面呈现的时间数据比较了 lxml 4.6.3（与 libxml2 2.9.10）与 CPython 3.8.10 标准库中最新发布版本的 ElementTree（使用 cElementTree 作为加速模块）。它们在一台 2.3GHz 双核 64 位 Intel i5 机器上运行，并运行在 Ubuntu Linux 20.04（Focal）下的单线程模式。

这些脚本对不同库运行了一些简单测试，使用不同的 XML 树配置：不同的树大小（T1-4），是否有属性（-/A），是否有 ASCII 字符串或 Unicode 文本（-/S/U），以及针对树或其序列化的 XML 形式（T/X）。在下面引用的结果中，T1 指的是一个有许多子节点的三层树，T2 交换为根元素下有许多子节点的树，T3 是一棵每层只有少数子节点的深树，T4 是一棵稍微宽一些的小树。如果涉及重复，通常意味着在树根的所有子节点上循环运行基准，否则操作是在根节点上运行（C/R）。

例如，字符代码（SATR T1）表示基准测试运行的是树 T1，具有普通字符串文本（S）和属性（A）。它是在数据树结构的根元素（R）上运行的（T）。

请注意，非常小的操作会在整数循环中重复，以使其可测量。因此，并不总是能直接比较单次访问基准（通常是循环的）和“一步获取所有内容”的基准，后者已经花费了足够的时间来进行测量，因此按原样测量。一个例子是单个子项的索引访问，它不能与 getchildren() 的时间数据进行比较。请查看脚本中的具体基准测试，以理解数据如何比较。

## 解析和序列化

序列化是 lxml 的一个优势领域。原因在于，它完全在 C 层面执行，而无需与 Python 代码交互。结果相当令人印象深刻，特别是对于 UTF-8，它是 libxml2 的本地编码格式。与（c）ElementTree 1.2（在 Python 2.7/3.2 之前是标准库的一部分）相比，lxml 快 20 到 40 倍，而与最近 Python 版本中大幅改进的 ElementTree 1.3 相比，lxml 仍然快好几倍：

```
lxe: tostring_utf16  (S-TR T1)    5.9340 msec/pass
cET: tostring_utf16  (S-TR T1)   38.3270 msec/pass

lxe: tostring_utf16  (UATR T1)    6.2032 msec/pass
cET: tostring_utf16  (UATR T1)   37.7944 msec/pass

lxe: tostring_utf16  (S-TR T2)    6.1841 msec/pass
cET: tostring_utf16  (S-TR T2)   40.2577 msec/pass

lxe: tostring_utf8   (S-TR T2)    4.6697 msec/pass
cET: tostring_utf8   (S-TR T2)   30.5173 msec/pass

lxe: tostring_utf8   (U-TR T3)    1.2085 msec/pass
cET: tostring_utf8   (U-TR T3)   9.0246 msec/pass
```

对于纯文本序列化，差异稍微小一些：

```
lxe: tostring_text_ascii     (S-TR T1)    2.6727 msec/pass
cET: tostring_text_ascii     (S-TR T1)    2.9683 msec/pass

lxe: tostring_text_ascii     (S-TR T3)    0.6952 msec/pass
cET: tostring_text_ascii     (S-TR T3)    1.0073 msec/pass

lxe: tostring_text_utf16     (S-TR T1)    2.7366 msec/pass
cET: tostring_text_utf16     (S-TR T1)   7.3647 msec/pass

lxe: tostring_text_utf16     (U-TR T1)    3.0322 msec/pass
cET: tostring_text_utf16     (U-TR T1)   7.5922 msec/pass
```

`tostring()` 函数还支持序列化为 Python 的 Unicode 字符串对象，在 CPython 3.8 下，ElementTree 的速度目前更快：

```
lxe: tostring_text_unicode   (S-TR T1)    2.7645 msec/pass
cET: tostring_text_unicode   (S-TR T1)    1.1806 msec/pass

lxe: tostring_text_unicode   (U-TR T1)    2.9871 msec/pass
cET: tostring_text_unicode   (U-TR T1)    1.1659 msec/pass

lxe: tostring_text_unicode   (S-TR T3)    0.7446 msec/pass
cET: tostring_text_unicode   (S-TR T3)    0.4532 msec/pass

lxe: tostring_text_unicode   (U-TR T4)    0.0048 msec/pass
cET: tostring_text_unicode   (U-TR T4)    0.0134 msec/pass
```

对于解析，lxml.etree 和 cElementTree 竞争速度的冠军。根据输入数据，二者中的任何一个都可能更快。（c）ET 库在 expat 解析器之上使用了一个非常薄的层，expat 解析器是著名的非常快速的解析器。以下是来自基准测试套件的一些时间数据：

```
lxe: parse_bytesIO   (SAXR T1)   14.2074 msec/pass
cET: parse_bytesIO   (SAXR T1)    7.9336 msec/pass

lxe: parse_bytesIO   (S-XR T3)    1.4477 msec/pass
cET: parse_bytesIO   (S-XR T3)    2.1925 msec/pass

lxe: parse_bytesIO   (UAXR T3)    8.4128 msec/pass
cET: parse_bytesIO   (UAXR T3)   12.2926 msec/pass
```

还有另外一些时间数据，来自 [一个基准测试](http://svn.effbot.org/public/elementtree-1.3/benchmark.py)，这是 Fredrik Lundh [用来推广 cElementTree 的](http://effbot.org/zone/celementtree.htm#benchmarks)，比较了多个不同的解析器。首先，解析一个包含莎士比亚《哈姆雷特》的 274KB XML 文件：

```
xml.etree.ElementTree.parse done in 0.006 seconds
xml.etree.cElementTree.parse done in 0.007 seconds
xml.etree.cElementTree.XMLParser.feed(): 6636 nodes read in 0.006 seconds
lxml.etree.parse done in 0.004 seconds
drop_whitespace.parse done in 0.004 seconds
lxml.etree.XMLParser.feed(): 6636 nodes read in 0.004 seconds
minidom tree read in 0.066 seconds
```

以及一个包含《旧约》内容的 3.4MB XML 文件：

```
xml.etree.ElementTree.parse done in 0.037 seconds
xml.etree.cElementTree.parse done in 0.036 seconds
xml.etree.cElementTree.XMLParser.feed(): 25317 nodes read in 0.036 seconds
lxml.etree.parse done in 0.025 seconds
drop_whitespace.parse done in 0.022 seconds
lxml.etree.XMLParser.feed(): 25317 nodes read in 0.026 seconds
minidom tree read in 0.194 seconds
```

以下是相同的基准测试，但这次包括了解析前后进程的内存使用情况（以 KB 为单位），并使用 os.fork() 确保每次都从一个干净的状态开始。对于 274KB 的 hamlet.xml 文件：

```
Memory usage: 9256
xml.etree.ElementTree.parse done in 0.006 seconds
Memory usage: 12764 (+3508)
xml.etree.cElementTree.parse done in 0.007 seconds
Memory usage: 12764 (+3508)
xml.etree.cElementTree.XMLParser.feed(): 6636 nodes read in 0.006 seconds
Memory usage: 12720 (+3464)
lxml.etree.parse done in 0.004 seconds
Memory usage: 15052 (+5796)
drop_whitespace.parse done in 0.004 seconds
Memory usage: 14040 (+4784)
lxml.etree.XMLParser.feed(): 6636 nodes read in 0.004 seconds
Memory usage: 15812 (+6556)
minidom tree read in 0.066 seconds
Memory usage: 15332 (+6076)
```

对于 3.4MB 的《旧约》XML 文件：

```
Memory usage: 12456
xml.etree.ElementTree.parse done in 0.037 seconds
Memory usage: 23288 (+10832)
xml.etree.cElementTree.parse done in 0.036 seconds
Memory usage: 23288 (+10832)
xml.etree.cElementTree.XMLParser.feed(): 25317 nodes read in 0.036 seconds
Memory usage: 23644 (+11220)
lxml.etree.parse done in 0.025 seconds
Memory usage: 31404 (+18948)
drop_whitespace.parse done in 0.022 seconds
Memory usage: 28752 (+16296)
lxml.etree.XMLParser.feed(): 25317 nodes read in 0.026 seconds
Memory usage: 33924 (+21500)
minidom tree read in 0.194 seconds
Memory usage: 31284 (+18828)
```

从这些大小可以看出，lxml.etree 和 cElementTree 都非常节省内存且快速。与较旧的 CPython 版本相比，minidom 库的内存占用在 CPython 3.3 中大幅减少，在这种情况下约减少了 4 倍。

对于普通的解析器性能，lxml.etree 和 cElementTree 通常相差不大，通常在两倍之内，且胜者在两者之间分布较为均匀。对于 iterparse() 函数，也可以观察到类似的时间数据：

```
lxe: iterparse_bytesIO   (SAXR T1)   20.3598 msec/pass
cET: iterparse_bytesIO   (SAXR T1)   10.8948 msec/pass

lxe: iterparse_bytesIO   (UAXR T3)    10.1640 msec/pass
cET: iterparse_bytesIO   (UAXR T3)   12.9926 msec/pass
```

然而，如果你基准测试完整的序列化-解析循环，那么结果会类似于以下数据：

```
lxe: write_utf8_parse_bytesIO   (S-TR T1)   18.9857 msec/pass
cET: write_utf8_parse_bytesIO   (S-TR T1)   35.7475 msec/pass

lxe: write_utf8_parse_bytesIO   (UATR T2)   22.4853 msec/pass
cET: write_utf8_parse_bytesIO   (UATR T2)   42.6254 msec/pass

lxe: write_utf8_parse_bytesIO   (S-TR T3)    3.3801 msec/pass
cET: write_utf8_parse_bytesIO   (S-TR T3)   11.2493 msec/pass

lxe: write_utf8_parse_bytesIO   (SATR T4)    0.4263 msec/pass
cET: write_utf8_parse_bytesIO   (SATR T4)    1.0326 msec/pass
```

对于需要高解析器吞吐量的大文件应用，并且几乎不进行序列化的应用，cET 和 lxml.etree 都是不错的选择。cET 库特别适合于 iterparse 应用，能够从大型 XML 数据集中提取少量数据或聚合信息，这些数据集无法完全加载到内存中。然而，当涉及到往返性能时，lxml 的总体速度要快数倍。因此，只要输入文档的大小不比输出文档大得多，lxml 无疑是最佳选择。

关于 HTML 解析，Ian Bicking 做过一些 [关于 lxml HTML 解析器的基准测试](http://blog.ianbicking.org/2008/03/30/python-html-parser-performance/)，并将其与其他几个著名的 Python HTML 解析器工具进行了比较。lxml 在这场竞争中遥遥领先。为了给出一个概念，数据表明，lxml.html 可以在其他工具仅用于解析的时间内完成几轮解析-序列化循环。比较中甚至显示了关于内存消耗的一些非常有利的结果。

Liza Daly 撰写了一篇文章，介绍了几种技巧，可以最大化 lxml 解析器在非常大 XML 文档中的性能表现。她非常推崇将 lxml.etree 作为一个 [高性能 XML 解析工具](http://www.ibm.com/developerworks/xml/library/x-hiperfparse/)。

最后，[xml.com](http://www.xml.com/) 发布了几篇关于 XML 解析器性能的文章。Farwick 和 Hafner 撰写了两篇有趣的文章，将 libxml2 解析器与一些主要的 Java XML 解析器进行了比较。一篇讨论了 [事件驱动解析器的性能](http://www.xml.com/lpt/a/1702)，另一篇展示了 [DOM 解析器的基准测试结果](http://www.xml.com/lpt/a/1703)。这两篇比较都表明，libxml2 的解析器性能在几乎所有情况下都优于所有常用的 Java 解析器。请注意，C 解析器的基准测试结果基于 [xmlbench](http://xmlbench.sourceforge.net/)，它为 libxml2 提供了比 lxml 更简单的设置。

## ElementTree API

由于这三种库都实现了相同的 API，因此在这一领域它们的性能比较非常直接。lxml 性能的一个主要劣势是其底层的 libxml2 所采用的不同树模型。虽然这种模型使 lxml 能够为元素提供父指针和完全的 XPath 支持，但也增加了树构建和重构的开销。从基准测试中的树设置时间（以秒为单位）可以看出这一点：

```
lxe:       --   S-   U-   -A     SA     UA
     T1: 0.0219 0.0254 0.0257 0.0216 0.0259 0.0259
     T2: 0.0234 0.0279 0.0283 0.0271 0.0318 0.0307
     T3: 0.0051 0.0050 0.0058 0.0218 0.0233 0.0231
     T4: 0.0001 0.0001 0.0001 0.0004 0.0004 0.0004
cET:       --   S-   U-   -A     SA     UA
     T1: 0.0035 0.0029 0.0078 0.0031 0.0031 0.0029
     T2: 0.0047 0.0051 0.0053 0.0046 0.0055 0.0048
     T3: 0.0016 0.0216 0.0027 0.0021 0.0023 0.0026
     T4: 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000
```

这些时间相对接近，尽管对于更大的树，cET 可能比 lxml 快几倍。原因之一是，lxml 必须将传入的字符串数据和标签名编码为 UTF-8，并在使用后丢弃创建的 Python 元素，当它们不再被引用时。而 ElementTree 通过这些对象表示树本身，从而减少了创建它们的开销。

## 子节点访问

相同的树结构开销使得像 `list(element)` 这样收集子节点的操作在 lxml 中变得更为耗时。cET 可以快速创建其子节点列表的浅拷贝，而 lxml 则需要为每个子节点创建一个 Python 对象并将其收集到列表中：

```
lxe: root_list_children        (--TR T1)    0.0036 msec/pass
cET: root_list_children        (--TR T1)    0.0005 msec/pass

lxe: root_list_children        (--TR T2)    0.0634 msec/pass
cET: root_list_children        (--TR T2)    0.0086 msec/pass
```

当访问单个子节点时，这种劣势也显而易见：

```
lxe: first_child               (--TR T2)    0.0601 msec/pass
cET: first_child               (--TR T2)    0.0548 msec/pass

lxe: last_child                (--TR T1)    0.0570 msec/pass
cET: last_child                (--TR T1)    0.0534 msec/pass
```

...除非你还需要计算在更大的列表中查找子节点索引的时间。ET 和 cET 在这里使用的是基于数组的 Python 列表，而 libxml2 使用的是一个链接树，因此，它是一个孩子节点的链表：

```
lxe: middle_child              (--TR T1)    0.0892 msec/pass
cET: middle_child              (--TR T1)    0.0510 msec/pass

lxe: middle_child              (--TR T2)    2.3038 msec/pass
cET: middle_child              (--TR T2)    0.0508 msec/pass
```

## 元素创建

与 ET 不同，libxml2 有一个文档的概念，每个元素必须属于某个文档。这导致了在创建独立元素并将其放入独立创建的文档中时，性能上的巨大差异：

```
lxe: create_elements           (--TC T2)    0.8032 msec/pass
cET: create_elements           (--TC T2)    0.0675 msec/pass
```

因此，总是建议为元素所在的文档创建元素，方法可以是作为元素的子元素，或者使用显式的 `Element.makeelement()` 调用：

```
lxe: makeelement               (--TC T2)    0.8030 msec/pass
cET: makeelement               (--TC T2)    0.0625 msec/pass

lxe: create_subelements        (--TC T2)    0.8621 msec/pass
cET: create_subelements        (--TC T2)    0.0923 msec/pass
```

因此，如果一个应用程序的主要性能瓶颈是在内存中通过调用 `Element` 和 `SubElement` 创建大型 XML 树，那么 cET 是最佳选择。然而，值得注意的是，序列化性能可能会平衡这种优势，尤其是对于较小的树或具有许多属性的树。

## 合并不同的源

对于 lxml 来说，一个关键操作是将元素在文档上下文之间移动。这需要 lxml 对整个移动的树结构进行递归调整。

以下基准测试将第二棵树的所有根子节点附加到第一棵树的根节点：

```
lxe: append_from_document      (--TR T1,T2)    1.3800 msec/pass
cET: append_from_document      (--TR T1,T2)    0.0513 msec/pass

lxe: append_from_document      (--TR T3,T4)    0.0150 msec/pass
cET: append_from_document      (--TR T3,T4)    0.0026 msec/pass
```

尽管与解析相比，这些数字相对较小，但它清楚地展示了 lxml 和 (c)ET 之间不同的性能等级。在后者不需要处理父指针和树结构的情况下，lxml 必须深度遍历被附加的树。因此，性能差异随着移动的树的大小增加而增大。

这种差异并不总是那么明显，但适用于 API 的大多数部分，例如插入新创建的元素：

```
lxe: insert_from_document         (--TR T1,T2)    5.2345 msec/pass
cET: insert_from_document         (--TR T1,T2)    0.0732 msec/pass
```

或者通过新创建的元素替换子元素切片：

```
lxe: replace_children_element   (--TC T1)    0.0720 msec/pass
cET: replace_children_element   (--TC T1)    0.0105 msec/pass
```

而不是用同一文档中的现有元素替换该切片：

```
lxe: replace_children           (--TC T1)    0.0060 msec/pass
cET: replace_children           (--TC T1)    0.0050 msec/pass
```

尽管这些数字在实际中不会产生显著的性能影响，但在合并非常大的树时，您应当考虑到这一差异。请注意，Element 类有一个 `makeelement()` 方法，它允许在同一文档内创建一个元素，从而避免在将元素插入到树中时的合并开销。

## 深拷贝

在 lxml 中，深拷贝树的速度很快：

```
lxe: deepcopy_all              (--TR T1)    4.1246 msec/pass
cET: deepcopy_all              (--TR T1)   2.5451 msec/pass

lxe: deepcopy_all              (-ATR T2)    4.7867 msec/pass
cET: deepcopy_all              (-ATR T2)   2.7504 msec/pass

lxe: deepcopy_all              (S-TR T3)    1.0097 msec/pass
cET: deepcopy_all              (S-TR T3)   0.6278 msec/pass
```

因此，例如，如果您有一个类似数据库的场景，在其中解析一个大树并随后搜索并复制独立的子树进行进一步处理，那么 lxml 在这里无疑是最好的选择。

## 树遍历

XML 处理中的另一个重要领域是树遍历的迭代。如果您的算法能够从逐步遍历 XML 树中获益，特别是当只有少数元素是感兴趣的，或者目标元素的标签名称已知时，`.iter()` 方法是一个不错的选择：

```
lxe: iter_all             (--TR T1)    1.3661 msec/pass
cET: iter_all             (--TR T1)    0.2670 msec/pass

lxe: iter_islice          (--TR T2)    0.0122 msec/pass
cET: iter_islice          (--TR T2)    0.0033 msec/pass

lxe: iter_tag             (--TR T2)    0.0098 msec/pass
cET: iter_tag             (--TR T2)    0.0086 msec/pass

lxe: iter_tag_all         (--TR T2)    0.6840 msec/pass
cET: iter_tag_all         (--TR T2)    0.4323 msec/pass
```

这直接导致了 `Element.findall()` 的类似时间表现：

```
lxe: findall              (--TR T2)    3.9611 msec/pass
cET: findall              (--TR T2)    0.9227 msec/pass

lxe: findall              (--TR T3)    0.3989 msec/pass
cET: findall              (--TR T3)    0.2670 msec/pass

lxe: findall_tag          (--TR T2)    0.7420 msec/pass
cET: findall_tag          (--TR T2)    0.4942 msec/pass

lxe: findall_tag          (--TR T3)    0.1099 msec/pass
cET: findall_tag          (--TR T3)    0.1748 msec/pass
```

请注意，目前所有三个库在 `.findall()` 方法上使用相同的 Python 实现，除了它们的本地树迭代器（`element.iter()`）。一般来说，lxml 在迭代方面非常快速，但在需要查找并实例化大量元素时，相比 cET 会有所逊色。因此，搜索越有选择性，lxml 的运行速度就越快。

## XPath

以下的时间测试基于基准脚本 [bench_xpath.py](https://github.com/lxml/lxml/blob/master/benchmark/bench_xpath.py)。

这一部分功能在 ElementTree 中没有等效实现。然而，lxml 提供了多种访问方式，因此在使用时应注意选择 lxml API 的哪一部分。最直接的方式是调用 `xpath()` 方法，作用于 `Element` 或 `ElementTree`：

```
lxe: xpath_method         (--TC T1)    0.2828 msec/pass
lxe: xpath_method         (--TC T2)    5.4705 msec/pass
lxe: xpath_method         (--TC T3)    0.0324 msec/pass
lxe: xpath_method         (--TC T4)    0.2804 msec/pass
```

这种方法非常适合测试，尤其是当 XPath 表达式和调用它们的树结构一样多样时。然而，如果你有一个单一的 XPath 表达式，并希望将其应用于大量不同的元素，那么使用 XPath 类是最有效的方式：

```
lxe: xpath_class          (--TC T1)    0.0570 msec/pass
lxe: xpath_class          (--TC T2)    0.6924 msec/pass
lxe: xpath_class          (--TC T3)    0.0148 msec/pass
lxe: xpath_class          (--TC T4)    0.0446 msec/pass
```

请注意，这仍然允许你在表达式中使用变量，因此你可以先解析一次，然后在调用时通过变量进行调整。在其他情况下，如果你有一个固定的 Element 或 ElementTree，并希望对其运行不同的表达式，应该考虑使用 XPathEvaluator：

```
lxe: xpath_element        (--TR T1)    0.0684 msec/pass
lxe: xpath_element        (--TR T2)    1.0865 msec/pass
lxe: xpath_element        (--TR T3)    0.0174 msec/pass
lxe: xpath_element        (--TR T4)    0.0665 msec/pass
```

尽管看起来稍微慢一些，但为每个表达式创建一个 XPath 对象会带来更高的开销：

```
lxe: xpath_class_repeat           (--TC T1   )    0.2813 msec/pass
lxe: xpath_class_repeat           (--TC T2   )    5.4042 msec/pass
lxe: xpath_class_repeat           (--TC T3   )    0.0339 msec/pass
lxe: xpath_class_repeat           (--TC T4   )    0.2706 msec/pass
```

请注意，如果您的代码在找到前几个元素后就终止，那么树遍历的速度可能会比 XPath 快得多。XPath 引擎始终会返回完整的结果集，而不管实际使用的部分有多少。

这是一个仅搜索第一个匹配元素的示例，XPath 语法也支持这种情况：

```
lxe: find_single                (--TR T2)    0.0031 msec/pass
cET: find_single                (--TR T2)    0.0026 msec/pass

lxe: iter_single                (--TR T2)    0.0019 msec/pass
cET: iter_single                (--TR T2)    0.0002 msec/pass

lxe: xpath_single               (--TR T2)    0.0861 msec/pass
```

当从多个元素中查找前两个元素时，XPath 的性能会大幅下降，因为限制结果子集需要更复杂的表达式：

```
lxe: iterfind_two               (--TR T2)    0.0050 msec/pass
cET: iterfind_two               (--TR T2)    0.0036 msec/pass

lxe: iter_two                   (--TR T2)    0.0021 msec/pass
cET: iter_two                   (--TR T2)    0.0014 msec/pass

lxe: xpath_two                  (--TR T2)    0.0916 msec/pass
```

## 一个更长的示例

... 基于 lxml 1.3。

不久前，Uche Ogbuji 提出了一个[基准测试建议](http://www.onlamp.com/pub/wlg/6291)，该测试将读取一个 3MB 的 XML 格式的[《旧约》](http://www.ibiblio.org/bosak/xml/eg/religion.2.00.xml.zip)圣经，并在所有章节中查找单词 _begat_。显然，它出现在近 24000 篇章节中的 120 篇中。使用 `findall()` 在 ElementTree 中实现这一功能非常简单。然而，最快且最节省内存的方式显然是 `iterparse()`，因为大部分数据并不需要关注。

Uche 最初的提议大致如下：

```
def bench_ET():
    tree = ElementTree.parse("ot.xml")
    result = []
    for v in tree.findall("//v"):
        text = v.text
        if 'begat' in text:
            result.append(text)
    return len(result)
```

今天在我的机器上运行大约需要一秒钟。更快的 `iterparse()` 变体如下：

```
def bench_ET_iterparse():
    result = []
    for event, v in ElementTree.iterparse("ot.xml"):
        if v.tag == 'v':
            text = v.text
            if 'begat' in text:
                result.append(text)
        v.clear()
    return len(result)
```

改进大约是 10%。当我第一次尝试时（2006年初），lxml 并不支持 `iterparse()`，但 `findall()` 变体已经比 ElementTree 更快了。当切换到 `cElementTree` 后，这一情况立即发生了变化。后者今天只需 0.17 秒就能完成此操作，而使用 `iterparse` 版本时只需 0.10 秒。即使在当时，`cElementTree` 的速度也比 lxml 快得多。

从那时起，lxml 已经成熟并且变得更快。现在，`iterparse` 版本的运行时间为 0.14 秒，如果去掉 `v.clear()`，运行速度会更快一点（而 `cElementTree` 则不然）。

lxml 中的众多优秀工具之一是 XPath，这是一把寻找 XML 文档内容的瑞士军刀。可以将整个过程转移到纯 XPath 实现，代码如下：

```
def bench_lxml_xpath_all():
    tree = etree.parse("ot.xml")
    result = tree.xpath("//v[contains(., 'begat')]/text()")
    return len(result)
```

这个实现大约需要 0.13 秒，是我能想到的最短实现（按 Python 代码行数计算）。现在，这个 XPath 表达式已经比我们最初的简单 `//v` ElementPath 表达式复杂了不少。既然这也是有效的 XPath，我们再试试下面这个：

```
def bench_lxml_xpath():
    tree = etree.parse("ot.xml")
    result = []
    for v in tree.xpath("//v"):
        text = v.text
        if 'begat' in text:
            result.append(text)
    return len(result)
```

这使得执行时间减少到了 0.12 秒，表明一个通用的 XPath 评估引擎并不总能与更简单、量身定制的解决方案相竞争。然而，由于这与最初的 `findall` 变体没有太大区别，因此我们可以完全去除 XPath 调用的复杂性，回到最开始的做法。在 lxml 下，这一版本的执行时间与 0.12 秒相同。

但还有一项尝试值得进行。我们可以将简单的 ElementPath 表达式替换为本地的树迭代器：

```
def bench_lxml_getiterator():
    tree = etree.parse("ot.xml")
    result = []
    for v in tree.getiterator("v"):
        text = v.text
        if 'begat' in text:
            result.append(text)
    return len(result)
```

这个实现与之前的相同，只是没有解析和评估路径表达式的开销。这样，它比之前的实现稍微更快，时间缩短到了 0.11 秒。相比之下，`cElementTree` 运行该版本需要 0.17 秒。

那么，我们学到了什么呢？

- Python 代码并不慢。纯 XPath 解决方案甚至没有比最初的 Python 实现更快。通常，更多的 Python 代码行使得事情更易读，这比最后 5% 的性能提升更为重要。
- 了解可用的选项很重要——值得从最简单的方案开始。在这个例子中，程序员可能会首先选择 `getiterator("v")` 或 `iterparse()`。无论选择哪个，它们都会是最有效的，具体取决于使用的库。
- 了解自己的工具也很重要。lxml 和 cElementTree 都是非常快速的库，但它们的性能特性不同。在某个库中最快的解决方案，在另一个库中可能会相对较慢。如果优化，应该针对特定的目标平台进行优化。
- 并不是所有情况都值得优化。经过这么多的努力，我们从最初的 0.12 秒缩短到 0.11 秒。切换到 `cElementTree` 并编写基于 `iterparse()` 的版本，会将时间缩短到 0.10 秒——对于 3MB 的 XML 数据而言，差距并不大。
- 注意操作的主导因素。在分解操作后，我们可以看到，lxml 在 `parse()` 上略慢于 cElementTree（两者大约都是 0.06 秒），但在 `iterparse()` 上的差异更明显：0.07 秒对比 0.10 秒。然而，lxml 的树迭代速度非常快，因此将整个树解析出来再进行迭代，可能比直接使用 `iterparse()` 一步完成要更好。或者，你可以等待 lxml 开发者在未来的版本中优化 `iterparse`。

## lxml.objectify

以下时间记录基于基准脚本 [bench_objectify.py](https://github.com/lxml/lxml/blob/master/benchmark/bench_objectify.py)。

Objectify 是一个基于 lxml.etree 的 XML 数据绑定 API，在版本 1.1 中加入。它使用标准的 Python 属性访问来遍历 XML 树。它还具有 ObjectPath，这是一个基于相同模型的快速路径语言。

与 lxml.etree 一样，lxml.objectify 会动态创建元素的 Python 表示。为了节省内存，正常的 Python 垃圾回收机制会在最后一个引用消失时丢弃这些元素。在频繁通过 objectify API 访问深度嵌套元素的情况下，创建和丢弃周期可能成为瓶颈，因为元素必须一遍又一遍地实例化。

## ObjectPath

ObjectPath 可用于加速访问树中深层的元素。它避免了沿路径逐步实例化 Python 元素，从而显著提高访问时间：

```
lxe: attribute                  (--TR T1)    2.4018 毫秒/次
lxe: attribute                  (--TR T2)   16.3755 毫秒/次
lxe: attribute                  (--TR T4)    2.3725 毫秒/次

lxe: objectpath                 (--TR T1)    1.1816 毫秒/次
lxe: objectpath                 (--TR T2)   14.4675 毫秒/次
lxe: objectpath                 (--TR T4)    1.2276 毫秒/次

lxe: attributes_deep            (--TR T1)    3.7086 毫秒/次
lxe: attributes_deep            (--TR T2)   17.5436 毫秒/次
lxe: attributes_deep            (--TR T4)    3.8407 毫秒/次

lxe: objectpath_deep            (--TR T1)    1.4980 毫秒/次
lxe: objectpath_deep            (--TR T2)   14.7266 毫秒/次
lxe: objectpath_deep            (--TR T4)    1.4834 毫秒/次
```

然而，请注意，解析 ObjectPath 表达式也不是免费的，因此它最适用于频繁访问相同元素的情况。

## 缓存元素

提高普通属性访问时间的一种方法是静态实例化 Python 对象，从而牺牲内存来换取速度。只需创建一个缓存字典并运行：

```
cache[root] = list(root.iter())
```

在解析后运行此操作，并且在完成树的操作后：

这将使所有元素的 Python 表示保持有效，从而避免了重复创建 Python 对象的开销。你还可以考虑使用过滤器或生成器表达式来进行选择性缓存。通过选择正确的树（甚至是子树和元素）进行缓存，你可以在内存使用与访问速度之间进行权衡：

```
lxe: attribute_cached           (--TR T1)    1.9207 毫秒/次
lxe: attribute_cached           (--TR T2)   15.6903 毫秒/次
lxe: attribute_cached           (--TR T4)    1.8718 毫秒/次

lxe: attributes_deep_cached     (--TR T1)    2.6512 毫秒/次
lxe: attributes_deep_cached     (--TR T2)   16.7937 毫秒/次
lxe: attributes_deep_cached     (--TR T4)    2.5539 毫秒/次

lxe: objectpath_deep_cached     (--TR T1)    0.8519 毫秒/次
lxe: objectpath_deep_cached     (--TR T2)   13.9337 毫秒/次
lxe: objectpath_deep_cached     (--TR T4)    0.8645 毫秒/次
```

需要注意的是：目前无法使用 `weakref.WeakKeyDictionary` 对象，因为 lxml 的元素对象不支持弱引用（这在内存方面是有成本的）。还要注意，当你向这些树中添加新的元素时，它们不会自动出现在缓存中，因此它们仍然会在所有 Python 引用消失时被垃圾回收。所以这种方法对于大部分不可变的树结构最为有效。在这种情况下，你应该考虑使用集合而不是列表，并手动将新元素添加进去。

## 进一步优化

如果需要优化，以下是一些可以尝试的方法：

- 很多时间通常花费在树遍历中，以便找到树中被地址定位的元素。如果你经常在子树中工作，可以像在 Python 对象中那样，分配子树的父元素到变量，或者将其传递到函数中，而不是从根节点开始。这样可以更直接地访问其后代。
- 尝试将数据值直接分配给属性，而不是通过 `DataElement` 传递。
- 如果你使用自定义数据类型且解析成本高，可以尝试在只读树上运行 `objectify.annotate()`，以加速读取访问时的属性类型推断。

请注意，这些措施并不能保证一定能加速你的应用。像往常一样，你应该更倾向于可读的代码，而不是过早进行优化，在进行优化前最好先分析你的预期用例。