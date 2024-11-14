# Scrapy 教程

在本教程中，我们假设您的系统上已安装 Scrapy。如果还没有，请参见 [安装指南](https://docs.scrapy.org/en/latest/intro/install.html#intro-install)。

我们将抓取 [quotes.toscrape.com](https://quotes.toscrape.com/) 这个网站，它列出了名人名言。

本教程将引导您完成以下任务：

1. 创建一个新的 Scrapy 项目
2. 编写一个 [spider](https://docs.scrapy.org/en/latest/topics/spiders.html#topics-spiders) 来抓取网站并提取数据
3. 使用命令行导出抓取的数据
4. 修改 spider 以递归地跟踪链接
5. 使用 spider 参数

Scrapy 是用 [Python](https://www.python.org/) 编写的。如果您刚接触这种语言，可以先了解一下 Python，以便更好地使用 Scrapy。

如果您已熟悉其他编程语言并想快速学习 Python，[Python 教程](https://docs.python.org/3/tutorial) 是一个不错的资源。

如果您是编程新手并希望从 Python 开始，以下书籍可能对您有所帮助：

- [自动化日常任务](https://automatetheboringstuff.com/)
- [像计算机科学家一样思考](http://openbookproject.net/thinkcs/python/english3e/)
- [学习 Python 3 的困难之路](https://learnpythonthehardway.org/python3/)

您还可以参考 [这个 Python 资源列表](https://wiki.python.org/moin/BeginnersGuide/NonProgrammers) 和 [learnpython 子论坛的推荐资源](https://www.reddit.com/r/learnpython/wiki/index#wiki_new_to_python.3F)。

## 创建一个项目[¶](https://docs.scrapy.org/en/latest/intro/tutorial.html#creating-a-project "链接到此标题")

在开始抓取之前，您需要设置一个新的 Scrapy 项目。进入您希望存储代码的目录并运行：

```
scrapy startproject tutorial
```

这将创建一个名为 `tutorial` 的目录，包含以下内容：

```
tutorial/
    scrapy.cfg            # 部署配置文件
    tutorial/             # 项目的 Python 模块，您将在此导入代码
        __init__.py
        items.py          # 项目 item 定义文件
        middlewares.py    # 项目中间件文件
        pipelines.py      # 项目管道文件
        settings.py       # 项目设置文件
        spiders/          # 目录，稍后您将把您的 spiders 放入此处
            __init__.py
```

## 我们的第一个 Spider[¶](https://docs.scrapy.org/en/latest/intro/tutorial.html#our-first-spider "链接到此标题")

Spider 是您定义的类，Scrapy 使用它从网站抓取信息。它们必须继承 [`Spider`](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.Spider "scrapy.Spider") 并定义初始请求、可选的链接跟踪方式以及解析页面内容以提取数据的方式。

以下是我们第一个 Spider 的代码。将其保存为 `quotes_spider.py` 文件，放在项目的 `tutorial/spiders` 目录下：

```
from pathlib import Path
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/2/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
```

如您所见，我们的 Spider 继承了 [`scrapy.Spider`](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.Spider "scrapy.Spider") 并定义了一些属性和方法：
- [`name`](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.Spider.name "scrapy.Spider.name")：标识 Spider。它在项目中必须是唯一的，即不同的 Spiders 不能设置相同的名称。
- [`start_requests()`](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.Spider.start_requests "scrapy.Spider.start_requests")：必须返回一个 Request 可迭代对象（可以返回请求列表或编写生成器函数），Spider 将从这些请求开始爬取。后续请求将由这些初始请求逐步生成。
- [`parse()`](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.Spider.parse "scrapy.Spider.parse")：该方法将在为每个请求下载的响应处理时调用。response 参数是一个 [`TextResponse`](https://docs.scrapy.org/en/latest/topics/request-response.html#scrapy.http.TextResponse "scrapy.http.TextResponse") 实例，包含页面内容并提供更多便于处理的方法。

### 如何运行我们的 spider[¶](https://docs.scrapy.org/en/latest/intro/tutorial.html#how-to-run-our-spider "链接到此标题")

要让我们的 spider 工作，请转到项目的顶级目录并运行以下命令：

```
scrapy crawl quotes
```

此命令运行我们刚刚添加的名为 `quotes` 的 spider，它将发送一些请求到 `quotes.toscrape.com` 域。您将得到类似如下的输出：

```
... (省略部分内容)
2016-12-16 21:24:05 [scrapy.core.engine] INFO: Spider opened
2016-12-16 21:24:05 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2016-12-16 21:24:05 [scrapy.extensions.telnet] DEBUG: Telnet console listening on 127.0.0.1:6023
2016-12-16 21:24:05 [scrapy.core.engine] DEBUG: Crawled (404) <GET https://quotes.toscrape.com/robots.txt> (referer: None)
2016-12-16 21:24:05 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://quotes.toscrape.com/page/1/> (referer: None)
2016-12-16 21:24:05 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://quotes.toscrape.com/page/2/> (referer: None)
2016-12-16 21:24:05 [quotes] DEBUG: Saved file quotes-1.html
2016-12-16 21:24:05 [quotes] DEBUG: Saved file quotes-2.html
2016-12-16 21:24:05 [scrapy.core.engine] INFO: Closing spider (finished)
...
```

现在，请检查当前目录中的文件。您应该会注意到创建了两个新文件：_quotes-1.html_ 和 _quotes-2.html_，包含相应 URL 的内容，如我们的 `parse` 方法所指示。