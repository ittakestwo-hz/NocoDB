# Python 非正式入门介绍

在以下示例中，输入和输出通过提示符的存在与否进行区分（`>>>` 和 `...`）：要重复示例，您必须在提示符出现时输入所有内容；不以提示符开头的行是解释器的输出。请注意，如果一个次级提示符单独出现在一行中，则意味着您必须输入一个空行；这是用来结束多行命令的。

您可以通过点击示例框右上角的 `>>>` 来切换提示符和输出的显示。如果您隐藏了示例的提示符和输出，那么您可以轻松地将输入行复制并粘贴到您的解释器中。

本手册中的许多示例，即使是交互式提示符输入的示例，也包括注释。Python 中的注释以井号字符 `#` 开始，并扩展到物理行的末尾。注释可以出现在一行的开头，或者跟随在空白字符或代码后面，但不能出现在字符串字面量中。字符串字面量中的井号字符只是一个井号字符。由于注释用于解释代码，并且不被 Python 解释，所以在输入示例时可以省略它们。

一些示例：

```python
# 这是第一个注释
spam = 1  # 这是第二个注释
          # ... 现在是第三个注释！
text = "# 这不是注释，因为它在引号内。"
```