# 视图概览

在 NocoDB 中，视图不仅可以根据您的喜好定制视觉呈现，还可以独立控制每个视图中的记录排序和筛选。每个视图都有其独立的筛选器、数据展示和启用字段的配置，这样的独立性确保了对某一视图配置的修改不会影响到其他视图。该功能使用户能够高效地个性化数据可视化，同时保持其他视图的完整性。

提示

视图展示来自表格的数据。在某个视图中对记录的任何更新将会同步反映到同一表格的所有其他视图中。

## 支持的视图类型

1.  [表格视图](https://docs.nocodb.com/views/view-types/grid)
2.  [表单视图](https://docs.nocodb.com/views/view-types/form)
3.  [画廊视图](https://docs.nocodb.com/views/view-types/gallery)
4.  [看板视图](https://docs.nocodb.com/views/view-types/kanban)
5.  [日历视图](https://docs.nocodb.com/views/view-types/calendar)

<iframe width="560" height="315" src="https://www.youtube.com/embed/gVk5ZwMwANU?si=JcUazOp0SFWyJ6a-&amp;start=24" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"></iframe>

## 视图权限类型

我们可以为每个视图设置权限。默认情况下，视图为 `协作模式`。要查看或更改视图类型，可以展开下方的 `视图工具栏菜单`。

![锁定视图](https://docs.nocodb.com/assets/images/locked-view-98e409b4c0859f73d2d59b6e418d338b.png)

### 协作视图（默认）

默认情况下，视图设置为“协作模式”，允许拥有编辑权限或更高权限的成员修改视图配置。在此模式下，所有成员可以对视图进行读写操作。这是所有视图的默认模式。

### 锁定视图

在“锁定视图”模式下，视图配置不能被任何人更改，除非解锁该视图。在此模式下，所有成员仅限于读取视图数据，无法对其设置或内容进行任何更改。当您希望与他人共享视图但不希望他们对其进行任何更改时，此模式非常实用。