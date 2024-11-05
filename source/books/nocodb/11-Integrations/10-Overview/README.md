# 概述

**集成**功能让 NocoDB 与外部平台无缝连接，有助于将分散在多个孤岛中的数据整合到一个通用平台中。

在单个工作区内，您可以添加多个集成实例，每个实例称为一个**连接**。一旦建立，这些连接就允许您在 NocoDB 基础库中使用集成平台的数据。如有需要，NocoDB 中的更改也可以同步回外部平台。

目前，NocoDB 支持与 _MySQL_ 和 _PostgreSQL_ 等数据库的集成，未来还将支持更多集成。如有特定的集成需求，请通过“**请求集成**”选项在 `集成` 菜单中提交您的请求。

信息

- 在云托管解决方案中，集成菜单将对工作区所有者和工作区创建者开放。
- 在自托管解决方案（OSS）中，集成菜单将对组织管理员和组织创建者开放。

所有与集成及其连接相关的活动都可以通过位于左侧边栏的 `集成` 菜单进行高效管理。

![集成](https://docs.nocodb.com/assets/images/integrations-1-af17f70922a33f7ad7cb52926fbe6af4.png)

您可以在以下部分了解更多关于使用集成的信息：

-   [创建新连接](https://docs.nocodb.com/integrations/create-connection)
-   [编辑连接](https://docs.nocodb.com/integrations/actions-on-connection#edit)
-   [删除连接](https://docs.nocodb.com/integrations/actions-on-connection#delete)