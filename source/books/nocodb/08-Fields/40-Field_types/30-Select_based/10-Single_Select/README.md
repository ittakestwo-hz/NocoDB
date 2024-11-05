# 单选框

`单选框` 字段允许您从选项列表中选择一个选项。选项可以在字段配置中定义。

## 创建单选框字段 [](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#create-a-single-select-field "直接链接到创建单选框字段")

1. 点击 `Fields header` 右侧的 `+` 图标。
2. 在下拉窗口中，输入字段名称（可选）。
3. 从下拉菜单中选择字段类型为 `SingleSelect`。
4. 点击 `Add option` 按钮添加选项。
5. 设置字段的默认值。选项将填充在下拉菜单中（可选）。
6. 点击 `Save Field` 按钮。

![image](https://docs.nocodb.com/assets/images/singleselect-0d82c6b862285fa9b33214680b7e6787.png)

## 编辑选项 [](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#edit-options "直接链接到编辑选项")

### 重命名选项 [](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#rename-options "直接链接到重命名选项")

您可以通过点击关联的选项文本框来重命名选项。点击 `Save Field` 按钮保存更改。

### 配置选项的颜色 [](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#configure-color-for-options "直接链接到配置选项的颜色")

您可以重新配置每个选项的背景颜色。当您希望突出显示某些选项时，这非常有用。例如，您可以将 `High` 选项配置为具有 `red` 背景颜色。要配置颜色，请点击选项旁边的 `color` 图标。从颜色选择器中选择颜色，然后点击 `Save Field` 按钮。

![image](https://docs.nocodb.com/assets/images/options-change-colour-08270506854710a13f2945a006fd3779.png)

### 重新排序选项 [](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#re-order-options "直接链接到重新排序选项")

您可以通过拖放选项来重新排序选项。要重新排序，请点击选项旁边的 `drag` 图标，并将其拖到所需位置。点击 `Save Field` 按钮保存顺序。

![image](https://docs.nocodb.com/assets/images/options-reorder-1ee3cf6240593e4055bd781a0c116949.png)

> 信息
> 为选项定义的顺序也将用于单元格下拉菜单。

### 编辑选项 [](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#edit-options-1 "直接链接到编辑选项")

您可以通过点击关联的选项文本框来重命名选项。点击 `Save Field` 按钮保存更改。

### 删除选项 [](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#delete-options "直接链接到删除选项")

您可以通过点击选项旁边的 `x` 图标来删除选项。您可以通过点击选项旁边的 `undo` 图标来撤销删除。点击 `Save Field` 按钮保存更改。

信息

- 删除选项时，该选项值将从所有单元格中移除。
- 如果选项值被设置为字段的默认值，则默认值将被移除。

![image](https://docs.nocodb.com/assets/images/options-remove-9e5b6dcf0682be419ac34c21db0b5716.png)

## 类似的选择型字段 [](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#similar-select-based-fields "直接链接到类似的选择型字段")

- [多选框](https://docs.nocodb.com/fields/field-types/select-based/multi-select)