# 如何选择 DataFrame 的子集？

```
In [1]: import pandas as pd
```

本教程使用的是存储为CSV格式的[泰坦尼克号数据集](https://github.com/pandas-dev/pandas/raw/main/doc/data/titanic.csv)。数据包含以下列：

- PassengerId：每个乘客的 ID。 
- Survived：表示乘客是否幸存。`0` 表示是，`1` 表示否。
- Pclass：票务类别，分为 1 类、2 类和 3 类。
- Name：乘客的姓名。  
- Sex：乘客的性别。 
- Age：乘客的年龄（以年为单位）。 
- SibSp：同行的兄弟姐妹或配偶数量。 
- Parch：同行的父母或子女数量。 
- Ticket：乘客的票号。 
- Fare：票价。 
- Cabin：乘客的舱位。 
- Embarked：登船港口。
    
```
In [2]: titanic = pd.read_csv("data/titanic.csv")

In [3]: titanic.head()
Out[3]: 
   PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
1            2         1       1  ...  71.2833   C85         C
2            3         1       3  ...   7.9250   NaN         S
3            4         1       1  ...  53.1000  C123         S
4            5         0       3  ...   8.0500   NaN         S

[5 rows x 12 columns]   
```

## 如何选择 DataFrame 中的特定列？

![选择列](https://pandas.pydata.org/docs/_images/03_subset_columns.svg)

我对泰坦尼克号乘客的年龄感兴趣。
    
```
In [4]: ages = titanic["Age"]

In [5]: ages.head()
Out[5]: 
0    22.0
1    38.0
2    26.0
3    35.0
4    35.0
Name: Age, dtype: float64
```
    
要选择单列，可以使用方括号 `[]` 包含列名。
    
每一列都是一个 [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series)。选择单列时，返回的是 pandas 的 [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series)。我们可以通过检查输出的类型来验证这一点：

```
In [6]: type(titanic["Age"])
Out[6]: pandas.core.series.Series
```

同时，查看输出的 `shape`：

```
In [7]: titanic["Age"].shape
Out[7]: (891,)
```

[`DataFrame.shape`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html#pandas.DataFrame.shape) 是 pandas `Series` 和 `DataFrame` 的一个属性，包含行数和列数：_(nrows, ncolumns)_。pandas 的 `Series` 是一维的，只有行数会返回。

我对泰坦尼克号乘客的年龄和性别感兴趣。
    
```
In [8]: age_sex = titanic[["Age", "Sex"]]
In [9]: age_sex.head()
Out[9]: 
    Age     Sex
0  22.0    male
1  38.0  female
2  26.0  female
3  35.0  female
4  35.0    male
```
    
要选择多列，可以在选择方括号 `[]` 内部使用列名的列表。

> **注意**
>
> 内部的方括号定义了一个 [Python 列表](https://docs.python.org/3/tutorial/datastructures.html#tut-morelists)，而外部的方括号用于从 pandas `DataFrame` 中选择数据，如上例所示。
> 
> 返回的数据类型是 pandas 的 `DataFrame`：

```
In [10]: type(titanic[["Age", "Sex"]])
Out[10]: pandas.core.frame.DataFrame
```

```
In [11]: titanic[["Age", "Sex"]].shape
Out[11]: (891, 2)
```

查询结果返回的是一个具有 891 行和 2 列的 `DataFrame`。

> **要点概要**
>
> `DataFrame` 是二维的，包含行和列。

## 如何过滤 DataFrame 中的特定行？

![过滤行](https://pandas.pydata.org/docs/_images/03_subset_rows.svg)

我对 35 岁以上的乘客感兴趣。
    
```
In [12]: above_35 = titanic[titanic["Age"] > 35]
In [13]: above_35.head()
Out[13]: 
    PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
1             2         1       1  ...  71.2833   C85         C
6             7         0       1  ...  51.8625   E46         S
11           12         1       1  ...  26.5500  C103         S
13           14         0       3  ...  31.2750   NaN         S
15           16         1       2  ...  16.0000   NaN         S

[5 rows x 12 columns]
```
    
要根据条件表达式选择行，可以在选择方括号 `[]` 中使用条件。
    

选择方括号中的条件 `titanic["Age"] > 35` 用来检查 `Age` 列中哪些行的值大于 35：

```
In [14]: titanic["Age"] > 35
Out[14]: 
0      False
1       True
2      False
3      False
4      False
       ...  
886    False
887    False
888    False
889    False
890    False
Name: Age, Length: 891, dtype: bool
```

条件表达式的输出（`>`，也可以是 `==`、`!=`、`<`、`<=` 等）实际上是一个 pandas `Series`，包含与原始 `DataFrame` 相同数量的布尔值（`True` 或 `False`）。这种布尔值的 `Series` 可以用于过滤 `DataFrame`，通过将其放入选择方括号 `[]` 中。只有值为 `True` 的行会被选中。

我们从前面知道，原始的泰坦尼克 `DataFrame` 有 891 行。我们可以通过检查 `above_35` 结果的 `shape` 属性来查看满足条件的行数：

```
In [15]: above_35.shape
Out[15]: (217, 12)
```

我对 2 类和 3 类的乘客感兴趣。
    
```
In [14]: titanic["Age"] > 35
Out[14]: 
0      False
1       True
2      False
3      False
4      False
       ...  
886    False
887    False
888    False
889    False
890    False
Name: Age, Length: 891, dtype: bool
```
    
条件表达式（如 `>`，以及 `==`、`!=`、`<`、`<=` 等）输出实际上是一个包含布尔值（`True` 或 `False`）的 pandas `Series`，其行数与原始的 `DataFrame` 相同。这样的布尔 `Series` 可以用于过滤 `DataFrame`，只需将其放在选择括号 `[]` 中。只有值为 `True` 的行会被选中。

我们知道原始的泰坦尼克号 `DataFrame` 包含 891 行。通过检查生成的 `DataFrame` `above_35` 的 `shape` 属性，我们可以看看满足条件的行数。

```
In [15]: above_35.shape
Out[15]: (217, 12)
```

我对舱位等级为 2 和 3 的泰坦尼克号乘客感兴趣。

```
In [16]: class_23 = titanic[titanic["Pclass"].isin([2, 3])]
In [17]: class_23.head()
Out[17]: 
   PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
2            3         1       3  ...   7.9250   NaN         S
4            5         0       3  ...   8.0500   NaN         S
5            6         0       3  ...   8.4583   NaN         Q
7            8         0       3  ...  21.0750   NaN         S

[5 rows x 12 columns]
```

与条件表达式类似，[`isin()`](https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html../../reference/api/pandas.Series.isin.html#pandas.Series.isin "pandas.Series.isin") 条件函数会对每一行的值是否在提供的列表中返回 `True`。要基于这样的函数过滤行，可以将条件函数放入选择括号 `[]` 中。在这种情况下，选择括号中的条件 `titanic["Pclass"].isin([2, 3])` 检查 `Pclass` 列的值是否为 2 或 3。

以上方式等同于过滤舱位等级为 2 或 3 的行，并用 `|`（或）运算符组合这两个条件。

```
In [18]: class_23 = titanic[(titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)]
In [19]: class_23.head()
Out[19]: 
   PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
2            3         1       3  ...   7.9250   NaN         S
4            5         0       3  ...   8.0500   NaN         S
5            6         0       3  ...   8.4583   NaN         Q
7            8         0       3  ...  21.0750   NaN         S

[5 rows x 12 columns]
```

`前往用户指南` 请参阅用户指南中的章节 [关于不同的索引选择](https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html../../user_guide/indexing.html#indexing-choice)，以更深入地了解 `loc` 和 `iloc` 的用法。

> **要点概括**
>
> - 选择数据的子集时，使用方括号 `[]`。
> - 在这些方括号内，可以使用单个列/行标签、列/行标签列表、标签范围、条件表达式或冒号。
> - 使用 `loc` 通过行和列的名称选择特定的行和/或列。
> - 使用 `iloc` 通过表格中的位置选择特定的行和/或列。
> - 您可以基于 `loc`/`iloc` 为选择的部分赋予新值。

`前往用户指南` 用户指南页面上的 [索引和选择数据](https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html../../user_guide/indexing.html#indexing) 提供了索引的完整概述。