# 多选

`Multi Select` 字段允许您从选项列表中选择多个选项。选项可以在字段配置中定义。

## 创建多选字段[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#create-a-multi-select-field "直接链接到创建多选字段")

1. 点击 `Fields header` 右侧的 `+` 图标。
2. 在下拉模态中，输入字段名称（可选）。
3. 从下拉菜单中选择字段类型为 `MultiSelect`。
4. 点击 `Add option` 按钮以添加选项。
5. 为字段设置默认值。选项将填充在下拉菜单中。由于是多选，您可以选择多个选项作为默认值（可选）。
6. 点击 `Save Field` 按钮。

![image](https://docs.nocodb.com/assets/images/multiselect-d61aaaf3d7f5175b899af60f0ecd6225.png)

注意

选项值中不允许使用 `,`。

### 为选项配置颜色[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#configure-color-for-options "直接链接到为选项配置颜色")

您可以为每个选项重新配置背景颜色。这在您想要突出某些选项时非常有用。例如，您可以将 `High` 选项配置为具有 `red` 背景色。要配置颜色，请点击选项旁边的 `color` 图标。从颜色选择器中选择颜色，然后点击 `Save Field` 按钮。

![image](https://docs.nocodb.com/assets/images/options-change-colour-08270506854710a13f2945a006fd3779.png)

### 重新排序选项[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#re-order-options "直接链接到重新排序选项")

您可以通过拖放选项来重新排序选项。要重新排序，点击选项旁边的 `drag` 图标，将其拖动到所需位置。点击 `Save Field` 按钮以保存顺序。

![image](https://docs.nocodb.com/assets/images/options-reorder-1ee3cf6240593e4055bd781a0c116949.png)

信息

为选项定义的顺序也将用于单元格下拉菜单中。

### 编辑选项[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#edit-options "直接链接到编辑选项")

您可以通过点击相关选项的文本框来重命名选项。点击 `Save Field` 按钮以保存更改。

### 删除选项[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#delete-options "直接链接到删除选项")

您可以通过点击选项旁边的 `x` 图标来删除选项。您可以通过点击选项旁边的 `undo` 图标来撤消删除。点击 `Save Field` 按钮以保存更改。

信息

- 删除选项时，该选项值将从所有单元格中删除。
- 如果选项值被设置为字段的默认值，则默认值也会被删除。

![image](https://docs.nocodb.com/assets/images/options-remove-9e5b6dcf0682be419ac34c21db0b5716.png)

## 相似选择字段[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#similar-select-based-fields "直接链接到相似选择字段")

- [单选](https://docs.nocodb.com/fields/field-types/select-based/single-select)