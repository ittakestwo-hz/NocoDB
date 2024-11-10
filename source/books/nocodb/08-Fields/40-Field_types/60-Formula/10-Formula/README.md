# 公式

## 创建公式字段

1. 点击 `字段标题` 右侧的 `+` 图标。
2. 在下拉模态框中，输入字段名称（可选）。
3. 从下拉菜单中选择字段类型为 `公式`。
4. 插入所需的公式。
5. 点击 `保存字段` 按钮。

![image](https://docs.nocodb.com/assets/images/formula-f6e9e22e90579dd9f7307338dde8ec07.png)

> **提示**
> 
> - 您可以根据需要使用明确的数值或字符串，例如 `123`（数字）或 `"123"`（字符串）。
> 
> - 在公式中可以使用 `{}` 引用字段名称，例如 `{字段名称}`。
> 
> - 支持嵌套公式（公式方程引用另一个公式字段）。

> **注意**
> 
> - 与其他字段类型不同，公式单元格无法通过双击进行修改，因为该值是基于公式生成的。
> ![image](https://user-images.githubusercontent.com/35857179/189109486-4d41f2b7-0a19-46ef-8bb4-a8d1aabd3592.png)

## 支持的公式函数

- [数值和逻辑运算符](https://docs.nocodb.com/fields/field-types/formula/operators)
- [数值函数](https://docs.nocodb.com/fields/field-types/formula/numeric-functions)
- [字符串函数](https://docs.nocodb.com/fields/field-types/formula/string-functions)
- [日期函数](https://docs.nocodb.com/fields/field-types/formula/date-functions)
- [条件表达式](https://docs.nocodb.com/fields/field-types/formula/conditional-expressions)