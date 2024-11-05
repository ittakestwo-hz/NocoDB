# 连接到集成

具有工作区所有者或创建者角色的用户可以在 NocoDB 中创建新的连接。要创建新连接，请按照以下步骤操作：

![Integrations](https://docs.nocodb.com/assets/images/integrations-2-20978d9edb34b6a45e16d76f9f2863ee.png)

1. 在左侧边栏中点击 `Integrations` 菜单。
2. 从列表中选择要连接的集成。
3. 在弹出的窗口中填写所需的详细信息。有关更多详情，请参考集成特定的文档：
   - [PostgreSQL](https://docs.nocodb.com/views/views-overview/#postgresql)
   - [MySQL](https://docs.nocodb.com/views/views-overview/#mysql)

创建的集成连接会显示在 `Integrations` 菜单下的 `Connections` 标签中。

**提示**

NocoDB 中的连接没有所有权概念。工作区中创建的所有连接对该工作区的所有符合条件的用户可见。

- 具有 **Workspace Creator+** 权限的用户可以创建、编辑、复制和删除连接
- 具有 **Base Creator+** 权限的用户可以使用数据库连接创建数据源

## 数据库集成

### PostgreSQL

本节介绍在 NocoDB 中创建新的 PostgreSQL 连接所需的详细信息。

![PostgreSQL Connection](https://docs.nocodb.com/assets/images/postgres-connection-ebcd9872b2e19b6da0551cb230975274.png)

1. **连接名称**：此连接在 NocoDB UI 上的显示名称
2. 输入以下数据库连接配置详细信息：
   - **主机地址**：PostgreSQL 服务器的主机名
   - **端口号**：PostgreSQL 服务器的端口号，默认是 5432
   - **用户名**：用于连接 PostgreSQL 服务器的用户名，默认是 "postgres"
   - **密码**：用于连接 PostgreSQL 服务器的密码
   - \[可选\] **数据库**：要连接的 PostgreSQL 数据库名称
   - \[可选\] **模式名称**：要连接的模式名称

**提示**

创建连接时，数据库名称和模式名称为可选字段。如果提供了这些信息，在使用该连接创建新数据源时会自动填充。

3. **连接参数**：如果有其他要求，可以以键值对的形式添加
4. **SSL 模式**：如果需要 TLS/MTLS 保护，可切换以启用 SSL 并选择 SSL 模式
   - **客户端证书**：上传客户端证书文件
   - **客户端密钥**：上传客户端密钥文件
   - **根 CA**：上传根 CA 文件
5. **测试数据库连接**：点击以验证连接
6. **创建连接**：点击以保存数据源

创建的连接会显示在 `Integrations` 菜单下的 `Connections` 标签中。

**注意**

如果您有连接 URL，可以自动填写连接详细信息。

![Connection URL](https://docs.nocodb.com/assets/images/connection-url-2-59b9846134da5a7e463be3ce7f29d0f2.png)

**注意**

可以通过点击 **Advanced Options** 查看整个连接参数的 JSON 形式，并根据数据库服务器类型进行编辑。

**示例**：当 SSL 模式设置为 "Required-Identity" 时，如果服务器证书的通用名 (cname) 与用于连接的实际 DNS/IP 不同，连接将失败。要解决此问题，请在 SSL 部分添加 "servername" 属性，并将其值设置为相同的 cname。更多详情请参考 [knex 配置选项](https://knexjs.org/guide/#configuration-options)。

### MySQL

本节介绍在 NocoDB 中创建新的 MySQL 连接所需的详细信息。

![MySQL Connection](https://docs.nocodb.com/assets/images/mysql-connection-61802b4529a3f9ddd552f116af974db5.png)

1. **连接名称**：此连接在 NocoDB UI 上的显示名称
2. 输入以下数据库连接配置详细信息：
   - **主机地址**：MySQL 服务器的主机名
   - **端口号**：MySQL 服务器的端口号，默认是 3306
   - **用户名**：用于连接 MySQL 服务器的用户名，默认是 "root"
   - **密码**：用于连接 MySQL 服务器的密码
   - \[可选\] **数据库**：要连接的 MySQL 数据库名称

**提示**

创建连接时，数据库名称为可选字段。如果提供了此信息，在使用该连接创建新数据源时会自动填充。

3. **连接参数**：如果有其他要求，可以以键值对的形式添加
4. **SSL 模式**：如果需要 TLS/MTLS 保护，可切换以启用 SSL 并选择 SSL 模式
   - **客户端证书**：上传客户端证书文件
   - **客户端密钥**：上传客户端密钥文件
   - **根 CA**：上传根 CA 文件
5. **测试数据库连接**：点击以验证连接
6. **创建连接**：点击以保存数据源

创建的连接会显示在 `Integrations` 菜单下的 `Connections` 标签中。

**注意**

如果您有连接 URL，可以自动填写连接详细信息。

![Connection URL](https://docs.nocodb.com/assets/images/connection-url-2-59b9846134da5a7e463be3ce7f29d0f2.png)

**注意**

可以通过点击 **Advanced Options** 查看整个连接参数的 JSON 形式，并根据数据库服务器类型进行编辑。

**示例**：当 SSL 模式设置为 "Required-Identity" 时，如果服务器证书的通用名 (cname) 与用于连接的实际 DNS/IP 不同，连接将失败。要解决此问题，请在 SSL 部分添加 "servername" 属性，并将其值设置为相同的 cname。更多详情请参考 [knex 配置选项](https://knexjs.org/guide/#configuration-options)。