# 评分

`评分字段` 允许您使用可视化比例来捕捉和显示评分。该比例可以通过不同的图标、颜色和最大值进行自定义。这使得以直观的方式收集反馈或评估变得理想。

## 创建复选框字段[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#create-a-checkbox-field "直接链接到创建复选框字段")

1. 点击 `字段标题` 右侧的 `+` 图标
2. 在下拉模态框中，输入字段名称（可选）。
3. 从下拉列表中选择字段类型为 `评分`。
4. 为字段选择图标；默认使用 `星星` 图标（可选）。
5. 配置字段的最大计数；默认为 `5`（可选）。
6. 为字段选择颜色；默认为 `灰色`（可选）。
7. 设置字段的默认值（可选）。
8. 点击 `保存字段` 按钮。

![image](https://docs.nocodb.com/assets/images/rating-7dcce304ae8fbf78908c340a87e90da4.png)

### 单元格显示[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#cell-display "直接链接到单元格显示")

单元格以所选的颜色和图标显示评分。  
![image](https://docs.nocodb.com/assets/images/rating-cell-ab9000c7aa5624758b22f06f59b5495e.png)

### 为字段设置值[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#setting-value-for-the-field "直接链接到为字段设置值")

- 点击 `第 n 个` 评分图标将字段的评分值设置为 `n`。
- 在单元格中输入评分值以设置字段的评分值。
- 在单元格中粘贴评分值以设置字段的评分值。

### 取消字段值设置[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#unsetting-value-for-the-field "直接链接到取消字段值设置")

- 再次点击 `第 n 个` 评分图标将字段的评分值设置为 `0`。
- 在单元格中输入 `0` 将字段的评分值设置为 `0`。
- 输入 `Delete` 将字段的评分值设置为 `0`。

### 支持的图标[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#supported-icons "直接链接到支持的图标")

NocoDB 支持以下评分字段类型的图标。  
![image](https://docs.nocodb.com/assets/images/rating-icon-06378f121f8364a58ce1b0da016f6b12.png)

- [复选框](https://docs.nocodb.com/fields/field-types/select-based/checkbox)