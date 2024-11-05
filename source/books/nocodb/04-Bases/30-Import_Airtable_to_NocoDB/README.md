# 导入 Airtable 到 NocoDB

NocoDB 提供了一种简化的流程，可以在几分钟内将您的 Airtable 数据库无缝转移到各种数据库管理系统，包括 MySQL、Postgres 和 SQLite。此功能特别适合希望将 Airtable 数据库迁移到更强大、可扩展的数据库管理系统的用户。

> 进行操作之前，您必须拥有有效的 Airtable 凭证。确保您能访问以下来自 Airtable 帐户的信息：

-   [API 密钥](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#retrieve-api-key) 或 [个人访问令牌](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#create-personal-access-token)
-   [共享Base ID / URL](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#retrieve-share-base-id--url)

打开 `快速导入 - AIRTABLE` 模态窗口开始导入过程。

1.  在左侧边栏上悬停Base名称，点击 `...` 图标打开Base上下文菜单。
2.  从Base上下文菜单中选择 `导入数据`。
3.  选择 `Airtable`。

![import data](https://docs.nocodb.com/assets/images/base-import-airtable-1-3370c224db06eadddda7dd6224076af1.png)

另外，您也可以从 `Base仪表板` 打开 `快速导入 - AIRTABLE` 模态窗口。

1.  转到您的Base仪表板，点击 `导入数据`。
2.  选择 `Airtable`。
![import data](https://docs.nocodb.com/assets/images/base-import-from-dashboard-1-0ccc1e3e8508c11049dd45647d6c0f91.png)

![import data](https://docs.nocodb.com/assets/images/base-import-from-dashboard-2-d10a91e0ec28bbe4c620cdc5d4e871d6.png)

继续在 `快速导入 - AIRTABLE` 模态窗口中执行以下步骤以完成导入过程：

1.  输入 [API 密钥](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#retrieve-api-key) / [个人访问令牌](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#create-personal-access-token)
2.  输入 [共享Base ID / URL](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#retrieve-share-base-id--url)
3.  配置 [Airtable 导入选项](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#configuration-options)（可选）
4.  点击 `导入`

![import data](https://docs.nocodb.com/assets/images/base-import-airtable-2-a758f2600b298ba29594cfb8da91e1a2.png)

> 等待直到模态窗口中的 `前往仪表板` 按钮被激活。导入详细信息会记录在日志窗口中。

![import data](https://docs.nocodb.com/assets/images/base-import-airtable-3-ff5f7ad98f229f0fcd630c0eea1432d6.png)

### 配置选项[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#configuration-options "直接链接到配置选项")

1.  **导入数据**：如果您禁用此选项，则只会创建表和视图（模式），不包括实际数据记录。
2.  **导入次要视图**：如果您禁用此选项，则仅会导入每个表的主网格视图，省略任何次要视图。
3.  **导入汇总字段**：如果您禁用此选项，可以跳过汇总字段的导入。
4.  **导入查找字段**：如果您禁用此选项，可以跳过查找字段的导入。
5.  **导入附件字段**：如果您禁用此选项，可以跳过附件字段的导入，附件字段通常存储与记录相关的文件附件。
6.  **导入公式字段**：请注意，当前不支持从 Airtable 导入公式字段。

## 获取 Airtable 凭证[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#get-airtable-credentials "直接链接到获取 Airtable 凭证")

### 创建个人访问令牌[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#create-personal-access-token "直接链接到创建个人访问令牌")

以下是生成 Airtable 个人访问令牌的步骤：

1.  访问 [Airtable 创建令牌](https://airtable.com/create/tokens) 页面并点击“创建令牌”按钮。
2.  在 `令牌名称` 字段中提供一个有意义的名称。
3.  选择所需的访问范围，最低要求为 `data.records:read`。
4.  选择您希望使用此令牌访问的特定Base。
5.  点击 `创建令牌` 按钮确认您的选择。
6.  复制新生成的 `个人访问令牌` 以供使用。

有关详细信息，请参阅 [Airtable 个人访问令牌指南](https://airtable.com/developers/web/guides/personal-access-tokens)。

![image](https://docs.nocodb.com/assets/images/pat-1-b1eb986ad72a1c426ccd1ad338b26ecc.png)

![image](https://docs.nocodb.com/assets/images/pat-2-a3fcb811ed325a6d621f45e17e3aee2f.png)

![image](https://docs.nocodb.com/assets/images/pat-3-fd78b26e00f9f01f395a073e54c465f6.png)

### 检索 API 密钥[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#retrieve-api-key "直接链接到检索 API 密钥")

-   从 [Airtable 创建 API 密钥](https://airtable.com/create/apikey) 页面复制您的 Airtable API 密钥 ![API 密钥](https://docs.nocodb.com/assets/images/airtable-api-key-877ce3d40ba4f18389ceede7c4fa50bb.png)

有关详细程序，请查看 [这里](https://support.airtable.com/hc/en-us/articles/205752117-Creating-a-base-share-link-or-a-view-share-link#basesharelink)。

1.  打开您项目 / Base中的 `共享` 菜单。
2.  打开 `公开共享` 选项卡。
3.  启用 `开启完整Base访问`。
4.  复制生成的共享Base URL。

![Shared base](https://docs.nocodb.com/assets/images/airtable-share-base-c48341713680e60f512768432df19fec.png)

## 相关文章[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#related-articles "直接链接到相关文章")

-   [Base概述](https://docs.nocodb.com/bases/base-overview)
-   [创建空Base](https://docs.nocodb.com/bases/create-base)
-   [从 Airtable 导入Base](https://docs.nocodb.com/bases/import-base-from-airtable)
-   [邀请团队成员协作Base](https://docs.nocodb.com/bases/base-collaboration)
-   [公开共享Base](https://docs.nocodb.com/bases/share-base)
-   [重命名Base](https://docs.nocodb.com/bases/actions-on-base#rename-base)
-   [复制Base](https://docs.nocodb.com/bases/actions-on-base#duplicate-base)
-   [收藏Base](https://docs.nocodb.com/bases/actions-on-base#star-base)
-   [删除Base](https://docs.nocodb.com/bases/actions-on-base#delete-base)