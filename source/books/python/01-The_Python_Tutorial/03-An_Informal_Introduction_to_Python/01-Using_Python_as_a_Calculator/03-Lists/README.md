# 列表

Python 知道多种 _复合_ 数据类型，用于将其他值组合在一起。最通用的是 _列表_ ，它可以写作用逗号分隔的值（项）列表，项之间用方括号括起来。列表可以包含不同类型的项，但通常这些项都具有相同的类型。

```
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
```

像字符串（以及所有其他内置的[序列](https://docs.python.org/3/tutorial/introduction.html#text../glossary.html#term-sequence)类型）一样，列表也可以通过索引和切片进行操作：

```
>>> squares[0] # 索引返回项目
1
>>> squares[-1]
25
>>> squares[-3:] # 切片返回一个新列表
[9, 16, 25]
```

列表也支持诸如连接（concatenation）之类的操作：

```
>>> squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

与字符串不同，字符串是[不可变](https://docs.python.org/3/tutorial/introduction.html#text../glossary.html#term-immutable)的，而列表是[可变](https://docs.python.org/3/tutorial/introduction.html#text../glossary.html#term-mutable)类型，即可以更改它们的内容：

```
>>> cubes = [1, 8, 27, 65, 125] # 这里有个问题
>>> 4 ** 3 # 4 的立方是 64，不是 65!
64
>>> cubes[3] = 64 # 替换错误的值
>>> cubes                    
[1, 8, 27, 64, 125]
```

你也可以通过使用 `list.append()` _方法_ 在列表的末尾添加新项（稍后我们会更详细地讲解方法）：

```
>>> cubes.append(216) # 添加 6 的立方
>>> cubes.append(7 ** 3) # 添加 7 的立方
>>> cubes
[1, 8, 27, 64, 125 , 216, 343]
```

在 Python 中，简单的赋值操作从不复制数据。当你将一个列表赋值给一个变量时，变量仅仅引用了 _现有的列表_ 。通过一个变量对列表进行的任何修改都会在所有引用该列表的其他变量中体现出来。

```
>>> rgb = ["Red", "Green", "Blue"]
>>> rgba = rgb
>>> id(rgb) == id(rgba) # 它们引用的是同一个对象
True
>>> rgba.append("Alph")
>>> rgb
['Red', 'Green', 'Blue', 'Alph']
```

所有切片操作都会返回一个包含请求元素的新列表。这意味着以下切片操作会返回该列表的[浅拷贝](https://docs.python.org/3/tutorial/introduction.html#text../library/copy.html#shallow-vs-deep-copy)：

```
>>> correct_rgba = rgba[:]
>>> correct_rgba[-1] = "Alpha"
>>> correct_rgba
['Red', 'Green', 'Blue', 'Alpha']
>>> rgba
['Red', 'Green', 'Blue', 'Alph']
```

也可以对切片进行赋值，这甚至可以改变列表的大小或将其完全清空：

