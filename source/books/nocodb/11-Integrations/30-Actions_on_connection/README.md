# 连接操作

## 列出连接[](https://docs.nocodb.com/views/views-overview/#list "直接链接到列表")

要在 NocoDB 中列出所有连接，请按照以下步骤操作：

1.  在左侧边栏中选择 **Integrations（集成）** 菜单。
2.  点击 **Connections（连接）** 标签。

![连接列表](https://docs.nocodb.com/assets/images/connections-list-ade76b85ae2223f9a23217e68b908935.png)

连接列表为该工作区中的所有连接提供了一个综合视图，详细信息包括：

-   连接名称，在创建时指定。
-   连接类型，即集成类型（例如：PG、MySQL）。
-   添加日期，指明该连接创建的日期。
-   创建人，指明创建此连接的用户。
-   使用情况，取决于集成的类型。
    -   对于数据库类型的集成，指定使用此连接的数据源数量。

info

请注意，NocoDB 中的连接没有所有权概念。一个工作区中创建的所有连接对该工作区内符合条件的所有用户均可访问。

-   具有“Workspace Creator+”权限的用户可以创建、编辑、复制和删除连接。
-   具有“Base Creator+”权限的用户可以使用这些连接创建数据源。

## 编辑连接[](https://docs.nocodb.com/views/views-overview/#edit "直接链接到编辑")

要在 NocoDB 中编辑连接，请打开 [连接列表](https://docs.nocodb.com/views/views-overview/#list) 并按照以下步骤操作：

-   点击要编辑的连接。
-   在接下来的弹窗中修改所需的详细信息。
-   如果适用，请点击 **测试连接**。
    -   适用于已更新数据库集成连接信息的情况。
-   点击 **更新连接** 按钮以保存更改。

## 复制连接[](https://docs.nocodb.com/views/views-overview/#duplicate "直接链接到复制")

要在 NocoDB 中复制连接，请打开 [连接列表](https://docs.nocodb.com/views/views-overview/#list) 并按照以下步骤操作：

1.  点击要复制的连接旁边的操作菜单（三个点）。
2.  从下拉菜单中选择 **复制** 选项。

复制的连接将创建一个与原始连接相同的连接条目，并在连接名称后加上 **\_copy** 后缀。

![复制连接](https://docs.nocodb.com/assets/images/connection-list-actions-bd0c2ef7ad7782c4ef45064eb80a6aa1.png)

## 删除连接[](https://docs.nocodb.com/views/views-overview/#delete "直接链接到删除")

要在 NocoDB 中删除连接，请打开 [连接列表](https://docs.nocodb.com/views/views-overview/#list) 并按照以下步骤操作：

1.  点击要删除的连接旁边的操作菜单（三个点）。
2.  从下拉菜单中选择 **删除** 选项。
3.  在随后的弹窗中点击 **删除** 按钮以确认删除。

![删除连接](https://docs.nocodb.com/assets/images/connection-list-actions-bd0c2ef7ad7782c4ef45064eb80a6aa1.png)

![删除连接确认](https://docs.nocodb.com/assets/images/connections-delete-confirmation-828f2cfcafb3e4fd81788030fe31f2bf.png)

warning

请注意，删除数据库连接**将删除所有使用该连接的关联数据源**，并从该工作区中的所有库中移除。