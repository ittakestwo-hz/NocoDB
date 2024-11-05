# 日期

`Date` 字段类型用于存储日期值。NocoDB 支持多种日期格式，详细信息见下表。

## 创建日期字段 [](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#create-a-date-field "直接链接到创建日期字段")

1. 点击 `Fields header` 右侧的 `+` 图标。
2. 在下拉框中输入字段名称（可选）。
3. 从下拉菜单中选择字段类型为 `Date`。
4. 配置 `日期格式`。
5. 配置默认值（可选）。
6. 点击 `保存字段` 按钮。

![image](https://docs.nocodb.com/assets/images/date-f31bd796ffe546c4ad5c3bd0def5df03.png)

### 支持的日期格式 [](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#supported-date-formats "直接链接到支持的日期格式")

| 格式 | 示例 |
| --- | --- |
| YYYY-MM-DD | 2023-09-22 |
| YYYY/MM/DD | 2023/09/22 |
| DD-MM-YYYY | 22-09-2023 |
| MM-DD-YYYY | 09-22-2023 |
| DD/MM/YYYY | 22/09/2023 |
| MM/DD/YYYY | 09/22/2023 |
| DD MM YYYY | 22 09 2023 |
| MM DD YYYY | 09 22 2023 |
| YYYY MM DD | 2023 09 22 |

-   [日期时间](https://docs.nocodb.com/fields/field-types/date-time-based/date-time)
-   [时间](https://docs.nocodb.com/fields/field-types/date-time-based/time)
-   [持续时间](https://docs.nocodb.com/fields/field-types/date-time-based/duration)