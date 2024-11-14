# 安装 lxml

## 目录

1. [安装lxml](#安装lxml)
2. [要求](#要求)
3. [安装](#安装)
4. [从开发源构建lxml](#从开发源构建lxml)
5. [在MS Windows上的源代码构建](#在MS-Windows上的源代码构建)

## 获取位置

lxml 通常通过 [PyPI](http://pypi.python.org/pypi/lxml) 进行分发。

大多数 **Linux** 平台都提供了某个版本的 lxml，通常为 python-lxml（Python 2.x 版本）和 python3-lxml（Python 3.x 版本）。如果可以使用该版本，安装 lxml 的最快方式是使用系统的包管理器，例如在 Debian/Ubuntu 上使用 apt-get：

```
sudo apt-get install python3-lxml
```

对于 **MacOS-X**，提供了 lxml 的 [macport](http://macports.org/) 版本。可以尝试以下命令：

```
sudo port install py27-lxml
```

要安装更新版本或在其他系统上安装 lxml，请参见下文。

## 要求

lxml 5.0 及更高版本需要 Python 3.6+。lxml 5.0 之前的版本支持 Python 2.7 和 3.6+。

除非你使用的是静态二进制发行版（例如来自 Windows 二进制安装程序），否则 lxml 需要安装 libxml2 和 libxslt，特别是：

- [libxml2](http://xmlsoft.org/) 版本 2.9.2 或更高版本。
- [libxslt](http://xmlsoft.org/XSLT/) 版本 1.1.27 或更高版本。
    - 我们推荐使用 libxslt 1.1.28 或更高版本。

新版本通常包含较少的错误，因此推荐使用。libxml2 还在继续进行 XML Schema 支持的开发，因此新版本会提供更好的 W3C 规范兼容性。

要在 Linux 系统上安装这些依赖项的开发包，请使用你所在发行版的安装工具，例如在 Debian/Ubuntu 上使用 apt-get：

```
sudo apt-get install libxml2-dev libxslt-dev python-dev
```

对于基于 Debian 的系统，安装已知的 lxml 包的构建依赖项应该足够，例如：

```
sudo apt-get build-dep python3-lxml
```

## 安装

如果系统没有提供二进制包，或者你希望安装更新版本，最好的方式是使用 [pip](http://pypi.python.org/pypi/pip) 包管理工具（或使用 [virtualenv](https://pypi.python.org/pypi/virtualenv)），然后运行以下命令：

```
pip install lxml
```

如果你没有在 virtualenv 中使用 pip，而是希望全局安装 lxml，你需要以管理员身份运行上述命令，例如在 Linux 上：

```
sudo pip install lxml
```

要安装特定版本，可以手动下载发行版并让 pip 安装，或者将所需的版本传递给 pip：

```
pip install lxml==5.0.0
```

为了加速测试环境中的构建，例如在持续集成服务器上，可以通过设置 CFLAGS 环境变量来禁用 C 编译器优化：

```
CFLAGS="-O0" pip install lxml
```

（该选项表示“零优化”）。

## MS Windows

对于 MS Windows，我们尽力提供包含较新库的二进制 wheel，尽管你可能仍然希望查看相关的 [常见问题条目](https://lxml.de/FAQ.html#where-are-the-binary-builds)。由于在 Windows 上构建软件通常较为困难，库版本（libxml2、libxslt、libiconv、zlib）可能与 Linux 或 macOS 上的版本不一致。这通常意味着 [WinLibs 项目](https://github.com/orgs/winlibs) 尚未更新他们的仓库。如果你需要更新的版本，请向他们报告更新请求。

## Linux

在 Linux（以及大多数其他良好支持的操作系统）上，只要正确安装了 libxml2 和 libxslt（包括开发包，例如头文件等），pip 就能够构建源代码发行版。请参见上述要求部分，并使用你所在系统的包管理工具查找如 libxml2-dev 或 libxslt-devel 的包。如果构建失败，请确保它们已安装。

另外，通过设置 STATIC_DEPS=true，可以自动下载并构建这两个库的最新版本，例如：

```
STATIC_DEPS=true pip install lxml
```

## MacOS-X

在 MacOS-X 上，我们提供了二进制 wheel（对于 Python 3.9+ 为 "universal2"），所以只需使用：

```
sudo pip3 install lxml
```

要构建源代码发行版，请使用以下命令，并确保你有一个有效的 Internet 连接，因为这将下载 libxml2 和 libxslt 以构建它们：

```
STATIC_DEPS=true sudo pip install lxml
```

## 从开发源代码构建 lxml

如果你希望从 GitHub 仓库构建 lxml，应该阅读 [如何从源代码构建 lxml](https://lxml.de/build.html)（或者源代码树中的 doc/build.txt 文件）。从开发者源代码或修改后的发行源代码构建需要 [Cython](http://www.cython.org/) 来将 lxml 源代码转换为 C 代码。源代码发行版附带了预生成的 C 源文件，因此你不需要安装 Cython 来从发布源代码构建。

如果你阅读了这些说明后仍然无法安装 lxml，你可以查阅 [邮件列表](http://lxml.de/mailinglist/) 归档，看是否有人遇到过相同的问题，或者发送邮件到邮件列表。

## 与 python-libxml2 一起使用 lxml

如果你希望将 lxml 与官方的 libxml2 Python 绑定一起使用（可能是因为你的某个依赖使用了它），你必须构建静态版本的 lxml。否则，这两个包将在 libxml2 库要求全局配置的地方发生冲突，可能会导致功能消失或发生崩溃。

要获取静态构建，可以将 `--static-deps` 选项传递给 `setup.py` 脚本，或者设置 STATIC_DEPS 或 STATICBUILD 环境变量为 true，例如：

```
STATIC_DEPS=true pip install lxml
```

STATICBUILD 环境变量与 STATIC_DEPS 变量的处理方式相同，但也会被其他扩展包使用。

## 在 MS Windows 上构建源代码

大多数 MS Windows 系统缺乏构建软件所需的工具，从 C 编译器开始。微软通常要求用户自行安装和配置这些工具，而这通常并不简单，也意味着分发者不能依赖这些依赖项在系统上可用。可以说，你得到了你所付出的，其他人也为此付出代价。

由于该平台缺少包管理工具，最佳的方式是在决定从源代码构建时，将库依赖静态链接，而不是使用二进制安装程序。为此，lxml 可以使用 [libxml2 和 libxslt 的二进制分发版本](http://www.zlatkovic.com/libxml.en.html)，并在静态构建过程中自动下载。它需要 libxml2 和 libxslt，以及 iconv 和 zlib，这些都可以从同一下载站点获取。进一步的构建说明见 [源代码构建文档](https://lxml.de/build.html)。

## 在 MacOS-X 上构建源代码

如果你不使用 macports 或希望使用更新版本的 lxml，你必须自己构建它。虽然最近的 MacOS-X 版本中预安装的 libxml2 和 libxslt 系统库比以前不那么过时，因此 lxml 应该能够直接与它们一起工作，但仍然建议使用静态构建，搭配最新的库版本。

幸运的是，lxml 的 `setup.py` 脚本内置了支持在构建过程中静态构建并集成这些库。请阅读 [MacOS-X 构建说明](https://lxml.de/build.html#building-lxml-on-macos-x)。