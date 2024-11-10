# 环境变量

对于生产环境，设置所有标记为 **"强制"** 的环境变量至关重要，以确保 NocoDB 的最佳性能、安全性和功能。

## 数据库

| 变量 | 强制 | 描述 | 如果未设置 |
| --- | --- | --- | --- |
| `NC_DB` | 是 | 所有 NocoDB 元数据和数据存储的主要数据库。示例格式：`pg://host.docker.internal:5432?u=username&p=password&d=database_name`。 | 如果未指定 `NC_DB`，将创建一个位于根文件夹中的本地 SQLite 数据库。 |
| `NC_DB_JSON` | 否 | 允许使用有效的 [knex 连接 JSON 字符串](https://knexjs.org/guide/#configuration-options) 设置数据库连接，而不是 `NC_DB`。 |  |
| `NC_DB_JSON_FILE` | 否 | 可以使用 knex 连接 JSON 文件的路径来指定数据库连接，作为 `NC_DB` 的替代。 |  |
| `DATABASE_URL` | 否 | 可以使用 [JDBC URL 字符串](https://jdbc.postgresql.org/documentation/use/#connecting-to-the-database) 进行数据库连接，而不是 `NC_DB`。 |  |
| `DATABASE_URL_FILE` | 否 | 可以为数据库连接指定包含 JDBC URL 的文件路径，作为 `NC_DB` 的替代。 |  |
| `NC_CONNECTION_ENCRYPT_KEY` | 否 | 用于加密外部数据库凭证的密钥。**警告：** 更改此变量可能会导致应用程序出现问题。如果必须更改，请按照 [NocoDB Secret CLI 文档](https://docs.nocodb.com/data-sources/updating-secret) 中的说明使用 CLI。 | 如果未设置，则连接凭证将以明文形式保存在数据库中。 |

## 认证

| 变量 | 强制 | 描述 | 如果未设置 |
| --- | --- | --- | --- |
| `NC_AUTH_JWT_SECRET` | 是 | 此 JWT 密钥用于生成身份验证令牌。 | 将自动生成一个随机密钥。 |
| `NC_JWT_EXPIRES_IN` | 否 | 指定 JWT 令牌的过期时间。 | 默认为 `10h`。 |
| `NC_GOOGLE_CLIENT_ID` | 否 | 激活 Google 认证所需的 Google 客户端 ID。 |  |
| `NC_GOOGLE_CLIENT_SECRET` | 否 | 激活 Google 认证所需的 Google 客户端密钥。 |  |
| `NC_ADMIN_EMAIL` | 否 | 超级管理员的电子邮件地址。这在您需要恢复用户名和密码时非常有用。 | 第一次访问 UI 时需要初始提示输入电子邮件和密码。 |
| `NC_ADMIN_PASSWORD` | 否 | 超级管理员密码。必须至少 8 个字符，包含一个大写字母、一个数字和一个特殊字符 `$&+,:;=?@#'.^*()%!_-\"`。这对于用户名和密码恢复非常有用。 |  |
| `NC_DISABLE_EMAIL_AUTH` | 否 | 禁用基于电子邮件和密码的身份验证，适用于已配置 Google 认证变量时使用。 |  |

## 存储

| 变量 | 强制 | 描述 | 如果未设置 |
| --- | --- | --- | --- |
| `NC_S3_BUCKET_NAME` | 否 | 用于 S3 存储插件的 AWS S3 存储桶名称。 |  |
| `NC_S3_REGION` | 否 | 存储桶所在的 AWS S3 区域。 |  |
| `NC_S3_ENDPOINT` | 否 | S3 存储插件的 S3 端点。 | 默认为 `s3.<region>.amazonaws.com` |
| `NC_S3_ACCESS_KEY` | 否 | S3 存储插件的 AWS 访问密钥 ID。如果未使用角色访问，则需要此项。 |  |
| `NC_S3_ACCESS_SECRET` | 否 | 与 S3 存储插件关联的 AWS 访问密钥。如果未使用角色访问，则需要此项。 |  |
| `NC_S3_FORCE_PATH_STYLE` | 否 | 是否强制对 S3 存储插件使用 [路径风格请求](https://docs.aws.amazon.com/AmazonS3/latest/userguide/VirtualHosting.html#path-style-access)。 |  |
| `NC_S3_ACL` | 否 | S3 中对象的 [ACL](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html) |  |
| `NC_ATTACHMENT_FIELD_SIZE` | 否 | 附件的最大文件大小（以字节为单位）。 | 默认为 `20971520`（20 MiB）。 |
| `NC_MAX_ATTACHMENTS_ALLOWED` | 否 | 每个单元格允许的最大附件数量。 | 默认为 `10`。 |
| `NC_ATTACHMENT_RETENTION_DAYS` | 否 | 删除所有引用后在存储中保留附件的天数。（设置为 0 以永久保留） | 默认为 `10`。 |
| `NC_SECURE_ATTACHMENTS` | 否 | 仅通过预签名 URL 访问附件。设置为 `true` 激活；所有其他值视为 `false`。⚠ 注意：启用此功能将使现有链接无法访问。 | 默认为 `false`。 |
| `NC_ATTACHMENT_EXPIRE_SECONDS` | 否 | 预签名 URL 开始过期的秒数。实际过期将在此时间之后加上额外 10 分钟后发生。仅在启用 `NC_SECURE_ATTACHMENTS` 时适用。 | 默认为 `7200`（2 小时）。 |

## 邮件通知

以下 SMTP 变量用于向用户发送电子邮件通知，例如邀请。

| 变量 | 强制 | 描述 | 如果未设置 |
| --- | --- | --- | --- |
| `NC_SMTP_FROM` | 是 | 用作 SMTP 插件发送者的电子邮件地址。 |  |
| `NC_SMTP_HOST` | 是 | SMTP 插件的邮件服务器主机名。 |  |
| `NC_SMTP_PORT` | 是 | SMTP 插件的邮件服务器网络端口。 |  |
| `NC_SMTP_USERNAME` | 是 | 用于与 SMTP 插件认证的用户名。 |  |
| `NC_SMTP_PASSWORD` | 是 | 用于与 SMTP 插件认证的密码。 |  |
| `NC_SMTP_SECURE` | 是 | 启用 SMTP 插件的安全认证。设置为 `true` 以启用；所有其他值视为 `false`。 |  |
| `NC_SMTP_IGNORE_TLS` | 是 | 忽略 SMTP 插件的 TLS。设置为 `true` 以忽略 TLS；所有其他值视为 `false`。更多详细信息请参见 [Nodemailer 的 SMTP 文档](https://nodemailer.com/smtp/)。 |  |

## 后端

| 变量 | 强制 | 描述 | 如果未设置 |
| --- | --- | --- | --- |
| `PORT` | 否 | 指定 NocoDB 运行的网络端口。 | 默认为 `8080`。 |
| `NODE_OPTIONS` | 否 | 要传递给实例的 Node.js [选项](https://nodejs.org/api/cli.html#node_optionsoptions)。 |  |

## 前端

| 变量 | 强制 | 描述 | 如果未设置 |
| --- | --- | --- | --- |
| `NC_PUBLIC_URL` | 否 | 用于构建电子邮件模板中的 URL、生成 Swagger 文档 URL 和处理后端 URL 要求的基本 URL。应设置为您的公共 NocoDB URL，以确保应用程序的一致性。 | 默认为从后端传入请求推断 URL。如果服务器位于代理后面，可能导致 URL 不正确。 |
| `NC_DASHBOARD_URL` | 否 | 定义自定义仪表板 URL 路径。 | 默认为 `/dashboard`。 |
| `NUXT_PUBLIC_NC_BACKEND_URL` | 否 | 指定自定义后端 URL。 | 默认为 `http://localhost:8080`。 |

## 缓存

| 变量 | 强制 | 描述 | 如果未设置 |
| --- | --- | --- | --- |
| `NC_REDIS_URL` | 是 | 指定用于缓存的 Redis URL。  
例如：`redis://:authpassword@127.0.0.1:6380/4` | 后端的缓存层 |

## 产品配置

| 变量 | 强制 | 描述 | 如果未设置 |
| --- | --- | --- | --- |
| `DB_QUERY_LIMIT_DEFAULT` | 否 | 数据表的默认分页限制。 | 默认为 `25`。最大为 `100` |
| `DB_QUERY_LIMIT_GROUP_BY_GROUP` | 否 | 每页的组数。 | 默认为 `10`。 |
| `DB_QUERY_LIMIT_GROUP_BY_RECORD` | 否 | 每组的记录数。 | 默认为 `10`。 |
| `DB_QUERY_LIMIT_MAX` | 否 | 允许的最大分页限制。 | 默认为 `1000`。 |
| `DB_QUERY_LIMIT_MIN` | 否 | 允许的最小分页限制。 | 默认为 `10` |
| `NC_CONNECT_TO_EXTERNAL_DB_DISABLED` | 否 | 禁用 NocoDB 连接到外部数据库。 | 默认为 `false`。 |
| `NC_DISABLE_EXTERNAL_DATABASE_CONNECTIONS` | 否 | 禁用通过 [REST API](https://docs.nocodb.com/api) 连接到外部数据库。 | 默认为 `false`。 |
| `NC_ENABLE_GQL` | 否 | 启用 GraphQL 功能，允许使用 GraphQL 查询 NocoDB 数据。 | 默认为 `false`。 |

## 高级配置

| 变量 | 强制 | 描述 | 如果未设置 |
| --- | --- | --- | --- |
| `NC_DISABLE_VCS` | 否 | 禁用版本控制系统。 | 默认为 `false`。 |
| `NC_DISABLE_SSO` | 否 | 禁用单点登录。 | 默认为 `false`。 |
| `NC_DISABLE_SYSTEM_DB` | 否 | 禁用系统数据库（数据表、外部数据库连接等）。 | 默认为 `false`。 |
| `NC_USE_NEW_FILTERS` | 否 | 启用新的筛选器。 | 默认为 `false`。 |
| `NC_USE_CLEANUP` | 否 | 启用后台清理作业，定期删除所有引用的附件。 | 默认为 `false`。 |
| `NC_DISABLE_SMTP` | 否 | 禁用 SMTP。 | 默认为 `false`。 |
| `NC_DISABLE_HTTP_LOGGING` | 否 | 禁用 HTTP 日志记录。 | 默认为 `false`。 |
| `NC_DISABLE_REDIS` | 否 | 禁用 Redis。 | 默认为 `false`。 |
| `NC_DISABLE_TRACING` | 否 | 禁用跟踪。 | 默认为 `false`。 |
| `NC_DISABLE_OPENAPI` | 否 | 禁用 OpenAPI。 | 默认为 `false`。 |

## 其他

| 变量 | 强制 | 描述 | 如果未设置 |
| --- | --- | --- | --- |
| `NC_DISABLE_TELEMETRY` | 否 | 禁用 NocoDB 发送匿名使用数据。 | 默认为 `false`。 |
| `NODE_ENV` | 否 | 指定 Node.js 的环境模式。 | 默认为 `development`。 |
| `NC_CORS_ORIGIN` | 否 | 允许跨域请求的原点。 | 默认为 `*`（所有源）。 |
| `NC_CORS_ALLOW_METHODS` | 否 | 允许的跨域请求方法。 | 默认为 `GET,HEAD,PUT,PATCH,POST,DELETE`。 |
| `NC_CORS_ALLOW_HEADERS` | 否 | 允许的跨域请求标头。 | 默认为 `X-Requested-With, Content-Type, Accept, Authorization`。 |
| `NC_CORS_EXPOSE_HEADERS` | 否 | 允许的跨域响应标头。 | 默认为 `Content-Length, X-JSON, X-Total-Count`。 |
| `NC_CORS_MAX_AGE` | 否 | 允许的跨域请求最大过期时间。 | 默认为 `600`。 |
| `NC_DISABLE_SECURITY` | 否 | 禁用安全性（不建议使用）。 | 默认为 `false`。 |