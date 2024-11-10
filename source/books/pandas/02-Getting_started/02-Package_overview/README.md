# 包概览

pandas 是一个 [Python](https://www.python.org/) 包，提供了快速、灵活且表达性强的数据结构，旨在使处理“关系型”或“标记”数据变得简单直观。它的目标是成为进行实际 **真实世界** 数据分析的基础高层构建模块。此外，它还具有更广泛的目标，即成为 **任何语言中最强大、最灵活的开源数据分析/处理工具**。它已经在朝着这个目标迈进。

pandas 非常适合处理各种不同类型的数据：

> - 带有不同类型列的表格数据，例如 SQL 表或 Excel 表格
> - 有序和无序（不一定是固定频率）的时间序列数据
> - 任意矩阵数据（无论是同质类型还是异质类型），带有行和列标签
> - 任何其他形式的观察性/统计数据集。数据不必被标记，也能被放入 pandas 数据结构中

pandas 的两个主要数据结构，[`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")（1 维）和 [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")（2 维），涵盖了金融、统计学、社会科学和许多工程领域的绝大多数典型用例。对于 R 用户，[`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 提供了 R 中 `data.frame` 所提供的一切功能，并且更多。pandas 构建于 [NumPy](https://numpy.org/) 之上，旨在与科学计算环境中的许多其他第三方库良好集成。

以下是 pandas 擅长的一些功能：

> - 轻松处理 **缺失数据**（表示为 NaN），无论是浮动点数据还是非浮动点数据
> - 大小可变性：可以 **插入和删除** DataFrame 和更高维度对象中的列
> - 自动和显式的 **数据对齐**：对象可以显式地对齐到一组标签，或者用户可以忽略标签，让 `Series`、`DataFrame` 等自动在计算中对齐数据
> - 强大且灵活的 **分组** 功能，执行分割-应用-组合操作，用于聚合和转换数据
> - 轻松将不规则、索引不同的数据结构转换为 DataFrame 对象
> - 智能的基于标签的 **切片**、**花式索引** 和 **子集操作**
> - 直观的 **合并** 和 **连接** 数据集
> - 灵活的数据集 **重塑** 和透视
> - **层次化** 的轴标签（每个刻度可能有多个标签）
> - 强大的 IO 工具，能够加载来自 **平面文件**（CSV 和分隔符文件）、Excel 文件、数据库的数据，并从超快速的 **HDF5 格式** 保存/加载数据
> - **时间序列** 特定功能：日期范围生成和频率转换、移动窗口统计、日期平移和滞后

这些原则大多数是为了应对其他语言/科学研究环境中常遇到的问题。对于数据科学家来说，处理数据通常分为多个阶段：数据清理与处理、分析/建模，然后将分析结果组织成适合绘图或表格显示的形式。pandas 是进行这些任务的理想工具。

其他注意事项：

> - pandas **速度很快**。许多底层算法已经在 [Cython](https://cython.org/) 代码中进行了优化。然而，像其他通用工具一样，通常在通用化的同时会牺牲一些性能。所以，如果你将应用专注于某个功能，可能会创建一个更快的专用工具。
> - pandas 是 [statsmodels](https://www.statsmodels.org/) 的依赖项，成为了 Python 中统计计算生态系统的重要部分。
> - pandas 已在金融应用中广泛投入生产使用。

## 数据结构[#](https://pandas.pydata.org/docs/getting_started/overview.html#data-structures "Link to this heading")

以下是您提供内容的 Markdown 表格：

| 维度       | 名称      | 描述                                                                         |
|------------|-----------|-----------------------------------------------------------------------------|
| 1          | Series    | 1D 标记的同质类型数组                                                         |
| 2          | DataFrame | 一般的 2D 标记的、大小可变的表格结构，列类型可能是异质的                     |

### 为什么需要多种数据结构？[#](https://pandas.pydata.org/docs/getting_started/overview.html#why-more-than-one-data-structure "Link to this heading")

理解 pandas 数据结构的最好方式是将它们看作是用于存储低维数据的灵活容器。例如，DataFrame 是 Series 的容器，而 Series 是标量的容器。我们希望能够像操作字典一样插入和移除这些容器中的对象。

此外，我们希望对于常见的 API 函数具有合理的默认行为，这些函数需要考虑到时间序列和横截面数据集的典型方向。当使用 N 维数组（ndarrays）存储 2D 和 3D 数据时，用户需要考虑数据集的方向，写函数时必须考虑轴的作用；在 pandas 中，轴的意义更多地是为了赋予数据更多的语义；也就是说，对于特定的数据集，可能会有一种“正确”的数据方向。我们的目标是减少在后续函数中进行数据转换时所需要的思考量。

例如，对于表格数据（DataFrame），将其视为 **索引**（行）和 **列** 要比看作轴 0 和轴 1 更有语义。在迭代 DataFrame 的列时，代码会更具可读性：

```
for col in df.columns:
    series = df[col]
    # do something with series
```

## 数据的可变性和复制[#](https://pandas.pydata.org/docs/getting_started/overview.html#mutability-and-copying-of-data "Link to this heading")

所有 pandas 数据结构都是值可变的（它们包含的值可以被修改），但并不总是大小可变的。Series 的长度不能改变，但例如可以向 DataFrame 中插入列。然而，绝大多数方法都会生成新对象，且不改变输入数据。一般来说，我们倾向于在合适的地方 **优先使用不可变性**。

## 获取支持[#](https://pandas.pydata.org/docs/getting_started/overview.html#getting-support "Link to this heading")

处理 pandas 问题和想法的首选途径是 [GitHub 问题跟踪器](https://github.com/pandas-dev/pandas/issues)。如果你有一般问题，可以通过 [Stack Overflow](https://stackoverflow.com/questions/tagged/pandas) 向 pandas 社区专家求助。

## 项目治理[#](https://pandas.pydata.org/docs/getting_started/overview.html#project-governance "Link to this heading")

自 2008 年项目成立以来，pandas 项目的治理流程已经非正式地进行了，现已在 [项目治理文档](https://github.com/pandas-dev/pandas/blob/main/web/pandas/about/governance.md) 中正式化。这些文档明确了如何做决策以及我们社区的各个部分如何互动，包括开源协作开发与可能由营利性或非营利实体资助的工作的关系。

Wes McKinney 是终身独裁者（BDFL）。

## 开发团队[#](https://pandas.pydata.org/docs/getting_started/overview.html#development-team "Link to this heading")

核心团队成员的名单和更多详细信息可以在 [pandas 网站](https://pandas.pydata.org/about/team.html) 找到。

## 合作伙伴[#](https://pandas.pydata.org/docs/getting_started/overview.html#institutional-partners "Link to this heading")

当前合作伙伴的信息可以在 [pandas 网站页面](https://pandas.pydata.org/about/sponsors.html) 找到。

## 许可[#](https://pandas.pydata.org/docs/getting_started/overview.html#license "Link to this heading")

---

BSD 3-Clause 许可协议

版权 (c) 2008-2011, AQR Capital Management, LLC, Lambda Foundry, Inc. 和 PyData 开发团队
保留所有权利。

版权 (c) 2011-2023, 开源贡献者。

在符合以下条件的情况下，可以重新分发和使用源代码及二进制形式，是否修改均可：

* 源代码的重新分发必须保留上述版权声明、此条件列表和以下免责声明。
* 二进制形式的重新分发必须在随分发提供的文档和/或其他材料中复制上述版权声明、此条件列表和以下免责声明。
* 未经授权的使用名称“pandas”来推销衍生产品需要经过授权。

此许可证不提供对任何专利的任何权利。(**[本许可证全文](https://opensource.org/licenses/BSD-3-Clause)**)

---

### 贡献[#](https://pandas.pydata.org/docs/getting_started/overview.html#contributing "Link to this heading")

想要贡献代码、文档或问题报告？你可以访问 [pandas GitHub](https://github.com/pandas-dev/pandas) 页面，参与其中。