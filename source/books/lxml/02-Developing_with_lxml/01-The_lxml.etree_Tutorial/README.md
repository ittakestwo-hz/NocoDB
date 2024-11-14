# lxml.etree 教程

这是一个关于使用 `lxml.etree` 处理 XML 的教程。它简要概述了 [ElementTree API](https://docs.python.org/3/library/xml.etree.elementtree.html) 的主要概念，以及一些使程序员生活更轻松的简单增强功能。

要查看 API 的完整参考文档，请参见 [生成的 API 文档](https://lxml.de/api/index.html)。

导入 `lxml.etree` 的常见方式如下：

```
In [1]:
from lxml import etree
```

如果你的代码仅使用 ElementTree API，并且不依赖于 `lxml.etree` 特有的任何功能，你也可以使用以下导入链作为回退，使用 Python 标准库中的 ElementTree：

```
In [2]:
try:
    from lxml import etree
    print("running with lxml.etree")
except ImportError:
    import xml.etree.ElementTree as etree
    print("running with Python's xml.etree.ElementTree")
Out [2]:
running with lxml.etree
```

为了帮助编写可移植代码，本教程在示例中明确指出哪些 API 部分是  `lxml.etree` 相对于原始 [ElementTree API](https://docs.python.org/3/library/xml.etree.elementtree.html) 的扩展。

## Element 类

Element 是 ElementTree API 中的主要容器对象。大多数 XML 树的功能通过这个类访问。元素可以通过 `etree.Element` 轻松创建：

```
In [3]:
root = etree.Element("root")
```

元素的 XML 标签名称通过 `tag` 属性访问：

元素在 XML 树结构中组织。要创建子元素并将其添加到父元素中，可以使用 `append()` 方法：

```
In [4]:
root.append( etree.Element("child1") )
```

然而，这种操作非常常见，因此有一种更简洁、更高效的方式来实现：使用 `etree.SubElement`。它接受与 `etree.Element` 相同的参数，但额外要求第一个参数是父元素：

```
In [5]:
child2 = etree.SubElement(root, "child2")
child3 = etree.SubElement(root, "child3")
```

要查看这确实是 XML，你可以将你创建的树序列化为字符串：

```
In [6]:
etree.tostring(root)
Out [6]:
b'<root><child1/><child2/><child3/></root>'
```

我们将创建一个小的辅助函数来美化打印 XML：

```
In [7]:
def prettyprint(element, **kwargs):
    xml = etree.tostring(element, pretty_print=True, **kwargs)
    print(xml.decode(), end='')
```

```
In [8]:
prettyprint(root)
Out [8]:
<root>
  <child1/>
  <child2/>
  <child3/>
</root>
```

## 元素是列表

为了方便访问这些子元素，元素尽可能模拟普通 Python 列表的行为：

```
In [9]:
child = root[0]
```

```
In [10]:
print(child.tag)
Out [10]:
child1
```

```
In [11]:
print(len(root))
Out [11]:
3
```

```
In [12]:
root.index(root[1])  # 仅限 lxml.etree!
Out [12]:
1
```

```
In [13]:
children = list(root)
```

```
In [14]:
for child in root:
    print(child.tag)
Out [14]:
child1
child2
child3
```

```
In [15]:
root.insert(0, etree.Element("child0"))
```

```
In [16]:
start = root[:1]
```

```
In [17]:
end = root[-1:]
```

```
In [18]:
print(start[0].tag)
Out [18]:
child0
```

```
In [19]:
print(end[0].tag)
Out [19]:
child3
```

在 ElementTree 1.3 和 lxml 2.0 之前，你还可以检查 Element 的布尔值来判断它是否有子元素，即判断子元素列表是否为空：

```
In [20]:
if root: # 现在不再适用!
    print("The root element has children")
Out [20]:
The root element has children
```

这不再被支持，因为人们倾向于期望“某物”在布尔值上下文中评估为 True，并期望元素是“某物”，无论它是否有子元素。因此，许多用户会感到惊讶，为什么任何元素在像上面这样的 if 语句中会评估为 False。取而代之，使用 `len(element)`，这样既更明确，又更不容易出错。

```
In [21]:
print(etree.iselement(root)) # 测试它是否是某种类型的 Element
Out [21]:
True
In [22]:
if len(root):  # 测试它是否有子元素
    print("The root element has children")
Out [22]:
The root element has children    
```

还有一种重要的情况，其中 lxml 中的元素（在 2.0 及之后版本中）的行为偏离了列表的行为，并且偏离了原始 ElementTree（1.3 版本之前或 Python 2.7/3.2 之前版本）的行为：

```
In [23]:
for child in root:
    print(child.tag)
Out [23]:
child0
child1
child2
child3
In [24]:
root[0] = root[-1]  # 这将在 lxml.etree 中移动元素！
In [25]:
for child in root:
    print(child.tag)
Out [25]:
child3
child1
child2
```

---

在这个例子中，最后一个元素被 _移动_ 到了不同的位置，而不是被 _复制_，即它会在放到新位置时自动从之前的位置移除。在列表中，对象可以同时出现在多个位置，而上述赋值仅仅会将项的引用复制到第一个位置，因此两个位置都包含相同的项：

```
l = [0, 1, 2, 3]
l[0] = l[-1]
l
[3, 1, 2, 3]

```

请注意，在原始的 ElementTree 中，单个 Element 对象可以出现在任意数量的树的任意位置，这使得与列表相同的复制操作成为可能。显而易见的缺点是，对这样的 Element 进行修改时，修改会应用到它出现在树中的所有位置，这可能是有意的，也可能不是。

这种差异的好处是，在 lxml.etree 中，一个 Element 始终只有一个父元素，可以通过 `getparent()` 方法查询到。原始的 ElementTree 不支持这一点。

```
root is root[0].getparent()  # 仅限 lxml.etree！
True

```

如果你想将一个元素 _复制_ 到 lxml.etree 中的不同位置，可以考虑使用 Python 标准库中的 `copy` 模块来创建一个独立的 _深拷贝_：

```
from copy import deepcopy

element = etree.Element("neu")
element.append( deepcopy(root[1]) )

print(element[0].tag)
child1
print([ c.tag for c in root ])
['child3', 'child1', 'child2']

```

元素的兄弟（或邻居）可以作为下一个元素和上一个元素来访问：

```
root[0] is root[1].getprevious()  # 仅限 lxml.etree！
True
root[1] is root[0].getnext()  # 仅限 lxml.etree！
True

```

## 元素携带属性（如字典）

XML 元素支持属性。你可以直接在 `etree.Element` 中创建它们：

```
root = etree.Element("root", interesting="totally")
etree.tostring(root)
b'<root interesting="totally"/>'

```

属性只是无序的名称-值对，因此处理它们的一个非常方便的方法是通过元素的类似字典的接口：

```
print(root.get("interesting"))
totally

print(root.get("hello"))
None
root.set("hello", "Huhu")
print(root.get("hello"))
Huhu

etree.tostring(root)
b'<root interesting="totally" hello="Huhu"/>'

sorted(root.keys())
['hello', 'interesting']

for name, value in sorted(root.items()):
...     print('%s = %r' % (name, value))
hello = 'Huhu'
interesting = 'totally'

```

对于你希望进行项查找或有其他原因需要获取一个“真实”字典样式的对象（例如传递它），你可以使用 `attrib` 属性：

```
attributes = root.attrib

print(attributes["interesting"])
totally
print(attributes.get("no-such-attribute"))
None

attributes["hello"] = "Guten Tag"
print(attributes["hello"])
Guten Tag
print(root.get("hello"))
Guten Tag

```

请注意，`attrib` 是一个字典样式的对象，由 Element 本身支持。这意味着对 Element 的任何修改都会反映在 `attrib` 中，反之亦然。它还意味着只要 `attrib` 被使用，XML 树就会一直保存在内存中。为了获得一个独立的属性快照，该快照不依赖于 XML 树，可以将其复制到一个字典中：

```
d = dict(root.attrib)
sorted(d.items())
[('hello', 'Guten Tag'), ('interesting', 'totally')]

```

## 元素包含文本

元素可以包含文本：

```
root = etree.Element("root")
root.text = "TEXT"

print(root.text)
TEXT

etree.tostring(root)
b'<root>TEXT</root>'

```

在许多 XML 文档（_以数据为中心_ 的文档）中，文本通常只出现在元素的内容中。它被封装在树层次结构最底层的叶标签中。

然而，如果 XML 用于标记文本文档，如 (X)HTML，文本也可以出现在不同元素之间，直接位于树的中间：

```
<html><body>Hello<br/>World</body></html>

```

在这里，`<br/>` 标签被文本包围。这通常被称为 _文档风格_ 或 _混合内容_ XML。元素通过其 `tail` 属性支持这种情况。它包含直接跟在元素之后的文本，直到 XML 树中的下一个元素：

```
html = etree.Element("html")
body = etree.SubElement(html, "body")
body.text = "TEXT"

etree.tostring(html)
b'<html><body>TEXT</body></html>'

br = etree.SubElement(body, "br")
etree.tostring(html)
b'<html><body>TEXT<br/></body></html>'

br.tail = "TAIL"
etree.tostring(html)
b'<html><body>TEXT<br/>TAIL</body></html>'

```

这两个属性 `.text` 和 `.tail` 足以表示 XML 文档中的任何文本内容。这样，ElementTree API 不需要任何额外的 [特殊文本节点](http://www.w3.org/TR/DOM-Level-3-Core/core.html#ID-1312295772)，这些节点通常会妨碍操作（如你可能知道的经典 [DOM](http://www.w3.org/TR/DOM-Level-3-Core/core.html) API）。

然而，也有一些情况下，`tail` 文本会妨碍操作。例如，当你从树中序列化一个元素时，你不总是希望它的 `tail` 文本出现在结果中（虽然你仍然希望它的子元素的 `tail` 文本保留）。为此，`tostring()` 函数接受 `with_tail` 关键字参数：

```
etree.tostring(br)
b'<br/>TAIL'
etree.tostring(br, with_tail=False) # 仅限 lxml.etree！
b'<br/>'

```

如果你只想读取 _文本_，即不包含任何中间标签，你必须递归地将所有文本和 `tail` 属性按正确顺序连接起来。同样，`tostring()` 函数可以派上用场，这次使用 `method` 关键字：

```
etree.tostring(html, method="text")
b'TEXTTAIL'

```

## 使用 XPath 查找文本

提取树的文本内容的另一种方式是使用 [XPath](https://lxml.de/xpathxslt.html#xpath)，它还允许你将独立的文本块提取到一个列表中：

```
print(html.xpath("string()")) # 仅限 lxml.etree！
TEXTTAIL
print(html.xpath("//text()")) # 仅限 lxml.etree！
['TEXT', 'TAIL']

```

如果你希望更频繁地使用这个功能，可以将它封装在一个函数中：

```
build_text_list = etree.XPath("//text()") # 仅限 lxml.etree！
print(build_text_list(html))
['TEXT', 'TAIL']

```

请注意，XPath 返回的字符串结果是一个特殊的“智能”对象，它知道自己的来源。你可以通过其 `getparent()` 方法查询它来自哪里，和查询元素一样：

```
texts = build_text_list(html)
print(texts[0])
TEXT
parent = texts[0].getparent()
print(parent.tag)
body

print(texts[1])
TAIL
print(texts[1].getparent().tag)
br

```

你还可以发现它是普通的文本内容还是尾部文本：

```
print(texts[0].is_text)
True
print(texts[1].is_text)
False
print(texts[1].is_tail)
True

```

虽然这对于 `text()` 函数的结果有效，但 lxml 不会告诉你通过 XPath 函数 `string()` 或 `concat()` 构造的字符串值的来源：

```
stringify = etree.XPath("string()")
print(stringify(html))
TEXTTAIL
print(stringify(html).getparent())
None

```

## 树的迭代

对于类似上述的问题，如果你希望递归地遍历树并对其元素做一些处理，树迭代是一个非常方便的解决方案。元素提供了一个树迭代器用于此目的。它按 _文档顺序_ 生成元素，即按你将树序列化为 XML 时标签出现的顺序：

```
root = etree.Element("root")
etree.SubElement(root, "child").text = "Child 1"
etree.SubElement(root, "child").text = "Child 2"
etree.SubElement(root, "another").text = "Child 3"

prettyprint(root)
<root>
  <child>Child 1</child>
  <child>Child 2</child>
  <another>Child 3</another>
</root>

for element in root.iter():
...     print(f"{element.tag} - {element.text}")
root - None
child - Child 1
child - Child 2
another - Child 3

```

如果你知道你只对某个标签感兴趣，可以将其名称传递给 `iter()` 来进行过滤。从 lxml 3.0 开始，你也可以传递多个标签，在迭代时拦截多个标签。

```
for element in root.iter("child"):
...     print(f"{element.tag} - {element.text}")
child - Child 1
child - Child 2

for element in root.iter("another", "child"):
...     print(f"{element.tag} - {element.text}")
child - Child 1
child - Child 2
another - Child 3

```

默认情况下，迭代返回树中的所有节点，包括处理指令、注释和实体实例。如果你只想确保返回的是 `Element` 对象，可以将 `Element` 工厂作为 `tag` 参数传递：

```
root.append(etree.Entity("#234"))
root.append(etree.Comment("some comment"))

for element in root.iter():
...     if isinstance(element.tag, str):
...         print(f"{element.tag} - {element.text}")
...     else:
...         print(f"SPECIAL: {element} - {element.text}")
root - None
child - Child 1
child - Child 2
another - Child 3
SPECIAL: &#234; - &#234;
SPECIAL: <!--some comment--> - some comment

for element in root.iter(tag=etree.Element):
...     print(f"{element.tag} - {element.text}")
root - None
child - Child 1
child - Child 2
another - Child 3

for element in root.iter(tag=etree.Entity):
...     print(element.text)
&#234;

```

请注意，传递一个通配符 "\*" 标签名也会返回所有的 `Element` 节点（且仅限元素节点）。

在 `lxml.etree` 中，元素提供了[进一步的迭代器](https://lxml.de/api.html#iteration)用于树中的所有方向：子元素、父元素（或更准确地说，祖先元素）以及兄弟元素。

## 序列化

序列化通常使用 `tostring()` 函数，它返回一个字符串，或使用 `ElementTree.write()` 方法，该方法将内容写入文件、类文件对象或 URL（通过 FTP PUT 或 HTTP POST）。这两种方法都接受相同的关键字参数，如 `pretty_print` 用于格式化输出，或 `encoding` 用于选择除纯 ASCII 以外的特定输出编码：

```
root = etree.XML('<root><a><b/></a></root>')

etree.tostring(root)
b'<root><a><b/></a></root>'

xml_string = etree.tostring(root, xml_declaration=True)
print(xml_string.decode(), end='')
<?xml version='1.0' encoding='ASCII'?>
<root><a><b/></a></root>

latin1_bytesstring = etree.tostring(root, encoding='iso8859-1')
print(latin1_bytesstring.decode('iso8859-1'), end='')
<?xml version='1.0' encoding='iso8859-1'?>
<root><a><b/></a></root>

print(etree.tostring(root, pretty_print=True).decode(), end='')
<root>
  <a>
    <b/>
  </a>
</root>

```

请注意，漂亮打印会在末尾添加一个换行符。因此，我们在这里使用 `end=''` 参数来防止 `print()` 函数再添加一个换行符。

为了对漂亮打印进行更细粒度的控制，你可以在序列化之前使用 `indent()` 函数（在 lxml 4.5 中新增）为树添加空白缩进：

```
root = etree.XML('<root><a><b/>\n</a></root>')
print(etree.tostring(root).decode())
<root><a><b/>
</a></root>

etree.indent(root)
print(etree.tostring(root).decode())
<root>
  <a>
    <b/>
  </a>
</root>

root.text
'\n  '
root[0].text
'\n    '

etree.indent(root, space="    ")
print(etree.tostring(root).decode())
<root>
    <a>
        <b/>
    </a>
</root>

etree.indent(root, space="\t")
etree.tostring(root)
b'<root>\n\t<a>\n\t\t<b/>\n\t</a>\n</root>'

```

在 lxml 2.0 及之后版本以及 `xml.etree` 中，序列化函数不仅仅支持 XML 序列化。你还可以通过传递 `method` 关键字来序列化为 HTML 或提取文本内容：

```
root = etree.XML(
...    '<html><head/><body><p>Hello<br/>World</p></body></html>')

etree.tostring(root)  # 默认: method = 'xml'
b'<html><head/><body><p>Hello<br/>World</p></body></html>'

etree.tostring(root, method='xml')  # 与上面相同
b'<html><head/><body><p>Hello<br/>World</p></body></html>'

etree.tostring(root, method='html')
b'<html><head></head><body><p>Hello<br>World</p></body></html>'

prettyprint(root, method='html')
<html>
<head></head>
<body><p>Hello<br>World</p></body>
</html>

etree.tostring(root, method='text')
b'HelloWorld'

```

关于 XML 序列化，纯文本序列化的默认编码是 ASCII：

```
br = next(root.iter('br'))  # 获取迭代的第一个结果
br.tail = 'Wörld'

etree.tostring(root, method='text')  # doctest: +ELLIPSIS
Traceback (most recent call last):
  ...
UnicodeEncodeError: 'ascii' codec can't encode character '\xf6' ...

etree.tostring(root, method='text', encoding="UTF-8")
b'HelloW\xc3\xb6rld'

```

在这里，将其序列化为 Python 文本字符串而不是字节字符串可能会变得很方便。只需将编码指定为 'unicode'：

```
etree.tostring(root, encoding='unicode', method='text')
'HelloWörld'
etree.tostring(root, encoding='unicode')
'<html><head/><body><p>Hello<br/>Wörld</p></body></html>'

```

W3C 有一篇关于 Unicode 字符集和字符编码的优秀文章，链接为 <[http://www.w3.org/International/tutorials/tutorial-char-enc/](http://www.w3.org/International/tutorials/tutorial-char-enc/)\>\`\_。

## ElementTree 类

`ElementTree` 主要是一个包含根节点的树的文档封装器。它提供了一些用于序列化和文档处理的方法。

```
root = etree.XML('''\
... <?xml version="1.0"?>
... <!DOCTYPE root SYSTEM "test" [ <!ENTITY tasty "parsnips"> ]>
... <root>
...   <a>&tasty;</a>
... </root>
... ''')

tree = etree.ElementTree(root)
print(tree.docinfo.xml_version)
1.0
print(tree.docinfo.doctype)
<!DOCTYPE root SYSTEM "test">

tree.docinfo.public_id = '-//W3C//DTD XHTML 1.0 Transitional//EN'
tree.docinfo.system_url = 'file://local.dtd'
print(tree.docinfo.doctype)
<!DOCTYPE root PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "file://local.dtd">

```

当你调用 `parse()` 函数解析文件或类文件对象时，返回的就是 `ElementTree` 对象（见下面的解析部分）。

一个重要的区别是，`ElementTree` 类会作为完整的文档进行序列化，而不是单个 `Element`。这包括顶级处理指令和注释，以及文档中的 DOCTYPE 和其他 DTD 内容：

```
prettyprint(tree)  # lxml 1.3.4 及之后版本
<!DOCTYPE root PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "file://local.dtd" [
<!ENTITY tasty "parsnips">
]>
<root>
  <a>parsnips</a>
</root>

```

在原始的 `xml.etree.ElementTree` 实现和 lxml 1.3.3 之前的版本中，输出与仅序列化根 `Element` 时的结果相同：

```
prettyprint(tree.getroot())
<root>
  <a>parsnips</a>
</root>

```

这种序列化行为在 lxml 1.3.4 中发生了变化。之前，树会被序列化时不包含 DTD 内容，这导致 lxml 在输入输出循环中丢失了 DTD 信息。

## 从字符串和文件中解析

`lxml.etree` 支持多种方式解析 XML，支持的主要来源包括字符串、文件、URL（http/ftp）以及类文件对象。主要的解析函数是 `fromstring()` 和 `parse()`，它们都接受源作为第一个参数。默认情况下，它们使用标准解析器，但你始终可以将不同的解析器作为第二个参数传递。

## `fromstring()` 函数

`fromstring()` 函数是解析字符串的最简单方式：

```
some_xml_data = "<root>data</root>"

root = etree.fromstring(some_xml_data)
print(root.tag)
root
etree.tostring(root)
b'<root>data</root>'

```

## `XML()` 函数

`XML()` 函数的行为类似于 `fromstring()` 函数，但通常用于将 XML 字面量直接写入源中：

```
root = etree.XML("<root>data</root>")
print(root.tag)
root
etree.tostring(root)
b'<root>data</root>'

```

对于 HTML 字面量，也有一个对应的函数 `HTML()`。

```
root = etree.HTML("<p>data</p>")
etree.tostring(root)
b'<html><body><p>data</p></body></html>'

```

## `parse()` 函数

`parse()` 函数用于从文件和类文件对象中解析。

作为类文件对象的一个示例，以下代码使用 `BytesIO` 类从字符串中读取，而不是从外部文件读取。然而，实际应用中，你显然会避免这样做，而是使用像 `fromstring()` 这样的字符串解析函数。

```
from io import BytesIO
some_file_or_file_like_object = BytesIO(b"<root>data</root>")

tree = etree.parse(some_file_or_file_like_object)

etree.tostring(tree)
b'<root>data</root>'

```

请注意，`parse()` 返回的是 `ElementTree` 对象，而不是像字符串解析函数那样的 `Element` 对象：

```
root = tree.getroot()
print(root.tag)
root
etree.tostring(root)
b'<root>data</root>'

```

这种差异的原因在于，`parse()` 是从文件返回完整的文档，而字符串解析函数通常用于解析 XML 片段。

`parse()` 函数支持以下任何来源：

-   一个打开的文件对象（确保以二进制模式打开）
-   一个具有 `.read(byte_count)` 方法的类文件对象，每次调用时返回一个字节串
-   一个文件名字符串
-   一个 HTTP 或 FTP URL 字符串

请注意，传递文件名或 URL 通常比传递打开的文件或类文件对象更快。然而，`libxml2` 中的 HTTP/FTP 客户端相对简单，因此像 HTTP 身份验证这样的操作需要一个专用的 URL 请求库，例如 `urllib2` 或 `requests`。这些库通常为结果提供一个类文件对象，你可以从中解析数据，同时响应正在流式传输。

## 解析器对象

默认情况下，`lxml.etree` 使用标准解析器和默认设置。如果你想配置解析器，可以创建一个新的实例：

```
parser = etree.XMLParser(remove_blank_text=True)  # 仅适用于 lxml.etree!

```

这会创建一个解析器，在解析过程中删除标签之间的空白文本，这可以减小树的大小，并避免尾部文本的悬挂。如果你知道仅包含空白的内容对你的数据没有意义，那么这种方式会有所帮助。示例：

```
root = etree.XML("<root>  <a/>   <b>  </b>     </root>", parser)

etree.tostring(root)
b'<root><a/><b>  </b></root>'

```

请注意，`<b>` 标签内的空白内容没有被移除，因为叶子元素中的内容通常是数据内容（即使是空白）。你可以通过遍历树的额外步骤轻松删除它：

```
for element in root.iter("*"):
...     if element.text is not None and not element.text.strip():
...         element.text = None

etree.tostring(root)
b'<root><a/><b/></root>'

```

查看 `help(etree.XMLParser)` 以了解可用的解析器选项。

## 增量解析

`lxml.etree` 提供了两种增量逐步解析的方法。一种是通过类文件对象，它会重复调用 `read()` 方法。这种方法最适合用于数据来自诸如 `urllib` 或任何其他可以按需提供数据的类文件对象的情况。请注意，在这种情况下，解析器会阻塞并等待数据的可用：

```
class DataSource:
...     data = [ b"<roo", b"t><", b"a/", b"><", b"/root>" ]
...     def read(self, requested_size):
...         try:
...             return self.data.pop(0)
...         except IndexError:
...             return b''

tree = etree.parse(DataSource())

etree.tostring(tree)
b'<root><a/></root>'

```

第二种方法是通过一个 `feed` 解析器接口，提供了 `feed(data)` 和 `close()` 方法：

```
parser = etree.XMLParser()

parser.feed("<roo")
parser.feed("t><")
parser.feed("a/")
parser.feed("><")
parser.feed("/root>")

root = parser.close()

etree.tostring(root)
b'<root><a/></root>'

```

在这里，你可以随时中断解析过程，并在之后通过再次调用 `feed()` 方法继续。这在你想避免阻塞解析器调用时非常有用，例如在像 Twisted 这样的框架中，或者当数据缓慢或分块到达时，你希望在等待下一个数据块的同时执行其他任务。

调用 `close()` 方法后（或当解析器抛出异常时），你可以通过再次调用其 `feed()` 方法来重用解析器：

```
parser.feed("<root/>")
root = parser.close()
etree.tostring(root)
b'<root/>'

```

## 事件驱动的解析

有时，你只需要文档中树结构某个深处的小部分，因此将整个树解析到内存中、遍历它并丢弃可能会带来过多的开销。`lxml.etree` 通过两种事件驱动的解析器接口来支持这种用例，一种是在构建树的同时生成解析事件（`iterparse`），另一种根本不构建树，而是以类似 SAX 的方式调用目标对象上的反馈方法。

这是一个简单的 `iterparse()` 示例：

```
some_file_like = BytesIO(b"<root><a>data</a></root>")

for event, element in etree.iterparse(some_file_like):
...     print(f"{event}, {element.tag:>4}, {element.text}")
end,    a, data
end, root, None

```

默认情况下，`iterparse()` 只有在完成解析一个元素后才会生成事件，但你可以通过 `events` 关键字参数来控制这一点：

```
some_file_like = BytesIO(b"<root><a>data</a></root>")

for event, element in etree.iterparse(some_file_like,
...                                       events=("start", "end")):
...     print(f"{event:>5}, {element.tag:>4}, {element.text}")
start, root, None
start,    a, data
  end,    a, data
  end, root, None

```

请注意，在接收到 `start` 事件时，元素的文本、尾部文本和子元素不一定已经存在。只有在接收到 `end` 事件时，才能保证元素已经被完全解析。

它还允许你通过 `.clear()` 或修改元素的内容来节省内存。因此，如果你解析一个较大的树并希望保持较小的内存使用，应该清理掉你不再需要的树的部分。`clear(keep_tail=True)` 参数确保不会触及当前元素后面的尾部文本内容。强烈不建议修改解析器可能尚未完全读取的内容。

```
some_file_like = BytesIO(
...     b"<root><a><b>data</b></a><a><b/></a></root>")

for event, element in etree.iterparse(some_file_like):
...     if element.tag == 'b':
...         print(element.text)
...     elif element.tag == 'a':
...         print("** cleaning up the subtree")
...         element.clear(keep_tail=True)
data
** cleaning up the subtree
None
** cleaning up the subtree

```

`iterparse()` 的一个非常重要的用例是解析大型生成的 XML 文件，例如数据库转储。通常，这些 XML 格式只有一个主数据项元素，它直接挂在根节点下，并且会重复成千上万次。在这种情况下，最好的做法是让 `lxml.etree` 来构建树，并仅拦截这一元素，使用常规的树 API 来提取数据。

```
xml_file = BytesIO(b'''\
... <root>
...   <a><b>ABC</b><c>abc</c></a>
...   <a><b>MORE DATA</b><c>more data</c></a>
...   <a><b>XYZ</b><c>xyz</c></a>
... </root>''')

for _, element in etree.iterparse(xml_file, tag='a'):
...     print('%s -- %s' % (element.findtext('b'), element[1].text))
...     element.clear(keep_tail=True)
ABC -- abc
MORE DATA -- more data
XYZ -- xyz

```

如果由于某些原因完全不希望构建树，可以使用 `lxml.etree` 的目标解析器接口。它通过调用目标对象的方法来生成类似 SAX 的事件。通过实现其中的一些或全部方法，你可以控制生成哪些事件：

```
class ParserTarget:
...     events = []
...     close_count = 0
...     def start(self, tag, attrib):
...         self.events.append(("start", tag, attrib))
...     def close(self):
...         events, self.events = self.events, []
...         self.close_count += 1
...         return events

parser_target = ParserTarget()

parser = etree.XMLParser(target=parser_target)
events = etree.fromstring('<root test="true"/>', parser)

print(parser_target.close_count)
1

for event in events:
...     print(f'event: {event[0]} - tag: {event[1]}')
...     for attr, value in event[2].items():
...         print(f' * {attr} = {value}')
event: start - tag: root
 * test = true

```

你可以根据需要多次重用解析器及其目标，因此应该确保 `.close()` 方法能够将目标重置为可用状态（即使在发生错误的情况下！）。

```
events = etree.fromstring('<root test="true"/>', parser)
print(parser_target.close_count)
2
events = etree.fromstring('<root test="true"/>', parser)
print(parser_target.close_count)
3
events = etree.fromstring('<root test="true"/>', parser)
print(parser_target.close_count)
4

for event in events:
...     print(f'event: {event[0]} - tag: {event[1]}')
...     for attr, value in event[2].items():
...         print(f' * {attr} = {value}')
event: start - tag: root
 * test = true

```

## 命名空间

ElementTree API 尽可能避免使用[命名空间前缀](http://www.w3.org/TR/xml-names/#ns-qualnames)，而是使用实际的命名空间（URI）：

```
xhtml = etree.Element("{http://www.w3.org/1999/xhtml}html")
body = etree.SubElement(xhtml, "{http://www.w3.org/1999/xhtml}body")
body.text = "Hello World"

prettyprint(xhtml)
<html:html xmlns:html="http://www.w3.org/1999/xhtml">
  <html:body>Hello World</html:body>
</html:html>

```

ElementTree 使用的标记法最初由[James Clark](http://www.jclark.com/xml/xmlns.htm)提出。其主要优点是为标签提供了一个全局限定的名称，无论文档中是否使用或定义了前缀。通过将前缀的间接性去除，使得命名空间感知代码更加清晰，容易正确实现。

如上所示，前缀只有在序列化结果时才变得重要。然而，由于命名空间名称过长，上述代码看起来有些冗长。而且反复输入或复制字符串容易出错。因此，常见的做法是将命名空间 URI 存储在全局变量中。为了适应序列化时的命名空间前缀，也可以将映射传递给 `etree.Element` 函数，例如定义默认命名空间：

```
XHTML_NAMESPACE = "http://www.w3.org/1999/xhtml"
XHTML = "{%s}" % XHTML_NAMESPACE

NSMAP = {None : XHTML_NAMESPACE} # 默认命名空间（无前缀）

xhtml = etree.Element(XHTML + "html", nsmap=NSMAP) # lxml 专用！
body = etree.SubElement(xhtml, XHTML + "body")
body.text = "Hello World"

prettyprint(xhtml)
<html xmlns="http://www.w3.org/1999/xhtml">
  <body>Hello World</body>
</html>

```

你还可以使用 `QName` 辅助类来构建或拆分合格的标签名称：

```
tag = etree.QName('http://www.w3.org/1999/xhtml', 'html')
print(tag.localname)
html
print(tag.namespace)
http://www.w3.org/1999/xhtml
print(tag.text)
{http://www.w3.org/1999/xhtml}html

tag = etree.QName('{http://www.w3.org/1999/xhtml}html')
print(tag.localname)
html
print(tag.namespace)
http://www.w3.org/1999/xhtml

root = etree.Element('{http://www.w3.org/1999/xhtml}html')
tag = etree.QName(root)
print(tag.localname)
html

tag = etree.QName(root, 'script')
print(tag.text)
{http://www.w3.org/1999/xhtml}script
tag = etree.QName('{http://www.w3.org/1999/xhtml}html', 'script')
print(tag.text)
{http://www.w3.org/1999/xhtml}script

```

lxml.etree 允许你通过 `.nsmap` 属性查看当前节点所定义的命名空间：

```
xhtml.nsmap
{None: 'http://www.w3.org/1999/xhtml'}

```

但是请注意，这包括在元素上下文中所有已知的前缀，而不仅仅是元素自身定义的前缀。

```
root = etree.Element('root', nsmap={'a': 'http://a.b/c'})
child = etree.SubElement(root, 'child',
...                          nsmap={'b': 'http://b.c/d'})
len(root.nsmap)
1
len(child.nsmap)
2
child.nsmap['a']
'http://a.b/c'
child.nsmap['b']
'http://b.c/d'

```

因此，修改返回的字典不会对元素产生实际影响。对其进行的任何更改都会被忽略。

属性上的命名空间处理类似，但从版本 2.3 开始，lxml.etree 会确保属性使用带前缀的命名空间声明。这是因为根据 XML 命名空间规范（[第 6.2 节](http://www.w3.org/TR/2009/REC-xml-names-20091208/#defaulting)），未加前缀的属性名称不被视为属于某个命名空间，因此它们可能在序列化-解析回合中丢失命名空间，即使它们出现在带命名空间的元素中。

```
body.set(XHTML + "bgcolor", "#CCFFAA")

prettyprint(xhtml)
<html xmlns="http://www.w3.org/1999/xhtml">
  <body xmlns:html="http://www.w3.org/1999/xhtml" html:bgcolor="#CCFFAA">Hello World</body>
</html>

print(body.get("bgcolor"))
None
body.get(XHTML + "bgcolor")
'#CCFFAA'

```

你还可以使用 XPath 结合完全限定名称：

```python
find_xhtml_body = etree.ETXPath(      # 仅限 lxml !
...     "//{%s}body" % XHTML_NAMESPACE)
results = find_xhtml_body(xhtml)

print(results[0].tag)
{http://www.w3.org/1999/xhtml}body
```

为了方便起见，你可以在 lxml.etree 的所有迭代器中使用 "\*" 通配符，适用于标签名称和命名空间：

```python
for el in xhtml.iter('*'): print(el.tag)   # 任意元素
{http://www.w3.org/1999/xhtml}html
{http://www.w3.org/1999/xhtml}body

for el in xhtml.iter('{http://www.w3.org/1999/xhtml}*'): print(el.tag)
{http://www.w3.org/1999/xhtml}html
{http://www.w3.org/1999/xhtml}body

for el in xhtml.iter('{*}body'): print(el.tag)
{http://www.w3.org/1999/xhtml}body
```

要查找没有命名空间的元素，可以直接使用标签名称，或显式提供空命名空间：

```python
[ el.tag for el in xhtml.iter('{http://www.w3.org/1999/xhtml}body') ]
['{http://www.w3.org/1999/xhtml}body']
[ el.tag for el in xhtml.iter('body') ]
[]
[ el.tag for el in xhtml.iter('{}body') ]
[]
[ el.tag for el in xhtml.iter('{}*') ]
[]
```

## E-Factory

E-factory 提供了一种简单而紧凑的语法来生成 XML 和 HTML：

```python
from lxml.builder import E

def CLASS(*args):  # class 在 Python 中是保留字
...     return {"class": ' '.join(args)}

html = page = (
...   E.html(       # 创建一个名为 "html" 的元素
...     E.head(
...       E.title("This is a sample document")
...     ),
...     E.body(
...       E.h1("Hello!", CLASS("title")),
...       E.p("This is a paragraph with ", E.b("bold"), " text in it!"),
...       E.p("This is another paragraph, with a", "\n      ",
...         E.a("link", href="http://www.python.org"), "."),
...       E.p("Here are some reserved characters: <spam&egg>."),
...       etree.XML("<p>And finally an embedded XHTML fragment.</p>"),
...     )
...   )
... )

prettyprint(page)
<html>
  <head>
    <title>This is a sample document</title>
  </head>
  <body>
    <h1 class="title">Hello!</h1>
    <p>This is a paragraph with <b>bold</b> text in it!</p>
    <p>This is another paragraph, with a
      <a href="http://www.python.org">link</a>.</p>
    <p>Here are some reserved characters: &lt;spam&amp;egg&gt;.</p>
    <p>And finally an embedded XHTML fragment.</p>
  </body>
</html>
```

基于属性访问创建元素，可以简化 XML 语言的构建：

```python
from lxml.builder import ElementMaker  # 仅限 lxml !

E = ElementMaker(namespace="http://my.de/fault/namespace",
...                  nsmap={'p': "http://my.de/fault/namespace"})

DOC = E.doc
TITLE = E.title
SECTION = E.section
PAR = E.par

my_doc = DOC(
...   TITLE("The dog and the hog"),
...   SECTION(
...     TITLE("The dog"),
...     PAR("Once upon a time, ..."),
...     PAR("And then ...")
...   ),
...   SECTION(
...     TITLE("The hog"),
...     PAR("Sooner or later ...")
...   )
... )

prettyprint(my_doc)
<p:doc xmlns:p="http://my.de/fault/namespace">
  <p:title>The dog and the hog</p:title>
  <p:section>
    <p:title>The dog</p:title>
    <p:par>Once upon a time, ...</p:par>
    <p:par>And then ...</p:par>
  </p:section>
  <p:section>
    <p:title>The hog</p:title>
    <p:par>Sooner or later ...</p:par>
  </p:section>
</p:doc>
```

一个这样的示例是模块 `lxml.html.builder`，它提供了 HTML 的词汇。

当处理多个命名空间时，最好为每个命名空间 URI 定义一个 `ElementMaker`。同样要注意，上述示例中在命名常量中预定义了标签生成器。这使得可以将一个命名空间的所有标签声明放入一个 Python 模块中，并从那里导入/使用标签名称常量。这可以避免诸如拼写错误或意外遗漏命名空间等问题。

## ElementPath

`ElementTree` 库带有一种简单的类 XPath 路径语言，称为 [ElementPath](http://effbot.org/zone/element-xpath.htm)。主要区别在于，你可以在 `ElementPath` 表达式中使用 `{namespace}tag` 的表示法。然而，复杂的特性（如值比较和函数）在该语言中不可用。

除了[完整的 XPath 实现](https://lxml.de/xpathxslt.html#xpath)外，`lxml.etree` 也以与 `ElementTree` 相同的方式支持 `ElementPath` 语言，甚至（几乎）使用相同的实现。API 提供了四种在元素和元素树上可以找到的方法：

-   `iterfind()`：迭代所有符合路径表达式的元素
-   `findall()`：返回符合条件的元素列表
-   `find()`：高效地返回第一个符合条件的元素
-   `findtext()`：返回第一个符合条件元素的 `.text` 内容

以下是一些示例：

```python
root = etree.XML("<root><a x='123'>aText<b/><c/><b/></a></root>")
```

查找元素的子元素：

```python
print(root.find("b"))
None
print(root.find("a").tag)
a
```

在树中查找任意位置的元素：

```python
print(root.find(".//b").tag)
b
[ b.tag for b in root.iterfind(".//b") ]
['b', 'b']
```

查找具有特定属性的元素：

```python
print(root.findall(".//a[@x]")[0].tag)
a
print(root.findall(".//a[@y]"))
[]
```

在 `lxml` 3.4 中，有一个新的辅助函数来生成元素的结构性 `ElementPath` 表达式：

```python
tree = etree.ElementTree(root)
a = root[0]
print(tree.getelementpath(a[0]))
a/b[1]
print(tree.getelementpath(a[1]))
a/c
print(tree.getelementpath(a[2]))
a/b[2]
tree.find(tree.getelementpath(a[2])) == a[2]
True
```

只要树结构没有被修改，此路径表达式就表示给定元素的标识符，可以在相同的树中使用 `find()` 方法重新找到该元素。与 XPath 相比，`ElementPath` 表达式的优势在于，即使对于使用命名空间的文档，它们也是自包含的。

`.iter()` 方法是一个特殊情况，它仅通过名称在树中查找特定标签，而不基于路径。这意味着以下命令在成功的情况下是等效的：

```python
print(root.find(".//b").tag)
b
print(next(root.iterfind(".//b")).tag)
b
print(next(root.iter("b")).tag)
b
```

请注意，如果未找到匹配项，`.find()` 方法会简单地返回 `None`，而其他两个示例则会引发 `StopIteration` 异常。