# Pandas 处理什么类型的数据？

我想开始使用 pandas。

```
In [1]: import pandas as pd
```

要加载 pandas 包并开始使用它，只需导入该包。社区约定的 pandas 别名是 `pd`，因此在 pandas 文档中，使用 `pd` 来加载 pandas 被认为是标准做法。

## pandas 数据表格表示

![../../_images/01_table_dataframe.svg](https://pandas.pydata.org/docs/_images/01_table_dataframe.svg)

我想存储泰坦尼克号乘客数据。对于一些乘客，我知道姓名（字符）、年龄（整数）和性别（男/女）。

```
In [2]: df = pd.DataFrame(
   ...:     {
   ...:         "Name": [
   ...:             "Braund, Mr. Owen Harris",
   ...:             "Allen, Mr. William Henry",
   ...:             "Bonnell, Miss. Elizabeth",
   ...:         ],
   ...:         "Age": [22, 35, 58],
   ...:         "Sex": ["male", "male", "female"],
   ...:     }
   ...: )
   ...: 

In [3]: df
Out[3]: 
                       Name  Age     Sex
0   Braund, Mr. Owen Harris   22    male
1  Allen, Mr. William Henry   35    male
2  Bonnell, Miss. Elizabeth   58  female
```

要手动存储数据在表格中，创建一个 `DataFrame`。当使用一个包含列表的 Python 字典时，字典的键将用作列标签，每个列表中的值将作为 `DataFrame` 的列。

一个 [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 是一个二维数据结构，可以存储不同类型的数据（包括字符、整数、浮动值、分类数据等）在列中。它类似于电子表格、SQL 表或 R 中的 `data.frame`。

- 该表有 3 列，每列都有一个列标签。列标签分别为 `Name`、`Age` 和 `Sex`。
- 列 `Name` 包含文本数据，每个值是一个字符串，列 `Age` 是数字，列 `Sex` 是文本数据。

在电子表格软件中，我们的数据表格表示将非常相似：

![../../_images/01_table_spreadsheet.png](https://pandas.pydata.org/docs/_images/01_table_spreadsheet.png)

## DataFrame 中的每一列都是一个 Series

![../../_images/01_table_series.svg](https://pandas.pydata.org/docs/_images/01_table_series.svg)

我只对处理 `Age` 列中的数据感兴趣。

```
In [4]: df["Age"]
Out[4]: 
0    22
1    35
2    58
Name: Age, dtype: int64
```

当选择 pandas [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 中的单列时，结果是一个 pandas [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")。要选择列，使用方括号 `[]` 中的列标签。

> **注意**
> 
> 如果你熟悉 Python 的 [字典](https://docs.python.org/3/tutorial/datastructures.html#tut-dictionaries "(在 Python v3.12 中)")，选择单个列非常类似于根据键选择字典值。
>
> 你也可以从头开始创建一个 `Series`：
```
In [5]: ages = pd.Series([22, 35, 58], name="Age")
In [6]: ages
Out[6]: 
0    22
1    35
2    58
Name: Age, dtype: int64
```

一个 pandas `Series` 没有列标签，因为它只是 `DataFrame` 中的一个单独列。`Series` 具有行标签。

## 对 DataFrame 或 Series 进行操作

我想知道乘客的最大年龄。

我们可以在 `DataFrame` 上选择 `Age` 列并应用 `max()`：

```
In [7]: df["Age"].max()
Out[7]: 58
```

或者在 `Series` 上选择:

```
In [8]: ages.max()
Out[8]: 58
```

如 `max()` 方法所示，你可以对 `DataFrame` 或 `Series` 做操作。pandas 提供了许多功能，每个功能都是你可以应用于 `DataFrame` 或 `Series` 的 _方法_。由于方法是函数，别忘了使用括号 `()`。

我对数据表中数值数据的一些基本统计信息感兴趣。

[`describe()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html#pandas.DataFrame.describe "pandas.DataFrame.describe") 方法提供了 `DataFrame` 中数值数据的快速概览。由于 `Name` 和 `Sex` 列是文本数据，这些列默认不会被 [`describe()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html#pandas.DataFrame.describe "pandas.DataFrame.describe") 方法考虑。

---

<span style="display: inline-flex; align-items: center;">
  <img src="https://avatars.githubusercontent.com/u/184599837?v=4" alt="Author" width="32" height="32" style="border-radius: 50%; vertical-align: middle;">
  <strong style="margin-left: 8px;">作者补充</strong>
</span>

```
In [9]: ages.describe()
Out[9]:
count     3.000000
mean     38.333333
std      18.230012
min      22.000000
25%      28.500000
50%      35.000000
75%      46.500000
max      58.000000
Name: Age, dtype: float64
```

---

许多 pandas 操作会返回一个 `DataFrame` 或 `Series`。[`describe()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html#pandas.DataFrame.describe "pandas.DataFrame.describe") 方法是一个返回 pandas `Series` 或 pandas `DataFrame` 的 pandas 操作示例。

> **注意**
>
> 这只是一个起点。与电子表格软件类似，pandas 以表格形式表示数据，并包含列和行。除了表示形式外，你在电子表格软件中进行的数据操作和计算也可以在 pandas 中完成。继续阅读下一教程，开始入门吧！

## 要点总结

- 导入包，即 `import pandas as pd`
- 数据表格存储为 pandas `DataFrame`
- `DataFrame` 中的每一列是一个 `Series`
- 你可以通过对 `DataFrame` 或 `Series` 应用方法来进行操作