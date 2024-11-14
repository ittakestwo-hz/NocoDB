# 爬虫

爬虫是定义如何抓取某个网站（或一组网站）类的代码，包括如何进行爬取（即跟踪链接）和如何从其页面中提取结构化数据（即抓取项目）。换句话说，爬虫是您为特定网站（或在某些情况下，一组网站）定义自定义行为的地方，包括抓取和解析页面的逻辑。

对于爬虫来说，抓取周期大致如下：

1.  首先，您会生成初始请求来抓取第一个 URL，并指定一个回调函数，该函数将在从这些请求下载的响应中被调用。
  
> 执行的第一个请求通过调用 [`start_requests()`](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.Spider.start_requests "scrapy.Spider.start_requests") 方法获得，该方法（默认情况下）会生成针对 [`start_urls`](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.Spider.start_urls "scrapy.Spider.start_urls") 中指定的 URL 的 `Request`，并将 [`parse`](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.Spider.parse "scrapy.Spider.parse") 方法作为请求的回调函数。

2.  在回调函数中，您解析响应（网页）并返回 [item 对象](https://docs.scrapy.org/en/latest/topics/items.html#topics-items)、`Request` 对象或这些对象的可迭代项。这些请求也会包含一个回调（可能是相同的），然后将被 Scrapy 下载，并由指定的回调处理响应。
3.  在回调函数中，您解析页面内容，通常使用 [选择器](https://docs.scrapy.org/en/latest/topics/selectors.html#topics-selectors)（但您也可以使用 BeautifulSoup、lxml 或任何您喜欢的机制）并使用解析的数据生成项目。
4.  最后，从爬虫返回的项目通常会被持久化到数据库中（在某些 [Item Pipeline](https://docs.scrapy.org/en/latest/topics/item-pipeline.html#topics-item-pipeline) 中），或使用 [Feed 导出](https://docs.scrapy.org/en/latest/topics/feed-exports.html#topics-feed-exports) 写入文件。   

即使这个抓取周期适用于任何类型的爬虫，Scrapy 也为不同的目的捆绑了不同种类的默认爬虫。我们将在这里讨论这些类型。

## scrapy.Spider

类：`scrapy.spiders.Spider`

类：`scrapy.Spider`

这是最简单的爬虫，是所有其他爬虫必须继承的基类（包括随 Scrapy 捆绑的爬虫，以及您自己编写的爬虫）。它不提供任何特殊功能。它只提供了一个默认的 [`start_requests()`](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.Spider.start_requests "scrapy.Spider.start_requests") 实现，该实现从 [`start_urls`](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.Spider.start_urls "scrapy.Spider.start_urls") 爬虫属性发送请求，并对每个结果响应调用爬虫的 `parse` 方法。

### name

一个字符串，用于定义该爬虫的名称。爬虫的名称用于 Scrapy 定位（并实例化）爬虫，因此它必须是唯一的。不过，您可以实例化同一个爬虫的多个实例。这个属性是爬虫中最重要的，并且是必需的。

如果爬虫抓取的是单一域名，通常的做法是将爬虫命名为该域名的名称，可以包含或不包含 [TLD](https://en.wikipedia.org/wiki/Top-level_domain)（顶级域名）。例如，一个抓取 `mywebsite.com` 的爬虫通常会被命名为 `mywebsite`。

### allowed_domains

一个可选的字符串列表，包含该爬虫允许抓取的域名。对于不属于此列表中指定的域名（或其子域名）的 URL 请求，如果启用了 [`OffsiteMiddleware`](https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#scrapy.downloadermiddlewares.offsite.OffsiteMiddleware "scrapy.downloadermiddlewares.offsite.OffsiteMiddleware")，则不会跟踪这些请求。

例如，如果目标 URL 是 `https://www.example.com/1.html`，则应将 `'example.com'` 添加到该列表中。

### start_urls

一个 URL 列表，爬虫将在这些 URL 上开始抓取，当没有指定特定 URL 时使用此列表。因此，首先下载的页面将是这里列出的页面。随后的 `Request` 会从起始 URL 中的数据逐步生成。

### custom_settings

一个字典，包含在运行该爬虫时将覆盖项目全局配置的设置。由于设置会在实例化之前更新，因此它必须作为类属性定义。

有关可用的内置设置，请参见：[内置设置参考](https://docs.scrapy.org/en/latest/topics/settings.html#topics-settings-ref)。

### crawler

该属性由 [`from_crawler()`](https://docs.scrapy.org/en/latest/topics/item-pipeline.html#from_crawler "from_crawler") 类方法在初始化类之后设置，并链接到该爬虫实例绑定的 [`Crawler`](https://docs.scrapy.org/en/latest/topics/api.html#scrapy.crawler.Crawler "scrapy.crawler.Crawler") 对象。

爬虫封装了项目中的许多组件，提供了它们的单一入口访问（例如扩展、middleware、中间件、信号管理器等）。查看 [爬虫 API](https://docs.scrapy.org/en/latest/topics/api.html#topics-api-crawler) 了解更多信息。

### settings
Configuration for running this spider. This is a [`Settings`](https://docs.scrapy.org/en/latest/topics/api.html#scrapy.settings.Settings "scrapy.settings.Settings") instance, see the [Settings](https://docs.scrapy.org/en/latest/topics/settings.html#topics-settings) topic for a detailed introduction on this subject.

### logger

由爬虫的 [`name`](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.Spider.name "scrapy.Spider.name") 创建的 Python 日志记录器。您可以通过它发送日志消息，具体使用方式请参考 [来自爬虫的日志记录](https://docs.scrapy.org/en/latest/topics/logging.html#topics-logging-from-spiders)。

### state

一个字典，您可以用它在不同的批次之间持久化某些爬虫状态。有关更多信息，请参见 [在批次之间保持持久化状态](https://docs.scrapy.org/en/latest/topics/jobs.html#topics-keeping-persistent-state-between-batches)。

### from_crawler(_crawler_, _\*args_, _\**kwargs_)

这是 Scrapy 用来创建爬虫的类方法。

您可能不需要直接重写此方法，因为默认实现作为 [`__init__()`](https://docs.scrapy.org/en/latest/topics/feed-exports.html#init__ "__init__") 方法的代理，使用给定的 `args` 和命名参数 `kwargs` 调用它。

不过，此方法会在新实例中设置 [`crawler`](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.Spider.crawler "scrapy.Spider.crawler") 和 [`settings`](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.Spider.settings "scrapy.Spider.settings") 属性，以便稍后在爬虫代码中访问。

版本 2.11 更新：现在可以在此方法中修改 `crawler.settings` 中的设置，这对于根据参数修改设置非常有用。因此，这些设置不是最终值，它们可以在稍后被修改（例如通过 [插件](https://docs.scrapy.org/en/latest/topics/addons.html#topics-addons)）。由于这个原因，大多数 [`Crawler`](https://docs.scrapy.org/en/latest/topics/api.html#scrapy.crawler.Crawler "scrapy.crawler.Crawler") 属性在此时并未初始化。

### 最终设置和已初始化的 [`Crawler`](https://docs.scrapy.org/en/latest/topics/api.html#scrapy.crawler.Crawler "scrapy.crawler.Crawler") 属性

最终的设置和已初始化的 [`Crawler`](https://docs.scrapy.org/en/latest/topics/api.html#scrapy.crawler.Crawler "scrapy.crawler.Crawler") 属性可以在 [`start_requests()`](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.Spider.start_requests "scrapy.Spider.start_requests") 方法、[`engine_started`](https://docs.scrapy.org/en/latest/topics/signals.html#std-signal-engine_started) 信号的处理程序以及后续处理中使用。

#### 参数

- **crawler** ([`Crawler`](https://docs.scrapy.org/en/latest/topics/api.html#scrapy.crawler.Crawler "scrapy.crawler.Crawler") 实例) – 该爬虫将绑定的爬虫
- **args** ([_list_](https://docs.python.org/3/library/stdtypes.html#list "(在 Python v3.13 中)")) – 传递给 [`__init__()`](https://docs.scrapy.org/en/latest/topics/feed-exports.html#init__ "__init__") 方法的参数
- **kwargs** ([_dict_](https://docs.python.org/3/library/stdtypes.html#dict "(在 Python v3.13 中)")) – 传递给 [`__init__()`](https://docs.scrapy.org/en/latest/topics/feed-exports.html#init__ "__init__") 方法的关键字参数

### _classmethod_ update_settings(_settings_)

`update_settings()` 方法用于修改爬虫的设置，并在爬虫实例初始化时调用。

它接受一个 [`Settings`](https://docs.scrapy.org/en/latest/topics/api.html#scrapy.settings.Settings "scrapy.settings.Settings") 对象作为参数，可以添加或更新爬虫的配置值。这个方法是一个类方法，这意味着它是针对 [`Spider`](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.Spider "scrapy.Spider") 类调用的，并允许所有爬虫实例共享相同的配置。

虽然每个爬虫的设置可以在 [`custom_settings`](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.Spider.custom_settings "scrapy.Spider.custom_settings") 中进行设置，但使用 `update_settings()` 允许您根据其他设置、爬虫属性或其他因素动态添加、移除或更改设置，并使用除 `'spider'` 以外的设置优先级。此外，通过重写 `update_settings()` 可以轻松地在子类中扩展它，而通过重写 [`custom_settings`](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.Spider.custom_settings "scrapy.Spider.custom_settings") 做到这一点可能较为困难。

例如，假设一个爬虫需要修改 [`FEEDS`](https://docs.scrapy.org/en/latest/topics/feed-exports.html#std-setting-FEEDS) 设置：

```
import scrapy

class MySpider(scrapy.Spider):
    name = "myspider"
    custom_feed = {
        "/home/user/documents/items.json": {
            "format": "json",
            "indent": 4,
        }
    }

    @classmethod
    def update_settings(cls, settings):
        super().update_settings(settings)
        settings.setdefault("FEEDS", {}).update(cls.custom_feed)
```

`start_requests()`[¶](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.Spider.start_requests "Permalink to this definition")

此方法必须返回一个可迭代对象，其中包含此爬虫的初始请求。当爬虫开启进行抓取时，Scrapy 会调用此方法。Scrapy 只会调用一次，因此将 `start_requests()` 实现为生成器是安全的。

默认实现会为 `start_urls` 中的每个 URL 生成 `Request(url, dont_filter=True)` 请求。

如果你想更改启动抓取时使用的请求，应该重写此方法。例如，如果你需要通过 POST 请求登录开始抓取，可以这样做：

```
import scrapy

class MySpider(scrapy.Spider):
    name = "myspider"

    def start_requests(self):
        return [
            scrapy.FormRequest(
                "http://www.example.com/login",
                formdata={"user": "john", "pass": "secret"},
                callback=self.logged_in,
            )
        ]

    def logged_in(self, response):
        # here you would extract links to follow and return Requests for
        # each of them, with another callback
        pass
```

`parse(_response_)`[¶](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.Spider.parse "Permalink to this definition")

这是 Scrapy 用来处理下载响应的默认回调方法，当请求没有指定回调时，`parse` 方法会被调用。

`parse` 方法负责处理响应并返回抓取的数据和/或更多的待跟踪 URL。其他请求的回调与 `Spider` 类有相同的要求。

此方法以及任何其他请求回调必须返回一个 `Request` 对象、一个 [item 对象](https://docs.scrapy.org/en/latest/topics/items.html#topics-items)、一个 `Request` 对象的可迭代集合和/或 [item 对象](https://docs.scrapy.org/en/latest/topics/items.html#topics-items)，或者返回 `None`。

参数

**response** ([`Response`](https://docs.scrapy.org/en/latest/topics/request-response.html#scrapy.http.Response "scrapy.http.Response")) – 要解析的响应

---

`log(_message_, [_level_], [_component_])`[¶](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.Spider.log "Permalink to this definition")

一个包装函数，通过 Spider 的 [`logger`](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.Spider.logger "scrapy.Spider.logger") 发送日志信息，为了向后兼容而保留。有关更多信息，请参见 [Logging from Spiders](https://docs.scrapy.org/en/latest/topics/logging.html#topics-logging-from-spiders)。

---

`closed(_reason_)`[¶](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.Spider.closed "Permalink to this definition")

当爬虫关闭时调用此方法。该方法提供了一个简便方式连接到 [`spider_closed`](https://docs.scrapy.org/en/latest/topics/signals.html#std-signal-spider_closed) 信号。

我们来看一个例子：

```
import scrapy

class MySpider(scrapy.Spider):
    name = "example.com"
    allowed_domains = ["example.com"]
    start_urls = [
        "http://www.example.com/1.html",
        "http://www.example.com/2.html",
        "http://www.example.com/3.html",
    ]

    def parse(self, response):
        self.logger.info("A response from %s just arrived!", response.url)
```

从单个回调返回多个请求和条目：

```
import scrapy

class MySpider(scrapy.Spider):
    name = "example.com"
    allowed_domains = ["example.com"]
    start_urls = [
        "http://www.example.com/1.html",
        "http://www.example.com/2.html",
        "http://www.example.com/3.html",
    ]

    def parse(self, response):
        for h3 in response.xpath("//h3").getall():
            yield {"title": h3}

        for href in response.xpath("//a/@href").getall():
            yield scrapy.Request(response.urljoin(href), self.parse)
```

你可以直接使用 [`start_requests()`](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.Spider.start_requests "scrapy.Spider.start_requests")，而不是 [`start_urls`](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.Spider.start_urls "scrapy.Spider.start_urls")；为了给数据提供更多结构，你可以使用 `Item` 对象：

```
import scrapy
from myproject.items import MyItem

class MySpider(scrapy.Spider):
    name = "example.com"
    allowed_domains = ["example.com"]

    def start_requests(self):
        yield scrapy.Request("http://www.example.com/1.html", self.parse)
        yield scrapy.Request("http://www.example.com/2.html", self.parse)
        yield scrapy.Request("http://www.example.com/3.html", self.parse)

    def parse(self, response):
        for h3 in response.xpath("//h3").getall():
            yield MyItem(title=h3)

        for href in response.xpath("//a/@href").getall():
            yield scrapy.Request(response.urljoin(href), self.parse)
```

## 爬虫参数[¶](https://docs.scrapy.org/en/latest/topics/spiders.html#spider-arguments "Permalink to this heading")

爬虫可以接收修改其行为的参数。爬虫参数的一些常见用途包括定义起始 URLs 或限制爬取站点的特定部分，但它们也可以用来配置爬虫的任何功能。

爬虫参数是通过 [`crawl`](https://docs.scrapy.org/en/latest/topics/commands.html#std-command-crawl) 命令使用 `-a` 选项传递的。例如：

```
scrapy crawl myspider -a category=electronics
```

爬虫可以在它们的 `__init__` 方法中访问参数：

```
import scrapy

class MySpider(scrapy.Spider):
    name = "myspider"

    def __init__(self, category=None, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.start_urls = [f"http://www.example.com/categories/{category}"]
        # ...
```

默认的 `__init__` 方法将接受任何爬虫参数，并将它们复制为爬虫的属性。上面的例子也可以写成如下形式：

```
import scrapy

class MySpider(scrapy.Spider):
    name = "myspider"

    def start_requests(self):
        yield scrapy.Request(f"http://www.example.com/categories/{self.category}")
```

如果你是通过 [脚本运行 Scrapy](https://docs.scrapy.org/en/latest/topics/practices.html#run-from-script)，可以在调用 [`CrawlerProcess.crawl`](https://docs.scrapy.org/en/latest/topics/api.html#scrapy.crawler.CrawlerProcess.crawl "scrapy.crawler.CrawlerProcess.crawl") 或 [`CrawlerRunner.crawl`](https://docs.scrapy.org/en/latest/topics/api.html#scrapy.crawler.CrawlerRunner.crawl "scrapy.crawler.CrawlerRunner.crawl") 时指定爬虫参数：

```
process = CrawlerProcess()
process.crawl(MySpider, category="electronics")
```

请注意，爬虫参数仅为字符串。爬虫不会自行解析这些参数。如果你通过命令行设置 `start_urls` 属性，你需要自己将其解析为列表，可以使用类似 [`ast.literal_eval()`](https://docs.python.org/3/library/ast.html#ast.literal_eval "(在 Python v3.13 中)") 或 [`json.loads()`](https://docs.python.org/3/library/json.html#json.loads "(在 Python v3.13 中)") 等方法，然后将其设置为属性。否则，会导致对 `start_urls` 字符串的迭代（这是一个非常常见的 Python 陷阱），从而将每个字符都视为一个单独的 URL。

一个有效的使用场景是设置 [`HttpAuthMiddleware`](https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware "scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware") 使用的 HTTP 认证凭证或 [`UserAgentMiddleware`](https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#scrapy.downloadermiddlewares.useragent.UserAgentMiddleware "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware") 使用的用户代理：

```
scrapy crawl myspider -a http_user=myuser -a http_pass=mypassword -a user_agent=mybot
```

爬虫参数也可以通过 Scrapyd 的 `schedule.json` API 传递。请参阅 [Scrapyd 文档](https://scrapyd.readthedocs.io/en/latest/)。

## 通用爬虫[¶](https://docs.scrapy.org/en/latest/topics/spiders.html#generic-spiders "Permalink to this heading")

Scrapy 提供了一些有用的通用爬虫，你可以基于这些爬虫创建子类。它们的目的是为一些常见的爬取场景提供方便的功能，比如根据特定规则跟踪网站上的所有链接、从 [网站地图](https://www.sitemaps.org/index.html) 爬取内容，或解析 XML/CSV 数据流。

在以下爬虫示例中，我们假设你有一个项目，并在 `myproject.items` 模块中声明了一个 `TestItem`：

```
import scrapy

class TestItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
```

### CrawlSpider[¶](https://docs.scrapy.org/en/latest/topics/spiders.html#crawlspider "Permalink to this heading")

_class_ scrapy.spiders.CrawlSpider[\[source\]](https://docs.scrapy.org/en/latest/_modules/scrapy/spiders/crawl.html#CrawlSpider)[¶](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.CrawlSpider "Permalink to this definition")

这是最常用的爬取常规网站的爬虫，因为它提供了一个方便的机制，可以通过定义一组规则来跟踪链接。它可能不适用于你特定的网站或项目，但它对于许多情况足够通用，因此你可以从它开始，根据需要进行覆盖或直接实现自己的爬虫。

除了从 Spider 类继承的必须指定的属性外，此类还支持一个新的属性：

rules[¶](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.CrawlSpider.rules "Permalink to this definition")

这是一个包含一个（或多个）[`Rule`](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.Rule "scrapy.spiders.Rule") 对象的列表。每个 [`Rule`](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.Rule "scrapy.spiders.Rule") 定义了一个爬取网站的行为。`Rule` 对象在下文中进行描述。如果多个规则匹配同一个链接，则按它们在此属性中定义的顺序使用第一个规则。

此爬虫还暴露了一个可重写的方法：

parse_start_url(_response_, _**kwargs_)[\[source\]](https://docs.scrapy.org/en/latest/_modules/scrapy/spiders/crawl.html#CrawlSpider.parse_start_url)[¶](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.CrawlSpider.parse_start_url "Permalink to this definition")

该方法对于爬虫的 `start_urls` 属性中的每个 URL 生成的响应都会被调用。它允许解析初始响应，并且必须返回一个 [item object](https://docs.scrapy.org/en/latest/topics/items.html#topics-items)、一个 `Request` 对象，或包含它们的可迭代对象。

#### 爬取规则[¶](https://docs.scrapy.org/en/latest/topics/spiders.html#crawling-rules "Permalink to this heading")

_class_ scrapy.spiders.Rule(_link_extractor=None_, _callback=None_, _cb_kwargs=None_, _follow=None_, _process_links=None_, _process_request=None_, _errback=None_)[\[source\]](https://docs.scrapy.org/en/latest/_modules/scrapy/spiders/crawl.html#Rule)[¶](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.Rule "Permalink to this definition")

`link_extractor` 是一个 [Link Extractor](https://docs.scrapy.org/en/latest/topics/link-extractors.html#topics-link-extractors) 对象，定义了如何从每个爬取的页面中提取链接。每个生成的链接将用于生成一个 `Request` 对象，链接的文本将包含在其 `meta` 字典中（`link_text` 键下）。如果省略此项，将使用一个默认的链接提取器，该提取器没有任何参数，从而提取所有链接。

`callback` 是一个可调用对象或字符串（在这种情况下，将使用爬虫对象中具有该名称的方法），它将在每个提取的链接上使用指定的链接提取器时被调用。此回调接收一个 [`Response`](https://docs.scrapy.org/en/latest/topics/request-response.html#scrapy.http.Response "scrapy.http.Response") 作为第一个参数，并且必须返回一个 [item objects](https://docs.scrapy.org/en/latest/topics/items.html#topics-items) 和/或 `Request` 对象（或它们的任何子类）的单个实例或可迭代对象。如上所述，接收到的 [`Response`](https://docs.scrapy.org/en/latest/topics/request-response.html#scrapy.http.Response "scrapy.http.Response") 对象将包含生成 `Request` 的链接文本，并在其 `meta` 字典中（`link_text` 键下）。

`cb_kwargs` 是一个字典，包含要传递给回调函数的关键字参数。

`follow` 是一个布尔值，用于指定是否应该从每个使用此规则提取的响应中跟踪链接。如果 `callback` 为 None，则 `follow` 默认为 `True`，否则默认为 `False`。

`process_links` 是一个可调用对象，或字符串（在这种情况下，将使用爬虫对象中具有该名称的方法），该方法将在使用指定的 `link_extractor` 从每个响应中提取的每个链接列表上被调用。它主要用于过滤目的。

`process_request` 是一个可调用对象（或字符串，在这种情况下，将使用爬虫对象中具有该名称的方法），该方法将在通过此规则提取的每个 `Request` 上被调用。此可调用对象应将请求作为第一个参数，并将生成该请求的 [`Response`](https://docs.scrapy.org/en/latest/topics/request-response.html#scrapy.http.Response "scrapy.http.Response") 作为第二个参数。它必须返回一个 `Request` 对象或 `None`（以过滤该请求）。

`errback` 是一个可调用对象或字符串（在这种情况下，将使用爬虫对象中具有该名称的方法），如果在处理由规则生成的请求时引发任何异常，将调用此方法。它接收一个 [`Twisted Failure`](https://docs.twisted.org/en/stable/api/twisted.python.failure.Failure.html "(in Twisted)") 实例作为第一个参数。

警告

由于其内部实现，编写基于 [`CrawlSpider`](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.CrawlSpider "scrapy.spiders.CrawlSpider") 的爬虫时，必须显式设置新请求的回调；否则可能会出现意外行为。

版本 2.0 新增：_errback_ 参数。

#### CrawlSpider 示例[¶](https://docs.scrapy.org/en/latest/topics/spiders.html#crawlspider-example "Permalink to this heading")

现在，让我们来看一个带有规则的 CrawlSpider 示例：

```
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MySpider(CrawlSpider):
    name = "example.com"
    allowed_domains = ["example.com"]
    start_urls = ["http://www.example.com"]

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(allow=(r"category\.php",), deny=(r"subsection\.php",))),
        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(LinkExtractor(allow=(r"item\.php",)), callback="parse_item"),
    )

    def parse_item(self, response):
        self.logger.info("Hi, this is an item page! %s", response.url)
        item = scrapy.Item()
        item["id"] = response.xpath('//td[@id="item_id"]/text()').re(r"ID: (\d+)")
        item["name"] = response.xpath('//td[@id="item_name"]/text()').get()
        item["description"] = response.xpath(
            '//td[@id="item_description"]/text()'
        ).get()
        item["link_text"] = response.meta["link_text"]
        url = response.xpath('//td[@id="additional_data"]/@href').get()
        return response.follow(
            url, self.parse_additional_page, cb_kwargs=dict(item=item)
        )

    def parse_additional_page(self, response, item):
        item["additional_data"] = response.xpath(
            '//p[@id="additional_data"]/text()'
        ).get()
        return item
```

这个爬虫将从 example.com 的主页开始爬取，收集类别链接和项目链接，并使用 `parse_item` 方法解析后者。对于每个项目响应，某些数据将通过 XPath 从 HTML 中提取，并将这些数据填充到 `Item` 中。

### XMLFeedSpider[¶](https://docs.scrapy.org/en/latest/topics/spiders.html#xmlfeedspider "Permalink to this heading")

_class_ scrapy.spiders.XMLFeedSpider[\[source\]](https://docs.scrapy.org/en/latest/_modules/scrapy/spiders/feed.html#XMLFeedSpider)[¶](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.XMLFeedSpider "Permalink to this definition")

XMLFeedSpider 旨在通过特定的节点名称遍历 XML feed。可以选择的迭代器包括：`iternodes`、`xml` 和 `html`。建议出于性能考虑使用 `iternodes` 迭代器，因为 `xml` 和 `html` 迭代器会一次性生成整个 DOM 以进行解析。然而，当解析标记错误的 XML 时，使用 `html` 作为迭代器可能会有所帮助。

要设置迭代器和标签名称，必须定义以下类属性：

iterator[¶](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.XMLFeedSpider.iterator "Permalink to this definition")

一个字符串，用于定义要使用的迭代器。可以是以下之一：

> - `'iternodes'` - 基于正则表达式的快速迭代器
>     
> - `'html'` - 使用 `Selector` 的迭代器。请记住，它使用 DOM 解析，并必须将整个 DOM 加载到内存中，对于大型 feed 可能会成为问题
>     
> - `'xml'` - 使用 `Selector` 的迭代器。请记住，它使用 DOM 解析，并必须将整个 DOM 加载到内存中，对于大型 feed 可能会成为问题
>     

默认为：`'iternodes'`。

itertag[¶](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.XMLFeedSpider.itertag "Permalink to this definition")

一个字符串，定义要遍历的节点（或元素）的名称。例如：

namespaces[¶](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.XMLFeedSpider.namespaces "Permalink to this definition")

一个 `(prefix, uri)` 元组的列表，定义该文档中可用的命名空间，这些命名空间将由该爬虫处理。`prefix` 和 `uri` 将用于通过 `register_namespace()` 方法自动注册命名空间。

然后，您可以在 [`itertag`](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.XMLFeedSpider.itertag "scrapy.spiders.XMLFeedSpider.itertag") 属性中指定带有命名空间的节点。

示例：

```
class YourSpider(XMLFeedSpider):

    namespaces = [('n', 'http://www.sitemaps.org/schemas/sitemap/0.9')]
    itertag = 'n:url'
    # ...
```

除了这些新的属性外，该爬虫还有以下可重写的方法：

adapt_response(_response_)[\[source\]](https://docs.scrapy.org/en/latest/_modules/scrapy/spiders/feed.html#XMLFeedSpider.adapt_response)[¶](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.XMLFeedSpider.adapt_response "Permalink to this definition")

该方法在爬虫从爬虫中间件接收到响应后立即调用，在爬虫开始解析之前。可以用来在解析响应之前修改响应体。此方法接收一个响应并返回一个响应（可能是相同的响应或另一个响应）。

parse_node(_response_, _selector_)[\[source\]](https://docs.scrapy.org/en/latest/_modules/scrapy/spiders/feed.html#XMLFeedSpider.parse_node)[¶](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.XMLFeedSpider.parse_node "Permalink to this definition")

该方法针对匹配提供的标签名（`itertag`）的节点进行调用。接收响应和每个节点的 `Selector`。必须重写此方法，否则爬虫无法工作。此方法必须返回一个 [item 对象](https://docs.scrapy.org/en/latest/topics/items.html#topics-items)、一个 `Request` 对象或包含它们的可迭代对象。

process_results(_response_, _results_)[\[source\]](https://docs.scrapy.org/en/latest/_modules/scrapy/spiders/feed.html#XMLFeedSpider.process_results)[¶](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.XMLFeedSpider.process_results "Permalink to this definition")

该方法针对爬虫返回的每个结果（item 或 request）进行调用，目的是在将结果返回给框架核心之前执行任何最后的处理，例如设置 item ID。它接收结果的列表以及导致这些结果的响应。它必须返回一个结果列表（items 或 requests）。

警告

由于其内部实现，编写基于 [`XMLFeedSpider`](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.XMLFeedSpider "scrapy.spiders.XMLFeedSpider") 的爬虫时，必须显式设置新请求的回调；否则可能会出现意外行为。

#### XMLFeedSpider 示例[¶](https://docs.scrapy.org/en/latest/topics/spiders.html#xmlfeedspider-example "Permalink to this heading")

这些爬虫使用起来非常简单，下面是一个示例：

```
from scrapy.spiders import XMLFeedSpider
from myproject.items import TestItem

class MySpider(XMLFeedSpider):
    name = "example.com"
    allowed_domains = ["example.com"]
    start_urls = ["http://www.example.com/feed.xml"]
    iterator = "iternodes"  # This is actually unnecessary, since it's the default value
    itertag = "item"

    def parse_node(self, response, node):
        self.logger.info(
            "Hi, this is a <%s> node!: %s", self.itertag, "".join(node.getall())
        )

        item = TestItem()
        item["id"] = node.xpath("@id").get()
        item["name"] = node.xpath("name").get()
        item["description"] = node.xpath("description").get()
        return item
```

基本上，我们在上面做的事情是创建了一个爬虫，它从给定的 `start_urls` 下载一个 feed，然后遍历其中每一个 `item` 标签，打印它们，并在一个 `Item` 中存储一些随机数据。

### CSVFeedSpider[¶](https://docs.scrapy.org/en/latest/topics/spiders.html#csvfeedspider "Permalink to this heading")

_class_ scrapy.spiders.CSVFeedSpider[\[source\]](https://docs.scrapy.org/en/latest/_modules/scrapy/spiders/feed.html#CSVFeedSpider)[¶](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.CSVFeedSpider "Permalink to this definition")

这个爬虫与 XMLFeedSpider 非常相似，不同之处在于它是遍历行而不是节点。在每次迭代中调用的方法是 [`parse_row()`](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.CSVFeedSpider.parse_row "scrapy.spiders.CSVFeedSpider.parse_row")。

delimiter[¶](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.CSVFeedSpider.delimiter "Permalink to this definition")

一个字符串，表示 CSV 文件中每个字段的分隔符。默认为 `','`（逗号）。

quotechar[¶](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.CSVFeedSpider.quotechar "Permalink to this definition")

一个字符串，表示 CSV 文件中每个字段的引号字符。默认为 `'"'`（引号）。

一个列表，包含 CSV 文件中的列名。

parse_row(_response_, _row_)[\[source\]](https://docs.scrapy.org/en/latest/_modules/scrapy/spiders/feed.html#CSVFeedSpider.parse_row)[¶](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.CSVFeedSpider.parse_row "Permalink to this definition")

接收一个响应和一个字典（表示每一行），字典的键是 CSV 文件中每个提供（或检测到）的头部。这个爬虫还提供了重写 `adapt_response` 和 `process_results` 方法的机会，用于预处理和后处理。

#### CSVFeedSpider 示例[¶](https://docs.scrapy.org/en/latest/topics/spiders.html#csvfeedspider-example "Permalink to this heading")

让我们来看一个类似于前面的例子，但使用 [`CSVFeedSpider`](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.CSVFeedSpider "scrapy.spiders.CSVFeedSpider"):

```
from scrapy.spiders import CSVFeedSpider
from myproject.items import TestItem

class MySpider(CSVFeedSpider):
    name = "example.com"
    allowed_domains = ["example.com"]
    start_urls = ["http://www.example.com/feed.csv"]
    delimiter = ";"
    quotechar = "'"
    headers = ["id", "name", "description"]

    def parse_row(self, response, row):
        self.logger.info("Hi, this is a row!: %r", row)

        item = TestItem()
        item["id"] = row["id"]
        item["name"] = row["name"]
        item["description"] = row["description"]
        return item
```

### SitemapSpider[¶](https://docs.scrapy.org/en/latest/topics/spiders.html#sitemapspider "Permalink to this heading")

_class_ scrapy.spiders.SitemapSpider[\[source\]](https://docs.scrapy.org/en/latest/_modules/scrapy/spiders/sitemap.html#SitemapSpider)[¶](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.SitemapSpider "Permalink to this definition")

SitemapSpider 允许你通过使用 [Sitemaps](https://www.sitemaps.org/index.html) 来发现并爬取网站的 URL。

它支持嵌套的 sitemap，并能从 [robots.txt](https://www.robotstxt.org/) 中发现 sitemap URLs。

sitemap_urls[¶](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.SitemapSpider.sitemap_urls "Permalink to this definition")

一个 URL 列表，指向你想爬取的 sitemap URLs。

你也可以指向一个 [robots.txt](https://www.robotstxt.org/)，它将被解析以提取其中的 sitemap URLs。

sitemap_rules[¶](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.SitemapSpider.sitemap_rules "Permalink to this definition")

一个包含元组 `(regex, callback)` 的列表，其中：

- `regex` 是用来匹配从 sitemap 中提取的 URLs 的正则表达式。`regex` 可以是字符串或者编译后的正则表达式对象。
- `callback` 是用于处理匹配正则表达式的 URLs 的回调函数。`callback` 可以是一个字符串（表示爬虫方法的名称）或者一个可调用对象。

例如：

```
sitemap_rules = [('/product/', 'parse_product')]
```

规则按顺序应用，只有第一个匹配的规则会被使用。

如果省略此属性，所有在 sitemap 中找到的 URLs 都会使用 `parse` 回调进行处理。

sitemap_follow[¶](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.SitemapSpider.sitemap_follow "Permalink to this definition")

一个正则表达式列表，指定应跟随的 sitemap。这仅适用于使用 [Sitemap 索引文件](https://www.sitemaps.org/protocol.html#index) 指向其他 sitemap 文件的网站。

默认情况下，所有的 sitemap 都会被跟随。

sitemap_alternate_links[¶](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.SitemapSpider.sitemap_alternate_links "Permalink to this definition")

指定是否应跟随同一 `url` 的备用链接。这些链接是指同一网站的其他语言版本，它们在同一 `url` 块中传递。

例如：

```
<url>
    <loc>http://example.com/</loc>
    <xhtml:link rel="alternate" hreflang="de" href="http://example.com/de"/>
</url>
```

启用 `sitemap_alternate_links` 后，这将获取两个 URL。禁用 `sitemap_alternate_links` 时，只会获取 `http://example.com/`。

默认情况下，`sitemap_alternate_links` 是禁用的。

sitemap_filter(_entries_)[\[source\]](https://docs.scrapy.org/en/latest/_modules/scrapy/spiders/sitemap.html#SitemapSpider.sitemap_filter)[¶](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.SitemapSpider.sitemap_filter "Permalink to this definition")

这是一个过滤函数，可以被重写，以便根据 sitemap 条目的属性选择条目。

例如：

```
<url>
    <loc>http://example.com/</loc>
    <lastmod>2005-01-01</lastmod>
</url>
```

我们可以定义一个 `sitemap_filter` 函数，通过日期过滤 `entries`：

```
from datetime import datetime
from scrapy.spiders import SitemapSpider


class FilteredSitemapSpider(SitemapSpider):
    name = "filtered_sitemap_spider"
    allowed_domains = ["example.com"]
    sitemap_urls = ["http://example.com/sitemap.xml"]

    def sitemap_filter(self, entries):
        for entry in entries:
            date_time = datetime.strptime(entry["lastmod"], "%Y-%m-%d")
            if date_time.year >= 2005:
                yield entry
```

这将仅检索在 2005 年及之后修改的 `entries`。

`entries` 是从 sitemap 文档中提取的字典对象。通常，字典的键是标签名，值是标签中的文本。

需要注意的是：

- 由于 `loc` 属性是必需的，因此没有该标签的条目会被丢弃。
- 替代链接存储在以 `alternate` 为键的列表中（见 `sitemap_alternate_links`）。
- 命名空间被移除，因此 lxml 标签名为 `{namespace}tagname` 的标签会变成 `tagname`。

如果忽略此方法，所有在 sitemap 中找到的条目都会被处理，且会考虑其他属性及其设置。

#### SitemapSpider 示例[¶](https://docs.scrapy.org/en/latest/topics/spiders.html#sitemapspider-examples "Permalink to this heading")

最简单的示例：使用 `parse` 回调处理通过 sitemap 发现的所有 URL：

```
from scrapy.spiders import SitemapSpider

class MySpider(SitemapSpider):
    sitemap_urls = ["http://www.example.com/sitemap.xml"]

    def parse(self, response):
        pass  # ... scrape item here ...
```

使用某些回调处理一些 URL，使用其他回调处理其他 URL：

```
from scrapy.spiders import SitemapSpider

class MySpider(SitemapSpider):
    sitemap_urls = ["http://www.example.com/sitemap.xml"]
    sitemap_rules = [
        ("/product/", "parse_product"),
        ("/category/", "parse_category"),
    ]

    def parse_product(self, response):
        pass  # ... scrape product ...

    def parse_category(self, response):
        pass  # ... scrape category ...
```

按照 [robots.txt](https://www.robotstxt.org/) 文件中定义的站点地图，只跟随 URL 中包含 `/sitemap_shop` 的站点地图：

```
from scrapy.spiders import SitemapSpider

class MySpider(SitemapSpider):
    sitemap_urls = ["http://www.example.com/robots.txt"]
    sitemap_rules = [
        ("/shop/", "parse_shop"),
    ]
    sitemap_follow = ["/sitemap_shops"]

    def parse_shop(self, response):
        pass  # ... scrape shop here ...
```

将 SitemapSpider 与其他 URL 来源结合使用：

```
from scrapy.spiders import SitemapSpider

class MySpider(SitemapSpider):
    sitemap_urls = ["http://www.example.com/robots.txt"]
    sitemap_rules = [
        ("/shop/", "parse_shop"),
    ]

    other_urls = ["http://www.example.com/about"]

    def start_requests(self):
        requests = list(super(MySpider, self).start_requests())
        requests += [scrapy.Request(x, self.parse_other) for x in self.other_urls]
        return requests

    def parse_shop(self, response):
        pass  # ... scrape shop here ...

    def parse_other(self, response):
        pass  # ... scrape other here ...
```