# 使用 lxml 的 XPath 和 XSLT

lxml 支持通过 libxml2 和 libxslt 库，以符合标准的方式实现 XPath 1.0、XSLT 1.0 以及 EXSLT 扩展。

## XPath

lxml.etree 支持 [find](http://effbot.org/zone/element.htm#searching-for-subelements)、[findall](http://effbot.org/zone/element.htm#searching-for-subelements) 和 [findtext](http://effbot.org/zone/element.htm#searching-for-subelements) 方法的简单路径语法，这些方法来自原始的 ElementTree 库 ([ElementPath](http://effbot.org/zone/element-xpath.htm))。作为 lxml 特有的扩展，这些类还提供了一个 xpath() 方法，支持完整的 XPath 语法表达式，并支持 [自定义扩展函数](https://lxml.de/extensions.html#xpath-extension-functions)。

此外，还有一些专门的 XPath 评估类，如 XPath 和 XPathEvaluator，它们在频繁计算时更加高效。具体使用哪种方法，可以参考 [性能对比](https://lxml.de/performance.html#xpath)。

这些类在用于 Elements 和 ElementTrees 时的语义，与上述的 xpath() 方法相同。

> **注意**
>
> .find*() 方法通常比完整的 XPath 支持要 _更快_。这些方法还通过 .iterfind() 方法支持增量树处理，而 XPath 则总是在返回之前收集所有结果。因此，除非需要高度选择性的 XPath 查询，否则建议使用 .find*() 方法，因其在速度和内存方面更加高效。

## xpath() 方法

对于 ElementTree，xpath 方法执行对文档的全局 XPath 查询（如果是绝对路径）或对根节点的查询（如果是相对路径）：

```
f = StringIO('<foo><bar></bar></foo>')
tree = etree.parse(f)

r = tree.xpath('/foo/bar')
len(r)
1
r[0].tag
'bar'

r = tree.xpath('bar')
r[0].tag
'bar'
```

当 xpath() 用于一个 Element 时，XPath 表达式会针对该元素进行求值（如果是相对路径），或者针对根树进行求值（如果是绝对路径）：

```
root = tree.getroot()
r = root.xpath('bar')
r[0].tag
'bar'

bar = root[0]
r = bar.xpath('/foo/bar')
r[0].tag
'bar'

tree = bar.getroottree()
r = tree.xpath('/foo/bar')
r[0].tag
'bar'
```

xpath() 方法支持 XPath 变量：

```
expr = "//*[local-name() = $name]"

print(root.xpath(expr, name = "foo")[0].tag)
foo

print(root.xpath(expr, name = "bar")[0].tag)
bar

print(root.xpath("$text", text = "Hello World!"))
Hello World!
```

## Namespaces and prefixes

If your XPath expression uses namespace prefixes, you must define them in a prefix mapping. To this end, pass a dictionary to the namespaces keyword argument that maps the namespace prefixes used in the XPath expression to namespace URIs:

```
f = StringIO('''\
... <a:foo xmlns:a="http://codespeak.net/ns/test1"
...        xmlns:b="http://codespeak.net/ns/test2">
...    <b:bar>Text</b:bar>
... </a:foo>
... ''')
doc = etree.parse(f)

r = doc.xpath('/x:foo/b:bar',
...               namespaces={'x': 'http://codespeak.net/ns/test1',
...                           'b': 'http://codespeak.net/ns/test2'})
len(r)
1
r[0].tag
'{http://codespeak.net/ns/test2}bar'
r[0].text
'Text'

```

The prefixes you choose here are not linked to the prefixes used inside the XML document. The document may define whatever prefixes it likes, including the empty prefix, without breaking the above code.

Note that XPath does not have a notion of a default namespace. The empty prefix is therefore undefined for XPath and cannot be used in namespace prefix mappings.

There is also an optional extensions argument which is used to define [custom extension functions](https://lxml.de/extensions.html#xpath-extension-functions) in Python that are local to this evaluation. The namespace prefixes that they use in the XPath expression must also be defined in the namespace prefix mapping.

## XPath return values

The return value types of XPath evaluations vary, depending on the XPath expression used:

-   True or False, when the XPath expression has a boolean result
-   a float, when the XPath expression has a numeric result (integer or float)
-   a 'smart' string (as described below), when the XPath expression has a string result.
-   a list of items, when the XPath expression has a list as result. The items may include Elements (also comments and processing instructions), strings and tuples. Text nodes and attributes in the result are returned as 'smart' string values. Namespace declarations are returned as tuples of strings: (prefix, URI).

XPath string results are 'smart' in that they provide a getparent() method that knows their origin:

-   for attribute values, result.getparent() returns the Element that carries them. An example is //foo/@attribute, where the parent would be a foo Element.
-   for the text() function (as in //text()), it returns the Element that contains the text or tail that was returned.

You can distinguish between different text origins with the boolean properties is\_text, is\_tail and is\_attribute.

Note that getparent() may not always return an Element. For example, the XPath functions string() and concat() will construct strings that do not have an origin. For them, getparent() will return None.

There are certain cases where the smart string behaviour is undesirable. For example, it means that the tree will be kept alive by the string, which may have a considerable memory impact in the case that the string value is the only thing in the tree that is actually of interest. For these cases, you can deactivate the parental relationship using the keyword argument smart\_strings.

```
root = etree.XML("<root><a>TEXT</a></root>")

find_text = etree.XPath("//text()")
text = find_text(root)[0]
print(text)
TEXT
print(text.getparent().text)
TEXT

find_text = etree.XPath("//text()", smart_strings=False)
text = find_text(root)[0]
print(text)
TEXT
hasattr(text, 'getparent')
False

```

## Generating XPath expressions

ElementTree objects have a method getpath(element), which returns a structural, absolute XPath expression to find that element:

```
a  = etree.Element("a")
b  = etree.SubElement(a, "b")
c  = etree.SubElement(a, "c")
d1 = etree.SubElement(c, "d")
d2 = etree.SubElement(c, "d")

tree = etree.ElementTree(c)
print(tree.getpath(d2))
/c/d[2]
tree.xpath(tree.getpath(d2)) == [d2]
True

```

## The XPath class

The XPath class compiles an XPath expression into a callable function:

```
root = etree.XML("<root><a><b/></a><b/></root>")

find = etree.XPath("//b")
print(find(root)[0].tag)
b

```

The compilation takes as much time as in the xpath() method, but it is done only once per class instantiation. This makes it especially efficient for repeated evaluation of the same XPath expression.

Just like the xpath() method, the XPath class supports XPath variables:

```
count_elements = etree.XPath("count(//*[local-name() = $name])")

print(count_elements(root, name = "a"))
1.0
print(count_elements(root, name = "b"))
2.0

```

This supports very efficient evaluation of modified versions of an XPath expression, as compilation is still only required once.

Prefix-to-namespace mappings can be passed as second parameter:

```
root = etree.XML("<root xmlns='NS'><a><b/></a><b/></root>")

find = etree.XPath("//n:b", namespaces={'n':'NS'})
print(find(root)[0].tag)
{NS}b

```

## Regular expressions in XPath

By default, XPath supports regular expressions in the [EXSLT](https://exslt.github.io/) namespace:

```
regexpNS = "http://exslt.org/regular-expressions"
find = etree.XPath("//*[re:test(., '^abc$', 'i')]",
...                    namespaces={'re':regexpNS})

root = etree.XML("<root><a>aB</a><b>aBc</b></root>")
print(find(root)[0].text)
aBc

```

You can disable this with the boolean keyword argument regexp which defaults to True.

## The XPathEvaluator classes

lxml.etree provides two other efficient XPath evaluators that work on ElementTrees or Elements respectively: XPathDocumentEvaluator and XPathElementEvaluator. They are automatically selected if you use the XPathEvaluator helper for instantiation:

```
root = etree.XML("<root><a><b/></a><b/></root>")
xpatheval = etree.XPathEvaluator(root)

print(isinstance(xpatheval, etree.XPathElementEvaluator))
True

print(xpatheval("//b")[0].tag)
b

```

This class provides efficient support for evaluating different XPath expressions on the same Element or ElementTree.

## ETXPath

ElementTree supports a language named [ElementPath](http://effbot.org/zone/element-xpath.htm) in its find\*() methods. One of the main differences between XPath and ElementPath is that the XPath language requires an indirection through prefixes for namespace support, whereas ElementTree uses the Clark notation ({ns}name) to avoid prefixes completely. The other major difference regards the capabilities of both path languages. Where XPath supports various sophisticated ways of restricting the result set through functions and boolean expressions, ElementPath only supports pure path traversal without nesting or further conditions. So, while the ElementPath syntax is self-contained and therefore easier to write and handle, XPath is much more powerful and expressive.

lxml.etree bridges this gap through the class ETXPath, which accepts XPath expressions with namespaces in Clark notation. It is identical to the XPath class, except for the namespace notation. Normally, you would write:

```
root = etree.XML("<root xmlns='ns'><a><b/></a><b/></root>")

find = etree.XPath("//p:b", namespaces={'p' : 'ns'})
print(find(root)[0].tag)
{ns}b

```

ETXPath allows you to change this to:

```
find = etree.ETXPath("//{ns}b")
print(find(root)[0].tag)
{ns}b

```

## Error handling

lxml.etree raises exceptions when errors occur while parsing or evaluating an XPath expression:

```
find = etree.XPath("\\")
Traceback (most recent call last):
  ...
lxml.etree.XPathSyntaxError: Invalid expression

```

lxml will also try to give you a hint what went wrong, so if you pass a more complex expression, you may get a somewhat more specific error:

```
find = etree.XPath("//*[1.1.1]")
Traceback (most recent call last):
  ...
lxml.etree.XPathSyntaxError: Invalid predicate

```

During evaluation, lxml will emit an XPathEvalError on errors:

```
find = etree.XPath("//ns:a")
find(root)
Traceback (most recent call last):
  ...
lxml.etree.XPathEvalError: Undefined namespace prefix

```

This works for the XPath class, however, the other evaluators (including the xpath() method) are one-shot operations that do parsing and evaluation in one step. They therefore raise evaluation exceptions in all cases:

```
root = etree.Element("test")
find = root.xpath("//*[1.1.1]")
Traceback (most recent call last):
  ...
lxml.etree.XPathEvalError: Invalid predicate

find = root.xpath("//ns:a")
Traceback (most recent call last):
  ...
lxml.etree.XPathEvalError: Undefined namespace prefix

find = root.xpath("\\")
Traceback (most recent call last):
  ...
lxml.etree.XPathEvalError: Invalid expression

```

Note that lxml versions before 1.3 always raised an XPathSyntaxError for all errors, including evaluation errors. The best way to support older versions is to except on the superclass XPathError.

## XSLT

lxml.etree introduces a new class, lxml.etree.XSLT. The class can be given an ElementTree or Element object to construct an XSLT transformer:

```
xslt_root = etree.XML('''\
... <xsl:stylesheet version="1.0"
...     xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
...     <xsl:template match="/">
...         <foo><xsl:value-of select="/a/b/text()" /></foo>
...     </xsl:template>
... </xsl:stylesheet>''')
transform = etree.XSLT(xslt_root)

```

You can then run the transformation on an ElementTree document by simply calling it, and this results in another ElementTree object:

```
f = StringIO('<a><b>Text</b></a>')
doc = etree.parse(f)
result_tree = transform(doc)

```

By default, XSLT supports all extension functions from libxslt and libexslt as well as Python regular expressions through the [EXSLT regexp functions](https://exslt.github.io/regexp/). Also see the documentation on [custom extension functions](https://lxml.de/extensions.html#xpath-extension-functions), [XSLT extension elements](https://lxml.de/extensions.html#xslt-extension-elements) and [document resolvers](https://lxml.de/resolvers.html). There is a separate section on [controlling access](https://lxml.de/resolvers.html#i-o-access-control-in-xslt) to external documents and resources.

Note

Due to a bug in libxslt the usage of <xsl:strip-space elements="\*"/> in an XSLT stylesheet can lead to crashes or memory failures. It is therefore advised not to use xsl:strip-space in stylesheets used with lxml.

For details see: [https://gitlab.gnome.org/GNOME/libxslt/-/issues/14](https://gitlab.gnome.org/GNOME/libxslt/-/issues/14)

## XSLT result objects

The result of an XSL transformation can be accessed like a normal ElementTree document:

```
root = etree.XML('<a><b>Text</b></a>')
result = transform(root)

result.getroot().text
'Text'

```

but, as opposed to normal ElementTree objects, can also be turned into an (XML or text) string by applying the bytes() function (str() in Python 2):

```
bytes(result)
b'<?xml version="1.0"?>\n<foo>Text</foo>\n'

```

The result is always a plain string, encoded as requested by the xsl:output element in the stylesheet. If you want a Python Unicode/Text string instead, you should set this encoding to UTF-8 (unless the ASCII default is sufficient). This allows you to call the builtin str() function on the result (unicode() in Python 2):

```
str(result)
'<?xml version="1.0"?>\n<foo>Text</foo>\n'

```

You can use other encodings at the cost of multiple recoding. Encodings that are not supported by Python will result in an error:

```
xslt_tree = etree.XML('''\
... <xsl:stylesheet version="1.0"
...     xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
...     <xsl:output encoding="UCS4"/>
...     <xsl:template match="/">
...         <foo><xsl:value-of select="/a/b/text()" /></foo>
...     </xsl:template>
... </xsl:stylesheet>''')
transform = etree.XSLT(xslt_tree)

result = transform(doc)
str(result)
Traceback (most recent call last):
  ...
LookupError: unknown encoding: UCS4

```

While it is possible to use the .write() method (known from ElementTree objects) to serialise the XSLT result into a file, it is better to use the .write\_output() method. The latter knows about the <xsl:output> tag and writes the expected data into the output file.

```
xslt_root = etree.XML('''\
... <xsl:stylesheet version="1.0"
...     xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
...     <xsl:output method="text" encoding="utf8" />
...     <xsl:template match="/">
...         <foo><xsl:value-of select="/a/b/text()" /></foo>
...     </xsl:template>
... </xsl:stylesheet>''')
transform = etree.XSLT(xslt_root)

result = transform(doc)
result.write_output("output.txt.gz", compression=9)    # doctest: +SKIP

```

> ```
> from io import BytesIO
> out = BytesIO()
> result.write_output(out)
> data = out.getvalue()
> b'Text' in data
> True
> 
> ```

## Stylesheet parameters

It is possible to pass parameters, in the form of XPath expressions, to the XSLT template:

```
xslt_tree = etree.XML('''\
... <xsl:stylesheet version="1.0"
...     xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
...     <xsl:param name="a" />
...     <xsl:template match="/">
...         <foo><xsl:value-of select="$a" /></foo>
...     </xsl:template>
... </xsl:stylesheet>''')
transform = etree.XSLT(xslt_tree)
doc_root = etree.XML('<a><b>Text</b></a>')

```

The parameters are passed as keyword parameters to the transform call. First, let's try passing in a simple integer expression:

```
result = transform(doc_root, a="5")
bytes(result)
b'<?xml version="1.0"?>\n<foo>5</foo>\n'

```

You can use any valid XPath expression as parameter value:

```
result = transform(doc_root, a="/a/b/text()")
bytes(result)
b'<?xml version="1.0"?>\n<foo>Text</foo>\n'

```

It's also possible to pass an XPath object as a parameter:

```
result = transform(doc_root, a=etree.XPath("/a/b/text()"))
bytes(result)
b'<?xml version="1.0"?>\n<foo>Text</foo>\n'

```

Passing a string expression looks like this:

```
result = transform(doc_root, a="'A'")
bytes(result)
b'<?xml version="1.0"?>\n<foo>A</foo>\n'

```

To pass a string that (potentially) contains quotes, you can use the .strparam() class method. Note that it does not escape the string. Instead, it returns an opaque object that keeps the string value.

```
plain_string_value = etree.XSLT.strparam(
...                          """ It's "Monty Python" """)
result = transform(doc_root, a=plain_string_value)
bytes(result)
b'<?xml version="1.0"?>\n<foo> It\'s "Monty Python" </foo>\n'

```

If you need to pass parameters that are not legal Python identifiers, pass them inside of a dictionary:

```
transform = etree.XSLT(etree.XML('''\
... <xsl:stylesheet version="1.0"
...     xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
...     <xsl:param name="non-python-identifier" />
...     <xsl:template match="/">
...         <foo><xsl:value-of select="$non-python-identifier" /></foo>
...     </xsl:template>
... </xsl:stylesheet>'''))

result = transform(doc_root, **{'non-python-identifier': '5'})
bytes(result)
b'<?xml version="1.0"?>\n<foo>5</foo>\n'

```

## Errors and messages

Like most of the processing oriented objects in lxml.etree, XSLT provides an error log that lists messages and error output from the last run. See the [parser documentation](https://lxml.de/parsing.html#error-log) for a description of the error log.

```
xslt_root = etree.XML('''\
... <xsl:stylesheet version="1.0"
...     xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
...     <xsl:template match="/">
...         <xsl:message terminate="no">STARTING</xsl:message>
...         <foo><xsl:value-of select="/a/b/text()" /></foo>
...         <xsl:message terminate="no">DONE</xsl:message>
...     </xsl:template>
... </xsl:stylesheet>''')
transform = etree.XSLT(xslt_root)

doc_root = etree.XML('<a><b>Text</b></a>')
result = transform(doc_root)
bytes(result)
b'<?xml version="1.0"?>\n<foo>Text</foo>\n'

print(transform.error_log)
<string>:0:0:ERROR:XSLT:ERR_OK: STARTING
<string>:0:0:ERROR:XSLT:ERR_OK: DONE

for entry in transform.error_log:
...     print('message from line %s, col %s: %s' % (
...                entry.line, entry.column, entry.message))
...     print('domain: %s (%d)' % (entry.domain_name, entry.domain))
...     print('type: %s (%d)' % (entry.type_name, entry.type))
...     print('level: %s (%d)' % (entry.level_name, entry.level))
...     print('filename: %s' % entry.filename)
message from line 0, col 0: STARTING
domain: XSLT (22)
type: ERR_OK (0)
level: ERROR (2)
filename: <string>
message from line 0, col 0: DONE
domain: XSLT (22)
type: ERR_OK (0)
level: ERROR (2)
filename: <string>

```

Note that there is no way in XSLT to distinguish between user messages, warnings and error messages that occurred during the run. libxslt simply does not provide this information. You can partly work around this limitation by making your own messages uniquely identifiable, e.g. with a common text prefix.

## The xslt() tree method

There's also a convenience method on ElementTree objects for doing XSL transformations. This is less efficient if you want to apply the same XSL transformation to multiple documents, but is shorter to write for one-shot operations, as you do not have to instantiate a stylesheet yourself:

```
result = doc.xslt(xslt_tree, a="'A'")
bytes(result)
b'<?xml version="1.0"?>\n<foo>A</foo>\n'

```

This is a shortcut for the following code:

```
transform = etree.XSLT(xslt_tree)
result = transform(doc, a="'A'")
bytes(result)
b'<?xml version="1.0"?>\n<foo>A</foo>\n'

```

## Dealing with stylesheet complexity

Some applications require a larger set of rather diverse stylesheets. lxml.etree allows you to deal with this in a number of ways. Here are some ideas to try.

The most simple way to reduce the diversity is by using XSLT parameters that you pass at call time to configure the stylesheets. The partial() function in the functools module may come in handy here. It allows you to bind a set of keyword arguments (i.e. stylesheet parameters) to a reference of a callable stylesheet. The same works for instances of the XPath() evaluator, obviously.

You may also consider creating stylesheets programmatically. Just create an XSL tree, e.g. from a parsed template, and then add or replace parts as you see fit. Passing an XSL tree into the XSLT() constructor multiple times will create independent stylesheets, so later modifications of the tree will not be reflected in the already created stylesheets. This makes stylesheet generation very straight forward.

A third thing to remember is the support for [custom extension functions](https://lxml.de/extensions.html#xpath-extension-functions) and [XSLT extension elements](https://lxml.de/extensions.html#xslt-extension-elements). Some things are much easier to express in XSLT than in Python, while for others it is the complete opposite. Finding the right mixture of Python code and XSL code can help a great deal in keeping applications well designed and maintainable.

## Profiling

If you want to know how your stylesheet performed, pass the profile\_run keyword to the transform:

```
result = transform(doc, a="/a/b/text()", profile_run=True)
profile = result.xslt_profile

```

The value of the xslt\_profile property is an ElementTree with profiling data about each template, similar to the following:

```
<profile>
  <template rank="1" match="/" name="" mode="" calls="1" time="1" average="1"/>
</profile>

```

Note that this is a read-only document. You must not move any of its elements to other documents. Please deep-copy the document if you need to modify it. If you want to free it from memory, just do:

```
del result.xslt_profile

```