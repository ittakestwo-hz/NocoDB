# 概述

创建模式后，您可以使用 REST API 操作数据或调用操作。我们提供了多种类型的 API 以满足不同的使用需求。有关更多详细信息，请参见以下链接：

- [Meta APIs](https://meta-apis-v2.nocodb.com/)
- [Data APIs](https://data-apis-v2.nocodb.com/)

要使用 API，您需要一个 API 密钥和终端。NocoDB 托管实例的终端 URL 格式为 `https://app.nocodb.com/api/v2/tables/TABLEID/records` 和 `https://app.nocodb.com/api/v2/meta/bases/BASEID/info`。

- 您可以在 NocoDB 中进入任意表格 > 详情 > API 代码片段，找到 TABLEID。
- 您可以点击任意数据库旁边的菜单图标 > REST APIs，并在 URL 中找到 BASEID。

有关 REST API 的其他信息，请参见下文。

## 查询参数

| **名称** | **别名** | **用例** | **默认值** | **示例值** |
| --- | --- | --- | --- | --- |
| [where](https://docs.nocodb.com/views/views-overview/#comparison-operators) | [w](https://docs.nocodb.com/views/views-overview/#comparison-operators) | 复杂的 where 条件 |  | `(colName,eq,colValue)~or(colName2,gt,colValue2)`  
[用法: 比较运算符](https://docs.nocodb.com/views/views-overview/#comparison-operators)  
[用法: 逻辑运算符](https://docs.nocodb.com/views/views-overview/#logical-operators) |
| limit | l | 获取的行数 (SQL limit 值) | 10 | 20 |
| offset | o | 分页的偏移量 (SQL offset 值) | 0 | 20 |
| sort | s | 按列名排序，用 `-` 前缀表示降序排序 |  | column\_name |
| fields | f | 结果中所需的列名 | \* | column\_name1,column\_name2 |
| shuffle | r | 分页的结果随机排列 | 0 | 1 (仅允许 0 或 1。其他值将视为 0) |

## 比较运算符

| 操作 | 含义 | 示例 |
| --- | --- | --- |
| eq | 等于 | (colName,eq,colValue) |
| neq | 不等于 | (colName,neq,colValue) |
| not | 不等于 (neq 的别名) | (colName,not,colValue) |
| gt | 大于 | (colName,gt,colValue) |
| ge | 大于或等于 | (colName,ge,colValue) |
| lt | 小于 | (colName,lt,colValue) |
| le | 小于或等于 | (colName,le,colValue) |
| is | 是 | (colName,is,true/false/null) |
| isnot | 不是 | (colName,isnot,true/false/null) |
| in | 在范围内 | (colName,in,val1,val2,val3,val4) |
| btw | 介于两值之间 | (colName,btw,val1,val2) |
| nbtw | 不在两值之间 | (colName,nbtw,val1,val2) |
| like | 类似于 | (colName,like,%name) |
| nlike | 不类似于 | (colName,nlike,%name) |
| isWithin | 在范围内 (仅适用于 `Date` 和 `DateTime`) | (colName,isWithin,sub\_op) |
| allof | 包含所有值 | (colName,allof,val1,val2,...) |
| anyof | 包含任意值 | (colName,anyof,val1,val2,...) |
| nallof | 不包含所有值 (包含部分或无值) | (colName,nallof,val1,val2,...) |
| nanyof | 不包含任意值 (不包含任何值) | (colName,nanyof,val1,val2,...) |

## 比较子运算符

在 `Date` 和 `DateTime` 列中提供以下子运算符。

| 操作 | 含义 | 示例 |
| --- | --- | --- |
| today | 今天 | (colName,eq,today) |
| tomorrow | 明天 | (colName,eq,tomorrow) |
| yesterday | 昨天 | (colName,eq,yesterday) |
| oneWeekAgo | 一周前 | (colName,eq,oneWeekAgo) |
| oneWeekFromNow | 一周后 | (colName,eq,oneWeekFromNow) |
| oneMonthAgo | 一个月前 | (colName,eq,oneMonthAgo) |
| oneMonthFromNow | 一个月后 | (colName,eq,oneMonthFromNow) |
| daysAgo | 若干天前 | (colName,eq,daysAgo,10) |
| daysFromNow | 若干天后 | (colName,eq,daysFromNow,10) |
| exactDate | 精确日期 | (colName,eq,exactDate,2022-02-02) |

在 `Date` 和 `DateTime` 列中使用 `isWithin` 时，可以使用不同的子运算符。

| 操作 | 含义 | 示例 |
| --- | --- | --- |
| pastWeek | 上周 | (colName,isWithin,pastWeek) |
| pastMonth | 上月 | (colName,isWithin,pastMonth) |
| pastYear | 去年 | (colName,isWithin,pastYear) |
| nextWeek | 下周 | (colName,isWithin,nextWeek) |
| nextMonth | 下月 | (colName,isWithin,nextMonth) |
| nextYear | 明年 | (colName,isWithin,nextYear) |
| nextNumberOfDays | 未来若干天 | (colName,isWithin,nextNumberOfDays,10) |
| pastNumberOfDays | 过去若干天 | (colName,isWithin,pastNumberOfDays,10) |

## 逻辑运算符

| 操作 | 示例 |
| --- | --- |
| ~or | (checkNumber,eq,JM555205)~or((amount,gt,200)~and(amount,lt,2000)) |
| ~and | (checkNumber,eq,JM555205)~and((amount,gt,200)~and(amount,lt,2000)) |
| ~not | ~not(checkNumber,eq,JM555205) |