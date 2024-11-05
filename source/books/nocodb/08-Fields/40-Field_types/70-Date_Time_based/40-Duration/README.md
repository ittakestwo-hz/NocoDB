# 持续时间

`Duration` 字段类型用于存储以秒或分钟为单位的时间持续时间。NocoDB 支持多种格式，具体如下表所示。

## 创建持续时间字段

1. 点击 `Fields header` 右侧的 `+` 图标。
2. 在下拉模态框中输入字段名称（可选）。
3. 从下拉菜单中选择字段类型为 `Duration`。
4. 配置 `Duration Format`（持续时间格式）。
5. 配置默认值（可选）。
6. 点击 `Save Field` 按钮。

![image](https://docs.nocodb.com/assets/images/duration-240ca3f3201ea99e948bebd59e41dce8.png)

### 支持的持续时间格式

| 格式 | 示例 |
| --- | --- |
| HH:mm | 14:20 |
| HH:mm:ss | 12:45:30 |
| HH:mm:ss.s | 12:45:30.5 |
| HH:mm.ss.ss | 12:45.30.50 |
| HH:mm.ss.sss | 12:45.30.500 |

- [日期时间](https://docs.nocodb.com/fields/field-types/date-time-based/date-time)
- [日期](https://docs.nocodb.com/fields/field-types/date-time-based/date)
- [时间](https://docs.nocodb.com/fields/field-types/date-time-based/time)