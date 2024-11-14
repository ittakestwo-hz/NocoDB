# 安装指南

## 支持的 Python 版本

Scrapy 需要 Python 3.8 及以上的版本，支持默认的 CPython 和 PyPy 实现（参见[其他实现](https://docs.python.org/3/reference/introduction.html#implementations)）。

## 安装 Scrapy

如果您使用 [Anaconda](https://docs.anaconda.com/anaconda/) 或 [Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)，可以从 [conda-forge](https://conda-forge.org/) 频道安装适用于 Linux、Windows 和 macOS 的最新包。

通过 `conda` 安装 Scrapy：

```
conda install -c conda-forge scrapy
```

或者，如果您熟悉 Python 包的安装，可以通过 PyPI 安装 Scrapy 及其依赖项。**建议将 Scrapy 安装在[专用的 virtualenv](https://docs.scrapy.org/en/latest/intro/install.html#intro-using-virtualenv) 中**，以避免与系统包发生冲突。

### 需了解的内容

Scrapy 完全使用 Python 编写，依赖以下关键 Python 包：

- [lxml](https://lxml.de/index.html)：高效的 XML 和 HTML 解析器
- [parsel](https://pypi.org/project/parsel/)：基于 lxml 的 HTML/XML 数据提取库
- [w3lib](https://pypi.org/project/w3lib/)：处理 URL 和网页编码的多功能辅助工具
- [twisted](https://twistedmatrix.com/trac/)：异步网络框架
- [cryptography](https://cryptography.io/en/latest/) 和 [pyOpenSSL](https://pypi.org/project/pyOpenSSL/)：用于网络安全的依赖项

其中部分包依赖于非 Python 包，可能需要额外的安装步骤。请查看[平台特定指南](https://docs.scrapy.org/en/latest/intro/install.html#intro-install-platform-notes)。

### 使用虚拟环境（推荐）

我们推荐在所有平台上将 Scrapy 安装在虚拟环境中，而不是系统范围内安装。**虚拟环境**允许您避免与系统包冲突（可能会破坏系统工具和脚本），并且可以在其中使用 `pip` 正常安装包。

创建虚拟环境后，您可以使用 `pip` 在其中安装 Scrapy。对于非 Python 依赖项，请参阅[平台特定指南](https://docs.scrapy.org/en/latest/intro/install.html#intro-install-platform-notes)。

## 平台特定的安装说明

### Windows

建议在 Windows 上通过 [Anaconda](https://docs.anaconda.com/anaconda/) 或 [Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) 使用 `conda-forge` 频道来安装 Scrapy，以避免大多数安装问题。

如果使用 `pip` 安装 Scrapy，需先安装 “Microsoft Visual C++” 构建工具（需较多磁盘空间）。步骤如下：

1. 下载并执行 [Microsoft C++ 构建工具](https://visualstudio.microsoft.com/visual-cpp-build-tools/) 以安装 Visual Studio 安装程序。
2. 在工作负载部分选择 **C++ 构建工具**，并确保选择以下可选组件：
    - **MSVC**（如 MSVC v142 - VS 2019 C++ x64/x86 构建工具）
    - **Windows SDK**（如 Windows 10 SDK (10.0.18362.0)）
3. 安装 Visual Studio 构建工具。

### Ubuntu 14.04 或以上

不要使用 Ubuntu 提供的 `python-scrapy` 包。建议通过以下命令安装 Scrapy 的依赖项：

```
sudo apt-get install python3 python3-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
```

在虚拟环境中，可使用 `pip` 安装 Scrapy。

### macOS

macOS 上通常使用 Apple 的 Xcode 开发工具来提供 C 编译器和开发头文件。遇到的常见问题包括：

**不要使用系统自带的 Python**。建议使用 [homebrew](https://brew.sh/) 安装独立的 Python 版本，避免系统冲突。通过以下命令更新 `PATH` 变量：

  ```
  echo "export PATH=/usr/local/bin:/usr/local/sbin:$PATH" >> ~/.bashrc
  ```

### PyPy

建议使用最新的 PyPy 版本。Linux 上测试通过，macOS 上可能需要 `brew install openssl` 来解决依赖项问题。

## 故障排除

### AttributeError: 'module' object has no attribute 'OP_NO_TLSv1_1'

如果您安装或升级了 Scrapy、Twisted 或 pyOpenSSL，可能会遇到此错误。原因是系统或虚拟环境中的 pyOpenSSL 版本不兼容。