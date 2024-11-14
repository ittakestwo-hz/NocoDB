# 如何计算摘要统计

![06_aggregate](06_aggregate.svg)

```
In [1]: import pandas as pd
```

本教程使用[泰坦尼克号数据集](https://github.com/pandas-dev/pandas/raw/main/doc/data/titanic.csv)，数据存储在 CSV 文件中。数据包括以下列：
- PassengerId：每位乘客的 ID。
- Survived：是否幸存的指示符，`0`表示幸存，`1`表示未幸存。
- Pclass：三等票类之一：`1`等、`2`等和`3`等。
- Name：乘客姓名。
- Sex：乘客性别。
- Age：乘客年龄（以年为单位）。
- SibSp：船上兄弟姐妹或配偶的数量。
- Parch：船上父母或孩子的数量。
- Ticket：乘客的票号。
- Fare：票价。
- Cabin：乘客的舱位号。
- Embarked：上船的港口。

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

## 聚合统计

泰坦尼克号乘客的平均年龄是多少？

```
In [4]: titanic["Age"].mean()
Out[4]: np.float64(29.69911764705882)
```

可以对数值列应用不同的统计函数。一般情况下操作会自动忽略缺失数据，并沿行执行。

![06_reduction](06_reduction.svg)

泰坦尼克号乘客的年龄中位数和票价中位数是多少？

```
In [5]: titanic[["Age", "Fare"]].median()
Out[5]: 
Age     28.0000
Fare    14.4542
dtype: float64
```

可以同时为多列计算统计汇总。请记住 `describe` 函数：

```
In [6]: titanic[["Age", "Fare"]].describe()
Out[6]: 
              Age        Fare
count  714.000000  891.000000
mean    29.699118   32.204208
std     14.526497   49.693429
min      0.420000    0.000000
25%     20.125000    7.910400
50%     28.000000   14.454200
75%     38.000000   31.000000
max     80.000000  512.329200
```

使用 `DataFrame.agg()` 方法自定义多列的统计组合：

```
In [7]: 
titanic.agg(
    {
        "Age": ["min", "max", "median", "skew"],
        "Fare": ["min", "max", "median", "mean"],
    }
)
Out[7]: 
              Age        Fare
min      0.420000    0.000000
max     80.000000  512.329200
median  28.000000   14.454200
skew     0.389108         NaN
mean          NaN   32.204208
```

## 按类别分组的聚合统计

![06_groupby](06_groupby.svg)

男性与女性泰坦尼克号乘客的平均年龄分别是多少？

```
In [8]: titanic[["Sex", "Age"]].groupby("Sex").mean()
Out[8]: 
              Age
Sex              
female  27.915709
male    30.726645
```

由于我们感兴趣的是每个性别的平均年龄，因此首先对这两列进行子选择：`titanic[["Sex", "Age"]]`。接下来，在 `Sex` 列上应用 [`groupby()`](https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html../../reference/api/pandas.DataFrame.groupby.html#pandas.DataFrame.groupby "pandas.DataFrame.groupby") 方法，为每个类别创建一个分组。然后计算并返回**每个性别**的平均年龄。

对每个类别（如 `Sex` 列中的男性/女性）计算某一统计量（例如 `mean` 年龄）是一种常见模式。`groupby` 方法用于支持此类操作。这种模式符合更通用的 **“拆分-应用-合并”** 模式：

- **拆分**数据为多个组
- **应用**某个函数到每个组
- **合并**结果到一个数据结构中

在 pandas 中，通常会一起执行应用和合并步骤。

```
In [9]: titanic.groupby("Sex").mean(numeric_only=True)
Out[9]: 
        PassengerId  Survived    Pclass  ...     SibSp     Parch       Fare
Sex                                      ...                               
female   431.028662  0.742038  2.159236  ...  0.694268  0.649682  44.479818
male     454.147314  0.188908  2.389948  ...  0.429809  0.235702  25.523893

[2 rows x 7 columns]
```

获取 `Pclass` 的平均值并没有太大意义。如果我们只对每个性别的平均年龄感兴趣，在分组数据上也可以像平常一样使用方括号 `[]` 进行列选择：

```
In [10]: titanic.groupby("Sex")["Age"].mean()
Out[10]: 
Sex
female    27.915709
male      30.726645
Name: Age, dtype: float64
```

![06_groupby_select_detail](06_groupby_select_detail.svg)

> **注意**
>
> `Pclass` 列包含数值数据，但实际上表示的是 3 个类别（或因子），分别标记为 ‘1’，‘2’ 和 ‘3’。对这些数据计算统计量没有太大意义。因此，pandas 提供了一个 `Categorical` 数据类型来处理此类数据。更多信息请参考用户指南中的 [分类数据](https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html../../user_guide/categorical.html#categorical) 部分。

每种性别和舱位等级组合的平均票价是多少？

```
In [11]: titanic.groupby(["Sex", "Pclass"])["Fare"].mean()
Out[11]: 
Sex     Pclass
female  1         106.125798
        2          21.970121
        3          16.118810
male    1          67.226127
        2          19.741782
        3          12.661633
Name: Fare, dtype: float64
```

可以通过多个列同时进行分组。将列名作为列表提供给 [`groupby()`](https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html../../reference/api/pandas.DataFrame.groupby.html#pandas.DataFrame.groupby "pandas.DataFrame.groupby") 方法。

`前往用户指南` 关于分割-应用-合并方法的完整描述，请参阅用户指南中的 [groupby 操作](https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html../../user_guide/groupby.html#groupby) 部分。

## 按类别统计记录数

![06_valuecounts](06_valuecounts.svg)

每个舱位类别的乘客数量是多少？

```
In [12]: titanic["Pclass"].value_counts()
Out[12]: 
Pclass
3    491
1    216
2    184
Name: count, dtype: int64
```

[`value_counts()`](https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html../../reference/api/pandas.Series.value_counts.html#pandas.Series.value_counts "pandas.Series.value_counts") 方法用于计算列中每个类别的记录数量。

该函数是一个快捷方式，因为它实际上是一个结合了对每个组内记录数量的计数的 `groupby` 操作：

```
In [13]: titanic.groupby("Pclass")["Pclass"].count()
Out[13]: 
Pclass
1    216
2    184
3    491
Name: Pclass, dtype: int64
```

> **注意**
>
> `size` 和 `count` 都可以与 `groupby` 一起使用。`size` 包括 `NaN` 值，并仅提供行数（表的大小），而 `count` 排除了缺失值。在 `value_counts` 方法中，可以使用 `dropna` 参数来包含或排除 `NaN` 值。

`前往用户指南` 用户指南中有专门关于 `value_counts` 的章节，请参阅 [离散化](https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html../../user_guide/basics.html#basics-discretization) 页面。

> **要点概要**
>
> - 聚合统计可应用于整列或整行。
> - `groupby` 实现了**分组-应用-合并**模式。
> - `value_counts` 方便统计每个类别中的条目数量。