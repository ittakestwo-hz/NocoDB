# 通过导入创建表格

## 从 CSV / Excel / JSON 导入表格

### 访问导入模式

有两种方式可以访问导入模式：

#### 1\. 从 Base 仪表板

![导入数据](https://docs.nocodb.com/assets/images/base-import-from-dashboard-1-0ccc1e3e8508c11049dd45647d6c0f91.png)

![从仪表板导入](https://docs.nocodb.com/assets/images/table-import-from-dashboard-625bb54d990e6d7a01ffd6bf9c7e8aa9.png)

![从侧边栏导入](https://docs.nocodb.com/assets/images/table-import-from-sidebar-53e3a9f2cefcbc24681b88541f56dab5.png)

### 导入文件

有两种方式上传源文件：

#### 1\. 从本地目录上传

1.  在快速导入模式中选择 `上传` 选项卡。
2.  点击 `文件上传` 按钮或将文件拖放至模式窗口。
3.  [高级设置]（可选）
4.  点击 `导入` 按钮。

![图片](https://docs.nocodb.com/assets/images/import-csv-b27b1106e326164fb98c79f7075da7f7.png)

#### 2\. 从 URL 上传

1.  在快速导入模式中选择 `URL` 选项卡。
2.  粘贴文件的 URL。
3.  [高级设置]（可选）
4.  点击 `导入` 按钮。

![图片](https://docs.nocodb.com/assets/images/import-csv-url-295ceb54663f0d2fbad788296bf3c594.png)

-   可以一次导入多个文件。
-   支持的文件格式：CSV, Excel, JSON
-   最大文件大小：5 MB

### 导入配置

1.  `表名` - 默认使用文件名；双击可编辑（可选）。
2.  `字段配置`（可选）
    -   `字段名` - 从导入文件标题中识别的字段名；点击编辑。
    -   `字段类型` - 默认将所有字段映射为 `单行文本`，可以在文件导入后根据需要更改字段类型。
3.  `移除字段` - 点击删除图标以排除源文件中的某个字段（可选）。
4.  点击 `导入` 按钮开始导入文件。

![图片](https://docs.nocodb.com/assets/images/import-stage-2-3ccb53c3abc02a0ad7e74fed2589acda.png)

### 高级设置

-   **使用首记录作为标题**：默认启用。如果选中，电子表格中的首记录将被视为标题记录，其内容将作为字段名。
-   **导入数据**：默认启用。如果选中，则导入所有数据；否则仅创建表格。

> 默认情况下，首字段将被选择为显示值。

## 相关文章

-   [创建新表格](https://docs.nocodb.com/tables/create-table)
-   [将数据从 CSV / Xlsx 导入现有表格](https://docs.nocodb.com/tables/import-data-into-existing-table)
-   [重命名表格](https://docs.nocodb.com/tables/actions-on-table#rename-table)
-   [复制表格](https://docs.nocodb.com/tables/actions-on-table#duplicate-table)
-   [删除表格](https://docs.nocodb.com/tables/actions-on-table#delete-table)