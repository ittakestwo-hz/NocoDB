# 将数据导入现有表

## 从 CSV / Excel 导入数据

### 访问导入模式

1.  点击工具栏中的 `...` 上下文菜单。
2.  点击 `上传` 按钮。
3.  选择 `上传 CSV` 或 `上传 Excel` 选项。

![image](https://docs.nocodb.com/assets/images/upload-csv-1-5060880a942894e2cf7d72a27b048520.png)

### 导入文件数据

有两种方式上传源文件：

#### 1\. 从本地目录上传

1.  在快速导入模式中选择 `上传` 选项卡。
2.  点击 `文件上传` 按钮或将文件拖放到模式窗口中。
3.  [高级设置](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#advance-settings)（可选）
4.  点击 `导入` 按钮。

![image](https://docs.nocodb.com/assets/images/upload-csv-2-8d2bf537b779871fcd91d482507b6ec2.png)

#### 2\. 从 URL 上传

1.  在快速导入模式中选择 `URL` 选项卡。
2.  粘贴文件的 URL。
3.  [高级设置](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#advance-settings)（可选）
4.  点击 `导入` 按钮。

![image](https://docs.nocodb.com/assets/images/upload-csv-url-e91498d1e314587238b1379f73bee6b1.png)

### 字段映射

1.  **表名**（可选）
    
    -   默认为文件名；双击即可编辑。
2.  **字段映射**（可选）
    
    -   现有字段名列在 `源字段` 下，从导入文件识别的新字段列在 `目标字段` 下。
    -   NocoDB 会根据源字段名自动映射目标字段名。
    -   您可以通过点击目标字段并使用下拉菜单来重新配置映射。
3.  **排除字段**（可选）
    
    -   提供了一个复选框，可用于排除某个字段不被导入。
4.  **开始导入**
    
    -   点击 `导入` 按钮开始文件导入过程。

![image](https://docs.nocodb.com/assets/images/upload-csv-3-2b437b676c7ea55dfc099c630c62bc32.png)

### 高级设置

-   `解析记录数以推断数据类型` - 默认解析 500 条记录。
-   `使用首行作为标题` - 默认启用。如果选中，电子表格中的首行将被视为标题行，并使用其内容作为字段名。

## 相关文章

-   [创建新表](https://docs.nocodb.com/tables/create-table)
-   [使用 CSV、Excel 或 JSON 创建表](https://docs.nocodb.com/tables/create-table-via-import)
-   [重命名表](https://docs.nocodb.com/tables/actions-on-table#rename-table)
-   [复制表](https://docs.nocodb.com/tables/actions-on-table#duplicate-table)
-   [删除表](https://docs.nocodb.com/tables/actions-on-table#delete-table)