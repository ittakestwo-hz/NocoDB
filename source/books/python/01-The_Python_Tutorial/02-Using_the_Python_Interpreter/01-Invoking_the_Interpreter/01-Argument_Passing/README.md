# 参数传递

当解释器已知脚本名和后续的附加参数时，它们会被转化为一个字符串列表，并赋值给 `sys` 模块中的 `argv` 变量。

你可以通过执行 `import sys` 来访问这个列表。

列表的长度至少为 1；如果没有提供脚本和参数，`sys.argv[0]` 将是一个空字符串。

当脚本名被指定为 `'-'`（表示标准输入）时，`sys.argv[0]` 被设置为 `'-'`。

当使用 [`-c`](https://docs.python.org/3/tutorial/interpreter.html../using/cmdline.html#cmdoption-c) _command_ 时，`sys.argv[0]` 被设置为 `'-c'`。

当使用 [`-m`](https://docs.python.org/3/tutorial/interpreter.html../using/cmdline.html#cmdoption-m) _module_ 时，`sys.argv[0]` 被设置为所定位模块的完整名称。

位于 [`-c`](https://docs.python.org/3/tutorial/interpreter.html../using/cmdline.html#cmdoption-c) _command_ 或 [`-m`](https://docs.python.org/3/tutorial/interpreter.html../using/cmdline.html#cmdoption-m) _module_ 后面的选项不会被 Python 解释器的选项处理程序消耗，而是保留在 `sys.argv` 中，由命令或模块来处理。