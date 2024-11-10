# 富文本

`Rich Text` 字段是基于文本的字段，是 `Long text` 的扩展，允许您为文本添加格式。您可以添加文本格式，例如粗体、斜体、下划线、删除线、水平线、有序列表、无序列表、代码、引用等。

## 创建 `Rich Text` 字段

1. 点击 `Fields header` 右侧的 `+` 图标。
2. 在下拉模态中，输入字段名称（可选）。
3. 从下拉菜单中选择字段类型为 `Long text`。
4. 启用 `Rich Text` 切换字段。
5. 设置字段的默认值（可选）。
6. 点击 `Save Field` 按钮。

![image](https://docs.nocodb.com/assets/images/richtext-fa2dd44b6fd13ec6e529edae4f156c9e.png)

**注意**

- 指定默认值时不要加引号。
- 使用 `Enter` 键添加新行。

### 单元格显示

`Rich Text` 字段在表视图中显示为单行文本字段。点击单元格中的展开图标以查看完整文本。

![image](https://docs.nocodb.com/assets/images/long-text-expand-d15b69ace110a10185959d52b19bce63.png) 

![image](https://docs.nocodb.com/assets/images/long-text-expand-2-09cce09ec85355082b79054a189abb37.png)

## 格式选项

NocoDB 支持用于格式化文本的 Markdown 语法。以下是支持的格式选项。

### 标题

要创建标题，请在标题文本前加上 `#` 符号。使用的 `#` 符号数量将决定标题的层级和字体大小。支持三种层级的标题。

```
# 标题 1
## 标题 2
### 标题 3
```

![image](https://docs.nocodb.com/assets/images/richtext-heading-993c1575b91f0b03d17e53a7fb3f5d45.png)

### 文本格式

您可以使用粗体、斜体、删除线或下划线格式选项来强调文本。下表显示了每种格式选项的语法、快捷键、示例和输出。

| 风格       | 语法                  | 快捷键              | 示例                       | 输出                   |
| ---------- | --------------------- | ------------------- | -------------------------- | ---------------------- |
| 粗体       | `**粗体文本**`       | `Ctrl/Cmd + B`      | `**这是粗体文本**`        | **这是粗体文本**       |
| 斜体       | `*斜体文本*`         | `Ctrl/Cmd + I`      | `*这是斜体文本*`          | _这是斜体文本_         |
| 删除线     | `~~删除线文本~~`     | `Ctrl/Cmd + Shift + X` | `~~这是删除线文本~~`      | ~这是删除线文本~       |
| 下划线     |                       | `Ctrl/Cmd + U`      | `这是下划线文本`          | 这是下划线文本         |

### 引用块

您可以使用 `>` 引用文本。

正常文本

> 引用文本

### 代码块

可以通过在代码前后使用三个反引号（```）来创建代码块。

````
```这是一个代码块```
````

### 链接

您可以通过在富文本工具栏中使用 `Link` 菜单选项来创建内联链接。

![image](https://docs.nocodb.com/assets/images/richtext-links-eaeaf695ad2dfee7d75804758cbeb0e4.png)

### 无序列表

您可以通过在富文本工具栏中使用 `Bulleted list` 菜单选项，或在文本前添加 `-`、`+` 或 `*` 符号来创建无序列表。

```
- 项目 1
- 项目 2
+ 项目 1
+ 项目 2
* 项目 1
* 项目 2
```

- 项目 1
- 项目 2
- 项目 1
- 项目 2

**注意**

您可以使用 `tab` 键和 `shift + tab` 键来缩进和取消缩进列表项，从而创建嵌套列表。

### 有序列表

您可以通过在富文本工具栏中使用 `Numbered list` 菜单选项，或在文本前添加 `1.` 符号来创建有序列表。

1. 项目 1
2. 项目 2

### 任务列表

您可以通过在富文本工具栏中使用 `Task list` 菜单选项，或在文本前添加 `[ ]` 符号来创建任务列表。您可以使用 `[x]` 符号将任务标记为已完成。

- 项目 1
- 项目 2

## 相似的基于文本的字段

以下是 NocoDB 中提供的其他基于文本的字段，专为特定用例定制。

- [单行文本](https://docs.nocodb.com/fields/field-types/text-based/single-line-text)
- [网址](https://docs.nocodb.com/fields/field-types/text-based/url)
- [电子邮件](https://docs.nocodb.com/fields/field-types/text-based/email)
- [电话](https://docs.nocodb.com/fields/field-types/text-based/phonenumber)