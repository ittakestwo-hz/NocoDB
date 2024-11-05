# 快速入门

NocoDB 提供两种灵活的选择：自托管和 SaaS（云托管）。在本节中，我们将引导您完成 NocoDB 的初始设置，无论您是选择在自己的基础设施上安装，还是使用我们便捷的云托管服务。让我们一起探索 NocoDB 在数据管理方面的潜力！

> **提示**  
> 在此入门指南中，我们建议您使用托管（SaaS）选项。新用户可享受免费试用期，以探索平台的各项功能。

## 自托管[](https://docs.nocodb.com/getting-started/quick-start#self-hosted "直接链接到自托管")

选择自托管时，您可以在自己掌控的服务器上运行应用程序。您可以选择将数据库托管在自己的场所或租用数据中心的服务器中。在这种自我管理的模式下，通常是在本地环境中，您需完全负责服务器的管理和维护。这种控制水平确保您对数据和服务的所有方面拥有完全的自主权，而无需依赖第三方服务提供商。这一选项非常适合需要高控制级别的组织，但也需要较高的技术知识。

在您的服务器上设置 NocoDB 的流程非常简单，以下文章将引导您逐步开始。

-   [安装](https://docs.nocodb.com/getting-started/self-hosted/installation/auto-upstall)
-   [环境变量](https://docs.nocodb.com/getting-started/self-hosted/environment-variables)
-   [升级](https://docs.nocodb.com/getting-started/self-hosted/upgrading)

## SaaS（云托管）[](https://docs.nocodb.com/getting-started/quick-start#saas-cloud-hosted "直接链接到 SaaS（云托管）")

### 注册 NocoDB 账户[](https://docs.nocodb.com/getting-started/quick-start#sign-up-for-a-nocodb-account "直接链接到注册 NocoDB 账户")

要开始使用 NocoDB 的云托管服务，请按以下步骤注册账户：

1.  访问 [NocoDB 官网](https://www.nocodb.com/)。
2.  点击右上角的“免费试用”按钮。
3.  使用 Google 账号 `注册`，或通过电子邮件注册。
4.  检查您的电子邮件以获取验证链接，并按照说明验证您的账户。

注册成功后，您将进入 NocoDB 仪表板，系统会为您创建一个默认的工作区。

### 创建新工作区[](https://docs.nocodb.com/getting-started/quick-start#create-another-workspace "直接链接到创建新工作区")

注册并登录到 NocoDB 后，系统会自动为您创建一个默认工作区。您可以使用该工作区或 [创建新工作区](https://docs.nocodb.com/workspaces/create-workspace)。

现在，您的新工作区已准备就绪，您可以在其中开始构建数据库。

### 构建数据库[](https://docs.nocodb.com/getting-started/quick-start#build-a-base "直接链接到构建数据库")

在 NocoDB 中构建数据库时，您可以定义数据库结构，创建用于存储数据的表格，为这些表格添加字段，并使用链接建立表之间的关系。这种关系型方法有助于有效地组织和管理数据，方便处理复杂的数据集并构建强大的应用程序。添加 [新数据库](https://docs.nocodb.com/bases/create-base)。或者，也可以从 Airtable 中 [导入现有数据库](https://docs.nocodb.com/bases/import-base-from-airtable) 并快速转换为 NocoDB 数据库。

#### 创建表格[](https://docs.nocodb.com/getting-started/quick-start#create-tables "直接链接到创建表格")

表格类似于电子表格，数据以行和列的形式排列。在创建数据库后，您可以开始 [添加新表格](https://docs.nocodb.com/tables/create-table)。您还可以 [从 CSV、Excel 或 JSON 文件中导入现有结构数据](https://docs.nocodb.com/tables/create-table-via-import) 来填充表格。

#### 添加字段[](https://docs.nocodb.com/getting-started/quick-start#add-fields "直接链接到添加字段")

在每个表格中，[定义字段](https://docs.nocodb.com/fields/fields-overview) 用于存储数据。字段是列式数据容器，用于存储特定类型的数据。字段可以表示各种类型的信息，例如文本、数字、日期等。查看支持的完整字段类型列表 [在此](https://docs.nocodb.com/fields/fields-overview)。

使用多字段编辑器快速批量管理字段 - 添加、编辑、重新排序、更改可见性、重新配置等都可以在单一窗口完成。[了解更多](https://docs.nocodb.com/fields/multi-fields-editor)。

#### 使用链接建立关系[](https://docs.nocodb.com/getting-started/quick-start#establish-relationships-with-links "直接链接到使用链接建立关系")

NocoDB 的强大功能之一是通过 [链接](https://docs.nocodb.com/fields/field-types/links-based/links) 建立表格之间的关系。例如，您可以通过在“项目”表中创建一个指向“任务”表的链接字段，将“任务”与特定的“项目”关联起来。

#### 添加记录[](https://docs.nocodb.com/getting-started/quick-start#add-records "直接链接到添加记录")

创建表格并定义必要的字段后，您可以开始将记录添加到表格中。记录是表格中的各个条目或行，包含您想要存储和管理的实际数据。您可以 [手动添加记录](https://docs.nocodb.com/records/create-record) 或 [从 CSV 文件中上传现有数据集](https://docs.nocodb.com/tables/import-data-into-existing-table)。

#### 创建视图[](https://docs.nocodb.com/getting-started/quick-start#create-views "直接链接到创建视图")

视图是用于显示数据的自定义方式。您可以为每个表创建多个视图，每个视图可以有其自己的字段、筛选器和布局设置。NocoDB 提供多种视图类型，包括 [网格视图](https://docs.nocodb.com/views/view-types/grid)、[看板视图](https://docs.nocodb.com/views/view-types/kanban) 和 [画廊视图](https://docs.nocodb.com/views/view-types/gallery)。如果您正在收集表单数据，还可以创建 [表单视图](https://docs.nocodb.com/views/view-types/form) 以表单格式显示数据。

#### 连接您的数据源[](https://docs.nocodb.com/getting-started/quick-start#connect-your-data-sources "直接链接到连接您的数据源")

NocoDB 不仅支持从零开始创建数据库和表格，还允许您通过 [连接现有数据源](https://docs.nocodb.com/data-sources/data-source-overview) 快速入门，并将表格 UI 应用于数据源。

### 团队协作[](https://docs.nocodb.com/getting-started/quick-start#collaborate-with-your-team "直接链接到团队协作")

NocoDB 使团队成员之间的协作变得简单。您可以 [邀请团队成员加入您的工作区](https://docs.nocodb.com/collaboration/workspace-collaboration) 并与他们共享您的数据库。您还可以 [分配角色和权限](https://docs.nocodb.com/roles-and-permissions/roles-permissions-overview) 以控制团队成员对数据库的访问权限。

希望公开分享信息？您可以 [创建公共链接](https://docs.nocodb.com/collaboration/share-base) 并分享给任何人。还可以 [将数据库嵌入](https://docs.nocodb.com/collaboration/share-base#embeddable-frame) 到您的网站或博客中。

就是这样！您现在已经准备好利用 NocoDB 的强大功能进行数据管理了。