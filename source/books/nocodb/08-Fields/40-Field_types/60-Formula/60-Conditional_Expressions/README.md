# 条件表达式

本速查表提供了数据分析和编程中常用的各种条件表达式的快速参考指南。每个表达式都附有其语法、示例用法和简要描述。

## IF

编程和电子表公式中的 IF 函数提供了一种执行条件操作的方法。它评估一个条件，并在该条件为 `TRUE` 时返回一个值，在条件为 `FALSE` 时返回另一个值。

#### 语法

```
IF(expr, successCase, elseCase)
```

#### 示例

```
IF({field} > 1, Value1, Value2) 
输出 - 如果 `{field} > 1` 评估为 TRUE，则返回 `Value1` - 否则返回 `Value2`
```

## SWITCH

SWITCH 函数是处理多个案例的多功能工具。它将给定表达式（expr）与一系列模式进行评估，并返回第一个匹配模式的相应值。如果没有匹配，则返回默认值。

#### 语法

```
SWITCH(expr, [pattern, value, ..., default])
```

#### 示例

```
SWITCH({field}, 1, 'One', 2, 'Two', '--') 
输出基于 `{field}` 的输出的开关案例值：- 如果 `{field} = 1`，则返回 `'One'` - 如果 `{field} = 2`，则返回 `'Two'` - 默认情况下返回 `'--'`
```

## AND

AND 函数是一个逻辑运算符，仅在其所有条件都为真时返回 TRUE。

#### 语法

#### 示例

```
AND({field} > 2, {field} < 10) 
输出 - 如果 `{field} > 2` 和 `{field} < 10` 都评估为 TRUE，则返回 TRUE
```

## OR

OR 函数是另一个逻辑运算符，如果至少有一个条件为真，则返回 TRUE。

#### 语法

#### 示例

```
OR({field} > 2, {field} < 10) 
输出 - 如果条件 `{field} > 2` 或 `{field} < 10` 至少有一个评估为 TRUE，则返回 TRUE
```

提示

逻辑运算符与数值运算符可以用于构建条件 `表达式`。

示例：

```
IF({marksSecured} > 80, "GradeA", "GradeB")  
```

```
SWITCH({quarterNumber},      1, 'Jan-Mar',    2, 'Apr-Jun',    3, 'Jul-Sep',    4, 'Oct-Dec',    'INVALID')
```

## 相关文章

-   [数值和逻辑运算符](https://docs.nocodb.com/fields/field-types/formula/operators)
-   [数值函数](https://docs.nocodb.com/fields/field-types/formula/numeric-functions)
-   [字符串函数](https://docs.nocodb.com/fields/field-types/formula/string-functions)
-   [日期函数](https://docs.nocodb.com/fields/field-types/formula/date-functions)