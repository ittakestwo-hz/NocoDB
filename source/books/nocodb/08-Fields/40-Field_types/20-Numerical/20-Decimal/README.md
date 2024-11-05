# 十进制

`Decimal` 字段类型用于存储十进制值。使用场景包括存储 `salary`（薪资）、`price`（价格）等。NocoDB 支持最多 8 位的精度。

## 创建十进制字段

1. 点击 `Fields header` 右侧的 `+` 图标。
2. 在下拉模态框中，输入字段名称（可选）。
3. 从下拉列表中选择字段类型为 `Decimal`。
4. 配置 `Precision` - NocoDB 支持最多 8 位的精度。
5. 设置字段的默认值（可选）。
6. 点击 `Save Field` 按钮。

![image](https://docs.nocodb.com/assets/images/decimal-8e66d00b5270b1f38775d7e71d46975a.png)

信息

- 默认的十进制精度为 1 位。

## 相似的数值字段

以下是 NocoDB 中其他可用的数值字段，带有一些自定义附加功能。

- [Number](https://docs.nocodb.com/fields/field-types/numerical/number)
- [Percent](https://docs.nocodb.com/fields/field-types/numerical/percent)
- [Currency](https://docs.nocodb.com/fields/field-types/numerical/currency)