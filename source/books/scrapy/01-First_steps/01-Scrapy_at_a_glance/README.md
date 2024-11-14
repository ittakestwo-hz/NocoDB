# Scrapy 概览

Scrapy (/ˈskreɪpaɪ/) 是一个用于爬取网站并提取结构化数据的应用框架，这些数据可以广泛应用于数据挖掘、信息处理或历史归档等场景。

尽管 Scrapy 最初设计用于 [网页抓取](https://en.wikipedia.org/wiki/Web_scraping)，它同样可以通过 API（如 [Amazon Associates Web Services](https://affiliate-program.amazon.com/gp/advertising/api/detail/main.html)）提取数据，或作为一个通用的网络爬虫使用。

## 示例蜘蛛的演练

为了展示 Scrapy 的功能，我们将通过一个简单的 Scrapy Spider 示例来展示其工作方式。

下面是一个抓取 [https://quotes.toscrape.com](https://quotes.toscrape.com/) 网站上名人名言的爬虫代码，支持分页功能：

```python
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/tag/humor/",
    ]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "author": quote.xpath("span/small/text()").get(),
                "text": quote.css("span.text::text").get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
```

将此代码保存为 `quotes_spider.py`，然后使用 [`runspider`](https://docs.scrapy.org/en/latest/topics/commands.html#std-command-runspider) 命令运行：

```
scrapy runspider quotes_spider.py -o quotes.jsonl
```

运行结束后，你将在 `quotes.jsonl` 文件中看到包含文本和作者信息的 JSON Lines 格式的名言列表，内容如下所示：

```
{"author": "Jane Austen", "text": "“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”"}
{"author": "Steve Martin", "text": "“A day without sunshine is like, you know, night.”"}
{"author": "Garrison Keillor", "text": "“Anyone who thinks sitting in church can make you a Christian must also think that sitting in a garage can make you a car.”"}
...
```

### 刚刚发生了什么？

当你运行命令 `scrapy runspider quotes_spider.py` 时，Scrapy 会查找其中定义的 Spider 并通过其爬虫引擎执行。

爬虫开始时会向 `start_urls` 属性中定义的 URL 发送请求（在本例中是幽默类别的名言页面），并调用默认的回调方法 `parse`，将响应对象作为参数传递。在 `parse` 回调中，我们使用 CSS 选择器遍历名言元素，生成包含名言文本和作者的字典，查找下一页链接并使用相同的 `parse` 方法回调调度新的请求。

Scrapy 的一个主要优势是请求是 [异步调度和处理](https://docs.scrapy.org/en/latest/topics/architecture.html#topics-architecture) 的。这意味着 Scrapy 不必等待请求完成就能发送其他请求或执行其他操作，即使请求失败或处理时发生错误，也不会影响其他请求的继续。

这种机制让你能够进行非常快速的爬取（同时发送多个并发请求并具备容错能力），同时 Scrapy 还允许通过 [一些设置](https://docs.scrapy.org/en/latest/topics/settings.html#topics-settings-ref) 控制爬取的礼貌性。你可以设置每个请求之间的下载延迟、限制每个域或 IP 的并发请求数量，甚至可以使用 [自动节流扩展](https://docs.scrapy.org/en/latest/topics/autothrottle.html#topics-autothrottle) 自动调节这些参数。

注意

这里使用了 [feed 导出](https://docs.scrapy.org/en/latest/topics/feed-exports.html#topics-feed-exports) 生成 JSON 文件，你可以轻松更改导出格式（如 XML 或 CSV）或存储后端（如 FTP 或 [Amazon S3](https://aws.amazon.com/s3/)）。你还可以编写 [item pipeline](https://docs.scrapy.org/en/latest/topics/item-pipeline.html#topics-item-pipeline) 将数据存入数据库。

## 还有什么？

你已经了解了如何使用 Scrapy 从网站提取并存储项目，但这只是开始。Scrapy 提供了许多强大的功能，使抓取变得简单高效，例如：

- 内置的 [选择和提取](https://docs.scrapy.org/en/latest/topics/selectors.html#topics-selectors) 功能，支持从 HTML/XML 源中使用扩展的 CSS 选择器和 XPath 表达式，并通过正则表达式提取数据。  
- [交互式 Shell 控制台](https://docs.scrapy.org/en/latest/topics/shell.html#topics-shell)（支持 IPython），用于尝试 CSS 和 XPath 表达式，便于编写和调试爬虫。
- 内置的 [多格式 feed 导出](https://docs.scrapy.org/en/latest/topics/feed-exports.html#topics-feed-exports) 支持，支持多种存储后端（FTP、S3、本地文件系统）。
- 强大的编码支持和自动检测，处理外来、非标准和破损的编码声明。
- [强大的扩展支持](https://docs.scrapy.org/en/latest/index.html#extending-scrapy)，允许使用 [signals](https://docs.scrapy.org/en/latest/topics/signals.html#topics-signals) 和 API（中间件、[扩展](https://docs.scrapy.org/en/latest/topics/extensions.html#topics-extensions)和 [pipelines](https://docs.scrapy.org/en/latest/topics/item-pipeline.html#topics-item-pipeline)）插入自定义功能。
- 内置的扩展和中间件广泛支持：
  - Cookie 和会话处理
  - HTTP 功能（如压缩、身份验证、缓存）
  - 用户代理伪装
  - robots.txt
  - 爬取深度限制
  - 以及更多功能

- [Telnet 控制台](https://docs.scrapy.org/en/latest/topics/telnetconsole.html#topics-telnetconsole)，允许在 Scrapy 进程中挂载 Python 控制台，便于检视和调试爬虫。

- 其他实用功能，例如可复用的爬虫，用于从 [Sitemaps](https://www.sitemaps.org/index.html) 和 XML/CSV feed 中爬取站点、媒体管道用于 [自动下载图片](https://docs.scrapy.org/en/latest/topics/media-pipeline.html#topics-media-pipeline)（或其他与抓取项目相关的媒体）、缓存 DNS 解析器等。

## 接下来做什么？

接下来的步骤是 [安装 Scrapy](https://docs.scrapy.org/en/latest/intro/install.html#intro-install)、[完成教程](https://docs.scrapy.org/en/latest/intro/tutorial.html#intro-tutorial) 以学习如何创建一个完整的 Scrapy 项目，并 [加入社区](https://scrapy.org/community/)。感谢您的关注！