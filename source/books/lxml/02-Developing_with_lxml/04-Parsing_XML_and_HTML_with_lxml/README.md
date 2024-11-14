# 使用 lxml 解析 XML 和 HTML

lxml 提供了一个非常简单且强大的 API 来解析 XML 和 HTML。它支持一步解析和基于事件驱动 API 的逐步解析（目前仅适用于 XML）。

通常的设置过程如下：

```python
from lxml import etree
```

以下示例还使用 `StringIO` 或 `BytesIO` 来演示如何从文件和类似文件的对象中解析。两者都在 `io` 模块中提供：

```python
from io import StringIO, BytesIO
```

## 解析器

解析器由解析器对象表示。lxml 支持解析 XML 和（不完整的）HTML。

> **注意**
>
> XHTML 最好作为 XML 解析，使用 HTML 解析器解析它可能会导致意外结果。

以下是从内存字符串解析 XML 的一个简单示例：

```python
xml = '<a xmlns="test"><b xmlns="test"/></a>'

root = etree.fromstring(xml)
etree.tostring(root)
b'<a xmlns="test"><b xmlns="test"/></a>'
```

要从文件或类似文件的对象中读取，可以使用 `parse()` 函数，该函数返回一个 `ElementTree` 对象，该对象封装了文档的根节点：

```
tree = etree.parse(StringIO(xml))
etree.tostring(tree.getroot())
b'<a xmlns="test"><b xmlns="test"/></a>'

```

注意，这里的 `parse()` 函数是从类文件对象读取的。如果是从真实文件进行解析，更常见（并且也更高效）的是传递文件名：

```
tree = etree.parse("doc/test.xml")

```

lxml 可以从本地文件、HTTP URL 或 FTP URL 进行解析。它还可以自动检测并读取 gzip 压缩的 XML 文件（.gz）。

如果您希望从字符串（字节或文本）进行解析，同时为文档提供一个基 URL（例如支持 XInclude 中的相对路径），可以传递 `base_url` 关键字参数：

```
root = etree.fromstring(xml, base_url="http://where.it/is/from.xml")

```

## 解析器选项

解析器接受许多配置选项作为关键字参数。上述示例可以很容易地扩展，在解析时清理命名空间：

```
parser = etree.XMLParser(ns_clean=True)
xml_root = etree.fromstring(xml, parser)
etree.tostring(xml_root)
b'<a xmlns="test"><b/></a>'

```

构造函数中的关键字参数主要基于 libxml2 解析器配置。如果请求验证或属性默认值，则还会加载 DTD。

可用的布尔类型关键字参数：

-   `attribute_defaults` - 读取 DTD（如果文档引用了它），并从中添加默认属性
-   `dtd_validation` - 在解析时验证（如果引用了 DTD）
-   `load_dtd` - 在解析时加载并解析 DTD（不执行验证）
-   `no_network` - 阻止在查找外部文档时访问网络（默认启用）
-   `ns_clean` - 尝试清理冗余的命名空间声明
-   `recover` - 尝试强力解析损坏的 XML
-   `remove_blank_text` - 丢弃标签间的空白文本节点，也称为可忽略的空白。最好与 DTD 或架构一起使用（它可以区分数据和噪声），否则将应用启发式方法。
-   `remove_comments` - 丢弃注释
-   `remove_pis` - 丢弃处理指令
-   `strip_cdata` - 将 CDATA 区段替换为普通文本内容（默认启用）
-   `resolve_entities` - 用其文本值替换实体（默认启用）
-   `huge_tree` - 禁用安全限制，支持非常深的树和非常长的文本内容（仅影响 libxml2 2.7+）
-   `compact` - 对短文本内容使用紧凑存储（默认启用）
-   `collect_ids` - 在解析过程中收集 XML ID 并存储在哈希表中（默认启用）。禁用此选项可以显著加快解析具有多个不同 ID 的文档的速度，如果之后不使用哈希查找。

其他关键字参数：

-   `encoding` - 覆盖文档编码
-   `target` - 一个解析目标对象，将接收解析事件（参见 [目标解析器接口](https://lxml.de/parsing.html#the-target-parser-interface)）
-   `schema` - 用于验证的 XMLSchema（参见 [验证](https://lxml.de/validation.html#xmlschema)）

## 错误日志

解析器具有 `error_log` 属性，列出了上次解析的错误和警告：

```
parser = etree.XMLParser()
print(len(parser.error_log))
0

tree = etree.XML("<root>\n</b>", parser)  # doctest: +ELLIPSIS
Traceback (most recent call last):
  ...
lxml.etree.XMLSyntaxError: Opening and ending tag mismatch: root line 1 and b, line 2, column 5...

print(len(parser.error_log))
1

error = parser.error_log[0]
print(error.message)
Opening and ending tag mismatch: root line 1 and b
print(error.line)
2
print(error.column)
5

```

日志中的每个条目都有以下属性：

-   `message`：消息文本
-   `domain`：域 ID（参见 `lxml.etree.ErrorDomains` 类）
-   `type`：消息类型 ID（参见 `lxml.etree.ErrorTypes` 类）
-   `level`：日志级别 ID（参见 `lxml.etree.ErrorLevels` 类）
-   `line`：消息来源的行号（如果适用）
-   `column`：消息来源的字符列号（如果适用）
-   `filename`：消息来源的文件名（如果适用）

为了方便起见，还有三个属性提供了 ID 值的可读名称：

-   `domain_name`
-   `type_name`
-   `level_name`

要过滤特定类型的消息，可以使用错误日志中的不同 `filter_*()` 方法（参见 `lxml.etree._ListErrorLog` 类）。

## 解析 HTML

HTML 解析同样简单。解析器具有一个 `recover` 关键字参数，该参数默认由 `HTMLParser` 设置。它允许 libxml2 尽力返回一个有效的 HTML 树，并解析它能够处理的所有内容。遇到解析错误时，它不会抛出异常。要使用此功能，您应该使用 libxml2 版本 2.6.21 或更高版本。

```
In [1]:
from lxml import etree
```

```
In [2]:
from io import StringIO, BytesIO
```

```
In [3]:
broken_html = "<html><head><title>test<body><h1>page title</h3>"
```

```
In [4]:
parser = etree.HTMLParser()
```

```
In [5]:
html_root = etree.fromstring(broken_html, parser)
```

```
In [6]:
result = etree.tostring(html_root, pretty_print=True, method="html")
```

```
In [7]:
print(result)
Out [7]:
b'<html>\n<head><title>test</title></head>\n<body><h1>page title</h1></body>\n</html>\n'
```

作为解析 HTML 字符串的一个更简洁的别名，lxml 提供了一个 `HTML()` 函数，类似于 ElementTree 中的 `XML()` 快捷方式：

```
In [8]:
html_root = etree.HTML("""
<html>
   <body>
      <h1>page title</h1>
  </body>
</html>
""")
result = etree.tostring(html_root, pretty_print=True, method="html")
print(result)
Out [8]:
b'<html>\n   <body>\n      <h1>page title</h1>\n  </body>\n</html>\n'
```

> **注意**
>
> 对破损 HTML 的解析完全依赖于 libxml2 的恢复算法。如果您发现某些文档严重破损，导致解析器无法处理，这并不是 lxml 的问题。如果结果树中缺少原始文档中的所有数据，也没有保证能够保留。解析器在尝试继续解析时可能需要丢弃一些严重损坏的部分。特别是元标签放错位置时，可能会出现编码问题。
>
> 需要注意的是，结果是一个有效的 HTML 树，但它可能不是一个格式良好的 XML 树。例如，XML 禁止注释中使用双破折号，而 HTML 解析器在恢复模式下会接受这一点。因此，如果您的目标是在解析后将 HTML 文档序列化为 XML/XHTML 文档，您可能需要先进行一些手动预处理。
>
> 另外，HTML 解析器旨在解析 HTML 文档。对于 XHTML 文档，应该使用 XML 解析器，它支持命名空间。

## Doctype 信息

使用 libxml2 解析器使一些额外的信息可以在 API 层访问。目前，ElementTree 对象可以访问解析文档提供的 DOCTYPE 信息，以及 XML 版本和原始编码。从 lxml 3.5 开始，DOCTYPE 引用是可变的。

```
pub_id = "-//W3C//DTD XHTML 1.0 Transitional//EN"
sys_url = "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"
doctype_string = '<!DOCTYPE html PUBLIC "%s" "%s">' % (pub_id, sys_url)
xml_header = '<?xml version="1.0" encoding="ascii"?>'
xhtml = xml_header + doctype_string + '<html><body></body></html>'

tree = etree.parse(StringIO(xhtml))
docinfo = tree.docinfo
print(docinfo.public_id)
-//W3C//DTD XHTML 1.0 Transitional//EN
print(docinfo.system_url)
http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd
docinfo.doctype == doctype_string
True
print(docinfo.xml_version)
1.0
print(docinfo.encoding)
ascii

docinfo.system_url = None
docinfo.public_id = None
print(etree.tostring(tree))
<!DOCTYPE html>
<html><body/></html>

```

## 目标解析器接口

[如同 ElementTree](http://effbot.org/elementtree/elementtree-xmlparser.htm)，并类似于 SAX 事件处理程序，您可以将目标对象传递给解析器：

```
class EchoTarget(object):
  def start(self, tag, attrib):
      print("start %s %r" % (tag, dict(attrib)))
  def end(self, tag):
      print("end %s" % tag)
  def data(self, data):
      print("data %r" % data)
  def comment(self, text):
      print("comment %s" % text)
  def close(self):
      print("close")
      return "closed!"

parser = etree.XMLParser(target = EchoTarget())

result = etree.XML("<element>some<!--comment-->text</element>",
                 parser)
start element {}
data 'some'
comment comment
data 'text'
end element
close

print(result)
closed!

```

`.close()` 方法对于重置解析器目标到可用状态非常重要，这样您可以根据需要多次重用解析器：

```
result = etree.XML("<element>some<!--comment-->text</element>",
                 parser)
start element {}
data 'some'
comment comment
data 'text'
end element
close

print(result)
closed!

```

从 lxml 2.3 开始，`.close()` 方法在出错时也会被调用。这与 ElementTree 的行为有所不同，但它允许目标对象在所有情况下清理其状态，以便解析器之后可以重新使用它们。

```
class CollectorTarget(object):
  def __init__(self):
      self.events = []
  def start(self, tag, attrib):
      self.events.append("start %s %r" % (tag, dict(attrib)))
  def end(self, tag):
      self.events.append("end %s" % tag)
  def data(self, data):
      self.events.append("data %r" % data)
  def comment(self, text):
      self.events.append("comment %s" % text)
  def close(self):
      self.events.append("close")
      return "closed!"

parser = etree.XMLParser(target = CollectorTarget())

result = etree.XML("<element>some</error>",
                 parser)        # doctest: +ELLIPSIS
Traceback (most recent call last):
  ...
lxml.etree.XMLSyntaxError: Opening and ending tag mismatch...

for event in parser.target.events:
  print(event)
start element {}
data 'some'
close

```

请注意，在使用解析器目标时，解析器不会构建树。解析器运行的结果是目标对象从其 `.close()` 方法返回的内容。如果您希望在此处返回 XML 树，则必须在目标对象中以编程方式创建它。一个构建树的解析器目标的例子是 `TreeBuilder`：

```
parser = etree.XMLParser(target = etree.TreeBuilder())

result = etree.XML("<element>some<!--comment-->text</element>",
                 parser)

print(result.tag)
element
print(result[0].text)
comment

```

## 进料解析器接口

从 lxml 2.0 开始，解析器提供了一个进料解析器接口，它与 [ElementTree 解析器](http://effbot.org/elementtree/elementtree-xmlparser.htm) 兼容。您可以使用它以受控的逐步方式将数据传递给解析器。

在 lxml.etree 中，您可以同时使用解析器的两种接口：`parse()` 或 `XML()` 函数和进料解析器接口。这两者是独立的，不会冲突（除非与解析器目标对象一起使用，如上所述）。

要使用进料解析器开始解析，只需调用其 `feed()` 方法来逐步传入数据。

```
parser = etree.XMLParser()

for data in ('<?xml versio', 'n="1.0"?', '><roo', 't><a', '/></root>'):
  parser.feed(data)

```

完成解析后，**必须**调用 `close()` 方法来获取解析结果文档的根元素，并解锁解析器：

```
root = parser.close()

print(root.tag)
root
print(root[0].tag)
a

```

如果不调用 `close()`，解析器将保持锁定状态，后续的 `feed()` 调用将继续追加数据，通常会导致文档不符合规范，并出现解析器错误。因此，确保每次使用后都关闭解析器，即使是在异常情况下也是如此。

另一种实现逐步解析的方法是编写您自己的类文件对象，使其在每次 `read()` 调用时返回一块数据。进料解析器接口允许您主动将数据块传递给解析器，而文件对象则是被动响应解析器的 `read()` 请求。根据数据源的不同，任一方式可能更加自然。

请注意，进料解析器有自己的错误日志，称为 `feed_error_log`。进料解析器中的错误不会显示在常规的 `error_log` 中，反之亦然。

您还可以将进料解析器接口与目标解析器结合使用：

```
parser = etree.XMLParser(target = EchoTarget())

parser.feed("<eleme")
parser.feed("nt>some text</elem")
start element {}
data 'some text'
parser.feed("ent>")
end element

result = parser.close()
close
print(result)
closed!

```

同样，这将防止自动创建 XML 树，并将所有事件处理交给目标对象。解析器的 `close()` 方法会转发目标的 `close()` 方法返回的值。

## 增量事件解析

在 Python 3.4 中，`xml.etree.ElementTree` 包扩展了进料解析器接口，新增了由 `XMLPullParser` 类实现的功能。它额外允许在每个增量解析步骤后，通过调用 `.read_events()` 方法并迭代其结果来处理解析事件。这对于数据块一个接一个到达并应尽可能在每个步骤中进行处理的非阻塞执行环境非常有用。

相同的功能在 lxml 3.3 中也可用。基本用法如下：

```
parser = etree.XMLPullParser(events=('start', 'end'))

def print_events(parser):
  for action, element in parser.read_events():
      print('%s: %s' % (action, element.tag))

parser.feed('<root>some text')
print_events(parser)
start: root
print_events(parser)    # 好吧，之前的事件已经没有了 ...

parser.feed('<child><a />')
print_events(parser)
start: child
start: a
end: a

parser.feed('</child></roo')
print_events(parser)
end: child
parser.feed('t>')
print_events(parser)
end: root

```

与普通的进料解析器一样，`XMLPullParser` 会在内存中构建一个树（并且您应该在完成解析后始终调用 `.close()` 方法）：

```
root = parser.close()
etree.tostring(root)
b'<root>some text<child><a/></child></root>'

```

然而，由于解析器提供了对该树的增量访问，您可以在处理完内容后显式地删除不再需要的部分。请阅读下面的 [修改树](https://lxml.de/parsing.html#modifying-the-tree) 部分，了解您可以在此进行的操作以及应避免的修改类型。

在 lxml 中，只需调用一次 `.read_events()` 方法，因为它返回的迭代器可以在有新事件时重复使用。

此外，像 lxml 中其他迭代器一样，您可以传递一个标签参数，用于选择 `.read_events()` 迭代器返回的解析事件。

## 事件类型

解析事件是由元组（事件类型，对象）组成的。`ElementTree` 和 `lxml.etree` 支持的事件类型包括字符串 `'start'`、`'end'`、`'start-ns'` 和 `'end-ns'`。`'start'` 和 `'end'` 事件表示元素的开始和结束，它们会附带相应的 `Element` 实例。默认情况下，仅生成 `'end'` 事件，而上面的示例请求生成 `'start'` 和 `'end'` 事件。

`'start-ns'` 和 `'end-ns'` 事件通知命名空间声明。它们不会带有 `Element` 对象。相反，`'start-ns'` 事件的值是一个元组 `(prefix, namespaceURI)`，表示前缀和命名空间映射的开始。相应的 `'end-ns'` 事件没有值（为 `None`）。通常的做法是使用列表作为命名空间栈，并在 `'end-ns'` 事件时弹出栈中的最后一个条目。

```
def print_events(events):
  for action, obj in events:
      if action in ('start', 'end'):
          print("%s: %s" % (action, obj.tag))
      elif action == 'start-ns':
          print("%s: %s" % (action, obj))
      else:
          print(action)

event_types = ("start", "end", "start-ns", "end-ns")
parser = etree.XMLPullParser(event_types)
events = parser.read_events()

parser.feed('<root><element>')
print_events(events)
start: root
start: element
parser.feed('text</element><element>text</element>')
print_events(events)
end: element
start: element
end: element
parser.feed('<empty-element xmlns="http://testns/" />')
print_events(events)
start-ns: ('', 'http://testns/')
start: {http://testns/}empty-element
end: {http://testns/}empty-element
end-ns
parser.feed('</root>')
print_events(events)
end: root

```

## 修改树

在处理 `'end'` 事件时，您可以修改元素及其后代。例如，为了节省内存，您可以删除不再需要的子树：

```
parser = etree.XMLPullParser()
events = parser.read_events()

parser.feed('<root><element key="value">text</element>')
parser.feed('<element><child /></element>')
for action, elem in events:
  print('%s: %d' % (elem.tag, len(elem)))  # 处理
  elem.clear(keep_tail=True)               # 删除子节点
element: 0
child: 0
element: 1
parser.feed('<empty-element xmlns="http://testns/" /></root>')
for action, elem in events:
  print('%s: %d' % (elem.tag, len(elem)))  # 处理
  elem.clear(keep_tail=True)               # 删除子节点
{http://testns/}empty-element: 0
root: 3

root = parser.close()
etree.tostring(root)
b'<root/>'

```

**警告**：在 `'start'` 事件期间，元素的任何内容（如后代、紧随其后的兄弟节点或文本）尚不可用，不应访问。只有属性会被保证已设置。在 `'end'` 事件期间，可以自由修改元素及其后代，但不应访问其后续兄弟节点。在这两种事件中，**绝对不可以**修改或移动当前元素的祖先（父元素）。也应避免移动或丢弃元素本身。黄金法则是：不要触及稍后解析器仍需处理的内容。

如果您的 XML 文件中有带有大量子节点的元素，并且希望在解析期间节省更多内存，可以清理当前元素的前面兄弟节点：

```
for event, element in parser.read_events():
  # 对元素进行某些处理
  element.clear(keep_tail=True)   # 清理子节点
  while element.getprevious() is not None:
      del element.getparent()[0]  # 清理前面的兄弟节点

```

`while` 循环会删除一连串的兄弟节点。如果您使用 `tag` 关键字参数跳过了其中一些兄弟节点，则此操作是必要的。否则，只需要一个简单的 `if` 语句即可。然而，您的 `tag` 选择越具体，就需要更多思考来找到正确的方法清理跳过的元素。因此，有时更容易遍历所有元素并在事件处理代码中手动进行标签选择。

## 选择性标签事件

作为 `ElementTree` 的扩展，`lxml.etree` 支持像 `element.iter(tag)` 一样的 `tag` 关键字参数。这可以将事件限制为特定的标签或命名空间：

```
parser = etree.XMLPullParser(tag="element")

parser.feed('<root><element key="value">text</element>')
parser.feed('<element><child /></element>')
parser.feed('<empty-element xmlns="http://testns/" /></root>')

for action, elem in parser.read_events():
  print("%s: %s" % (action, elem.tag))
end: element
end: element

event_types = ("start", "end")
parser = etree.XMLPullParser(event_types, tag="{http://testns/}*")

parser.feed('<root><element key="value">text</element>')
parser.feed('<element><child /></element>')
parser.feed('<empty-element xmlns="http://testns/" /></root>')

for action, elem in parser.read_events():
  print("%s: %s" % (action, elem.tag))
start: {http://testns/}empty-element
end: {http://testns/}empty-element

```

## 带有自定义目标的事件

您可以将拉取解析器与解析目标结合使用。在这种情况下，目标需要负责生成事件值。无论它从 `.start()` 和 `.end()` 方法中返回什么，都会作为解析事件元组中的第二个项返回给拉取解析器。

```
class Target(object):
  def start(self, tag, attrib):
      print('-> start(%s)' % tag)
      return '>>START: %s<<' % tag
  def end(self, tag):
      print('-> end(%s)' % tag)
      return '>>END: %s<<' % tag
  def close(self):
      print('-> close()')
      return "CLOSED!"

event_types = ('start', 'end')
parser = etree.XMLPullParser(event_types, target=Target())

parser.feed('<root><child1 /><child2 /></root>')
-> start(root)
-> start(child1)
-> end(child1)
-> start(child2)
-> end(child2)
-> end(root)

for action, value in parser.read_events():
  print('%s: %s' % (action, value))
start: >>START: root<<
start: >>START: child1<<
end: >>END: child1<<
start: >>START: child2<<
end: >>END: child2<<
end: >>END: root<<

print(parser.close())
-> close()
CLOSED!

```

如您所见，事件值甚至不必是 `Element` 对象。目标可以自由决定如何使用解析器的回调来创建 XML 树或其他内容。然而，在许多情况下，您可能希望让自定义目标继承自 `TreeBuilder` 类，以便它能够构建一个可以正常处理的树。`TreeBuilder` 的 `.start()` 和 `.end()` 方法会返回所创建的 `Element` 对象，因此您可以重写它们并根据需要修改输入或输出。下面是一个过滤属性的示例，在它们被添加到树之前进行处理：

```
class AttributeFilter(etree.TreeBuilder):
  def start(self, tag, attrib):
      attrib = dict(attrib)
      if 'evil' in attrib:
          del attrib['evil']
      return super(AttributeFilter, self).start(tag, attrib)

parser = etree.XMLPullParser(target=AttributeFilter())
parser.feed('<root><child1 test="123" /><child2 evil="YES" /></root>')

for action, element in parser.read_events():
  print('%s: %s(%r)' % (action, element.tag, element.attrib))
end: child1({'test': '123'})
end: child2({})
end: root({})

root = parser.close()

```

## `iterparse` 和 `iterwalk`

如同 `ElementTree` 中已知的那样，`iterparse()` 工具函数返回一个迭代器，该迭代器为 XML 文件（或类文件对象）生成解析事件，同时构建树。您可以将其视为 `XMLPullParser` 的封装器，它会自动并增量地从输入文件读取数据并为您提供一个单一的迭代器：

```
xml = '''
<root>
<element key='value'>text</element>
<element>text</element>tail
<empty-element xmlns="http://testns/" />
</root>
'''

context = etree.iterparse(StringIO(xml))
for action, elem in context:
  print("%s: %s" % (action, elem.tag))
end: element
end: element
end: {http://testns/}empty-element
end: root

```

翻译：

在解析之后，可以通过迭代器的 `root` 属性访问生成的树：

```
context.root.tag
'root'
```

其他事件类型可以通过 `events` 关键字参数激活：

```
events = ("start", "end")
context = etree.iterparse(StringIO(xml), events=events)
for action, elem in context:
  print("%s: %s" % (action, elem.tag))
start: root
start: element
end: element
start: element
end: element
start: {http://testns/}empty-element
end: {http://testns/}empty-element
end: root
```

`iterparse()` 还支持 `tag` 参数，用于选择性事件迭代，并且有多个其他参数来控制解析器的设置。`tag` 参数可以是单个标签或标签序列。你还可以通过传递 `html=True` 来解析 HTML 输入。

## iterwalk

为了方便，lxml 还提供了 `iterwalk()` 函数。它的行为与 `iterparse()` 完全相同，但作用于元素（Elements）和元素树（ElementTrees）。以下是一个通过 `iterparse()` 解析的树的示例：

```
f = StringIO(xml)
context = etree.iterparse(
          f, events=("start", "end"), tag="element")

for action, elem in context:
  print("%s: %s" % (action, elem.tag))
start: element
end: element
start: element
end: element

root = context.root
```

现在，我们可以使用 `iterwalk()` 遍历内存中的树，获取相同的事件，而无需再次解析输入：

```
context = etree.iterwalk(
          root, events=("start", "end"), tag="element")

for action, elem in context:
  print("%s: %s" % (action, elem.tag))
start: element
end: element
start: element
end: element
```

为了避免在树的无关部分浪费时间，可以指示 `iterwalk` 迭代器使用 `.skip_subtree()` 方法跳过整个子树。

```
root = etree.XML('''
<root>
<a> <b /> </a>
<c />
</root>
''')

context = etree.iterwalk(root, events=("start", "end"))

for action, elem in context:
  print("%s: %s" % (action, elem.tag))
  if action == 'start' and elem.tag == 'a':
      context.skip_subtree()  # 忽略 <b>
start: root
start: a
end: a
start: c
end: c
end: root
```

请注意，`.skip_subtree()` 只有在处理 `start` 或 `start-ns` 事件时才有效。

## Python Unicode 字符串

与 ElementTree 库相比，lxml.etree 对 Python 的 Unicode 字符串有更广泛的支持。首先，lxml.etree 中的解析器可以直接处理 Unicode 字符串，而不像 ElementTree 那样抛出异常。这对于使用 `XML()` 函数在源代码中嵌入的 XML 片段特别有用：

```
root = etree.XML( '<test> \uf8d1 + \uf8d2 </test>' )
```

然而，这要求 Unicode 字符串本身不能指定冲突的编码，否则会与其实际编码不符：

```
etree.XML( '<?xml version="1.0" encoding="ASCII"?>\n' +
         '<test> \uf8d1 + \uf8d2 </test>' )
Traceback (most recent call last):
  ...
ValueError: Unicode strings with encoding declaration are not supported. Please use bytes input or XML fragments without declaration.
```

类似地，当你尝试使用一个在头部的 meta 标签中指定字符集的 Unicode 字符串进行 HTML 数据解析时，也会遇到错误。通常情况下，你应该避免在将 XML/HTML 数据传递给解析器之前将其转换为 Unicode。这不仅更慢，而且容易出错。

## 序列化为 Unicode 字符串

要序列化结果，通常会使用 `tostring()` 模块函数，它默认会将数据序列化为纯 ASCII 编码，或者如果需要的话，可以使用其他字节编码：

```
etree.tostring(root)
b'<test> &#63697; + &#63698; </test>'

etree.tostring(root, encoding='UTF-8', xml_declaration=False)
b'<test> \xef\xa3\x91 + \xef\xa3\x92 </test>'
```

作为扩展，lxml.etree 识别 'unicode' 作为编码参数的值，用于构建树的 Python Unicode 表示：

```
etree.tostring(root, encoding='unicode')
'<test> \uf8d1 + \uf8d2 </test>'

el = etree.Element("test")
etree.tostring(el, encoding='unicode')
'<test/>'

subel = etree.SubElement(el, "subtest")
etree.tostring(el, encoding='unicode')
'<test><subtest/></test>'

tree = etree.ElementTree(el)
etree.tostring(tree, encoding='unicode')
'<test><subtest/></test>'

```

`tostring(encoding='unicode')` 的结果可以像任何其他 Python Unicode 字符串一样处理，然后可以将其传回解析器。然而，如果你想将结果保存到文件中或通过网络传输，应该使用 `write()` 或 `tostring()` 配合字节编码（通常是 UTF-8）来序列化 XML。主要原因是 `tostring(encoding='unicode')` 返回的 Unicode 字符串不是字节流，并且它们永远不会包含 XML 声明来指定其编码。这些字符串很可能无法被其他 XML 库解析。

对于常规字节编码，`tostring()` 函数会根据需要自动添加一个声明，反映返回字符串的编码。这使得其他解析器能够正确解析 XML 字节流。请注意，在大多数情况下，使用 UTF-8 编码的 `tostring()` 速度也会显著更快。