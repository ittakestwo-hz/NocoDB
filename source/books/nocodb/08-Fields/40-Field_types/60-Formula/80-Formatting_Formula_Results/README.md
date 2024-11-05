# 格式化公式结果

格式化公式的输出允许您根据结果的类型定制数据的显示方式。提供了多种格式选项，以确保您的数据以最有用且视觉上吸引人的方式呈现。

![image](https://docs.nocodb.com/assets/images/formula-format-003ced2896bb1778b6f1d8ee995a47b0.png)

## 数字格式

![image](https://docs.nocodb.com/img/v2/fields/numeric-format.png)

### 小数

`小数格式`用于以指定的小数位数显示结果，允许您定义精度。

### 货币

`货币格式`非常适合显示货币值，并可设置和显示特定的货币符号。

### 百分比

`百分比格式`将结果显示为数字，并包括将其配置为进度条的选项。

### 评分

`评分格式`非常适合用于 1 到 10 的评分。它允许您自定义图标、颜色，并选择该范围内的最大评分值。

## 日期格式

![image](https://docs.nocodb.com/img/v2/fields/date-format.png)

### 日期时间

`日期时间格式`同时显示日期和时间值。

### 日期

`日期格式`仅显示日期值，提供多种日期格式。

### 时间

`时间格式`以 12 小时或 24 小时格式显示结果。

## 文本格式

![image](https://docs.nocodb.com/img/v2/fields/text-format.png)

### 电子邮件

`电子邮件格式`用于将结果显示为可点击的电子邮件链接。当在公式输出中检测到电子邮件地址时，它将被格式化为 mailto 链接，允许用户点击并打开其默认的电子邮件客户端以发送电子邮件。

### URL

`URL 格式`旨在将结果显示为可点击的网页链接。当在公式输出中识别到有效的 URL 时，它将被格式化为超链接，使用户能够点击并直接导航到指定的网页地址。

### 电话号码

`电话号码格式`非常适合将结果显示为电话号码。

## 布尔格式

![image](https://docs.nocodb.com/img/v2/fields/boolean-format.png)

### 复选框

当 NocoDB 将公式的输出识别为布尔结果时，您可以应用 `复选框格式` 以类似于复选框字段的方式显示它。您可以根据需要自定义图标和颜色。

___

## 相关文章

- [数字函数](https://docs.nocodb.com/fields/field-types/formula/numeric-functions)
- [字符串函数](https://docs.nocodb.com/fields/field-types/formula/string-functions)
- [日期函数](https://docs.nocodb.com/fields/field-types/formula/date-functions)
- [条件表达式](https://docs.nocodb.com/fields/field-types/formula/conditional-expressions)