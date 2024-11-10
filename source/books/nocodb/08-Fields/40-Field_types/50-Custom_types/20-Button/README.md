# 按钮

**按钮**字段允许用户在表中创建交互式按钮。这些按钮可以触发特定的操作，使工作流程更加动态和高效。通过按钮字段，您可以通过单击一次导航到外部 URL、运行自定义 webhook，甚至运行自定义脚本（即将推出！）。

NocoDB 目前支持两种类型的按钮字段操作：

1.  **打开 URL**：打开一个新标签页，显示由按钮字段中的公式生成的 URL。该 URL 可以是静态的，也可以是基于当前记录数据的动态 URL。
2.  **运行 Webhook**：使用配置的 URL 和自定义有效负载触发一个 webhook。有效负载可以包含当前记录的数据。

<iframe width="560" height="315" src="https://www.youtube.com/embed/V20tQDkbkvU?si=7EL1IppfR7V9LRBF&amp;start=13" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"></iframe>

## 创建按钮字段 [](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#create-a-button-field "直接链接到创建按钮字段")

1.  点击 `Fields` 标题右侧的 `+` 图标。
2.  在下拉模态中，输入字段名称（可选）。
3.  从下拉菜单中选择字段类型为 `Button`。
4.  根据需要配置按钮的 **外观** 设置。这包括按钮文本、颜色和图标。
5.  从下拉菜单中选择操作类型。
6.  根据需要配置按钮的 **操作** 设置。这取决于您希望按钮执行的操作：
    -   **打开 URL**：使用公式编辑器创建动态 URL。
    -   **运行 Webhook**：从下拉菜单中选择一个 webhook 或通过点击 `+` 图标创建一个新的 webhook。
7.  点击 `Save Field` 按钮。

### 按钮 URL [](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#button-url "直接链接到按钮 URL")

![image](https://docs.nocodb.com/assets/images/button-url-25c2124e1e7b2b07546ed1663958784a.png)

### 按钮 Webhook [](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#button-webhook "直接链接到按钮 Webhook")

![image](https://docs.nocodb.com/assets/images/button-webhook-4df33807af242c3c21f99f32de6418ca.png)

信息

-   对于“运行 Webhook”操作，必须在 `Webhooks` 部分创建特定触发类型的 webhook。您可以在多个按钮字段中使用相同的 webhook。
-   在共享视图和共享 Base 中，“运行 Webhook”操作将被禁用。

#### 编辑 Webhook [](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#edit-webhook "直接链接到编辑 Webhook")

要编辑 webhook，请点击按钮字段设置中 webhook 名称旁边的 `Edit` 图标。这将打开 webhook 设置模态，在此您可以编辑 webhook 的 URL、方法、头信息和有效负载。点击 `Save changes` 按钮以保存更改。

![](https://docs.nocodb.com/img/v2/fields/types/button-webhook-edit.png)

![image](https://docs.nocodb.com/assets/images/button-webhook-edit-2-cffa4301c5f5ec66673595ac4cf32f68.png)

创建的 webhook 可以通过详细信息选项卡中的 [Webhook](https://docs.nocodb.com/category/webhook) 部分访问。有关更多详细信息，请参考以下文章：

-   [创建 webhook](https://docs.nocodb.com/automation/webhook/create-webhook#create-webhook)
-   [编辑 webhook](https://docs.nocodb.com/automation/webhook/actions-on-webhook#edit-webhook)
-   [删除 webhook](https://docs.nocodb.com/automation/webhook/actions-on-webhook#delete-webhook)

注意

-   删除一个 webhook 将从所有使用它的按钮字段中移除它。
-   删除一个按钮字段不会删除与之关联的 webhook。
-   同一个 webhook 可以在多个按钮字段中使用。