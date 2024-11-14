# 交互模式

当命令从 tty 读取时，解释器处于 _交互模式_。

在此模式下，它通过 _主提示符_ 提示输入下一个命令，通常是三个大于号（`>>>`）；对于续行，它使用 _次级提示符_，默认为三个点（`...`）。

在显示第一个提示符之前，解释器会打印一条欢迎信息，说明其版本号和版权声明：

```
(base) PS C:\Users\Ra>python
Python 3.12.4 | packaged by Anaconda, Inc. | (main, Jun 18 2024, 15:03:56) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

在输入多行构造时，需要使用续行。举个例子，看看这个 if 语句：

```
>>> the_world_is_flat = True
>>> if the_world_is_flat:
...     print("Be careful not to fall off!")
...
Be careful not to fall off!
```

有关交互模式的更多信息，请参阅[《交互模式》](https://docs.python.org/3/tutorial/appendix.html#tut-interac)。