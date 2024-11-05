# 条形码

`Barcode` 是一种自定义字段类型，允许您从字符串值生成条形码。这对于生成诸如 URL、电话号码或其他可以表示为字符串的数据的条形码非常有用。

以下字段类型支持作为参考字段：

-  公式
-  单行文本
-  长文本
-  电话号码
-  URL
-  电子邮件

## 创建条形码字段

1. 点击 `Fields header` 右侧的 `+` 图标。
2. 在下拉模态中，输入字段名称（可选）。
3. 从下拉菜单中选择字段类型为 `Barcode`。
4. 选择用作条形码源的字段。
5. 从下拉菜单中选择条形码类型。
6. 点击 `Save Field` 按钮。

![image](https://docs.nocodb.com/assets/images/barcode-a4164f41826b6ad850b8672d09f0457c.png)

### 单元格显示

单元格显示从源字段生成的条形码。点击单元格可打开二维码的放大视图。

![image](https://docs.nocodb.com/assets/images/barcode-cell-5e6612ed1460a61d5e51629f7b068d35.png)  
![image](https://docs.nocodb.com/assets/images/barcode-expand-29f49619f7b7dd014841681482c8a8af.png)

### 支持的条形码类型

NocoDB 支持以下条形码类型作为条形码字段类型。

-  CODE128
-  EAN-13
-  EAN-8
-  EAN-5
-  EAN-2
-  UPC (A)
-  CODE39
-  ITF-14
-  MSI
-  Pharma code
-  Coda bar

-  [二维码](https://docs.nocodb.com/fields/field-types/custom-types/QR-code)