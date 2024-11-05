# Base 的操作

Base 的上下文菜单提供了一系列可以对 Base 执行的快速操作。要访问此菜单，请点击位于左侧边栏中 Base 名称旁边的省略号符号（`...`）。![Base 上下文菜单](https://docs.nocodb.com/assets/images/base-context-menu-8cdc9e3b6c6f450d66cb324e8ea1feea.png)

## 重命名 Base [](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#rename-base "重命名 Base 的直接链接")

要修改 Base 的名称，您可以按照以下步骤轻松完成：

1. 点击位于左侧边栏中 Base 名称旁边的省略号（`...`），以启动 Base 上下文菜单。
2. 在出现的下拉菜单中选择“重命名”选项。
3. 在提供的字段中输入 Base 的新名称，然后按 `Enter` 键确认并保存更新后的名称。

![Base 上下文菜单](https://docs.nocodb.com/assets/images/base-context-menu-8cdc9e3b6c6f450d66cb324e8ea1feea.png)

![重命名 Base](https://docs.nocodb.com/assets/images/base-rename-027fd5fbcdca058a00c8213c263d1836.png)

## 收藏 Base [](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#star-base "收藏 Base 的直接链接")

您可以通过以下简单步骤收藏 Base：

1. 点击位于左侧边栏中 Base 名称旁边的省略号（`...`）以启动 Base 上下文菜单。
2. 在出现的下拉菜单中选择“添加到收藏”选项。
3. 之后，指定的 Base 将被放入左侧边栏的“收藏”部分。

![Base 上下文菜单](https://docs.nocodb.com/assets/images/base-context-menu-8cdc9e3b6c6f450d66cb324e8ea1feea.png)

![已收藏的 Base](https://docs.nocodb.com/assets/images/base-starred-082719a6b8a527be8b23a2d511867ccd.png)

> 已收藏的 Base 将出现在左侧边栏的“收藏”部分。

### 从收藏列表中移除 Base [](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#remove-a-base-from-starred-list "从收藏列表中移除 Base 的直接链接")

1. 点击位于左侧边栏中 Base 名称旁边的省略号（`...`）以启动 Base 上下文菜单。
2. 在出现的下拉菜单中选择“从收藏中移除”选项。
3. 之后，指定的 Base 将从“收藏”部分中移除。

![image](https://docs.nocodb.com/assets/images/base-remove-from-starred-a5fc6ed9e9cbc2251844fc0cd8afba24.png)

## 复制 Base [](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#duplicate-base "复制 Base 的直接链接")

要复制 Base，您可以按照以下简单步骤进行：

1. 点击位于左侧边栏中 Base 名称旁边的省略号（`...`）以启动 Base 上下文菜单。
2. 在出现的下拉菜单中选择“复制”选项。
3. 可选地，您可以通过以下选项配置复制过程：a) `包含数据`：您可以选择是否连同数据一起复制 Base。b) `包含视图`：您可以决定是否连同视图一起复制 Base。
4. 点击弹出确认对话框中的“确认”按钮。
5. 将根据第 3 步中指定的配置创建一个新的 Base，该 Base 将反映原始 Base 的架构和数据/视图。

![Base 上下文菜单](https://docs.nocodb.com/assets/images/base-context-menu-8cdc9e3b6c6f450d66cb324e8ea1feea.png)

![image](https://docs.nocodb.com/assets/images/base-duplicate-88ebe6a5fcc9c36b5f7d76b65726d9b5.png)

- 复制的 Base 将在与原始 Base 相同的工作区中生成。
- 复制的 Base 名称后将附加 `Copy`。
- 在复制 Base 时，您将被指定为 `Base 所有者`。
- 现有的 Base 成员将不会转移到复制的 Base。

## 删除 Base [](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#delete-base "删除 Base 的直接链接")

如果您确定某个 Base 不再需要，您可以选择将其从工作区中永久删除。删除 Base 将删除与其关联的所有表和数据。

> **此操作无法撤销。**

> 仅 **Base 所有者** 可以删除工作区。

要删除 Base：

1. 点击位于左侧边栏中 Base 名称旁边的省略号（`...`）以启动 Base 上下文菜单。
2. 在出现的下拉菜单中选择“删除”选项。
3. 在确认对话框中选择“删除 Base”按钮。

![Base 上下文菜单](https://docs.nocodb.com/assets/images/base-context-menu-8cdc9e3b6c6f450d66cb324e8ea1feea.png)

![删除 Base](https://docs.nocodb.com/assets/images/base-delete-15390ff1d15eddee39ea1ea63f72a6af.png)

## 开发者功能 [](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#developer-features "开发者功能的直接链接")

### Base 设置 [](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#base-settings "Base 设置的直接链接")

您可以在 Base 设置中修改一些常规配置。

1.  **显示 M2M 表**：切换此选项以在左侧边栏中显示/隐藏 M2M 表。多对多关系通过连接表支持，默认情况下隐藏。
2.  **在单元格中显示 NULL**：切换此选项以在表的单元格中显示/隐藏 NULL 值。这有助于区分持有空字符串的单元格。
3.  **在筛选器中显示 NULL 和空值**：启用“额外”筛选器以区分包含 NULL 和空字符串的字段。默认支持空白将 NULL 和空字符串视为相同。

要配置 Base 设置，您可以按照以下步骤进行：

1. 点击位于左侧边栏中 Base 名称旁边的省略号（`...`）以启动 Base 上下文菜单。
2. 在出现的下拉菜单中选择“设置”选项。

![Base 上下文菜单](https://docs.nocodb.com/assets/images/base-context-menu-8cdc9e3b6c6f450d66cb324e8ea1feea.png)

![Base 设置](https://docs.nocodb.com/assets/images/base-settings-194c9bb15d79c76f4bfea5746a077125.png)

### REST APIs [](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#rest-apis "REST APIs 的直接链接")

NocoDB 为每个 Base 提供 Swagger UI。要访问 Swagger UI，请按照以下步骤操作：

1. 点击位于左侧边栏中 Base 名称旁边的省略号（`...`）以启动 Base 上下文菜单。
2. 在出现的下拉菜单中选择“REST APIs”选项。

![Base 上下文菜单](https://docs.nocodb.com/assets/images/base-context-menu-8cdc9e3b6c6f450d66cb324e8ea1feea.png)

![Swagger](https://docs.nocodb.com/assets/images/base-swagger-66b41d2cd5d5e0a8f51ff026b6cfab85.png)

### 关系 [](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#relations "关系的直接链接")

NocoDB 提供了 Base 中表之间关系的可视化表示。要访问关系图，请按照以下步骤操作：

1. 点击位于左侧边栏中 Base 名称旁边的省略号（`...`）以启动 Base 上下文菜单。
2. 在出现的下拉菜单中选择“关系”选项。

![Base 上下文菜单](https://docs.nocodb.com/assets/images/base-context-menu-8cdc9e3b6c6f450d66cb324e8ea1feea.png)

![Base 关系](https://docs.nocodb.com/assets/images/base-relations-aaa09c0623353f552c7b90a8aa6beacb.png)

## 相关文章 [](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#related-articles "相关文章的直接链接")

- [关于 NocoDB 的帮助](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#help)
- [设置 NocoDB 的文档](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#installation)
- [NocoDB 的功能概述](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#features)