# 看板

看板视图允许您使用卡片作为各种堆栈的一部分来可视化数据。您可以通过拖放轻松地将卡片重新排列到不同的堆栈中。本部分将介绍在看板视图中可以执行的所有操作。

![1010-2 看板](https://docs.nocodb.com/assets/images/kanban-e00b90c6413259b626deeeb6659281ea.png)

## 看板视图操作[](https://docs.nocodb.com/views/views-overview/#kanban-view-actions "直接链接到看板视图操作")

1.  [创建新的看板视图](https://docs.nocodb.com/views/create-view#create-new-view)
2.  [重命名现有看板视图](https://docs.nocodb.com/views/actions-on-view#rename-view)
3.  [复制看板视图](https://docs.nocodb.com/views/actions-on-view#duplicate-view)
4.  [删除看板视图](https://docs.nocodb.com/views/actions-on-view#delete-view)
5.  [共享看板视图](https://docs.nocodb.com/views/share-view)
6.  [锁定看板视图以禁止编辑](https://docs.nocodb.com/views/views-overview#view-permission-types)

## 看板视图操作[](https://docs.nocodb.com/views/views-overview/#kanban-view-operations "直接链接到看板视图操作")

1.  [重新排列看板中的字段](https://docs.nocodb.com/table-operations/field-operations#rearranging-fields)
2.  [显示或隐藏看板中的字段](https://docs.nocodb.com/table-operations/field-operations#showhide-fields)
3.  [应用筛选器以显示特定记录](https://docs.nocodb.com/table-operations/filter)
4.  [按一个或多个条件对看板上的记录进行排序](https://docs.nocodb.com/table-operations/sort)
5.  [在字段中快速搜索特定数据](https://docs.nocodb.com/table-operations/search)
6.  [将数据导出为CSV或Excel格式](https://docs.nocodb.com/table-operations/download#download-data)
7.  [更改封面图片](https://docs.nocodb.com/table-operations/field-operations#change-cover-field-gallerykanban-view)

## 看板视图堆栈字段操作[](https://docs.nocodb.com/views/views-overview/#kanban-view-stacked-by-field-operations "直接链接到看板视图堆栈字段操作")

### 更改堆栈字段[](https://docs.nocodb.com/views/views-overview/#change-stacked-by-field "直接链接到更改堆栈字段")

您可以按照以下步骤更改看板视图中记录的堆栈字段：

1.  点击工具栏中的 `堆栈字段` 菜单。
2.  点击当前选择为堆栈字段的字段名称。
3.  从下拉菜单中选择要用来堆叠记录的新字段。

![更改堆栈字段](https://docs.nocodb.com/assets/images/kanban-change-stack-a8d26dff838ea4b480a30e2db1d0624f.png)

### 添加/修改堆栈字段选项[](https://docs.nocodb.com/views/views-overview/#addmodify-stacked-by-field-options "直接链接到添加/修改堆栈字段选项")

您可以通过以下步骤在堆栈的单选字段中添加/修改选项：

1.  点击工具栏中的 `堆栈字段` 菜单。下拉列表显示此字段上的所有 `选择选项`。
2.  根据需要添加/修改选项。
3.  点击 `保存` 以保存更改。

![添加/修改堆栈字段选项](https://docs.nocodb.com/assets/images/kanban-edit-stack-options-7f9e0324e6068956dae0268031c712f7.png)

### 折叠堆栈[](https://docs.nocodb.com/views/views-overview/#collapse-stack "直接链接到折叠堆栈")

为便于查看，您可以通过以下步骤折叠看板上的堆栈：

1.  点击堆栈标题上的下拉图标。
2.  从下拉菜单中选择 `折叠堆栈`。
3.  折叠的堆栈将在看板视图中显示为垂直条。

![折叠堆栈](https://docs.nocodb.com/assets/images/kanban-collapse-stack-8ec03d704b55aba7bbc1510efd0f746d.png)

### 删除堆栈[](https://docs.nocodb.com/views/views-overview/#delete-stack "直接链接到删除堆栈")

要从看板视图中删除堆栈，请按照以下步骤操作：

1.  点击堆栈标题上的下拉图标。
2.  从下拉菜单中选择 `删除堆栈`。
3.  将显示一个确认对话框。点击 `删除` 以删除堆栈。

![删除堆栈](https://docs.nocodb.com/assets/images/kanban-delete-stack-b51611d8427f1a16a295861c0c91eb94.png)

![删除堆栈确认](https://docs.nocodb.com/assets/images/kanban-delete-stack-confirmation-e4b55be5361259d84852953931f63f8c.png)

### 重新排序堆栈[](https://docs.nocodb.com/views/views-overview/#reorder-stacks "直接链接到重新排序堆栈")

您可以通过拖放堆栈到所需位置来重新排序看板视图中的堆栈。

## 看板视图记录操作[](https://docs.nocodb.com/views/views-overview/#kanban-view-record-operations "直接链接到看板视图记录操作")

### 在堆栈内移动记录[](https://docs.nocodb.com/views/views-overview/#move-records-within-stacks "直接链接到在堆栈内移动记录")

您可以通过拖放卡片将记录移动到堆栈内的所需位置。

### 添加新记录到看板[](https://docs.nocodb.com/views/views-overview/#add-a-new-record-to-the-kanban "直接链接到添加新记录到看板")

在看板中，您可以使用堆栈底部的 `添加记录` 按钮直接向特定堆栈添加新记录。这将打开一个扩展的记录视图，您可以在其中输入新记录的数据。保存后，该记录将显示在看板视图中。您也可以在表中添加新记录，它将显示在看板视图中。

![添加记录](https://docs.nocodb.com/assets/images/kanban-add-record-6d53ed410a1ee0323790496461b53aff.png)

### 编辑看板中的现有记录[](https://docs.nocodb.com/views/views-overview/#edit-an-existing-record-on-the-kanban "直接链接到编辑看板中的现有记录")

点击看板视图中的卡片以在扩展记录视图中打开该记录。您可以在扩展记录视图中编辑记录并保存。

### 从看板中删除单个记录[](https://docs.nocodb.com/views/views-overview/#delete-a-single-record-from-the-kanban "直接链接到从看板中删除单个记录")

右键点击卡片以访问上下文菜单，并选择 `删除` 选项。

## 相关文章[](https://docs.nocodb.com/views/views-overview/#related-articles "直接链接到相关文章")

[表格视图](https://docs.nocodb.com/views/view-types/grid)  
[看板视图](https://docs.nocodb.com/views/view-types/kanban)  
[表单视图](https://docs.nocodb.com/views/view-types/form)