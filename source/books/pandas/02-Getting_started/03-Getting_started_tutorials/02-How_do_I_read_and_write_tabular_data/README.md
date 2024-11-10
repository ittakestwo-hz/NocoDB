# 如何读取和写入表格数据？

```
In [1]: import pandas as pd
```

本教程使用的是存储为CSV格式的[泰坦尼克号数据集](https://github.com/pandas-dev/pandas/raw/main/doc/data/titanic.csv)。数据包含以下列：

- PassengerId：每个乘客的ID。
- Survived：表示乘客是否生还。`0` 表示生还，`1` 表示未生还。
- Pclass：三种票类中的一种：1号舱、2号舱和3号舱。
- Name：乘客的姓名。
- Sex：乘客的性别。
- Age：乘客的年龄（以年为单位）。
- SibSp：同行的兄弟姐妹或配偶数量。
- Parch：同行的父母或孩子数量。
- Ticket：乘客的票号。
- Fare：票价。
- Cabin：乘客的舱位号。
- Embarked：登船港口。
![../../_images/02_io_readwrite.svg](https://pandas.pydata.org/docs/_images/02_io_readwrite.svg)

我想分析泰坦尼克号乘客数据。

先将它存储为CSV文件。

```
In [2]: titanic = pd.read_csv("data/titanic.csv")
```

pandas 提供了 [`read_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv "pandas.read_csv") 函数来读取存储为CSV文件的数据到 pandas `DataFrame` 中。pandas 支持许多不同的文件格式或数据源（如CSV、Excel、SQL、JSON、Parquet等），每种格式都有相应的 `read_*` 前缀。

确保在读取数据后总是检查数据。当显示 `DataFrame` 时，默认会显示前5行和最后5行：

```
In [3]: titanic
Out[3]: 
     PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0              1         0       3  ...   7.2500   NaN         S
1              2         1       1  ...  71.2833   C85         C
2              3         1       3  ...   7.9250   NaN         S
3              4         1       1  ...  53.1000  C123         S
4              5         0       3  ...   8.0500   NaN         S
..           ...       ...     ...  ...      ...   ...       ...
886          887         0       2  ...  13.0000   NaN         S
887          888         1       1  ...  30.0000   B42         S
888          889         0       3  ...  23.4500   NaN         S
889          890         1       1  ...  30.0000  C148         C
890          891         0       3  ...   7.7500   NaN         Q

[891 rows x 12 columns]
```

我想查看 pandas ``DataFrame` 的前8行。

```
In [4]: titanic.head(8)
Out[4]: 
   PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
1            2         1       1  ...  71.2833   C85         C
2            3         1       3  ...   7.9250   NaN         S
3            4         1       1  ...  53.1000  C123         S
4            5         0       3  ...   8.0500   NaN         S
5            6         0       3  ...   8.4583   NaN         Q
6            7         0       1  ...  51.8625   E46         S
7            8         0       3  ...  21.0750   NaN         S

[8 rows x 12 columns]
```
要查看 `DataFrame` 的前 N 行，可以使用 [`head()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html#pandas.DataFrame.head "pandas.DataFrame.head") 方法，并将所需的行数（此例中为8）作为参数。

> **注意**
>
> 如果你想查看最后的 N 行，pandas 也提供了 [`tail()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.tail.html#pandas.DataFrame.tail "pandas.DataFrame.tail") 方法。例如，`titanic.tail(10)` 将返回 `DataFrame` 的最后10行。

---

<span style="display: inline-flex; align-items: center;">
  <img src="https://avatars.githubusercontent.com/u/184599837?v=4" alt="Author" width="32" height="32" style="border-radius: 50%; vertical-align: middle;">
  <strong style="margin-left: 8px;">作者补充</strong>
</span>

![tail()](titanic.tail(10).png)

---

可以通过请求 pandas `dtypes` 属性来检查 pandas 如何解释每一列的数据类型：

```
In [6]: titanic.dtypes
Out[6]: 
PassengerId      int64
Survived         int64
Pclass           int64
Name            object
Sex             object
Age            float64
SibSp            int64
Parch            int64
Ticket          object
Fare           float64
Cabin           object
Embarked        object
dtype: object
```

每一列所使用的数据类型被列出。该 `DataFrame` 中的数据类型包括整数（`int64`）、浮点数（`float64`）和字符串（`object`）。

> **注意**
>
> 当请求 `dtypes` 时，不需要加`()`！`dtypes` 是 `DataFrame` 和 `Series` 的一个属性。`DataFrame` 或 `Series` 的属性不需要`()`。属性表示 `DataFrame`/`Series` 的特性，而方法（需要`()`）是对 `DataFrame`/`Series` 执行某些操作的方法，如在 [2.3.2 Pandas 处理什么类型的数据？](http://localhost:3000/books/pandas/Getting_started/Getting_started_tutorials/What_kind_of_data_does_pandas_handle/index.html) 中介绍的。

我的同事要求将泰坦尼克号数据保存为电子表格。

---

<span style="display: inline-flex; align-items: center;">
  <img src="https://avatars.githubusercontent.com/u/184599837?v=4" alt="Author" width="32" height="32" style="border-radius: 50%; vertical-align: middle;">
  <strong style="margin-left: 8px;">作者补充</strong>
</span>

```
In [7]: pip install -q openpyxl
In [8]: titanic.to_excel("data/titanic.xlsx", sheet_name="passengers", index=False)
```

---

对于 `read_*` 函数用于读取数据，`to_*` 方法用于存储数据。[`to_excel()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html#pandas.DataFrame.to_excel "pandas.DataFrame.to_excel") 方法将数据存储为 Excel 文件。在此示例中，`sheet_name` 设置为 _passengers_，而不是默认的 _Sheet1_。通过设置 `index=False`，行索引标签不会保存到电子表格中。

等效的读取函数 `read_excel()` 将重新加载数据到 `DataFrame`：

```
In [9]: titanic = pd.read_excel("data/titanic.xlsx", sheet_name="passengers")
```

```
In [10]: titanic.head()
Out[10]: 
   PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
1            2         1       1  ...  71.2833   C85         C
2            3         1       3  ...   7.9250   NaN         S
3            4         1       1  ...  53.1000  C123         S
4            5         0       3  ...   8.0500   NaN         S
[5 rows x 12 columns]
```

我想查看 `DataFrame` 的技术摘要。

```
In [11]: titanic.info()
Out[11]:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  891 non-null    int64  
 1   Survived     891 non-null    int64  
 2   Pclass       891 non-null    int64  
 3   Name         891 non-null    object 
 4   Sex          891 non-null    object 
 5   Age          714 non-null    float64
 6   SibSp        891 non-null    int64  
 7   Parch        891 non-null    int64  
 8   Ticket       891 non-null    object 
 9   Fare         891 non-null    float64
 10  Cabin        204 non-null    object 
 11  Embarked     889 non-null    object 
dtypes: float64(2), int64(5), object(5)
memory usage: 83.7+ KB
```

`info()` 方法是查看 `DataFrame` 的技术摘要的好方法。