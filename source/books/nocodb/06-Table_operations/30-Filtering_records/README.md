# 记录筛选

筛选器提供了强大的方式，可根据您的具体需求来缩小和组织数据范围。NocoDB 支持嵌套筛选，允许您选择多个字段和条件进行筛选。您可以选择 `and` 或 `or` 模式来组合筛选条件，且筛选还支持查找、公式和嵌套数据。

### 添加或编辑筛选器

要添加或编辑筛选器，只需点击工具栏中的 `Filter` 按钮，然后选择 `Add filter` 或 `Add filter group`。

![添加筛选器](https://docs.nocodb.com/assets/images/filter-1-6d82d6adaa0df9338b4c29b6376de557.png)

通过指定 `Field`（字段）、`Operation`（操作）和 `Value`（值，如果适用）来配置筛选器。

![筛选器配置](https://docs.nocodb.com/assets/images/filter-2-51019e4c6061e78b8b3df002cf6db8f5.png)

您可以使用 `And` 或 `Or` 模式组合多个筛选条件。

![嵌套筛选器](https://docs.nocodb.com/assets/images/filter-3-f6db70222f513a250bf4b0bd36e3c158.png)

### 删除筛选器

要删除筛选器，点击相应筛选器右侧的垃圾桶图标。

![删除筛选器](https://docs.nocodb.com/assets/images/filter-5-e2ea016b369c57c5787ec7c4259f7fc6.png)

### 分组筛选器

您还可以选择使用筛选器组将多个筛选器分组在一起。

![分组筛选器](https://docs.nocodb.com/assets/images/filter-4-058ba55633cb86f5b1a5431c1ee8766d.png)

## 启用 NULL 和 EMPTY 筛选器

默认情况下，NULL 筛选器（`is null` 和 `is not null`）以及 EMPTY 筛选器（`is empty` 和 `is not empty`）是隐藏的。如果您希望明确筛选掉这些值，可以在 [项目设置](https://docs.nocodb.com/bases/actions-on-base#base-settings) 中启用 `Show NULL and EMPTY Filter`。

启用 `Show NULL and EMPTY Filter` 之前：

![显示 isBlank](https://docs.nocodb.com/assets/images/filter-is-blank-93b9ad8f1a235a7a0c0e198c076a7caf.png)

启用后，您可以使用 `is null` 和 `is empty` 筛选器筛选出包含 NULL 或 EMPTY 值的单元格。

![显示 NULL 和 EMPTY 筛选器](https://docs.nocodb.com/assets/images/filter-is-null-empty-1341b5cc9439c361df4992106ff00ad6.png)

另外，您也可以使用空白筛选器来筛选掉包含 NULL 或 EMPTY 值的单元格。

### 支持的筛选器

NocoDB 目前支持各字段对应的多种筛选器类型。请参阅下方的矩阵了解详细信息。

[筛选器矩阵](https://docs.google.com/spreadsheets/d/e/2PACX-1vTpCNKtA-szaXUKJEO5uuSIRnzUOK793MKnyBz9m2rQcwn7HqK19jPHeER-IIRWH9X56J78wfxXZuuv/pubhtml?gid=427284630&single=true&widget=true&headers=false)

-   [字段操作](https://docs.nocodb.com/table-operations/field-operations)
-   [排序](https://docs.nocodb.com/table-operations/sort)
-   [分组](https://docs.nocodb.com/table-operations/group-by)
-   [行高](https://docs.nocodb.com/table-operations/row-height)
-   [快速搜索](https://docs.nocodb.com/table-operations/search)
-   [下载](https://docs.nocodb.com/table-operations/download)