# REST APIS

### API 令牌相关操作
- **获取 API 令牌列表**：`GET /api/v1/db/meta/projects/{projectId}/api-tokens`
- **创建 API 令牌**：`POST /api/v1/db/meta/projects/{projectId}/api-tokens`
- **删除 API 令牌**：`DELETE /api/v1/db/meta/projects/{projectId}/api-tokens/{token}`

### 项目用户管理
- **获取项目用户列表**：`GET /api/v1/db/meta/projects/{projectId}/users`
- **添加项目用户**：`POST /api/v1/db/meta/projects/{projectId}/users`
- **更新项目用户**：`PATCH /api/v1/db/meta/projects/{projectId}/users/{userId}`
- **删除项目用户**：`DELETE /api/v1/db/meta/projects/{projectId}/users/{userId}`
- **重新发送用户邀请**：`POST /api/v1/db/meta/projects/{projectId}/users/{userId}/resend-invite`

### 数据库表相关操作
- **创建表**：`POST /api/v1/db/meta/projects/{projectId}/tables`
- **获取表列表**：`GET /api/v1/db/meta/projects/{projectId}/tables`
- **创建表列**：`POST /api/v1/db/meta/tables/{tableId}/columns`
- **更新表列**：`PATCH /api/v1/db/meta/tables/{tableId}/columns/{columnId}`
- **删除表列**：`DELETE /api/v1/db/meta/tables/{tableId}/columns/{columnId}`
- **设置主列**：`POST /api/v1/db/meta/tables/{tableId}/columns/{columnId}/primary`

### 表过滤器操作
- **获取过滤器**：`GET /api/v1/db/meta/filters/{filterId}`
- **更新过滤器**：`PATCH /api/v1/db/meta/filters/{filterId}`
- **删除过滤器**：`DELETE /api/v1/db/meta/filters/{filterId}`
- **读取视图的过滤器**：`GET /api/v1/db/meta/views/{viewId}/filters`
- **创建视图过滤器**：`POST /api/v1/db/meta/views/{viewId}/filters`

### 表排序相关操作
- **获取排序列表**：`GET /api/v1/db/meta/views/{viewId}/sorts`
- **创建排序**：`POST /api/v1/db/meta/views/{viewId}/sorts`
- **读取排序**：`GET /api/v1/db/meta/sorts/{sortId}`
- **更新排序**：`PATCH /api/v1/db/meta/sorts/{sortId}`
- **删除排序**：`DELETE /api/v1/db/meta/sorts/{sortId}`

### Webhook 操作
- **获取 Webhook 列表**：`GET /api/v1/db/meta/tables/{tableId}/hooks`
- **创建 Webhook**：`POST /api/v1/db/meta/tables/{tableId}/hooks`
- **测试 Webhook**：`POST /api/v1/db/meta/tables/{tableId}/hooks/test`
- **更新 Webhook**：`PATCH /api/v1/db/meta/hooks/{hookId}`
- **删除 Webhook**：`DELETE /api/v1/db/meta/hooks/{hookId}`

### 视图操作
- **获取表的视图列表**：`GET /api/v1/db/meta/tables/{tableId}/views`
- **读取视图**：`GET /api/v1/db/meta/tables/{tableId}`
- **更新视图**：`PATCH /api/v1/db/meta/tables/{tableId}`
- **删除视图**：`DELETE /api/v1/db/meta/tables/{tableId}`
- **重新排序视图**：`POST /api/v1/db/meta/tables/{tableId}/reorder`

### 插件相关操作
- **获取插件列表**：`GET /api/v1/db/meta/plugins`
- **获取插件状态**：`GET /api/v1/db/meta/plugins/{pluginTitle}/status`
- **测试插件**：`POST /api/v1/db/meta/plugins/test`
- **更新插件**：`PATCH /api/v1/db/meta/plugins/{pluginId}`

### 项目信息操作
- **获取项目信息**：`GET /api/v1/db/meta/projects/{projectId}/info`
- **获取项目可见性规则**：`GET /api/v1/db/meta/projects/{projectId}/visibility-rules`
- **设置项目可见性规则**：`POST /api/v1/db/meta/projects/{projectId}/visibility-rules`

### 项目共享操作
- **获取项目共享信息**：`GET /api/v1/db/meta/projects/{projectId}/shared`
- **禁用项目共享**：`DELETE /api/v1/db/meta/projects/{projectId}/shared`
- **创建项目共享**：`POST /api/v1/db/meta/projects/{projectId}/shared`
- **更新项目共享**：`PATCH /api/v1/db/meta/projects/{projectId}/shared`

### 存储操作
- **文件上传**：`POST /api/v1/db/storage/upload`
- **通过 URL 上传文件**：`POST /api/v1/db/storage/upload-by-url`

### 应用和缓存操作
- **获取应用信息**：`GET /api/v1/db/meta/nocodb/info`
- **获取应用版本**：`GET /api/v1/version`
- **检查应用健康状态**：`GET /api/v1/health`
- **获取聚合元数据信息**：`GET /api/v1/aggregated-meta-info`
- **测试项目连接**：`POST /api/v1/db/meta/projects/connection/test`

这是对 API 的描述和翻译。希望对你使用这些接口有所帮助！