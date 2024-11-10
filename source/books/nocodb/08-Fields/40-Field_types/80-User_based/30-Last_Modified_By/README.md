# 最后修改者

自版本 v0.204.0（2024年1月）以来，NocoDB 内部捕获了最后修改记录的用户信息。此信息作为系统字段存储在数据库中，默认不包含在表中。要在表中查看此信息，可以按照以下步骤手动创建一个 `Last Modified By` 字段。

## 创建 `Last Modified By` 字段

1. 点击 `Fields header` 右侧的 `+` 图标。
2. 在下拉模态框中输入字段名称（可选）。
3. 从下拉菜单中选择字段类型为 `LastModifiedBy`。
4. 点击 `Save Field` 按钮。

![image](https://docs.nocodb.com/assets/images/last-modified-by-0d4c173ec1213bbad45123371f32f4b7.png)

注意

- 当连接到外部数据库时，最后修改记录的用户信息不会自动捕获。您可以按照上述步骤手动创建 `Last Modified By` 字段。对于外部数据库连接，此字段不是系统字段，可以被删除。
- `Last Modified By` 字段为空表示记录要么：
    - 记录已创建但从未修改。
    - 在最后修改者功能推出之前（v0.204.0，2024年1月）。在此功能发布之前，未捕获此信息。
    - 外部数据库连接：信息仅在显式创建字段后捕获。
- 在记录首次创建时，`Last Modified By` 字段不会更新（初始化为 NULL）。

## 单元格显示

`Last Modified By` 字段在表视图中显示为只读字段。如果用户没有设置显示名称，则显示最后修改记录的用户的电子邮件地址。如果用户设置了显示名称，则显示名称将被显示。

- [创建者](https://docs.nocodb.com/fields/field-types/user-based/created-by)