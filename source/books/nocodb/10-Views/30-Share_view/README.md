# 分享视图

当您需要与组织外的人员协作，并且他们只需访问数据库的特定部分时，共享特定视图非常有用。此共享视图提供只读模式，任何人都可以访问，无论其是否属于您的工作区。您可以控制哪些数据字段和记录对这些外部查看者可见，从而确保任何敏感数据保持隐藏。此外，如果您对视图中的可见字段或记录进行了更改，共享链接会实时更新，立即反映这些调整。

1. 点击工具栏右上角的 `共享` 按钮
2. 切换 `启用公共查看` 来创建共享视图链接
3. 点击 `复制` 按钮将链接复制到剪贴板

![share button](https://docs.nocodb.com/assets/images/share-button-9751630544eab59c43f368bcbe4aaaae.png)

![shared view](https://docs.nocodb.com/assets/images/share-view-modal-2c40f95aa822fa2830e1f205431a4b4e.png)

#### 密码保护

如果您希望对视图进行密码保护，可以启用 `使用密码限制访问`

![password protection](https://docs.nocodb.com/assets/images/share-view-modal-2-4bb63f03e7cb528595d3f2f6335fca02.png)

#### 下载选项

您可以切换 `允许下载` 按钮，以启用或禁用共享视图链接中的 CSV/XLSX 下载选项

![download options](https://docs.nocodb.com/assets/images/share-view-modal-3-1202422c5c9bf2b234a5b5ed7a05e805.png)

表单视图在共享视图中有其他自定义选项。您可以为共享表单视图启用/禁用以下选项：

1. `调查模式`：启用此选项后，表单将以调查模式显示。
2. `从右到左显示`：启用此选项后，表单将以从右到左的方向显示。
3. `主题`：您可以从下拉菜单中为表单选择一个主题。

![form view options](https://docs.nocodb.com/assets/images/share-view-form-a0f60904770cda6be5710e12a60077bd.png)

要访问共享视图，请按照以下步骤操作：点击 `共享视图链接`。如果链接受密码保护，系统会提示您输入密码以解锁。请输入所需的密码继续。

![password modal](https://docs.nocodb.com/assets/images/share-view-password-8b55b2f905ed895f6ceddccad842c205.png)

成功输入密码并通过验证后，您将能够访问共享视图。如果链接不受密码保护，您将直接访问共享视图，无需输入密码。

![share-view](https://docs.nocodb.com/assets/images/share-view-22f8daabd281e5b6199d1e03ab814378.png)

拥有共享视图链接的用户只能查看数据，无法对视图或其内容进行任何更改。在共享视图中的记录和字段会随着原始视图的更改实时更新。访问共享视图的用户可以根据需要应用筛选器和排序。

**注意**：应用于共享视图的筛选和排序不会被保存。当重新访问共享视图时，这些筛选和排序将会被重置。