# 电子邮件

`Email` 字段是为存储电子邮件 ID 定制的文本字段。它是一种特殊类型的 `单行文本` 字段，具有以下特点：

- 可选的电子邮件 ID 验证
- 单元格显示为可点击链接

## 创建一个 `Email` 字段 [](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#create-an-email-field "直接链接到创建 Email 字段")

1. 点击 `Fields header` 右侧的 `+` 图标
2. 在下拉模态框中输入字段名称（可选）。
3. 从下拉菜单中选择字段类型为 `Email`。
4. 通过切换 `Validate Email` 复选框启用验证（可选）。
5. 设置字段的默认值（可选）。
6. 点击 `Save Field` 按钮。

![image](https://docs.nocodb.com/assets/images/email-764cb45f6208ba575ca2b5c1dabded86.png)

注意

- 指定默认值时不要加引号。
- 验证仅确保输入的值是有效的电子邮件 ID，并不检查该电子邮件 ID 是否存在。

## 类似的文本字段 [](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#similar-text-based-fields "直接链接到类似的文本字段")

以下是 NocoDB 中可用的其他文本字段，专为特定用例定制。

- [单行文本](https://docs.nocodb.com/fields/field-types/text-based/single-line-text)
- [长文本](https://docs.nocodb.com/fields/field-types/text-based/long-text)
- [URL](https://docs.nocodb.com/fields/field-types/text-based/url)
- [电话](https://docs.nocodb.com/fields/field-types/text-based/phonenumber)