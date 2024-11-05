# 日期函数

本速查表提供了常用于数据分析和编程的各种日期函数的快速参考指南。每个函数都附带其语法、示例用法及简要描述。

## DATETIME\_DIFF

DATETIME\_DIFF 函数用于计算两个日期之间的差异，并以各种单位返回结果。

#### 语法

```
DATETIME_DIFF(date1, date2, ["milliseconds" | "ms" | "seconds" | "s" | "minutes" | "m" | "hours" | "h" | "days" | "d" | "weeks" | "w" | "months" | "M" | "quarters" | "Q" | "years" | "y"])
```

#### 示例

```
DATETIME_DIFF("2022/10/14", "2022/10/15", "seconds") => -86400
```

该函数比较两个日期，并返回指定单位的差值。正整数表示第二个日期在第一个日期之前，负值则相反。

___

## DATEADD

DATEADD 函数用于将指定的值添加到一个日期或日期时间。

#### 语法

```
DATEADD(date | datetime, value, ["day" | "week" | "month" | "year"])
```

#### 示例

```
DATEADD('2022-03-14', 1, 'day')     => 2022-03-15
DATEADD('2022-03-14', 1, 'week')    => 2022-03-21
DATEADD('2022-03-14', 1, 'month')   => 2022-04-14
DATEADD('2022-03-14', 1, 'year')    => 2023-03-14
```

#### 条件示例

```
IF(NOW() < DATEADD(date, 10, 'day'), "true", "false") => 如果当前日期小于指定日期加上10天，则返回 true，否则返回 false。
```

该函数支持日期和日期时间字段，且可处理负值。

___

## NOW

NOW 函数返回当前的时间和日期。

#### 语法

```
NOW()
```

#### 示例

```
NOW() => 2022-05-19 17:20:43 (当前日期和时间)
```

#### 条件示例

```
IF(NOW() < date, "true", "false") => 如果当前日期小于指定日期，则返回 true，否则返回 false。
```

该函数提供当前的时间和日期，支持日期时间字段和负值。

___

## WEEKDAY

WEEKDAY 函数返回星期几，以整数形式表示。

#### 语法

```
WEEKDAY(date, [startDayOfWeek])
```

#### 示例

```
WEEKDAY(NOW()) => 如果今天是星期一，返回 0。
WEEKDAY(NOW(), "sunday") => 如果今天是星期一，返回 1。
```

该函数返回一个介于 0 到 6（含）之间的整数，默认情况下星期一为起始日。可通过指定第二个参数更改周的起始日。

___

## DATESTR

DATESTR 函数将日期或日期时间字段转换为 "YYYY-MM-DD" 格式的字符串。

#### 语法

```
DATESTR(date | datetime)
```

#### 示例

```
DATESTR('2022-03-14') => 2022-03-14
DATESTR('2022-03-14 12:00:00') => 2022-03-14
```

该函数将日期或日期时间字段转换为 "YYYY-MM-DD" 格式的字符串，忽略时间部分。

___

## DAY

DAY 函数返回月份中的日期，以整数形式表示。

#### 语法

```
DAY(date | datetime)
```

#### 示例

```
DAY('2022-03-14') => 14
DAY('2022-03-14 12:00:00') => 14
```

该函数返回月份中的日期，整数值介于 1 到 31（含）之间。注意：获取的日期信息基于服务器的时区（默认 GMT）。如果浏览器时区与服务器时区不同，日期值可能会有所不同。

___

## MONTH

MONTH 函数返回年份中的月份，以整数形式表示。

#### 语法

```
MONTH(date | datetime)
```

#### 示例

```
MONTH('2022-03-14') => 3
MONTH('2022-03-14 12:00:00') => 3
```

该函数返回年份中的月份，整数值介于 1 到 12（含）之间。注意：获取的月份信息基于服务器的时区（默认 GMT）。如果浏览器时区与服务器时区不同，月份值可能会有所不同。

___

## HOUR

HOUR 函数返回一天中的小时数，以整数形式表示。

#### 语法

```
HOUR(date | datetime)
```

#### 示例

```
HOUR('2022-03-14 12:00:00') => 12
```

该函数返回一天中的小时数，整数值介于 0 到 23（含）之间。小时信息基于24小时制，并以服务器的时区（默认 GMT）为准。注意：如果浏览器时区与服务器时区不同，小时值可能会有所不同。

___

## 相关文章

-   [数值与逻辑运算符](https://docs.nocodb.com/fields/field-types/formula/operators)
-   [数值函数](https://docs.nocodb.com/fields/field-types/formula/numeric-functions)
-   [字符串函数](https://docs.nocodb.com/fields/field-types/formula/string-functions)
-   [条件表达式](https://docs.nocodb.com/fields/field-types/formula/conditional-expressions)