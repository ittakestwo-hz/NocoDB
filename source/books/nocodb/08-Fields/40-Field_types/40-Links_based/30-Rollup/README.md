# 汇总

`Rollup` 字段用于从相关表的字段中聚合数据。通常用于计算总数、平均值和其他聚合数据。

## 创建汇总字段

1. 点击 `Fields header` 右侧的 `+` 图标。
2. 在下拉模态框中输入字段名称（可选）。
3. 从下拉菜单中选择字段类型为 `Rollup`。
4. 从下拉菜单中选择链接字段。该字段将当前表与相关表连接起来。
5. 从下拉菜单中选择要显示的字段。该字段将在当前表中显示。
6. 从下拉菜单中选择聚合函数。该函数将用于聚合数据。
7. 点击 `Save Field` 按钮。

![image](https://docs.nocodb.com/assets/images/rollup-bf68cdbc91743484a43f978f74ce18ef.png)

### 聚合函数

以下是 NocoDB 支持的每个聚合函数的简要描述表：

| 聚合函数       | 描述                           |
| -------------- | ------------------------------ |
| Count          | 计算数据集中记录的数量。      |
| Minimum        | 从数据集中获取最小值。        |
| Maximum        | 从数据集中获取最大值。        |
| Average        | 计算数据集中的平均值。        |
| Sum            | 将数据集中的所有值相加。      |
| Count Distinct | 计算数据集中不同值的数量。    |
| Sum Distinct   | 将数据集中所有不同值相加。    |
| Average Distinct| 计算数据集中不同值的平均值。 |

## 类似链接字段

- [Links](https://docs.nocodb.com/fields/field-types/links-based/links)
- [Lookup](https://docs.nocodb.com/fields/field-types/links-based/lookup)