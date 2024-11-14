# 重复标签

`Index` 对象不要求是唯一的；你可以有重复的行标签或列标签。这在一开始可能会有些困惑。如果你熟悉 SQL，你会知道行标签类似于 SQL 表中的主键，而在 SQL 表中你通常不希望出现重复项。但 pandas 的一个作用是清理杂乱无章的真实数据，然后将其传递给下游系统。真实世界的数据通常会有重复，即使是那些本应唯一的字段也不例外。

本节将描述重复标签如何改变某些操作的行为，以及如何在操作过程中防止重复标签的出现，或在它们出现时进行检测。

```
In [1]: import pandas as pd
In [2]: import numpy as np
```

## 重复标签的后果

某些 pandas 方法（例如 `Series.reindex()`）在存在重复标签时无法正常工作。由于输出无法确定，pandas 会抛出错误。

```
In [3]: s1 = pd.Series([0, 1, 2], index=["a", "b", "b"])
In [4]: s1.reindex(["a", "b", "c"])
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[4], line 1
----> 1 s1.reindex(["a", "b", "c"])

File ~/work/pandas/pandas/pandas/core/series.py:5153, in Series.reindex(self, index, axis, method, copy, level, fill_value, limit, tolerance)
   5136 @doc(
   5137     NDFrame.reindex,  # type: ignore[has-type]
   5138     klass=_shared_doc_kwargs["klass"],
   (...)
   5151     tolerance=None,
   5152 ) -> Series:
-> 5153     return super().reindex(
   5154         index=index,
   5155         method=method,
   5156         copy=copy,
   5157         level=level,
   5158         fill_value=fill_value,
   5159         limit=limit,
   5160         tolerance=tolerance,
   5161     )

File ~/work/pandas/pandas/pandas/core/generic.py:5610, in NDFrame.reindex(self, labels, index, columns, axis, method, copy, level, fill_value, limit, tolerance)
   5607     return self._reindex_multi(axes, copy, fill_value)
   5609 # perform the reindex on the axes
-> 5610 return self._reindex_axes(
   5611     axes, level, limit, tolerance, method, fill_value, copy
   5612 ).__finalize__(self, method="reindex")

File ~/work/pandas/pandas/pandas/core/generic.py:5633, in NDFrame._reindex_axes(self, axes, level, limit, tolerance, method, fill_value, copy)
   5630     continue
   5632 ax = self._get_axis(a)
-> 5633 new_index, indexer = ax.reindex(
   5634     labels, level=level, limit=limit, tolerance=tolerance, method=method
   5635 )
   5637 axis = self._get_axis_number(a)
   5638 obj = obj._reindex_with_indexers(
   5639     {axis: [new_index, indexer]},
   5640     fill_value=fill_value,
   5641     copy=copy,
   5642     allow_dups=False,
   5643 )

File ~/work/pandas/pandas/pandas/core/indexes/base.py:4429, in Index.reindex(self, target, method, level, limit, tolerance)
   4426     raise ValueError("cannot handle a non-unique multi-index!")
   4427 elif not self.is_unique:
   4428     # GH#42568
-> 4429     raise ValueError("cannot reindex on an axis with duplicate labels")
   4430 else:
   4431     indexer, _ = self.get_indexer_non_unique(target)

ValueError: cannot reindex on an axis with duplicate labels

```

其他方法，如索引，可能会产生非常意外的结果。通常，使用标量进行索引会**减少维度**。用标量切片 `DataFrame` 会返回一个 `Series`，用标量切片 `Series` 会返回一个标量。但如果有重复标签，情况就不一样了。

```
In [5]: df1 = pd.DataFrame([[0, 1, 2], [3, 4, 5]], columns=["A", "A", "B"])
In [6]: df1
Out[6]: 
   A  A  B
0  0  1  2
1  3  4  5

```

我们在列中有重复项。如果我们切片 `'B'`，将返回一个 `Series`。

```
In [7]: df1["B"]  # a series
Out[7]: 
0    2
1    5
Name: B, dtype: int64
```

但是切片 `'A'` 返回的是一个 `DataFrame`。

```
In [8]: df1["A"]  # a DataFrame
Out[8]: 
   A  A
0  0  1
1  3  4
```

这同样适用于行标签。

```
In [9]: df2 = pd.DataFrame({"A": [0, 1, 2]}, index=["a", "a", "b"])
In [10]: df2
Out[10]: 
   A
a  0
a  1
b  2
In [11]: df2.loc["b", "A"]  # a scalar
Out[11]: 2
In [12]: df2.loc["a", "A"]  # a Series
Out[12]: 
a    0
a    1
Name: A, dtype: int64
```
