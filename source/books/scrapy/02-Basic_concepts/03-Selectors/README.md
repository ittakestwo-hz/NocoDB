# 选择器

当你在爬取网页时，最常见的任务是从 HTML 源代码中提取数据。为此，提供了几个库，常见的有：

- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) 是 Python 程序员中非常流行的一个网页爬取库，它根据 HTML 代码的结构构建一个 Python 对象，并且能够合理地处理格式不规范的标记，但它有一个缺点：速度较慢。
- [lxml](https://lxml.de/) 是一个 XML 解析库（也可以解析 HTML），它基于 [`ElementTree`](https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree "(in Python v3.13)") 提供了一个符合 Python 风格的 API。（lxml 不是 Python 标准库的一部分。）

Scrapy 提供了自己的数据提取机制。这些机制被称为选择器，因为它们通过 [XPath](https://www.w3.org/TR/xpath/all/) 或 [CSS](https://www.w3.org/TR/selectors) 表达式“选择” HTML 文档中的特定部分。

[XPath](https://www.w3.org/TR/xpath/all/) 是一种用于选择 XML 文档中节点的语言，也可以与 HTML 一起使用。[CSS](https://www.w3.org/TR/selectors) 是一种用于对 HTML 文档应用样式的语言，它定义了选择器，用于将这些样式与特定的 HTML 元素关联。

> **注意**
>
> Scrapy 选择器是对 [parsel](https://parsel.readthedocs.io/en/latest/) 库的一个轻量封装；该封装的目的是提供与 Scrapy Response 对象的更好集成。
>
> [parsel](https://parsel.readthedocs.io/en/latest/) 是一个独立的网页爬取库，可以不依赖 Scrapy 使用。它在底层使用了 [lxml](https://lxml.de/) 库，并在其上实现了一个简单的 API。这意味着 Scrapy 选择器在速度和解析准确性上与 lxml 非常相似。

## 使用选择器[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#using-selectors "此标题的永久链接")

### 构建选择器[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#constructing-selectors "此标题的永久链接")

Response 对象通过 `.selector` 属性暴露了一个 `Selector` 实例：

```
>>> response.selector.xpath("//span/text()").get()
'good'
```

Querying responses using XPath and CSS is so common that responses include two more shortcuts: `response.xpath()` and `response.css()`:

```
>>> response.xpath("//span/text()").get()
'good'
>>> response.css("span::text").get()
'good'

```

Scrapy selectors are instances of `Selector` class constructed by passing either [`TextResponse`](https://docs.scrapy.org/en/latest/topics/request-response.html#scrapy.http.TextResponse "scrapy.http.TextResponse") object or markup as a string (in `text` argument).

Usually there is no need to construct Scrapy selectors manually: `response` object is available in Spider callbacks, so in most cases it is more convenient to use `response.css()` and `response.xpath()` shortcuts. By using `response.selector` or one of these shortcuts you can also ensure the response body is parsed only once.

But if required, it is possible to use `Selector` directly. Constructing from text:

```
>>> from scrapy.selector import Selector
>>> body = "<html><body><span>good</span></body></html>"
>>> Selector(text=body).xpath("//span/text()").get()
'good'

```

Constructing from response - [`HtmlResponse`](https://docs.scrapy.org/en/latest/topics/request-response.html#scrapy.http.HtmlResponse "scrapy.http.HtmlResponse") is one of [`TextResponse`](https://docs.scrapy.org/en/latest/topics/request-response.html#scrapy.http.TextResponse "scrapy.http.TextResponse") subclasses:

```
>>> from scrapy.selector import Selector
>>> from scrapy.http import HtmlResponse
>>> response = HtmlResponse(url="http://example.com", body=body, encoding="utf-8")
>>> Selector(response=response).xpath("//span/text()").get()
'good'

```

`Selector` automatically chooses the best parsing rules (XML vs HTML) based on input type.

### Using selectors[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#id1 "Permalink to this heading")

To explain how to use the selectors we’ll use the `Scrapy shell` (which provides interactive testing) and an example page located in the Scrapy documentation server:

For the sake of completeness, here’s its full HTML code:

```
<!DOCTYPE html>

<html>
  <head>
    <base href='http://example.com/' />
    <title>Example website</title>
  </head>
  <body>
    <div id='images'>
      <a href='image1.html'>Name: My image 1 <br /><img src='image1_thumb.jpg' alt='image1'/></a>
      <a href='image2.html'>Name: My image 2 <br /><img src='image2_thumb.jpg' alt='image2'/></a>
      <a href='image3.html'>Name: My image 3 <br /><img src='image3_thumb.jpg' alt='image3'/></a>
      <a href='image4.html'>Name: My image 4 <br /><img src='image4_thumb.jpg' alt='image4'/></a>
      <a href='image5.html'>Name: My image 5 <br /><img src='image5_thumb.jpg' alt='image5'/></a>
    </div>
  </body>
</html>

```

First, let’s open the shell:

```
scrapy shell https://docs.scrapy.org/en/latest/_static/selectors-sample1.html

```

Then, after the shell loads, you’ll have the response available as `response` shell variable, and its attached selector in `response.selector` attribute.

Since we’re dealing with HTML, the selector will automatically use an HTML parser.

So, by looking at the [HTML code](https://docs.scrapy.org/en/latest/topics/selectors.html#topics-selectors-htmlcode) of that page, let’s construct an XPath for selecting the text inside the title tag:

```
>>> response.xpath("//title/text()")
[<Selector query='//title/text()' data='Example website'>]

```

To actually extract the textual data, you must call the selector `.get()` or `.getall()` methods, as follows:

```
>>> response.xpath("//title/text()").getall()
['Example website']
>>> response.xpath("//title/text()").get()
'Example website'

```

`.get()` always returns a single result; if there are several matches, content of a first match is returned; if there are no matches, None is returned. `.getall()` returns a list with all results.

Notice that CSS selectors can select text or attribute nodes using CSS3 pseudo-elements:

```
>>> response.css("title::text").get()
'Example website'

```

As you can see, `.xpath()` and `.css()` methods return a [`SelectorList`](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.SelectorList "scrapy.selector.SelectorList") instance, which is a list of new selectors. This API can be used for quickly selecting nested data:

```
>>> response.css("img").xpath("@src").getall()
['image1_thumb.jpg',
'image2_thumb.jpg',
'image3_thumb.jpg',
'image4_thumb.jpg',
'image5_thumb.jpg']

```

If you want to extract only the first matched element, you can call the selector `.get()` (or its alias `.extract_first()` commonly used in previous Scrapy versions):

```
>>> response.xpath('//div[@id="images"]/a/text()').get()
'Name: My image 1 '

```

It returns `None` if no element was found:

```
>>> response.xpath('//div[@id="not-exists"]/text()').get() is None
True

```

A default return value can be provided as an argument, to be used instead of `None`:

```
>>> response.xpath('//div[@id="not-exists"]/text()').get(default="not-found")
'not-found'

```

Instead of using e.g. `'@src'` XPath it is possible to query for attributes using `.attrib` property of a `Selector`:

```
>>> [img.attrib["src"] for img in response.css("img")]
['image1_thumb.jpg',
'image2_thumb.jpg',
'image3_thumb.jpg',
'image4_thumb.jpg',
'image5_thumb.jpg']

```

As a shortcut, `.attrib` is also available on SelectorList directly; it returns attributes for the first matching element:

```
>>> response.css("img").attrib["src"]
'image1_thumb.jpg'

```

This is most useful when only a single result is expected, e.g. when selecting by id, or selecting unique elements on a web page:

```
>>> response.css("base").attrib["href"]
'http://example.com/'

```

Now we’re going to get the base URL and some image links:

```
>>> response.xpath("//base/@href").get()
'http://example.com/'

>>> response.css("base::attr(href)").get()
'http://example.com/'

>>> response.css("base").attrib["href"]
'http://example.com/'

>>> response.xpath('//a[contains(@href, "image")]/@href').getall()
['image1.html',
'image2.html',
'image3.html',
'image4.html',
'image5.html']

>>> response.css("a[href*=image]::attr(href)").getall()
['image1.html',
'image2.html',
'image3.html',
'image4.html',
'image5.html']

>>> response.xpath('//a[contains(@href, "image")]/img/@src').getall()
['image1_thumb.jpg',
'image2_thumb.jpg',
'image3_thumb.jpg',
'image4_thumb.jpg',
'image5_thumb.jpg']

>>> response.css("a[href*=image] img::attr(src)").getall()
['image1_thumb.jpg',
'image2_thumb.jpg',
'image3_thumb.jpg',
'image4_thumb.jpg',
'image5_thumb.jpg']

```

### Extensions to CSS Selectors[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#extensions-to-css-selectors "Permalink to this heading")

Per W3C standards, [CSS selectors](https://www.w3.org/TR/selectors-3/#selectors) do not support selecting text nodes or attribute values. But selecting these is so essential in a web scraping context that Scrapy (parsel) implements a couple of **non-standard pseudo-elements**:

-   to select text nodes, use `::text`
    
-   to select attribute values, use `::attr(name)` where _name_ is the name of the attribute that you want the value of
    

Warning

These pseudo-elements are Scrapy-/Parsel-specific. They will most probably not work with other libraries like [lxml](https://lxml.de/) or [PyQuery](https://pypi.org/project/pyquery/).

Examples:

-   `title::text` selects children text nodes of a descendant `<title>` element:
    

```
>>> response.css("title::text").get()
'Example website'

```

-   `*::text` selects all descendant text nodes of the current selector context:
    

```
>>> response.css("#images *::text").getall()
['\n   ',
'Name: My image 1 ',
'\n   ',
'Name: My image 2 ',
'\n   ',
'Name: My image 3 ',
'\n   ',
'Name: My image 4 ',
'\n   ',
'Name: My image 5 ',
'\n  ']

```

-   `foo::text` returns no results if `foo` element exists, but contains no text (i.e. text is empty):
    

```
>>> response.css("img::text").getall()
[]

This means ``.css('foo::text').get()`` could return None even if an element
exists. Use ``default=''`` if you always want a string:

```

```
>>> response.css("img::text").get()
>>> response.css("img::text").get(default="")
''

```

-   `a::attr(href)` selects the _href_ attribute value of descendant links:
    

```
>>> response.css("a::attr(href)").getall()
['image1.html',
'image2.html',
'image3.html',
'image4.html',
'image5.html']

```

Note

See also: [Selecting element attributes](https://docs.scrapy.org/en/latest/topics/selectors.html#selecting-attributes).

Note

You cannot chain these pseudo-elements. But in practice it would not make much sense: text nodes do not have attributes, and attribute values are string values already and do not have children nodes.

### Nesting selectors[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#nesting-selectors "Permalink to this heading")

The selection methods (`.xpath()` or `.css()`) return a list of selectors of the same type, so you can call the selection methods for those selectors too. Here’s an example:

```
>>> links = response.xpath('//a[contains(@href, "image")]')
>>> links.getall()
['<a href="image1.html">Name: My image 1 <br><img src="image1_thumb.jpg" alt="image1"></a>',
'<a href="image2.html">Name: My image 2 <br><img src="image2_thumb.jpg" alt="image2"></a>',
'<a href="image3.html">Name: My image 3 <br><img src="image3_thumb.jpg" alt="image3"></a>',
'<a href="image4.html">Name: My image 4 <br><img src="image4_thumb.jpg" alt="image4"></a>',
'<a href="image5.html">Name: My image 5 <br><img src="image5_thumb.jpg" alt="image5"></a>']

>>> for index, link in enumerate(links):
...     href_xpath = link.xpath("@href").get()
...     img_xpath = link.xpath("img/@src").get()
...     print(f"Link number {index} points to url {href_xpath!r} and image {img_xpath!r}")
...
Link number 0 points to url 'image1.html' and image 'image1_thumb.jpg'
Link number 1 points to url 'image2.html' and image 'image2_thumb.jpg'
Link number 2 points to url 'image3.html' and image 'image3_thumb.jpg'
Link number 3 points to url 'image4.html' and image 'image4_thumb.jpg'
Link number 4 points to url 'image5.html' and image 'image5_thumb.jpg'

```

### Selecting element attributes[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#selecting-element-attributes "Permalink to this heading")

There are several ways to get a value of an attribute. First, one can use XPath syntax:

```
>>> response.xpath("//a/@href").getall()
['image1.html', 'image2.html', 'image3.html', 'image4.html', 'image5.html']

```

XPath syntax has a few advantages: it is a standard XPath feature, and `@attributes` can be used in other parts of an XPath expression - e.g. it is possible to filter by attribute value.

Scrapy also provides an extension to CSS selectors (`::attr(...)`) which allows to get attribute values:

```
>>> response.css("a::attr(href)").getall()
['image1.html', 'image2.html', 'image3.html', 'image4.html', 'image5.html']

```

In addition to that, there is a `.attrib` property of Selector. You can use it if you prefer to lookup attributes in Python code, without using XPaths or CSS extensions:

```
>>> [a.attrib["href"] for a in response.css("a")]
['image1.html', 'image2.html', 'image3.html', 'image4.html', 'image5.html']

```

This property is also available on SelectorList; it returns a dictionary with attributes of a first matching element. It is convenient to use when a selector is expected to give a single result (e.g. when selecting by element ID, or when selecting an unique element on a page):

```
>>> response.css("base").attrib
{'href': 'http://example.com/'}
>>> response.css("base").attrib["href"]
'http://example.com/'

```

`.attrib` property of an empty SelectorList is empty:

```
>>> response.css("foo").attrib
{}

```

### Using selectors with regular expressions[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#using-selectors-with-regular-expressions "Permalink to this heading")

`Selector` also has a `.re()` method for extracting data using regular expressions. However, unlike using `.xpath()` or `.css()` methods, `.re()` returns a list of strings. So you can’t construct nested `.re()` calls.

Here’s an example used to extract image names from the [HTML code](https://docs.scrapy.org/en/latest/topics/selectors.html#topics-selectors-htmlcode) above:

```
>>> response.xpath('//a[contains(@href, "image")]/text()').re(r"Name:\s*(.*)")
['My image 1 ',
'My image 2 ',
'My image 3 ',
'My image 4 ',
'My image 5 ']

```

There’s an additional helper reciprocating `.get()` (and its alias `.extract_first()`) for `.re()`, named `.re_first()`. Use it to extract just the first matching string:

```
>>> response.xpath('//a[contains(@href, "image")]/text()').re_first(r"Name:\s*(.*)")
'My image 1 '

```

### extract() and extract\_first()[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#extract-and-extract-first "Permalink to this heading")

If you’re a long-time Scrapy user, you’re probably familiar with `.extract()` and `.extract_first()` selector methods. Many blog posts and tutorials are using them as well. These methods are still supported by Scrapy, there are **no plans** to deprecate them.

However, Scrapy usage docs are now written using `.get()` and `.getall()` methods. We feel that these new methods result in a more concise and readable code.

The following examples show how these methods map to each other.

1.  `SelectorList.get()` is the same as `SelectorList.extract_first()`:
    

```
>>> response.css("a::attr(href)").get()
'image1.html'
>>> response.css("a::attr(href)").extract_first()
'image1.html'

```

2.  `SelectorList.getall()` is the same as `SelectorList.extract()`:
    

```
>>> response.css("a::attr(href)").getall()
['image1.html', 'image2.html', 'image3.html', 'image4.html', 'image5.html']
>>> response.css("a::attr(href)").extract()
['image1.html', 'image2.html', 'image3.html', 'image4.html', 'image5.html']

```

3.  `Selector.get()` is the same as `Selector.extract()`:
    

```
>>> response.css("a::attr(href)")[0].get()
'image1.html'
>>> response.css("a::attr(href)")[0].extract()
'image1.html'

```

4.  For consistency, there is also `Selector.getall()`, which returns a list:
    

```
>>> response.css("a::attr(href)")[0].getall()
['image1.html']

```

So, the main difference is that output of `.get()` and `.getall()` methods is more predictable: `.get()` always returns a single result, `.getall()` always returns a list of all extracted results. With `.extract()` method it was not always obvious if a result is a list or not; to get a single result either `.extract()` or `.extract_first()` should be called.

## Working with XPaths[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#working-with-xpaths "Permalink to this heading")

Here are some tips which may help you to use XPath with Scrapy selectors effectively. If you are not much familiar with XPath yet, you may want to take a look first at this [XPath tutorial](http://www.zvon.org/comp/r/tut-XPath_1.html).

### Working with relative XPaths[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#working-with-relative-xpaths "Permalink to this heading")

Keep in mind that if you are nesting selectors and use an XPath that starts with `/`, that XPath will be absolute to the document and not relative to the `Selector` you’re calling it from.

For example, suppose you want to extract all `<p>` elements inside `<div>` elements. First, you would get all `<div>` elements:

```
>>> divs = response.xpath("//div")

```

At first, you may be tempted to use the following approach, which is wrong, as it actually extracts all `<p>` elements from the document, not only those inside `<div>` elements:

```
>>> for p in divs.xpath("//p"):  # this is wrong - gets all <p> from the whole document
...     print(p.get())
...

```

This is the proper way to do it (note the dot prefixing the `.//p` XPath):

```
>>> for p in divs.xpath(".//p"):  # extracts all <p> inside
...     print(p.get())
...

```

Another common case would be to extract all direct `<p>` children:

```
>>> for p in divs.xpath("p"):
...     print(p.get())
...

```

For more details about relative XPaths see the [Location Paths](https://www.w3.org/TR/xpath/all/#location-paths) section in the XPath specification.

### When querying by class, consider using CSS[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#when-querying-by-class-consider-using-css "Permalink to this heading")

Because an element can contain multiple CSS classes, the XPath way to select elements by class is the rather verbose:

```
*[contains(concat(' ', normalize-space(@class), ' '), ' someclass ')]

```

If you use `@class='someclass'` you may end up missing elements that have other classes, and if you just use `contains(@class, 'someclass')` to make up for that you may end up with more elements that you want, if they have a different class name that shares the string `someclass`.

As it turns out, Scrapy selectors allow you to chain selectors, so most of the time you can just select by class using CSS and then switch to XPath when needed:

```
>>> from scrapy import Selector
>>> sel = Selector(
...     text='<div class="hero shout"><time datetime="2014-07-23 19:00">Special date</time></div>'
... )
>>> sel.css(".shout").xpath("./time/@datetime").getall()
['2014-07-23 19:00']

```

This is cleaner than using the verbose XPath trick shown above. Just remember to use the `.` in the XPath expressions that will follow.

### Beware of the difference between //node\[1\] and (//node)\[1\][¶](https://docs.scrapy.org/en/latest/topics/selectors.html#beware-of-the-difference-between-node-1-and-node-1 "Permalink to this heading")

`//node[1]` selects all the nodes occurring first under their respective parents.

`(//node)[1]` selects all the nodes in the document, and then gets only the first of them.

Example:

```
>>> from scrapy import Selector
>>> sel = Selector(
...     text="""
...     <ul class="list">
...         <li>1</li>
...         <li>2</li>
...         <li>3</li>
...     </ul>
...     <ul class="list">
...         <li>4</li>
...         <li>5</li>
...         <li>6</li>
...     </ul>"""
... )
>>> xp = lambda x: sel.xpath(x).getall()

```

This gets all first `<li>` elements under whatever it is its parent:

```
>>> xp("//li[1]")
['<li>1</li>', '<li>4</li>']

```

And this gets the first `<li>` element in the whole document:

```
>>> xp("(//li)[1]")
['<li>1</li>']

```

This gets all first `<li>` elements under an `<ul>` parent:

```
>>> xp("//ul/li[1]")
['<li>1</li>', '<li>4</li>']

```

And this gets the first `<li>` element under an `<ul>` parent in the whole document:

```
>>> xp("(//ul/li)[1]")
['<li>1</li>']

```

### Using text nodes in a condition[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#using-text-nodes-in-a-condition "Permalink to this heading")

When you need to use the text content as argument to an [XPath string function](https://www.w3.org/TR/xpath/all/#section-String-Functions), avoid using `.//text()` and use just `.` instead.

This is because the expression `.//text()` yields a collection of text elements – a _node-set_. And when a node-set is converted to a string, which happens when it is passed as argument to a string function like `contains()` or `starts-with()`, it results in the text for the first element only.

Example:

```
>>> from scrapy import Selector
>>> sel = Selector(
...     text='<a href="#">Click here to go to the <strong>Next Page</strong></a>'
... )

```

Converting a _node-set_ to string:

```
>>> sel.xpath("//a//text()").getall()  # take a peek at the node-set
['Click here to go to the ', 'Next Page']
>>> sel.xpath("string(//a[1]//text())").getall()  # convert it to string
['Click here to go to the ']

```

A _node_ converted to a string, however, puts together the text of itself plus of all its descendants:

```
>>> sel.xpath("//a[1]").getall()  # select the first node
['<a href="#">Click here to go to the <strong>Next Page</strong></a>']
>>> sel.xpath("string(//a[1])").getall()  # convert it to string
['Click here to go to the Next Page']

```

So, using the `.//text()` node-set won’t select anything in this case:

```
>>> sel.xpath("//a[contains(.//text(), 'Next Page')]").getall()
[]

```

But using the `.` to mean the node, works:

```
>>> sel.xpath("//a[contains(., 'Next Page')]").getall()
['<a href="#">Click here to go to the <strong>Next Page</strong></a>']

```

### Variables in XPath expressions[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#variables-in-xpath-expressions "Permalink to this heading")

XPath allows you to reference variables in your XPath expressions, using the `$somevariable` syntax. This is somewhat similar to parameterized queries or prepared statements in the SQL world where you replace some arguments in your queries with placeholders like `?`, which are then substituted with values passed with the query.

Here’s an example to match an element based on its “id” attribute value, without hard-coding it (that was shown previously):

```
>>> # `$val` used in the expression, a `val` argument needs to be passed
>>> response.xpath("//div[@id=$val]/a/text()", val="images").get()
'Name: My image 1 '

```

Here’s another example, to find the “id” attribute of a `<div>` tag containing five `<a>` children (here we pass the value `5` as an integer):

```
>>> response.xpath("//div[count(a)=$cnt]/@id", cnt=5).get()
'images'

```

All variable references must have a binding value when calling `.xpath()` (otherwise you’ll get a `ValueError: XPath error:` exception). This is done by passing as many named arguments as necessary.

[parsel](https://parsel.readthedocs.io/en/latest/), the library powering Scrapy selectors, has more details and examples on [XPath variables](https://parsel.readthedocs.io/en/latest/usage.html#variables-in-xpath-expressions).

### Removing namespaces[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#removing-namespaces "Permalink to this heading")

When dealing with scraping projects, it is often quite convenient to get rid of namespaces altogether and just work with element names, to write more simple/convenient XPaths. You can use the `Selector.remove_namespaces()` method for that.

Let’s show an example that illustrates this with the Python Insider blog atom feed.

First, we open the shell with the url we want to scrape:

```
$ scrapy shell https://feeds.feedburner.com/PythonInsider

```

This is how the file starts:

```
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet ...
<feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:openSearch="http://a9.com/-/spec/opensearchrss/1.0/"
      xmlns:blogger="http://schemas.google.com/blogger/2008"
      xmlns:georss="http://www.georss.org/georss"
      xmlns:gd="http://schemas.google.com/g/2005"
      xmlns:thr="http://purl.org/syndication/thread/1.0"
      xmlns:feedburner="http://rssnamespace.org/feedburner/ext/1.0">
  ...

```

You can see several namespace declarations including a default “[http://www.w3.org/2005/Atom](http://www.w3.org/2005/Atom)” and another one using the “gd:” prefix for “[http://schemas.google.com/g/2005](http://schemas.google.com/g/2005)”.

Once in the shell we can try selecting all `<link>` objects and see that it doesn’t work (because the Atom XML namespace is obfuscating those nodes):

```
>>> response.xpath("//link")
[]

```

But once we call the `Selector.remove_namespaces()` method, all nodes can be accessed directly by their names:

```
>>> response.selector.remove_namespaces()
>>> response.xpath("//link")
[<Selector query='//link' data='<link rel="alternate" type="text/html" h'>,
    <Selector query='//link' data='<link rel="next" type="application/atom+'>,
    ...

```

If you wonder why the namespace removal procedure isn’t always called by default instead of having to call it manually, this is because of two reasons, which, in order of relevance, are:

1.  Removing namespaces requires to iterate and modify all nodes in the document, which is a reasonably expensive operation to perform by default for all documents crawled by Scrapy
    
2.  There could be some cases where using namespaces is actually required, in case some element names clash between namespaces. These cases are very rare though.
    

### Using EXSLT extensions[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#using-exslt-extensions "Permalink to this heading")

Being built atop [lxml](https://lxml.de/), Scrapy selectors support some [EXSLT](http://exslt.org/) extensions and come with these pre-registered namespaces to use in XPath expressions:

#### Regular expressions[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#regular-expressions "Permalink to this heading")

The `test()` function, for example, can prove quite useful when XPath’s `starts-with()` or `contains()` are not sufficient.

Example selecting links in list item with a “class” attribute ending with a digit:

```
>>> from scrapy import Selector
>>> doc = """
... <div>
...     <ul>
...         <li class="item-0"><a href="link1.html">first item</a></li>
...         <li class="item-1"><a href="link2.html">second item</a></li>
...         <li class="item-inactive"><a href="link3.html">third item</a></li>
...         <li class="item-1"><a href="link4.html">fourth item</a></li>
...         <li class="item-0"><a href="link5.html">fifth item</a></li>
...     </ul>
... </div>
... """
>>> sel = Selector(text=doc, type="html")
>>> sel.xpath("//li//@href").getall()
['link1.html', 'link2.html', 'link3.html', 'link4.html', 'link5.html']
>>> sel.xpath('//li[re:test(@class, "item-\d$")]//@href').getall()
['link1.html', 'link2.html', 'link4.html', 'link5.html']

```

Warning

C library `libxslt` doesn’t natively support EXSLT regular expressions so [lxml](https://lxml.de/)’s implementation uses hooks to Python’s `re` module. Thus, using regexp functions in your XPath expressions may add a small performance penalty.

#### Set operations[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#set-operations "Permalink to this heading")

These can be handy for excluding parts of a document tree before extracting text elements for example.

Example extracting microdata (sample content taken from [https://schema.org/Product](https://schema.org/Product)) with groups of itemscopes and corresponding itemprops:

```
>>> doc = """
... <div itemscope itemtype="http://schema.org/Product">
...   <span itemprop="name">Kenmore White 17" Microwave</span>
...   <img src="kenmore-microwave-17in.jpg" alt='Kenmore 17" Microwave' />
...   <div itemprop="aggregateRating"
...     itemscope itemtype="http://schema.org/AggregateRating">
...    Rated <span itemprop="ratingValue">3.5</span>/5
...    based on <span itemprop="reviewCount">11</span> customer reviews
...   </div>
...   <div itemprop="offers" itemscope itemtype="http://schema.org/Offer">
...     <span itemprop="price">$55.00</span>
...     <link itemprop="availability" href="http://schema.org/InStock" />In stock
...   </div>
...   Product description:
...   <span itemprop="description">0.7 cubic feet countertop microwave.
...   Has six preset cooking categories and convenience features like
...   Add-A-Minute and Child Lock.</span>
...   Customer reviews:
...   <div itemprop="review" itemscope itemtype="http://schema.org/Review">
...     <span itemprop="name">Not a happy camper</span> -
...     by <span itemprop="author">Ellie</span>,
...     <meta itemprop="datePublished" content="2011-04-01">April 1, 2011
...     <div itemprop="reviewRating" itemscope itemtype="http://schema.org/Rating">
...       <meta itemprop="worstRating" content = "1">
...       <span itemprop="ratingValue">1</span>/
...       <span itemprop="bestRating">5</span>stars
...     </div>
...     <span itemprop="description">The lamp burned out and now I have to replace
...     it. </span>
...   </div>
...   <div itemprop="review" itemscope itemtype="http://schema.org/Review">
...     <span itemprop="name">Value purchase</span> -
...     by <span itemprop="author">Lucas</span>,
...     <meta itemprop="datePublished" content="2011-03-25">March 25, 2011
...     <div itemprop="reviewRating" itemscope itemtype="http://schema.org/Rating">
...       <meta itemprop="worstRating" content = "1"/>
...       <span itemprop="ratingValue">4</span>/
...       <span itemprop="bestRating">5</span>stars
...     </div>
...     <span itemprop="description">Great microwave for the price. It is small and
...     fits in my apartment.</span>
...   </div>
...   ...
... </div>
... """
>>> sel = Selector(text=doc, type="html")
>>> for scope in sel.xpath("//div[@itemscope]"):
...     print("current scope:", scope.xpath("@itemtype").getall())
...     props = scope.xpath(
...         """
...                 set:difference(./descendant::*/@itemprop,
...                                .//*[@itemscope]/*/@itemprop)"""
...     )
...     print(f"    properties: {props.getall()}")
...     print("")
...

current scope: ['http://schema.org/Product']
    properties: ['name', 'aggregateRating', 'offers', 'description', 'review', 'review']

current scope: ['http://schema.org/AggregateRating']
    properties: ['ratingValue', 'reviewCount']

current scope: ['http://schema.org/Offer']
    properties: ['price', 'availability']

current scope: ['http://schema.org/Review']
    properties: ['name', 'author', 'datePublished', 'reviewRating', 'description']

current scope: ['http://schema.org/Rating']
    properties: ['worstRating', 'ratingValue', 'bestRating']

current scope: ['http://schema.org/Review']
    properties: ['name', 'author', 'datePublished', 'reviewRating', 'description']

current scope: ['http://schema.org/Rating']
    properties: ['worstRating', 'ratingValue', 'bestRating']

```

Here we first iterate over `itemscope` elements, and for each one, we look for all `itemprops` elements and exclude those that are themselves inside another `itemscope`.

### Other XPath extensions[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#other-xpath-extensions "Permalink to this heading")

Scrapy selectors also provide a sorely missed XPath extension function `has-class` that returns `True` for nodes that have all of the specified HTML classes.

For the following HTML:

```
>>> from scrapy.http import HtmlResponse
>>> response = HtmlResponse(
...     url="http://example.com",
...     body="""
... <html>
...     <body>
...         <p class="foo bar-baz">First</p>
...         <p class="foo">Second</p>
...         <p class="bar">Third</p>
...         <p>Fourth</p>
...     </body>
... </html>
... """,
...     encoding="utf-8",
... )

```

You can use it like this:

```
>>> response.xpath('//p[has-class("foo")]')
[<Selector query='//p[has-class("foo")]' data='<p class="foo bar-baz">First</p>'>,
<Selector query='//p[has-class("foo")]' data='<p class="foo">Second</p>'>]
>>> response.xpath('//p[has-class("foo", "bar-baz")]')
[<Selector query='//p[has-class("foo", "bar-baz")]' data='<p class="foo bar-baz">First</p>'>]
>>> response.xpath('//p[has-class("foo", "bar")]')
[]

```

So XPath `//p[has-class("foo", "bar-baz")]` is roughly equivalent to CSS `p.foo.bar-baz`. Please note, that it is slower in most of the cases, because it’s a pure-Python function that’s invoked for every node in question whereas the CSS lookup is translated into XPath and thus runs more efficiently, so performance-wise its uses are limited to situations that are not easily described with CSS selectors.

Parsel also simplifies adding your own XPath extensions.

parsel.xpathfuncs.set\_xpathfunc(_fname: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _func: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional "(in Python v3.13)")\[[Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.13)")\]_) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[\[source\]](https://docs.scrapy.org/en/latest/_modules/parsel/xpathfuncs.html#set_xpathfunc)[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#parsel.xpathfuncs.set_xpathfunc "Permalink to this definition")

Register a custom extension function to use in XPath expressions.

The function `func` registered under `fname` identifier will be called for every matching node, being passed a `context` parameter as well as any parameters passed from the corresponding XPath expression.

If `func` is `None`, the extension function will be removed.

See more [in lxml documentation](https://lxml.de/extensions.html#xpath-extension-functions).

## Built-in Selectors reference[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#module-scrapy.selector "Permalink to this heading")

### Selector objects[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#selector-objects "Permalink to this heading")

_class_ scrapy.selector.Selector(_\*args: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.13)")_, _\*\*kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.13)")_)[\[source\]](https://docs.scrapy.org/en/latest/_modules/scrapy/selector/unified.html#Selector)[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.Selector "Permalink to this definition")

An instance of [`Selector`](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.Selector "scrapy.selector.Selector") is a wrapper over response to select certain parts of its content.

`response` is an [`HtmlResponse`](https://docs.scrapy.org/en/latest/topics/request-response.html#scrapy.http.HtmlResponse "scrapy.http.HtmlResponse") or an [`XmlResponse`](https://docs.scrapy.org/en/latest/topics/request-response.html#scrapy.http.XmlResponse "scrapy.http.XmlResponse") object that will be used for selecting and extracting data.

`text` is a unicode string or utf-8 encoded text for cases when a `response` isn’t available. Using `text` and `response` together is undefined behavior.

`type` defines the selector type, it can be `"html"`, `"xml"`, `"json"` or `None` (default).

If `type` is `None`, the selector automatically chooses the best type based on `response` type (see below), or defaults to `"html"` in case it is used together with `text`.

If `type` is `None` and a `response` is passed, the selector type is inferred from the response type as follows:

-   `"html"` for [`HtmlResponse`](https://docs.scrapy.org/en/latest/topics/request-response.html#scrapy.http.HtmlResponse "scrapy.http.HtmlResponse") type
    
-   `"xml"` for [`XmlResponse`](https://docs.scrapy.org/en/latest/topics/request-response.html#scrapy.http.XmlResponse "scrapy.http.XmlResponse") type
    
-   `"json"` for [`TextResponse`](https://docs.scrapy.org/en/latest/topics/request-response.html#scrapy.http.TextResponse "scrapy.http.TextResponse") type
    
-   `"html"` for anything else
    

Otherwise, if `type` is set, the selector type will be forced and no detection will occur.

xpath(_query: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _namespaces: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional "(in Python v3.13)")\[[Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.13)")\[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")\]\] \= None_, _\*\*kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.13)")_) → SelectorList\[\_SelectorType\][\[source\]](https://docs.scrapy.org/en/latest/_modules/parsel/selector.html#Selector.xpath)[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.Selector.xpath "Permalink to this definition")

Find nodes matching the xpath `query` and return the result as a [`SelectorList`](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.SelectorList "scrapy.selector.SelectorList") instance with all elements flattened. List elements implement [`Selector`](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.Selector "scrapy.selector.Selector") interface too.

`query` is a string containing the XPATH query to apply.

`namespaces` is an optional `prefix: namespace-uri` mapping (dict) for additional prefixes to those registered with `register_namespace(prefix, uri)`. Contrary to `register_namespace()`, these prefixes are not saved for future calls.

Any additional named arguments can be used to pass values for XPath variables in the XPath expression, e.g.:

```
selector.xpath('//a[href=$url]', url="http://www.example.com")

```

Note

For convenience, this method can be called as `response.xpath()`

css(_query: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_) → SelectorList\[\_SelectorType\][\[source\]](https://docs.scrapy.org/en/latest/_modules/parsel/selector.html#Selector.css)[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.Selector.css "Permalink to this definition")

Apply the given CSS selector and return a [`SelectorList`](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.SelectorList "scrapy.selector.SelectorList") instance.

`query` is a string containing the CSS selector to apply.

In the background, CSS queries are translated into XPath queries using [cssselect](https://pypi.python.org/pypi/cssselect/) library and run `.xpath()` method.

Note

For convenience, this method can be called as `response.css()`

jmespath(_query: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _\*\*kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.13)")_) → SelectorList\[\_SelectorType\][\[source\]](https://docs.scrapy.org/en/latest/_modules/parsel/selector.html#Selector.jmespath)[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.Selector.jmespath "Permalink to this definition")

Find objects matching the JMESPath `query` and return the result as a [`SelectorList`](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.SelectorList "scrapy.selector.SelectorList") instance with all elements flattened. List elements implement [`Selector`](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.Selector "scrapy.selector.Selector") interface too.

`query` is a string containing the [JMESPath](https://jmespath.org/) query to apply.

Any additional named arguments are passed to the underlying `jmespath.search` call, e.g.:

```
selector.jmespath('author.name', options=jmespath.Options(dict_cls=collections.OrderedDict))

```

Note

For convenience, this method can be called as `response.jmespath()`

get() → [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.13)")[\[source\]](https://docs.scrapy.org/en/latest/_modules/parsel/selector.html#Selector.get)[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.Selector.get "Permalink to this definition")

Serialize and return the matched nodes.

For HTML and XML, the result is always a string, and percent-encoded content is unquoted.

See also: [extract() and extract\_first()](https://docs.scrapy.org/en/latest/topics/selectors.html#old-extraction-api)

attrib[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.Selector.attrib "Permalink to this definition")

Return the attributes dictionary for underlying element.

See also: [Selecting element attributes](https://docs.scrapy.org/en/latest/topics/selectors.html#selecting-attributes).

re(_regex: [Union](https://docs.python.org/3/library/typing.html#typing.Union "(in Python v3.13)")\[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"), [Pattern](https://docs.python.org/3/library/typing.html#typing.Pattern "(in Python v3.13)")\[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")\]\]_, _replace\_entities: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") \= True_) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")\[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")\][\[source\]](https://docs.scrapy.org/en/latest/_modules/parsel/selector.html#Selector.re)[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.Selector.re "Permalink to this definition")

Apply the given regex and return a list of strings with the matches.

`regex` can be either a compiled regular expression or a string which will be compiled to a regular expression using `re.compile(regex)`.

By default, character entity references are replaced by their corresponding character (except for `&amp;` and `&lt;`). Passing `replace_entities` as `False` switches off these replacements.

re\_first(_regex: [Union](https://docs.python.org/3/library/typing.html#typing.Union "(in Python v3.13)")\[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"), [Pattern](https://docs.python.org/3/library/typing.html#typing.Pattern "(in Python v3.13)")\[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")\]\]_, _default: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") \= None_, _replace\_entities: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") \= True_) → [Optional](https://docs.python.org/3/library/typing.html#typing.Optional "(in Python v3.13)")\[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")\][\[source\]](https://docs.scrapy.org/en/latest/_modules/parsel/selector.html#Selector.re_first)[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.Selector.re_first "Permalink to this definition")

re\_first(_regex: [Union](https://docs.python.org/3/library/typing.html#typing.Union "(in Python v3.13)")\[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"), [Pattern](https://docs.python.org/3/library/typing.html#typing.Pattern "(in Python v3.13)")\[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")\]\]_, _default: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _replace\_entities: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") \= True_) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

Apply the given regex and return the first string which matches. If there is no match, return the default value (`None` if the argument is not provided).

By default, character entity references are replaced by their corresponding character (except for `&amp;` and `&lt;`). Passing `replace_entities` as `False` switches off these replacements.

register\_namespace(_prefix: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _uri: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[\[source\]](https://docs.scrapy.org/en/latest/_modules/parsel/selector.html#Selector.register_namespace)[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.Selector.register_namespace "Permalink to this definition")

Register the given namespace to be used in this [`Selector`](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.Selector "scrapy.selector.Selector"). Without registering namespaces you can’t select or extract data from non-standard namespaces. See [Selector examples on XML response](https://docs.scrapy.org/en/latest/topics/selectors.html#selector-examples-xml).

remove\_namespaces() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[\[source\]](https://docs.scrapy.org/en/latest/_modules/parsel/selector.html#Selector.remove_namespaces)[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.Selector.remove_namespaces "Permalink to this definition")

Remove all namespaces, allowing to traverse the document using namespace-less xpaths. See [Removing namespaces](https://docs.scrapy.org/en/latest/topics/selectors.html#removing-namespaces).

\_\_bool\_\_() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[\[source\]](https://docs.scrapy.org/en/latest/_modules/parsel/selector.html#Selector.__bool__)[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.Selector.__bool__ "Permalink to this definition")

Return `True` if there is any real content selected or `False` otherwise. In other words, the boolean value of a [`Selector`](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.Selector "scrapy.selector.Selector") is given by the contents it selects.

getall() → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")\[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")\][\[source\]](https://docs.scrapy.org/en/latest/_modules/parsel/selector.html#Selector.getall)[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.Selector.getall "Permalink to this definition")

Serialize and return the matched node in a 1-element list of strings.

This method is added to Selector for consistency; it is more useful with SelectorList. See also: [extract() and extract\_first()](https://docs.scrapy.org/en/latest/topics/selectors.html#old-extraction-api)

### SelectorList objects[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#selectorlist-objects "Permalink to this heading")

_class_ scrapy.selector.SelectorList(_iterable\=()_, _/_)[\[source\]](https://docs.scrapy.org/en/latest/_modules/scrapy/selector/unified.html#SelectorList)[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.SelectorList "Permalink to this definition")

The [`SelectorList`](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.SelectorList "scrapy.selector.SelectorList") class is a subclass of the builtin `list` class, which provides a few additional methods.

xpath(_xpath: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _namespaces: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional "(in Python v3.13)")\[[Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.13)")\[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")\]\] \= None_, _\*\*kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.13)")_) → SelectorList\[\_SelectorType\][\[source\]](https://docs.scrapy.org/en/latest/_modules/parsel/selector.html#SelectorList.xpath)[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.SelectorList.xpath "Permalink to this definition")

Call the `.xpath()` method for each element in this list and return their results flattened as another [`SelectorList`](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.SelectorList "scrapy.selector.SelectorList").

`xpath` is the same argument as the one in [`Selector.xpath()`](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.Selector.xpath "scrapy.selector.Selector.xpath")

`namespaces` is an optional `prefix: namespace-uri` mapping (dict) for additional prefixes to those registered with `register_namespace(prefix, uri)`. Contrary to `register_namespace()`, these prefixes are not saved for future calls.

Any additional named arguments can be used to pass values for XPath variables in the XPath expression, e.g.:

```
selector.xpath('//a[href=$url]', url="http://www.example.com")

```

css(_query: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_) → SelectorList\[\_SelectorType\][\[source\]](https://docs.scrapy.org/en/latest/_modules/parsel/selector.html#SelectorList.css)[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.SelectorList.css "Permalink to this definition")

Call the `.css()` method for each element in this list and return their results flattened as another [`SelectorList`](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.SelectorList "scrapy.selector.SelectorList").

`query` is the same argument as the one in [`Selector.css()`](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.Selector.css "scrapy.selector.Selector.css")

jmespath(_query: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _\*\*kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.13)")_) → SelectorList\[\_SelectorType\][\[source\]](https://docs.scrapy.org/en/latest/_modules/parsel/selector.html#SelectorList.jmespath)[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.SelectorList.jmespath "Permalink to this definition")

Call the `.jmespath()` method for each element in this list and return their results flattened as another [`SelectorList`](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.SelectorList "scrapy.selector.SelectorList").

`query` is the same argument as the one in [`Selector.jmespath()`](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.Selector.jmespath "scrapy.selector.Selector.jmespath").

Any additional named arguments are passed to the underlying `jmespath.search` call, e.g.:

```
selector.jmespath('author.name', options=jmespath.Options(dict_cls=collections.OrderedDict))

```

getall() → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")\[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")\][\[source\]](https://docs.scrapy.org/en/latest/_modules/parsel/selector.html#SelectorList.getall)[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.SelectorList.getall "Permalink to this definition")

Call the `.get()` method for each element is this list and return their results flattened, as a list of strings.

See also: [extract() and extract\_first()](https://docs.scrapy.org/en/latest/topics/selectors.html#old-extraction-api)

get(_default: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") \= None_) → [Optional](https://docs.python.org/3/library/typing.html#typing.Optional "(in Python v3.13)")\[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")\][\[source\]](https://docs.scrapy.org/en/latest/_modules/parsel/selector.html#SelectorList.get)[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.SelectorList.get "Permalink to this definition")

get(_default: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

Return the result of `.get()` for the first element in this list. If the list is empty, return the default value.

See also: [extract() and extract\_first()](https://docs.scrapy.org/en/latest/topics/selectors.html#old-extraction-api)

re(_regex: [Union](https://docs.python.org/3/library/typing.html#typing.Union "(in Python v3.13)")\[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"), [Pattern](https://docs.python.org/3/library/typing.html#typing.Pattern "(in Python v3.13)")\[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")\]\]_, _replace\_entities: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") \= True_) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")\[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")\][\[source\]](https://docs.scrapy.org/en/latest/_modules/parsel/selector.html#SelectorList.re)[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.SelectorList.re "Permalink to this definition")

Call the `.re()` method for each element in this list and return their results flattened, as a list of strings.

By default, character entity references are replaced by their corresponding character (except for `&amp;` and `&lt;`. Passing `replace_entities` as `False` switches off these replacements.

re\_first(_regex: [Union](https://docs.python.org/3/library/typing.html#typing.Union "(in Python v3.13)")\[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"), [Pattern](https://docs.python.org/3/library/typing.html#typing.Pattern "(in Python v3.13)")\[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")\]\]_, _default: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") \= None_, _replace\_entities: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") \= True_) → [Optional](https://docs.python.org/3/library/typing.html#typing.Optional "(in Python v3.13)")\[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")\][\[source\]](https://docs.scrapy.org/en/latest/_modules/parsel/selector.html#SelectorList.re_first)[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.SelectorList.re_first "Permalink to this definition")

re\_first(_regex: [Union](https://docs.python.org/3/library/typing.html#typing.Union "(in Python v3.13)")\[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"), [Pattern](https://docs.python.org/3/library/typing.html#typing.Pattern "(in Python v3.13)")\[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")\]\]_, _default: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")_, _replace\_entities: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") \= True_) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

Call the `.re()` method for the first element in this list and return the result in an string. If the list is empty or the regex doesn’t match anything, return the default value (`None` if the argument is not provided).

By default, character entity references are replaced by their corresponding character (except for `&amp;` and `&lt;`. Passing `replace_entities` as `False` switches off these replacements.

attrib[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.SelectorList.attrib "Permalink to this definition")

Return the attributes dictionary for the first element. If the list is empty, return an empty dict.

See also: [Selecting element attributes](https://docs.scrapy.org/en/latest/topics/selectors.html#selecting-attributes).

## Examples[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#examples "Permalink to this heading")

### Selector examples on HTML response[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#selector-examples-on-html-response "Permalink to this heading")

Here are some [`Selector`](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.Selector "scrapy.selector.Selector") examples to illustrate several concepts. In all cases, we assume there is already a [`Selector`](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.Selector "scrapy.selector.Selector") instantiated with a [`HtmlResponse`](https://docs.scrapy.org/en/latest/topics/request-response.html#scrapy.http.HtmlResponse "scrapy.http.HtmlResponse") object like this:

```
sel = Selector(html_response)

```

1.  Select all `<h1>` elements from an HTML response body, returning a list of [`Selector`](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.Selector "scrapy.selector.Selector") objects (i.e. a [`SelectorList`](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.SelectorList "scrapy.selector.SelectorList") object):
    
2.  Extract the text of all `<h1>` elements from an HTML response body, returning a list of strings:
    
    ```
    sel.xpath("//h1").getall()  # this includes the h1 tag
    sel.xpath("//h1/text()").getall()  # this excludes the h1 tag
    
    ```
    
3.  Iterate over all `<p>` tags and print their class attribute:
    
    ```
    for node in sel.xpath("//p"):
        print(node.attrib["class"])
    
    ```
    

### Selector examples on XML response[¶](https://docs.scrapy.org/en/latest/topics/selectors.html#selector-examples-on-xml-response "Permalink to this heading")

Here are some examples to illustrate concepts for [`Selector`](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.Selector "scrapy.selector.Selector") objects instantiated with an [`XmlResponse`](https://docs.scrapy.org/en/latest/topics/request-response.html#scrapy.http.XmlResponse "scrapy.http.XmlResponse") object:

```
sel = Selector(xml_response)

```

1.  Select all `<product>` elements from an XML response body, returning a list of [`Selector`](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.Selector "scrapy.selector.Selector") objects (i.e. a [`SelectorList`](https://docs.scrapy.org/en/latest/topics/selectors.html#scrapy.selector.SelectorList "scrapy.selector.SelectorList") object):
    
2.  Extract all prices from a [Google Base XML feed](https://support.google.com/merchants/answer/160589?hl=en&ref_topic=2473799) which requires registering a namespace:
    
    ```
    sel.register_namespace("g", "http://base.google.com/ns/1.0")
    sel.xpath("//g:price").getall()
    
    ```