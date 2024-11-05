# 日历视图

日历视图可以将数据以日历格式展示。您可以轻松地通过拖拽将记录重新排列到不同的日期中。同时，您还可以以日、周、月或年的格式查看记录。本节将介绍日历视图中的所有操作。

![1010-2 日历](https://docs.nocodb.com/assets/images/markers-0b9e6cd1c8f6b0296112e6b13bebeccd.png)

## 日历视图操作[](https://docs.nocodb.com/views/views-overview/#calendar-view-actions "直接链接到日历视图操作")

1.  [创建新的日历视图](https://docs.nocodb.com/views/create-view#create-new-view)
2.  [重命名现有的日历视图](https://docs.nocodb.com/views/actions-on-view#rename-view)
3.  [复制日历视图](https://docs.nocodb.com/views/actions-on-view#duplicate-view)
4.  [删除日历视图](https://docs.nocodb.com/views/actions-on-view#delete-view)
5.  [分享日历视图](https://docs.nocodb.com/views/share-view)
6.  [锁定日历视图以防编辑](https://docs.nocodb.com/views/views-overview#view-permission-types)

## 时间刻度[](https://docs.nocodb.com/views/views-overview/#timescales "直接链接到时间刻度")

在日历视图中，NocoDB 支持 4 种不同的时间刻度：

### 日视图[](https://docs.nocodb.com/views/views-overview/#day "直接链接到日视图")

在日视图中，您可以查看单日的记录。对于包含日期时间字段的记录，您可以将其拖动到当天的不同时间段。

![日视图](https://docs.nocodb.com/assets/images/day-scale-be0c966b44860de53cb410e87e1392a2.png)

### 周视图[](https://docs.nocodb.com/views/views-overview/#week "直接链接到周视图")

在周视图中，您可以查看一周的记录，并可以将记录拖动到不同的日期。对于包含日期时间字段的记录，您可以在不同时间段之间移动它们。

![周视图](https://docs.nocodb.com/assets/images/week-scale-1ec5cb296b55dc10967bc63aabde4bec.png)

### 月视图[](https://docs.nocodb.com/views/views-overview/#month "直接链接到月视图")

在月视图中，您可以查看整个月的记录，并可以将记录拖动到不同的日期。

![月视图](https://docs.nocodb.com/assets/images/month-scale-ede2ec05c3b4bcce16deb434f844136d.png)

### 年视图[](https://docs.nocodb.com/views/views-overview/#year "直接链接到年视图")

年视图允许您从全局视角查看整年的记录。日期上的蓝色标记表示当天有记录。您可以点击日期查看当天的记录。

![年视图](https://docs.nocodb.com/assets/images/year-scale-c7b02552a300e08dd181c1f256667dbe.png)

## 日历视图操作[](https://docs.nocodb.com/views/views-overview/#calendar-view-operations "直接链接到日历视图操作")

### 自定义记录标签[](https://docs.nocodb.com/views/views-overview/#customize-record-label "直接链接到自定义记录标签")

您可以自定义显示在日历上的记录标签。点击工具栏中的 `字段` 菜单，在下拉菜单中：

- 使用切换开关启用或禁用您想要在日历上显示的字段。
- 使用拖拽重新排序您想要显示的字段顺序。
- 使用格式菜单选项自定义字段显示，可以选择将字段设为加粗、斜体或下划线。

![字段菜单](https://docs.nocodb.com/assets/images/fields-menu-d5f58a5a678ce396d0279f86773000b5.png)

### 添加新记录[](https://docs.nocodb.com/views/views-overview/#add-new-records "直接链接到添加新记录")

要向日历添加新记录，请点击日历右下角的 `+` 图标。或者，您也可以双击日历中的空白区域添加新记录。在弹出的表单中填写详细信息并点击 `保存`。

### 展开记录详情[](https://docs.nocodb.com/views/views-overview/#expand-record-details "直接链接到展开记录详情")

要查看记录详情，点击记录即可展开并查看所有详细信息。

### 编辑记录详情[](https://docs.nocodb.com/views/views-overview/#edit-record-details "直接链接到编辑记录详情")

通过拖动记录到不同的日期或时间来调整位置。要编辑记录的其他详细信息，点击记录展开后进行编辑。完成修改后点击 `保存`。

### 删除记录[](https://docs.nocodb.com/views/views-overview/#delete-record "直接链接到删除记录")

要删除记录，点击记录展开后，在记录的上下文菜单中点击 `删除` 按钮，并在确认对话框中点击 `删除` 确认。

1.  [应用筛选器以在日历上显示特定记录](https://docs.nocodb.com/table-operations/filter)
2.  [按一个或多个条件对日历上的记录排序](https://docs.nocodb.com/table-operations/sort)
3.  [在字段中执行快速搜索以查找特定数据](https://docs.nocodb.com/table-operations/search)
4.  [将数据导出为 CSV 或 Excel 格式](https://docs.nocodb.com/table-operations/download#download-data)