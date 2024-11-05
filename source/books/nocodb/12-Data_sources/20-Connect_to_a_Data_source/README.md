# 连接到数据源

要将外部数据库作为 NocoDB 的新数据源进行连接，请按照以下步骤操作：

1. 在左侧边栏中点击基名称以进入 **基主页**。
2. 点击 **连接外部数据** 按钮。
3. 为数据源命名。
4. 选择连接以选择数据库的凭据：
   - (a) 从下拉列表中选择已有连接
   - (b) 点击 `+ 新连接` 按钮以创建一个新连接（仅当用户具备创建新连接的权限时可用）。
5. 根据需要配置/更改数据库和架构详情。如果在创建连接时已提供默认的数据库和架构详情，这些信息会自动填充。
6. [配置数据源的权限](https://docs.nocodb.com/views/views-overview/#configuring-permissions)。
7. 点击 `测试数据库连接` 按钮以验证连接。
8. 点击 `添加源` 按钮以保存数据源。

![数据源](https://docs.nocodb.com/assets/images/data-source-1-415bba7ce4ad096e93431d4ff71b5d22.png)

![数据源](https://docs.nocodb.com/assets/images/data-source-2-b4fb1aea42c2828d47f4c27000031eac.png)

![数据源](https://docs.nocodb.com/assets/images/data-source-3-bf8268f28fdaf05fcd70428a3b8d3e4e.png)

> 信息  
> 仅当用户具备所需权限（工作区创建者及以上）时，(4b) 中创建新连接的选项才可用。

## 配置权限

本部分涵盖配置数据源权限时可用的设置。这些设置决定了连接数据库的访问级别和允许的修改操作。

![数据源-1](https://docs.nocodb.com/assets/images/data-source-permissions-88d03ae84eaba95b92db5a5953a77271.png)

NocoDB 提供以下架构和数据权限选项：

### 允许数据编辑

启用该选项时，用户可以插入、更新和删除表中的记录。此选项允许用户直接通过 NocoDB UI 管理数据，但应谨慎使用以避免对外部数据源中的记录造成意外更改。此访问级别适合需要直接修改数据的管理员用户。

默认情况下，数据编辑是启用的。

当数据编辑被禁用时，用户仍可查看数据并执行只读操作，如筛选、排序和分组。这确保了用户可以进行数据分析和报告，而不会修改记录。

> 注意  
> 仅在架构编辑也被禁用的情况下才能禁用数据编辑。

### 允许架构编辑

启用该选项时，用户可以修改数据库架构的结构。在启用状态下，用户可以通过 NocoDB UI 创建、修改和删除表、字段和关系（链接）。此选项为用户提供了根据需求调整数据库架构设计的灵活性。

> 警告  
> NocoDB 强烈建议除非必要不要启用架构编辑选项。此选项需极度谨慎使用，因为不当的更改可能会严重影响连接数据源的数据完整性和功能。

默认情况下，架构编辑是禁用的。

即使架构编辑被禁用，用户仍然可以：

- 添加（增强）虚拟列，如查找、汇总和公式。这些虚拟列不会更改连接数据源的底层架构。
- 创建视图以自定义数据展示，而不修改原始表。
- 创建 Webhook 以在连接数据源中的特定事件发生时触发外部操作。
- 通过显式邀请或共享视图与其他用户协作。