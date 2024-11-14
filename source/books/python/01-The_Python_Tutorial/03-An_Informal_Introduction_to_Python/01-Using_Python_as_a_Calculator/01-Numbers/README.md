# 数字

解释器充当一个简单的计算器：你可以输入一个表达式，它会输出结果。

表达式的语法很简单：

- 运算符 `+`、`-`、`*` 和 `/` 可以用于执行算术运算
- 圆括号 (`()`) 可用于分组。

例如：

```
>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8 / 5  # 除法总是返回浮点数
1.6
```

整数（例如 `2`、`4`、`20`）的类型为 [`int`](https://docs.python.org/3/tutorial/introduction.html../library/functions.html#int "int")，带小数部分的数字（例如 `5.0`、`1.6`）的类型为 [`float`](https://docs.python.org/3/tutorial/introduction.html../library/functions.html#float "float")。

我们将在教程的后面部分了解更多关于数字类型的内容。

除法（`/`）总是返回浮点数。

要进行 [向下取整除法](https://docs.python.org/3/tutorial/introduction.html../glossary.html#term-floor-division) 并获取整数结果，可以使用 `//` 运算符；要计算余数，可以使用 `%`：

```
>>> 17 / 3  # 经典除法返回浮点数
5.666666666666667
>>> 17 // 3  # 整数除法舍弃小数部分
5
>>> 17 % 3  # % 运算符返回除法的余数
2
>>> 5 * 3 + 2  # 向下取整的商 * 除数 + 余数
17
```

在 Python 中，可以使用 `**` 运算符来计算幂：

```
>>> 5 ** 2  # 5 的平方
25
>>> 2 ** 7  # 2 的 7 次方
128
```

等号（`=`）用于将一个值赋给一个变量。在此之后，在下一个交互式提示符出现之前，不会显示任何结果：

```
>>> width = 20
>>> height = 5 * 9
>>> width * height
900
```

如果一个变量没有“定义”（没有赋值），尝试使用它会导致错误：

```
>>> n  # 尝试访问一个未定义的变量                               
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined
```

完全支持浮点数；运算符与混合类型的操作数一起使用时，会将整数操作数转换为浮点数：

```
>>> 4 * 3.75 - 1
14.0
```

在交互模式下，最后打印的表达式会被赋值给变量 `_`。这意味着，当你将 Python 用作桌面计算器时，继续计算会变得更加方便，例如：

```
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
```

这个变量应该被用户视为只读。不要显式地给它赋值——这样会创建一个独立的局部变量，使用相同的名称，从而掩盖了具有魔法行为的内建变量。

除了 [`int`](https://docs.python.org/3/tutorial/introduction.html../library/functions.html#int "int") 和 [`float`](https://docs.python.org/3/tutorial/introduction.html../library/functions.html#float "float")，Python 还支持其他类型的数字，例如 [`Decimal`](https://docs.python.org/3/tutorial/introduction.html../library/decimal.html#decimal.Decimal "decimal.Decimal") 和 [`Fraction`](https://docs.python.org/3/tutorial/introduction.html../library/fractions.html#fractions.Fraction "fractions.Fraction")。Python 还内建支持 [复数](https://docs.python.org/3/tutorial/introduction.html../library/stdtypes.html#typesnumeric)，并使用 `j` 或 `J` 后缀来表示虚部（例如 `3+5j`）。