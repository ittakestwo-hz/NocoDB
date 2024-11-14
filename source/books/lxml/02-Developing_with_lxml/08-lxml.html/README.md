# lxml.html

从版本 2.0 开始，lxml 提供了一个专门处理 HTML 的 Python 包：`lxml.html`。它基于 lxml 的 HTML 解析器，并为 HTML 元素提供了特殊的 Element API，以及一些用于常见 HTML 处理任务的工具。

该包的主要 API 基于 [lxml.etree](https://lxml.de/tutorial.html) API，从而也基于 [ElementTree](http://effbot.org/zone/element-index.htm) API。

## 解析 HTML

### 解析 HTML 片段

有几种可用的函数用于解析 HTML：

- **parse(filename_url_or_file)**：
  - 解析指定的文件或 URL，或者如果对象具有 `.read()` 方法，则从该对象中解析。
  - 如果提供了一个 URL，或者对象具有 `.geturl()` 方法（如从 `urllib.urlopen()` 返回的文件类对象），则该 URL 会用作基础 URL。也可以通过 `base_url` 关键字参数提供明确的基础 URL。
- **document_fromstring(string)**：
  - 从给定字符串解析文档。这将始终创建一个正确的 HTML 文档，其中父节点为 `<html>`，并包含 `<body>`，可能还包含 `<head>`。
- **fragment_fromstring(string, create_parent=False)**：
  - 从字符串返回一个 HTML 片段。片段必须只包含一个元素，除非指定 `create_parent`；例如，`fragment_fromstring(string, create_parent='div')` 会将该元素包裹在一个 `<div>` 中。
- **fragments_fromstring(string)**：
  - 返回片段中找到的元素列表。
- **fromstring(string)**
  - 根据字符串内容是完整文档还是片段，返回 `document_fromstring` 或 `fragment_fromstring`。

## 解析严重损坏的页面

通常的 HTML 解析器能够处理损坏的 HTML 页面，但对于格式极其混乱的页面（俗称“tag soup”），可能仍无法有效解析。处理这种情况的一个方法是使用 [ElementSoup](https://lxml.de/elementsoup.html)，它利用知名的 [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) 解析器来构建 lxml 的 HTML 树。

需要注意的是，网页最常见的问题是缺少或错误的编码声明。因此，通常只需使用 BeautifulSoup 的编码检测工具 UnicodeDammit，其他部分则交由 lxml 的 HTML 解析器处理，因为 lxml 的解析速度比 BeautifulSoup 快很多倍。

## HTML Element 方法

HTML 元素具备 ElementTree 所有的方法，并且包含一些额外方法：

- `.drop_tree()`：删除该元素及其所有子元素。与 `el.getparent().remove(el)` 不同，此方法不会删除尾部文本；`drop_tree` 会将尾部文本合并到前一个元素中。
- `.drop_tag()`：删除标签，但保留其子元素和文本。
- `.find_class(class_name)`：返回具有指定 CSS 类名的所有元素列表。请注意，HTML 中类名是用空格分隔的，因此 `doc.find_class('highlight')` 会找到类似 `<div class="sidebar highlight">` 的元素。类名是区分大小写的。
- `.find_rel_links(rel)`：返回所有 `<a rel="{rel}">` 元素的列表。例如，`doc.find_rel_links('tag')` 会返回所有标记为标签的链接（参考 [microformats](http://microformats.org/wiki/rel-tag) 的 `rel-tag`）。
- `.get_element_by_id(id, default=None)`：返回具有指定 id 的元素，若找不到则返回默认值。如果有多个元素拥有相同的 id（不推荐，但常见），只返回第一个。
- `.text_content()`：返回元素及其子元素的文本内容，不包含任何标记。
- `.cssselect(expr)`：使用 CSS 选择器表达式，从该元素及其子元素中选择匹配的元素。（与所有 lxml 元素一样，也可以使用 `.xpath(expr)` 方法。）
- `.label`：返回该元素对应的 `<label>` 元素（若存在则返回，没有则返回 None）。`label` 元素有一个 `label.for_element` 属性，指向关联的元素。
- `.base_url`：返回解析过程中保存的基础 URL。如果没有保存基础 URL，则为 None。此属性不可手动设置。
- `.classes`：返回一个类似集合的对象，可以访问和修改元素的 `class` 属性中的名称。（lxml 3.5 新增功能）
- `.set(key, value=None)`：设置 HTML 属性。如果未提供值或值为 None，则创建布尔属性，例如 `<form novalidate></form>` 或 `<div custom-attribute></div>`。在 XML 中，属性必须至少设置为空字符串，如 `<form novalidate=""></form>`，而在 HTML 中，布尔属性可以没有值，仅需存在或缺失。

## 运行 HTML doctests

lxml.html 包中一个有趣的模块处理 doctests。比较两个 HTML 页面是否相等比较困难，因为空白差异没有实际意义，结构格式也可能不同。这在 doctests 中更成问题，输出被用于相等测试，少量的空白或属性顺序差异可能导致测试失败。由于基于标签的语言通常很冗长，查找 doctest 输出中的实际差异可能需要更多时间。

幸运的是，lxml 提供了 `lxml.doctestcompare` 模块，支持 XML 和 HTML 页面之间的宽松比较，并在测试失败时提供可读的差异对比。通过在 doctest 中导入 `usedoctest` 模块，可以更方便地使用 HTML 比较功能：

```
>>> import lxml.html.usedoctest
```

现在，如果你有一个 HTML 文档，想在 doctest 中将它与预期的结果文档进行比较，可以这样做：

```
>>> import lxml.html
>>> html = lxml.html.fromstring('''\
...    <html><body onload="" color="white">
...      <p>Hi  !</p>
...    </body></html>
... ''')

>>> print lxml.html.tostring(html)
<html><body onload="" color="white"><p>Hi !</p></body></html>

>>> print lxml.html.tostring(html)
<html> <body color="white" onload=""> <p>Hi    !</p> </body> </html>

>>> print lxml.html.tostring(html)
<html>
  <body color="white" onload="">
    <p>Hi !</p>
  </body>
</html>
```

在文档中，通常会偏好美化的 HTML 输出，因为它更易读。不过，从 HTML 工具的角度看，这三个文档是等效的，因此 doctest 会默默接受任一形式。这允许在 doctest 中专注于可读性，即便真实输出是一行难看的 HTML 代码。

另外，还可以导入 `lxml.usedoctest` 模块用于 XML 比较。HTML 解析器忽略命名空间和某些 XML 特性。

## 使用 E-factory 创建 HTML

lxml.html 提供了一个为 [E-factory](http://online.effbot.org/2006_11_01_archive.htm#et-builder) 预定义的 HTML 词汇表，最初由 Fredrik Lundh 编写。这可以让你快速生成 HTML 页面和片段：

```
>>> from lxml.html import builder as E
>>> from lxml.html import usedoctest
>>> html = E.HTML(
...   E.HEAD(
...     E.LINK(rel="stylesheet", href="great.css", type="text/css"),
...     E.TITLE("Best Page Ever")
...   ),
...   E.BODY(
...     E.H1(E.CLASS("heading"), "Top News"),
...     E.P("World News only on this page", style="font-size: 200%"),
...     "Ah, and here's some more text, by the way.",
...     lxml.html.fromstring("<p>... and this is a parsed fragment ...</p>")
...   )
... )

>>> print lxml.html.tostring(html)
<html>
  <head>
    <link href="great.css" rel="stylesheet" type="text/css">
    <title>Best Page Ever</title>
  </head>
  <body>
    <h1 class="heading">Top News</h1>
    <p style="font-size: 200%">World News only on this page</p>
    Ah, and here's some more text, by the way.
    <p>... and this is a parsed fragment ...</p>
  </body>
</html>
```

注意，应该使用 `lxml.html.tostring` 而**不要**使用 `lxml.tostring`。`lxml.tostring(doc)` 会返回文档的 XML 表示形式，这不符合 HTML 规范。例如，`<script src="..."></script>` 会被序列化为 `<script src="..." />`，这会让浏览器困惑。

## 查看 HTML

查看 HTML 的便捷方法：`lxml.html.open_in_browser(lxml_doc)` 会将文档写入磁盘并在浏览器中打开（使用 [webbrowser 模块](http://python.org/doc/current/lib/module-webbrowser.html)）。

## 操作链接

有几种方法可以在元素上查看和修改文档中的链接。

`.iterlinks()`：

对于文档中的每个链接，生成 `(element, attribute, link, pos)`。如果链接在文本中（例如 `<style>` 标签中的 `@import`），`attribute` 可能为 `None`。

此方法会在 `action`、`archive`、`background`、`cite`、`classid`、`codebase`、`data`、`href`、`longdesc`、`profile`、`src`、`usemap`、`dynsrc` 或 `lowsrc` 属性中查找链接。同时也会在样式属性中查找 `url(link)`，以及 `<style>` 标签中的 `@import` 和 `url()`。

此函数不会关注 `<base href>`。

`.resolve_base_href()`：

如果文档包含 `<base href>` 标签，该函数将会修改文档以考虑到这个标签，并在过程中移除此标签。

`.make_links_absolute(base_href, resolve_base_href=True)`：

此方法将文档中的所有链接转换为绝对链接，假设 `base_href` 是文档的 URL。如果 `base_href="http://localhost/foo/bar.html"`，并且有一个指向 `baz.html` 的链接，那么它将被重写为 `http://localhost/foo/baz.html`。

如果 `resolve_base_href` 为 `true`，则会考虑 `<base href>` 标签（相当于调用 `self.resolve_base_href()`）。

`.rewrite_links(link_repl_func, resolve_base_href=True, base_href=None)`：

此方法使用给定的链接替换函数重写文档中的所有链接。如果提供 `base_href` 值，所有链接在加入该 URL 后会被传入。

对于每个链接，`link_repl_func(link)` 会被调用。该函数返回新的链接，或者返回 `None` 来移除包含该链接的属性或标签。请注意，所有链接都会传递，包括像 `#anchor`（纯内部链接）以及类似 "mailto:bob@example.com"（或 `javascript:...`）这样的链接。

如果你希望访问链接的上下文，应该使用 `.iterlinks()`。

## 函数

除了这些方法之外，还有对应的函数：

- `iterlinks(html)`
- `make_links_absolute(html, base_href, ...)`
- `rewrite_links(html, link_repl_func, ...)`
- `resolve_base_href(html)`

这些函数会解析 HTML（如果它是字符串），然后返回新的 HTML 字符串。如果传入的是一个文档，该文档会被复制（`iterlinks()` 除外），执行相应方法后返回新的文档。

## 表单

文档中的任何 `<form>` 元素可以通过列表 `doc.forms` 访问（例如，`doc.forms[0]`）。`form`、`input`、`select` 和 `textarea` 元素都有特殊的方法。

输入元素（包括 `<select>` 和 `<textarea>`）具有以下属性：

- `.name`：元素的名称。
- `.value`：输入元素的值，`textarea` 的内容，`select` 的选中项。该属性是可设置的。

对于多选的 `<select>` 元素（`<select multiple>`），此属性是选中的选项集合；你可以添加或移除项来选择或取消选择选项。

`select` 元素的属性：

- `.value_options`：对于 `select` 元素，这是所有可选值（所有选项的值）。
- `.multiple`：对于 `select` 元素，如果这是一个 `<select multiple>` 元素，则返回 `True`。

输入元素的属性：

- `.type`：`<input>` 元素的 `type` 属性。
- `.checkable`：如果可以被选中（即对于 `type=radio` 和 `type=checkbox`，返回 `True`）。
- `.checked`：如果该元素是可选中的，返回其选中状态。如果是不可选中的输入，会引发 `AttributeError`。

表单本身具有以下属性：

- `.inputs`：一个类似字典的对象，可通过名称访问输入元素。当有多个具有相同名称的输入元素时，返回类似列表的结构，且可以将选项和值作为一组进行访问。
- `.fields`：一个类似字典的对象，用于按名称访问值。`form.inputs` 返回元素，而该属性仅返回值。在此字典中设置值会影响表单的输入。基本上，`form.fields[x]` 等价于 `form.inputs[x].value`，`form.fields[x] = y` 等价于 `form.inputs[x].value = y`。（请注意，有时 `form.inputs[x]` 返回的是复合对象，但这些对象也有 `.value` 属性。）

如果设置该属性，相当于执行 `form.fields.clear(); form.fields.update(new_value)`。

- `.form_values()`：返回一个列表 `[(name, value), ...]`，适合传递给 `urllib.urlencode()` 用于表单提交。
- `.action`：`action` 属性。如果可能，它会被解析为绝对 URL。
- `.method`：`method` 属性，默认为 `GET`。

## 表单填写示例

请注意，您可以更改这些属性（如值、方法、操作等），然后将表单序列化，以查看更新后的值。例如，您可以执行以下操作：

```
>>> from lxml.html import fromstring, tostring
>>> form_page = fromstring('''<html><body><form>
...   Your name: <input type="text" name="name"> <br>
...   Your phone: <input type="text" name="phone"> <br>
...   Your favorite pets: <br>
...   Dogs: <input type="checkbox" name="interest" value="dogs"> <br>
...   Cats: <input type="checkbox" name="interest" value="cats"> <br>
...   Llamas: <input type="checkbox" name="interest" value="llamas"> <br>
...   <input type="submit"></form></body></html>''')
>>> form = form_page.forms[0]
>>> form.fields = dict(
...     name='John Smith',
...     phone='555-555-3949',
...     interest=set(['cats', 'llamas']))
>>> print(tostring(form))
<html>
  <body>
    <form>
    Your name:
      <input name="name" type="text" value="John Smith">
      <br>Your phone:
      <input name="phone" type="text" value="555-555-3949">
      <br>Your favorite pets:
      <br>Dogs:
      <input name="interest" type="checkbox" value="dogs">
      <br>Cats:
      <input checked name="interest" type="checkbox" value="cats">
      <br>Llamas:
      <input checked name="interest" type="checkbox" value="llamas">
      <br>
      <input type="submit">
    </form>
  </body>
</html>

```

## 表单提交

您可以使用 `lxml.html.submit_form(form_element)` 提交表单。此操作将返回一个类似文件的对象（即 `urllib.urlopen()` 的结果）。

如果您想传递额外的输入值，可以使用关键字参数 `extra_values`，例如 `extra_values={'submit': 'Yes!'}`。这是唯一可以将提交值添加到表单中的方法，因为这些元素没有“已提交”状态。

您还可以通过 `open_http` 关键字参数传递一个替代的 opener，这个 opener 是一个函数，签名为 `open_http(method, url, values)`。

示例：

```
>>> from lxml.html import parse, submit_form
>>> page = parse('http://tinyurl.com').getroot()
>>> page.forms[0].fields['url'] = 'http://lxml.de/'
>>> result = parse(submit_form(page.forms[0])).getroot()

>>> [a.attrib['href'] for a in result.xpath("//a[@target='_blank']")]
['http://tinyurl.com/2xae8s', 'http://preview.tinyurl.com/2xae8s']

```

## HTML 差异

`lxml.html.diff` 模块提供了几种可视化 HTML 文档差异的方法。这些差异是面向 _内容_ 的。也就是说，标记中的变化大多被忽略；只有内容本身的变化才会被突出显示。

有两种查看差异的方法：`htmldiff` 和 `html_annotate`。其中一种使用 `<ins>` 和 `<del>` 标记显示差异，另一种则类似于 svn blame，对一组更改进行注解。两个函数都操作文本，最好用于内容片段（仅 `<body>` 内的内容），而不是完整文档。

`htmldiff` 示例：

```
>>> from lxml.html.diff import htmldiff, html_annotate
>>> doc1 = '''<p>Here is some text.</p>'''
>>> doc2 = '''<p>Here is <b>a lot</b> of <i>text</i>.</p>'''
>>> doc3 = '''<p>Here is <b>a little</b> <i>text</i>.</p>'''
>>> print htmldiff(doc1, doc2)
<p>Here is <ins><b>a lot</b> of <i>text</i>.</ins> <del>some text.</del> </p>
>>> print html_annotate([(doc1, 'author1'), (doc2, 'author2'),
...                      (doc3, 'author3')])
<p><span title="author1">Here is</span>
   <b><span title="author2">a</span>
   <span title="author3">little</span></b>
   <i><span title="author2">text</span></i>
   <span title="author2">.</span></p>

```

正如你所看到的，它并不完美，像这类东西通常都是如此。在较大文本块和较大编辑的情况下，它通常会表现得更好。

`html_annotate` 函数还可以接受一个可选的第二个参数 `markup`。这是一个像 `markup(text, version)` 的函数，它返回给定文本并使用给定版本进行标记。默认版本的输出如下所示：

```
def default_markup(text, version):
    return '<span title="%s">%s</span>' % (
        cgi.escape(unicode(version), 1), text)

```

## 示例

## 微格式示例

这个例子解析了 [hCard](http://microformats.org/wiki/hcard) 微格式。

首先获取页面：

```
>>> import urllib
>>> from lxml.html import fromstring
>>> url = 'http://microformats.org/'
>>> content = urllib.urlopen(url).read()
>>> doc = fromstring(content)
>>> doc.make_links_absolute(url)

```

然后我们创建一些对象来存放信息：

```
>>> class Card(object):
...     def __init__(self, **kw):
...         for name, value in kw:
...             setattr(self, name, value)
>>> class Phone(object):
...     def __init__(self, phone, types=()):
...         self.phone, self.types = phone, types

```

一些用于微格式的常用函数：

```
>>> def get_text(el, class_name):
...     els = el.find_class(class_name)
...     if els:
...         return els[0].text_content()
...     else:
...         return ''
>>> def get_value(el):
...     return get_text(el, 'value') or el.text_content()
>>> def get_all_texts(el, class_name):
...     return [e.text_content() for e in els.find_class(class_name)]
>>> def parse_addresses(el):
...     # 理想情况下，这应该解析街道等
...     return el.find_class('adr')

```

然后进行解析：

```
>>> for el in doc.find_class('hcard'):
...     card = Card()
...     card.el = el
...     card.fn = get_text(el, 'fn')
...     card.tels = []
...     for tel_el in card.find_class('tel'):
...         card.tels.append(Phone(get_value(tel_el),
...                                get_all_texts(tel_el, 'type')))
...     card.addresses = parse_addresses(el)

```