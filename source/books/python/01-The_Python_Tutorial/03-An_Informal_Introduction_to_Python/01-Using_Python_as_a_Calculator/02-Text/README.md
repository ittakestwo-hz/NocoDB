# 文本

Python 可以处理文本（由 [`str`](https://docs.python.org/3/tutorial/introduction.html../library/stdtypes.html#str "str") 类型表示，也就是“字符串”）和数字。

这包括字符“`!`”、单词“`rabbit`”、名称“`Paris`”、句子“`Got your back.`”等，甚至“`Yay! :)`”。

它们可以用单引号（`'...'`）或双引号（`"..."`）括起来，结果是一样的。

```
>>> 'spam eggs' # 单引号
'spam eggs'
>>> "Paris rabbit got your back :)! Yay!" # 双引号  
'Paris rabbit got your back :)! Yay!'
>>> '1975' # 用引号括起来的数字和数值也是字符串  
'1975'
```

要引用引号，需要使用反斜杠 `\` 对其进行“转义”。

或者，也可以使用另一种类型的引号：

```
>>> 'doesn\'t' # 使用 \' 来转义单引号
"doesn't"
>>> "doesn't" # 或者直接使用双引号
"doesn't"
>>> '"Yes," they said.'
'"Yes," they said.'
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
>>> print('"Isn\'t," they said.')
"Isn't," they said.
```

在 Python Shell 中，字符串的定义和输出可能看起来不同。[`print()`](https://docs.python.org/3/tutorial/introduction.html../library/functions.html#print "print") 函数会生成更具可读性的输出，省略了外层引号，并将转义字符和特殊字符显示为其实际效果：

```
>>> s = 'First line.\nSecond line.' # \n 表示换行符
>>> s # 不使用 print() 时，特殊字符会保留在字符串中
'First line.\nSecond line.'
>>> print(s)  # 使用 print() 时，特殊字符会被解释，\n 表示换行
First line.
Second line.
```

如果你不希望以 `\` 开头的字符被解释为特殊字符，可以在第一个引号前加上 `r` 来使用原始字符串：

```
>>> print('C:\some\name') # 这里的 \n 表示换行！
<stdin>:1: SyntaxWarning: invalid escape sequence '\s'
C:\some
ame
>>> print(r'C:\some\name') # 注意引号前的 r
C:\some\name
```

原始字符串有一个细微之处：一个原始字符串不能以奇数个 `\` 字符结尾；更多信息和解决方法请参见[常见问题解答](https://docs.python.org/3/tutorial/introduction.html../faq/programming.html#faq-programming-raw-string-backslash)。

字符串字面量可以跨多行。

方法之一是使用三重引号：`"""..."""` 或 `'''...'''`。换行符会自动包含在字符串中，但可以通过在行尾添加 `\` 来避免。

在以下示例中，初始换行符未被包含：

```
>>> print("""\
... Usage: thingy [OPTIONS]
...     -h      Display this usage message                   
...     -H hostname     Hostname to connect to
... """)
Usage: thingy [OPTIONS]
        -h      Display this usage message
        -H hostname     Hostname to connect to
```

字符串可以使用 `+` 运算符进行连接（拼接），使用 `*` 运算符进行重复：

```
>>> # 'un' 重复 3 次，后跟 'ium'
>>> 3 * 'un' + 'ium'
'unununium'
```

两个或更多的 _字符串文字_（即被引号括起来的部分）放在一起时，会自动连接。

```
>>> 'Py' 'thon'
'Python'
```

这个特性在你想要拆分长字符串时特别有用：

```
>>> text = ('Put several strings within parentheses '
...     'to have them joined together.')
>>> text
'Put several strings within parentheses to have them joined together.'
```

不过，这仅适用于两个字面量（literals），不适用于变量或表达式：

```
>>> prefix = 'Py'
>>> prefix 'thon' # 不能将变量和字符串字面量连接在一起
  File "<stdin>", line 1
    prefix 'thon' # 不能将变量和字符串字面量连接在一起
           ^^^^^^
SyntaxError: invalid syntax
>>> ('un' * 3) 'ium'
  File "<stdin>", line 1
    ('un' * 3) 'ium'
               ^^^^^
SyntaxError: invalid syntax
```

如果你想连接变量或变量和字面量，请使用 `+`：

```
>>> prefix + 'thon'                             
'Python'
```

字符串可以通过 _索引_ （下标）访问，第一个字符的索引为 0。Python 中没有单独的字符类型；字符只是长度为一的字符串：

```
>>> word = 'Python'
>>> word[0] # 位置 0 的字符
'P'
>>> word[5] # 位置 5 的字符
'n'
```

索引也可以是负数，从右边开始计数：

```
>>> word[-1] # 最后一个字符
'n'
>>> word[-2] # 倒数第二个字符
'o'
>>> word[-6]
'P'
```

请注意，由于 `-0` 与 `0` 相同，负索引从 `-1` 开始。

除了索引，Python 还支持**切片**。索引用于获取单个字符，而**切片**则可以让你获取子字符串：

```
>>> word[0:2] # 从位置 0（包含）到 位置 2（不包含）的字符
'Py'
>>> word[2:5] # 从位置 2（包含）到 位置 5（不包含）的字符
'tho'
```

切片索引有一些有用的默认值；省略的第一个索引默认为零，省略的第二个索引默认为被切片字符串的长度。

```
>>> word[:2] # 从开头到位置 2（不包含）的字符
'Py'
>>> word[:4] # 从位置 4（包含）到结尾的字符
'Pyth'
>>> word[-2:] # 从倒数第二个（包含）到结尾的字符
'on'
```

请注意，起始索引总是包含在内，而结束索引总是排除在外。这确保了 `s[:i] + s[i:]` 始终等于 `s`：

```
>>> word[:2] + word[2:]
'Python'
>>> word[:4] + word[4:]
'Python'
```

一种记住切片如何工作的方式是将索引视为指向字符之间的位置，字符串中第一个字符的左边缘编号为 0。然后，字符串中有 _n_ 个字符时，最后一个字符的右边缘的索引是 _n_，例如：

```
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```

数字的第一行给出了字符串中索引 0 到 6 的位置；第二行给出了对应的负索引。_i_ 到 _j_ 的切片包含了从索引 _i_ 到索引 _j_ 之间的所有字符。

对于非负索引，如果两个索引都在范围内，切片的长度是它们的差。例如，`word[1:3]` 的长度是 2。

如果尝试使用一个超出范围的索引，将会导致错误：

```
>>> word[42] # 该单词只有 6 个字符
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```

然而，当用于切片时，超出范围的索引会被优雅地处理：

```
>>> word[4:42]
'on'
>>> word[42:]
''
```

Python 字符串是不可变的 — 它们是 [immutable](https://docs.python.org/3/tutorial/introduction.html#text../glossary.html#term-immutable)。因此，尝试给字符串中的索引位置赋值会导致错误：

```
>>> word[0] = 'J'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> word[2:] = 'py'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

如果你需要一个不同的字符串，你应该创建一个新的字符串：

```
>>> 'J' + word[1:]
'Jython'
>>> word[:2] + 'py'
'Pypy'
```

内置函数 [`len()`](https://docs.python.org/3/tutorial/introduction.html#text../library/functions.html#len "len") 返回字符串的长度：

 ```
 >>> s = 'supercalifragilisticexpialidocious'
>>> len(s)
34
```


> **另见**
> 
> [文本序列类型 — str](https://docs.python.org/3/tutorial/introduction.html#text../library/stdtypes.html#textseq)
>  - 字符串是_序列类型_的例子，支持此类类型常见的操作。
> 
> [字符串方法](https://docs.python.org/3/tutorial/introduction.html#text../library/stdtypes.html#string-methods)
>  - 字符串支持大量用于基本转换和搜索的方法。
> 
> [f-strings](https://docs.python.org/3/tutorial/introduction.html#text../reference/lexical_analysis.html#f-strings)
>  - 包含嵌入表达式的字符串字面量。
> 
> [格式化字符串语法](https://docs.python.org/3/tutorial/introduction.html#text../library/string.html#formatstrings)
> 
>  - 有关使用[`str.format()`](https://docs.python.org/3/tutorial/introduction.html#text../library/stdtypes.html#str.format "str.format")进行字符串格式化的信息。
> 
> [printf 风格的字符串格式化](https://docs.python.org/3/tutorial/introduction.html#text../library/stdtypes.html#old-string-formatting)
>  - 当字符串是 `%` 运算符的左操作数时，描述了旧的格式化操作。