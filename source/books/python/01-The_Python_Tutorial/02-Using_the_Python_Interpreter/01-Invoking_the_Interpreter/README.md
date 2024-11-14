# 调用解释器

Python 解释器通常安装在 `/usr/local/bin/python3.13` 这样的路径下，前提是该机器上已安装 Python；将 `/usr/local/bin` 添加到你的 Unix shell 的搜索路径中，就可以通过输入以下命令启动解释器：

```
python3.13
```

至 shell 中。[\[1\]](https://docs.python.org/3/tutorial/interpreter.html#id2) 由于解释器安装路径是一个配置选项，其他位置也是可能的；可以向本地的 Python 专家或系统管理员咨询。（例如，`/usr/local/python` 是一个常见的替代位置。）

在 Windows 系统上，如果你是通过 [Microsoft Store](https://docs.python.org/3/tutorial/interpreter.html../using/windows.html#windows-store) 安装的 Python，`python3.13` 命令会可用。如果你安装了 [py.exe 启动器](https://docs.python.org/3/tutorial/interpreter.html../using/windows.html#launcher)，你也可以使用 `py` 命令。有关其他启动 Python 的方法，请参阅 [附录：设置环境变量](https://docs.python.org/3/tutorial/interpreter.html../using/windows.html#setting-envvars)。

在主提示符下键入结束文件字符（Unix 上为 Control-D，Windows 上为 Control-Z）会使解释器退出，且退出状态为零。如果这不起作用，你可以通过键入以下命令来退出解释器：`quit()`。

解释器的行编辑功能包括交互式编辑、历史替代和代码自动完成，这些功能在支持 [GNU Readline](https://tiswww.case.edu/php/chet/readline/rltop.html) 库的系统上可用。检查命令行编辑是否支持的最快方法是，在首次出现的 Python 提示符下键入 Control-P。如果有蜂鸣声，说明支持命令行编辑；有关按键的介绍，请参见附录 [交互输入编辑和历史替代](https://docs.python.org/3/tutorial/interpreter.htmlinteractive.html#tut-interacting)。如果没有任何反应，或者显示 `^P`，则命令行编辑不可用；你只能使用退格键删除当前行的字符。

解释器的工作方式有些类似于 Unix shell：当通过标准输入连接到 tty 设备时，它会交互式地读取并执行命令；当通过文件名参数或文件作为标准输入调用时，它会从该文件中读取并执行 _脚本_。

启动解释器的第二种方式是 `python -c command [arg] ...`，这会执行 _command_ 中的语句，类似于 shell 的 [`-c`](https://docs.python.org/3/tutorial/interpreter.html../using/cmdline.html#cmdoption-c) 选项。由于 Python 语句通常包含空格或其他对 shell 特殊的字符，因此通常建议将 _command_ 完整地用引号括起来。

一些 Python 模块也可以作为脚本使用。可以通过 `python -m module [arg] ...` 调用这些模块，这样就像在命令行中拼写出它的完整名称一样执行 _module_ 的源文件。

当使用脚本文件时，有时你可能希望在运行脚本后进入交互模式。这可以通过在脚本之前传递 [`-i`](https://docs.python.org/3/tutorial/interpreter.html../using/cmdline.html#cmdoption-i) 来实现。

所有命令行选项的详细描述，请参见 [命令行和环境](https://docs.python.org/3/tutorial/interpreter.html../using/cmdline.html#using-on-general)。