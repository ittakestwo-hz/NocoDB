# 特定数据库类型

## 创建特定数据库类型字段

1. 点击 `Fields header` 右侧的 `+` 图标。
2. 在下拉模态框中，输入字段名称（可选）。
3. 从下拉菜单中选择字段类型为 `Specific DB Type`。
4. 配置字段的默认值（可选）。
5. 提供数据库特定数据类型的配置。
6. 点击 `Save Field` 按钮。

![image](https://docs.nocodb.com/assets/images/specific-db-type-8f55b4cd889fbfd2d9a88abc8a4c2b97.png)

### 高级字段属性

- `NN` **Not Null**：确保列不能有 NULL 值，要求始终提供一个值。
- `PK` **Primary Key**：唯一标识表中的每一条记录。
- `AI` **Auto Increment**：为每条新记录自动生成一个唯一编号，通常与主键一起使用。
- `UN` **Unsigned**：确保列只能存储非负数，常用于计数器、标识符或货币值。
- `AU` **Auto Update**：在记录更新时自动将列更新为当前时间戳，通常用于时间戳或日期时间列。

> 注：特定数据库类型仅适用于外部数据源连接。