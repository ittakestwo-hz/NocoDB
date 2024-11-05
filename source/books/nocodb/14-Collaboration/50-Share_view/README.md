# 分享视图

1. 点击工具栏右上角的 `分享` 按钮
2. 切换 `启用公开查看` 来创建共享视图链接
3. 点击 `复制` 按钮将链接复制到剪贴板

![分享按钮](https://docs.nocodb.com/assets/images/share-button-9751630544eab59c43f368bcbe4aaaae.png)

![共享视图](https://docs.nocodb.com/assets/images/share-view-modal-2c40f95aa822fa2830e1f205431a4b4e.png)

#### 密码保护

如果您希望设置密码保护的视图，可以启用 `用密码限制访问`

![密码保护](https://docs.nocodb.com/assets/images/share-view-modal-2-4bb63f03e7cb528595d3f2f6335fca02.png)

#### 下载选项

您可以切换 `允许下载` 按钮来启用或禁用共享视图链接中的 CSV/XLSX 下载选项

![下载选项](https://docs.nocodb.com/assets/images/share-view-modal-3-1202422c5c9bf2b234a5b5ed7a05e805.png)

表单视图具有额外的共享视图自定义选项。您可以启用/禁用以下选项以便共享表单视图：

1. `调查模式`：启用此选项时，将以调查模式显示表单。
2. `RTL 方向`：启用此选项时，将以 RTL 方向显示表单。
3. `主题`：您可以从下拉菜单中选择表单的主题。![表单视图选项](https://docs.nocodb.com/assets/images/share-view-form-a0f60904770cda6be5710e12a60077bd.png)

要访问共享视图，请按照以下步骤操作：点击 `共享视图 URL`。如果 URL 受到密码保护，系统会提示您输入密码以解锁它。请输入所需的密码以继续。

![密码模态](https://docs.nocodb.com/assets/images/share-view-password-8b55b2f905ed895f6ceddccad842c205.png)

成功输入和验证密码后，您将获得对共享视图的访问权限。如果 URL 没有密码保护，您将直接被引导到共享视图，无需输入密码。

![共享视图](https://docs.nocodb.com/assets/images/share-view-22f8daabd281e5b6199d1e03ab814378.png)

拥有共享视图链接的用户只能查看数据，无法对视图或其内容进行任何更改。共享视图中的记录和字段将在原始视图发生更改时实时更新。访问共享视图的用户可以根据需要应用过滤器和对记录进行排序。

信息

请注意，对共享视图应用的过滤器和排序不会被保留。再次访问共享视图时，这些过滤器和排序将被重置。