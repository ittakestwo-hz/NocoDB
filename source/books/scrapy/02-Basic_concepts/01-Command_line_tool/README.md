# 命令行工具¶

Scrapy 通过 `scrapy` 命令行工具进行控制，在这里我们将其称为“Scrapy 工具”，以区别于子命令，我们通常将子命令称为“命令”或“Scrapy 命令”。

Scrapy 工具提供了多个命令，用于不同的目的，每个命令接受不同的参数和选项。

（`scrapy deploy` 命令在 1.0 版本中已被移除，取而代之的是独立的 `scrapyd-deploy`。详见 [部署你的项目](https://scrapyd.readthedocs.io/en/latest/deploy.html)。）

## 配置设置¶

Scrapy 会在标准位置查找配置参数，使用 ini 风格的 `scrapy.cfg` 文件：

1.  `/etc/scrapy.cfg` 或 `c:\scrapy\scrapy.cfg`（系统范围的配置），
2.  `~/.config/scrapy.cfg` (`$XDG_CONFIG_HOME`) 和 `~/.scrapy.cfg` (`$HOME`)（全局（用户范围）设置），
3.  Scrapy 项目的根目录中的 `scrapy.cfg`（见下一节）。

这些文件中的设置会按照优先顺序合并：用户定义的值优先于系统范围的默认值，项目范围的设置会覆盖所有其他设置（如果已定义）。

Scrapy 还支持通过多个环境变量进行配置。目前支持的环境变量有：

- `SCRAPY_SETTINGS_MODULE`（参见 [指定设置模块](https://docs.scrapy.org/en/latest/topics/commands.htmlsettings.html#topics-settings-module-envvar)）
- `SCRAPY_PROJECT`（参见 [在项目间共享根目录](https://docs.scrapy.org/en/latest/topics/commands.html#topics-project-envvar)）
- `SCRAPY_PYTHON_SHELL`（参见 [Scrapy shell](https://docs.scrapy.org/en/latest/topics/commands.htmlshell.html#topics-shell)）

## Scrapy 项目的默认结构¶

在深入了解命令行工具及其子命令之前，我们首先了解一下 Scrapy 项目的目录结构。

尽管可以修改，但所有 Scrapy 项目默认的文件结构都相同，类似于以下结构：

```
scrapy.cfg
myproject/
    __init__.py
    items.py
    middlewares.py
    pipelines.py
    settings.py
    spiders/
        __init__.py
        spider1.py
        spider2.py
        ...
```

`scrapy.cfg` 文件所在的目录被称为 _项目根目录_。该文件包含定义项目设置的 Python 模块的名称。以下是一个示例：

```
[settings]
default = myproject.settings
```

## 在多个项目之间共享根目录¶

一个项目根目录（包含 `scrapy.cfg` 的目录）可以被多个 Scrapy 项目共享，每个项目都有自己的设置模块。

在这种情况下，您必须在 `scrapy.cfg` 文件中的 `[settings]` 部分为这些设置模块定义一个或多个别名：

```
[settings]
default = myproject1.settings
project1 = myproject1.settings
project2 = myproject2.settings
```

默认情况下，`scrapy` 命令行工具将使用 `default` 设置。可以使用 `SCRAPY_PROJECT` 环境变量指定 `scrapy` 使用其他项目：

```
$ scrapy settings --get BOT_NAME
Project 1 Bot
$ export SCRAPY_PROJECT=project2
$ scrapy settings --get BOT_NAME
Project 2 Bot
```

## 使用 `scrapy` 工具

您可以通过不带任何参数运行 Scrapy 工具，它将打印一些使用帮助信息和可用的命令：

```
Scrapy X.Y - no active project

Usage:
  scrapy <command> [options] [args]

Available commands:
  crawl         Run a spider
  fetch         Fetch a URL using the Scrapy downloader
[...]
```

第一行将打印当前激活的项目，如果您位于一个 Scrapy 项目中。在这个例子中，它是在项目外部运行的。如果从项目内部运行，它将打印类似以下内容：

```
Scrapy X.Y - project: myproject

Usage:
  scrapy <command> [options] [args]

[...]
```

### 创建项目

使用 `scrapy` 工具时，通常首先要做的事情就是创建 Scrapy 项目：

```
scrapy startproject myproject [project_dir]
```

这将会在 `project_dir` 目录下创建一个 Scrapy 项目。如果没有指定 `project_dir`，则默认 `project_dir` 会与 `myproject` 相同。

接下来，你进入新的项目目录：

然后，你就可以在这个目录下使用 `scrapy` 命令来管理和控制你的项目了。

### 控制项目

你可以在项目目录中使用 `scrapy` 工具来控制和管理你的项目。

例如，创建一个新的爬虫：

```
scrapy genspider mydomain mydomain.com
```

一些 Scrapy 命令（例如 [`crawl`](https://docs.scrapy.org/en/latest/topics/commands.html#std-command-crawl)）必须在 Scrapy 项目内部运行。有关哪些命令必须在项目内部运行，哪些不需要，更多信息请参阅下面的 [命令参考](https://docs.scrapy.org/en/latest/topics/commands.html#topics-commands-ref)。

另外，请记住，一些命令在项目内部运行时可能会有些不同的行为。例如，`fetch` 命令会使用爬虫重写的行为（例如使用 `user_agent` 属性来覆盖用户代理），如果正在获取的 URL 与某个特定的爬虫相关联。这是故意的，因为 `fetch` 命令旨在用于检查爬虫下载页面的方式。

## 可用工具命令

本节包含了可用的内置命令列表，每个命令都附带了描述和一些使用示例。记住，你可以通过运行以下命令获取每个命令的更多信息：

```
scrapy <command> -h
```

你还可以通过运行以下命令查看所有可用命令：

```
scrapy -h
```

Scrapy 命令分为两种类型：仅在 Scrapy 项目内部有效的命令（项目特定命令）和在没有激活 Scrapy 项目的情况下也能使用的命令（全局命令）。不过，它们在项目内部运行时可能会有所不同（因为它们会使用项目中重写的设置）。

全局命令：

- [`startproject`](https://docs.scrapy.org/en/latest/topics/commands.html#std-command-startproject)
- [`genspider`](https://docs.scrapy.org/en/latest/topics/commands.html#std-command-genspider)
- [`settings`](https://docs.scrapy.org/en/latest/topics/commands.html#std-command-settings)
- [`runspider`](https://docs.scrapy.org/en/latest/topics/commands.html#std-command-runspider)
- [`shell`](https://docs.scrapy.org/en/latest/topics/commands.html#std-command-shell)
- [`fetch`](https://docs.scrapy.org/en/latest/topics/commands.html#std-command-fetch)
- [`view`](https://docs.scrapy.org/en/latest/topics/commands.html#std-command-view)
- [`version`](https://docs.scrapy.org/en/latest/topics/commands.html#std-command-version)

仅限项目的命令：

- [`crawl`](https://docs.scrapy.org/en/latest/topics/commands.html#std-command-crawl)
- [`check`](https://docs.scrapy.org/en/latest/topics/commands.html#std-command-check)
- [`list`](https://docs.scrapy.org/en/latest/topics/commands.html#std-command-list)
- [`edit`](https://docs.scrapy.org/en/latest/topics/commands.html#std-command-edit)
- [`parse`](https://docs.scrapy.org/en/latest/topics/commands.html#std-command-parse)
- [`bench`](https://docs.scrapy.org/en/latest/topics/commands.html#std-command-bench)
    

### startproject[¶](https://docs.scrapy.org/en/latest/topics/commands.html#startproject "Permalink to this heading")

- 语法: `scrapy startproject <project_name> [project_dir]`
- 需要项目: _否_

创建一个新的 Scrapy 项目，项目名为 `project_name`，位于 `project_dir` 目录下。如果没有指定 `project_dir`，则 `project_dir` 将与 `project_name` 相同。

使用示例：

```
$ scrapy startproject myproject
```

### genspider[¶](https://docs.scrapy.org/en/latest/topics/commands.html#genspider "Permalink to this heading")

- 语法: `scrapy genspider [-t template] <name> <domain 或 URL>`
- 需要项目: _否_

版本 2.6.0 新增功能：可以传递 URL 而不是域名。

在当前文件夹中，或在项目内部的 `spiders` 文件夹中创建一个新的爬虫（如果从项目内部调用）。`<name>` 参数将被设置为爬虫的 `name`，而 `<domain 或 URL>` 用于生成爬虫的 `allowed_domains` 和 `start_urls` 属性。

使用示例：

```
$ scrapy genspider -l
Available templates:
  basic
  crawl
  csvfeed
  xmlfeed

$ scrapy genspider example example.com
Created spider 'example' using template 'basic'

$ scrapy genspider -t crawl scrapyorg scrapy.org
Created spider 'scrapyorg' using template 'crawl'
```

这只是一个用于基于预定义模板创建爬虫的便捷快捷命令，但绝不是创建爬虫的唯一方式。你完全可以自己创建爬虫源代码文件，而不使用这个命令。

### crawl[¶](https://docs.scrapy.org/en/latest/topics/commands.html#crawl "Permalink to this heading")

- 语法: `scrapy crawl <spider>`
- 需要项目: _是_

使用爬虫开始爬取。

支持的选项：

- `-h, --help`: 显示帮助信息并退出
- `-a NAME=VALUE`: 设置爬虫参数（可以重复）
- `--output FILE` 或 `-o FILE`: 将抓取的项目追加到文件的末尾（使用 `-` 表示输出到标准输出），通过在输出 URI 后加冒号来定义格式（例如 `-o FILE:FORMAT`）
- `--overwrite-output FILE` 或 `-O FILE`: 将抓取的项目写入文件，覆盖任何现有文件，通过在输出 URI 后加冒号来定义格式（例如 `-O FILE:FORMAT`）
- `--output-format FORMAT` 或 `-t FORMAT`: 定义用于输出项目的格式的过时方式，不能与 `-O` 一起使用

使用示例：

```
$ scrapy crawl myspider
[ ... myspider starts crawling ... ]

$ scrapy crawl -o myfile:csv myspider
[ ... myspider starts crawling and appends the result to the file myfile in csv format ... ]

$ scrapy crawl -O myfile:json myspider
[ ... myspider starts crawling and saves the result in myfile in json format overwriting the original content... ]

$ scrapy crawl -o myfile -t csv myspider
[ ... myspider starts crawling and appends the result to the file myfile in csv format ... ]
```

### check[¶](https://docs.scrapy.org/en/latest/topics/commands.html#check "Permalink to this heading")

- 语法: `scrapy check [-l] <spider>`
- 需要项目: _是_

运行契约检查。

使用示例：

```
$ scrapy check -l
first_spider
  * parse
  * parse_item
second_spider
  * parse
  * parse_item

$ scrapy check
[FAILED] first_spider:parse_item
>>> 'RetailPricex' field is missing

[FAILED] first_spider:parse
>>> Returned 92 requests, expected 0..4
```

### list[¶](https://docs.scrapy.org/en/latest/topics/commands.html#list "Permalink to this heading")

- 语法: `scrapy list`
- 需要项目: _是_

列出当前项目中所有可用的蜘蛛。输出每行一个蜘蛛。

使用示例：

```
$ scrapy list
spider1
spider2
```

### edit[¶](https://docs.scrapy.org/en/latest/topics/commands.html#edit "Permalink to this heading")

- 语法: `scrapy edit <spider>`
- 需要项目: _是_

使用在 `EDITOR` 环境变量中定义的编辑器编辑指定的蜘蛛（如果未设置，则使用 [`EDITOR`](https://docs.scrapy.org/en/latest/topics/settings.html#std-setting-EDITOR) 设置的编辑器）。

此命令仅作为常用情况的便捷快捷方式提供，开发者当然可以选择任何工具或集成开发环境（IDE）来编写和调试蜘蛛。

使用示例：

```
scrapy edit spider1
```

### fetch[¶](https://docs.scrapy.org/en/latest/topics/commands.html#fetch "Permalink to this heading")

- 语法: `scrapy fetch <url>`
- 需要项目: _否_

使用 Scrapy 下载器下载给定的 URL，并将内容写入标准输出。

这个命令的有趣之处在于，它以蜘蛛下载页面的方式来抓取页面。例如，如果蜘蛛有一个 `USER_AGENT` 属性用于覆盖 User Agent，它会使用该属性中的值。

因此，这个命令可以用来“查看”蜘蛛如何抓取某个页面。

如果在项目外使用，则不会应用特定于蜘蛛的行为，它将使用默认的 Scrapy 下载器设置。

支持的选项：

- `--spider=SPIDER`：绕过蜘蛛自动检测，强制使用指定的蜘蛛
- `--headers`：打印响应的 HTTP 头部，而不是响应体
- `--no-redirect`：不跟随 HTTP 3xx 重定向（默认情况下会跟随）

使用示例：

```
$ scrapy fetch --nolog http://www.example.com/some/page.html
[ ... html content here ... ]

$ scrapy fetch --nolog --headers http://www.example.com/
{'Accept-Ranges': ['bytes'],
 'Age': ['1263   '],
 'Connection': ['close     '],
 'Content-Length': ['596'],
 'Content-Type': ['text/html; charset=UTF-8'],
 'Date': ['Wed, 18 Aug 2010 23:59:46 GMT'],
 'Etag': ['"573c1-254-48c9c87349680"'],
 'Last-Modified': ['Fri, 30 Jul 2010 15:30:18 GMT'],
 'Server': ['Apache/2.2.3 (CentOS)']}
```

### view

- 语法：`scrapy view <url>`
- 需要项目：_否_

在浏览器中打开给定的 URL，就像您的 Scrapy 蜘蛛“看到”它一样。有时蜘蛛看到的页面与普通用户看到的不同，因此可以用来检查蜘蛛“看到”的内容，并确认是否符合预期。

支持的选项：

- `--spider=SPIDER`：绕过蜘蛛自动检测，强制使用指定的蜘蛛
- `--no-redirect`：不跟随 HTTP 3xx 重定向（默认情况下会跟随）

使用示例：

```
$ scrapy view http://www.example.com/some/page.html
[ ... browser starts ... ]
```

### shell

- 语法：`scrapy shell [url]`
- 需要项目：_否_

启动 Scrapy shell 来处理给定的 URL（如果提供了 URL）或者为空（如果未提供 URL）。也支持 UNIX 风格的本地文件路径，既可以是相对路径（带 `./` 或 `../` 前缀）也可以是绝对路径。更多信息请参见 [Scrapy shell](https://docs.scrapy.org/en/latest/topics/shell.html#topics-shell)。

支持的选项：

- `--spider=SPIDER`：绕过蜘蛛自动检测，强制使用指定的蜘蛛
- `-c code`：在 shell 中评估代码，打印结果并退出
- `--no-redirect`：不跟随 HTTP 3xx 重定向（默认情况下会跟随）；此选项只影响命令行中传递的 URL 参数；一旦进入 shell，`fetch(url)` 仍会默认跟随 HTTP 重定向。

使用示例：

```
$ scrapy shell http://www.example.com/some/page.html
[ ... scrapy shell starts ... ]

$ scrapy shell --nolog http://www.example.com/ -c '(response.status, response.url)'
(200, 'http://www.example.com/')

# shell follows HTTP redirects by default
$ scrapy shell --nolog http://httpbin.org/redirect-to?url=http%3A%2F%2Fexample.com%2F -c '(response.status, response.url)'
(200, 'http://example.com/')

# you can disable this with --no-redirect
# (only for the URL passed as command line argument)
$ scrapy shell --no-redirect --nolog http://httpbin.org/redirect-to?url=http%3A%2F%2Fexample.com%2F -c '(response.status, response.url)'
(302, 'http://httpbin.org/redirect-to?url=http%3A%2F%2Fexample.com%2F')
```

### parse

- 语法：`scrapy parse <url> [选项]`
- 需要项目：_是_

获取给定的 URL，并使用与之相关的蜘蛛进行解析，采用通过 `--callback` 选项传递的方法，若未给出，则使用 `parse` 方法。

支持的选项：

- `--spider=SPIDER`：绕过蜘蛛自动检测，强制使用指定的蜘蛛
- `--a NAME=VALUE`：设置蜘蛛参数（可以重复）
- `--callback` 或 `-c`：用于解析响应的回调蜘蛛方法
- `--meta` 或 `-m`：将额外的请求元数据传递给回调请求。这必须是有效的 JSON 字符串。例如：`--meta='{"foo" : "bar"}'`
- `--cbkwargs`：将额外的关键字参数传递给回调。这必须是有效的 JSON 字符串。例如：`--cbkwargs='{"foo" : "bar"}'`
- `--pipelines`：通过管道处理抓取的项目
- `--rules` 或 `-r`：使用 [`CrawlSpider`](https://docs.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.CrawlSpider "scrapy.spiders.CrawlSpider") 规则发现用于解析响应的回调（即蜘蛛方法）
- `--noitems`：不显示抓取的项目
- `--nolinks`：不显示提取的链接
- `--nocolour`：避免使用 pygments 为输出添加颜色
- `--depth` 或 `-d`：递归跟踪请求的深度级别（默认：1）
- `--verbose` 或 `-v`：显示每个深度级别的详细信息
- `--output` 或 `-o`：将抓取的项目输出到文件

版本 2.3 中新增。

使用示例：

```
$ scrapy parse http://www.example.com/ -c parse_item
[ ... scrapy log lines crawling example.com spider ... ]

>>> STATUS DEPTH LEVEL 1 <<<
# Scraped Items  ------------------------------------------------------------
[{'name': 'Example item',
 'category': 'Furniture',
 'length': '12 cm'}]

# Requests  -----------------------------------------------------------------
[]
```

### settings

- 语法：`scrapy settings [选项]`
- 需要项目：_否_

获取 Scrapy 设置的值。

如果在项目内使用，它将显示项目设置的值，否则它将显示该设置的默认 Scrapy 值。

使用示例：

```
$ scrapy settings --get BOT_NAME
scrapybot
$ scrapy settings --get DOWNLOAD_DELAY
0
```

### runspider

- 语法：`scrapy runspider <spider_file.py>`
- 需要项目：_否_

运行一个自包含的 Python 文件中的蜘蛛，无需创建项目。

使用示例：

```
$ scrapy runspider myspider.py
[ ... spider starts crawling ... ]
```

### version

- 语法：`scrapy version [-v]`
- 需要项目：_否_

打印 Scrapy 版本。如果使用 `-v`，它还会打印 Python、Twisted 和平台信息，这对于报告错误非常有用。

### bench

- 语法：`scrapy bench`
- 需要项目：_否_

运行一个快速的基准测试。[基准测试](https://docs.scrapy.org/en/latest/topics/benchmarking.html#benchmarking)。

## 自定义项目命令

您还可以通过使用 [`COMMANDS_MODULE`](https://docs.scrapy.org/en/latest/topics/commands.html#std-setting-COMMANDS_MODULE) 设置来添加自定义项目命令。有关如何实现自定义命令的示例，请参阅 Scrapy 命令在 [scrapy/commands](https://github.com/scrapy/scrapy/tree/master/scrapy/commands) 中的实现。

### COMMANDS\_MODULE

默认值：`''`（空字符串）

用于查找自定义 Scrapy 命令的模块。此模块用于为您的 Scrapy 项目添加自定义命令。

示例：

```
COMMANDS_MODULE = "mybot.commands"
```

### 通过 setup.py 入口点注册命令

您还可以通过在库的 `setup.py` 文件的入口点中添加 `scrapy.commands` 部分，来添加来自外部库的 Scrapy 命令。

以下示例添加了 `my_command` 命令：

```
from setuptools import setup, find_packages

setup(
    name="scrapy-mymodule",
    entry_points={
        "scrapy.commands": [
            "my_command=my_scrapy_module.commands:MyCommand",
        ],
    },
)
```