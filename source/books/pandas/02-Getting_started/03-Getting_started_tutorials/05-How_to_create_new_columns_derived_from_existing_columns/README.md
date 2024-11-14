# 如何创建由现有列派生的新列

![../../_images/05_newcolumn_1.svg](https://pandas.pydata.org/docs/_images/05_newcolumn_1.svg)

```
In [1]: import pandas as pd
```

本教程使用了 [OpenAQ](https://openaq.org/) 提供的[空气质量数据](https://github.com/pandas-dev/pandas/tree/main/doc/data/air_quality_no2.csv)，并借助 [py-openaq](http://dhhagan.github.io/py-openaq/index.html) 包。数据集 `air_quality_no2.csv` 包含巴黎（_FR04014_）、安特卫普（_BETR801_）和伦敦（_London Westminster_）的测量站数据。

```
In [2]: air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)
In [3]: air_quality.head()
Out[3]: 
                     station_antwerp  station_paris  station_london
datetime                                                           
2019-05-07 02:00:00              NaN            NaN            23.0
2019-05-07 03:00:00             50.5           25.0            19.0
2019-05-07 04:00:00             45.0           27.7            19.0
2019-05-07 05:00:00              NaN           50.4            16.0
2019-05-07 06:00:00              NaN           61.9             NaN
```

我想用 mg/m³ 表示伦敦站 NO₂ 的浓度。（假设温度为 25°C、气压为 1013 hPa，转换因子为 1.882）

```
In [4]: air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882
In [5]: air_quality.head()
Out[5]: 
                     station_antwerp  ...  london_mg_per_cubic
datetime                              ...                     
2019-05-07 02:00:00              NaN  ...               43.286
2019-05-07 03:00:00             50.5  ...               35.758
2019-05-07 04:00:00             45.0  ...               35.758
2019-05-07 05:00:00              NaN  ...               30.112
2019-05-07 06:00:00              NaN  ...                  NaN

[5 rows x 4 columns]
```

要创建新列，可使用 `[]` 括号，左侧为新列名。

> **注意**
>
> 值的计算是 **逐元素** 的，即所有列中的值都乘以 1.882。无需逐行循环！

![../../_images/05_newcolumn_2.svg](https://pandas.pydata.org/docs/_images/05_newcolumn_2.svg)

我想检查巴黎与安特卫普站值的比率，并将结果保存在新列中。

```
In [6]: 
air_quality["ratio_paris_antwerp"] = (
    air_quality["station_paris"] / air_quality["station_antwerp"]
)
In [7]: air_quality.head()
Out[7]: 
                     station_antwerp  ...  ratio_paris_antwerp
datetime                              ...                     
2019-05-07 02:00:00              NaN  ...                  NaN
2019-05-07 03:00:00             50.5  ...             0.495050
2019-05-07 04:00:00             45.0  ...             0.615556
2019-05-07 05:00:00              NaN  ...                  NaN
2019-05-07 06:00:00              NaN  ...                  NaN

[5 rows x 5 columns]
```

此计算同样是逐元素的，因此 `/` 运算符在每一行的值上应用。

其他数学运算符（如 `+`、`-`、`*`、`/` 等）或逻辑运算符（如 `<`、`>`、`==` 等）同样逐元素应用。可参考 [如何选择 DataFrame 的子集？](http://localhost:3000/books/pandas/Getting_started/Getting_started_tutorials/How_do_I_select_a_subset_of_a_DataFrame/index.html)用于使用条件表达式筛选表格行。

如果需要更高级的逻辑，可通过 [`apply()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html#pandas.DataFrame.apply "pandas.DataFrame.apply") 使用任意 Python 代码。

我想将数据列重命名为 [OpenAQ](https://openaq.org/) 使用的测量站标识符。

```
In [8]:
air_quality_renamed = air_quality.rename(
    columns={
        "station_antwerp": "BETR801",
        "station_paris": "FR04014",
        "station_london": "London Westminster",
    }
)
In [9]: air_quality_renamed.head()
Out[9]: 
                     BETR801  FR04014  ...  london_mg_per_cubic  ratio_paris_antwerp
datetime                               ...                                          
2019-05-07 02:00:00      NaN      NaN  ...               43.286                  NaN
2019-05-07 03:00:00     50.5     25.0  ...               35.758             0.495050
2019-05-07 04:00:00     45.0     27.7  ...               35.758             0.615556
2019-05-07 05:00:00      NaN     50.4  ...               30.112                  NaN
2019-05-07 06:00:00      NaN     61.9  ...                  NaN                  NaN

[5 rows x 5 columns]
```

[`rename()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html#pandas.DataFrame.rename "pandas.DataFrame.rename") 函数可用于行标签和列标签的重命名。使用键为当前名称、值为新名称的字典进行更新。

不仅限于固定名称，还可以使用映射函数，例如，将列名转换为小写字母：

```
In [10]: air_quality_renamed = air_quality_renamed.rename(columns=str.lower)
In [11]: air_quality_renamed.head()
Out[11]: 
                     betr801  fr04014  ...  london_mg_per_cubic  ratio_paris_antwerp
datetime                               ...                                          
2019-05-07 02:00:00      NaN      NaN  ...               43.286                  NaN
2019-05-07 03:00:00     50.5     25.0  ...               35.758             0.495050
2019-05-07 04:00:00     45.0     27.7  ...               35.758             0.615556
2019-05-07 05:00:00      NaN     50.4  ...               30.112                  NaN
2019-05-07 06:00:00      NaN     61.9  ...                  NaN                  NaN

[5 rows x 5 columns]
```

`前往用户指南` 详细内容请见用户指南中的 [标签重命名](https://pandas.pydata.org/docs/user_guide/basics.html#basics-rename) 部分。

> **要点概要**
>
> - 通过在 `[]` 中赋予新列名为 DataFrame 创建新列。
> - 操作逐元素应用，无需逐行循环。
> - 使用 `rename` 的字典或函数来重命名行标签或列名。