# 创建 Webhook

## 创建 Webhook

### 访问 Webhook 页面

1. 在左侧边栏中点击需要配置 Webhook 的表。
2. 打开顶部的 `详情` 标签。
3. 点击 `Webhooks` 标签。
4. 点击 `添加新的 Webhook`。

### 配置 Webhook

1. 设置 Webhook 的名称。
2. 选择需要触发 Webhook 的事件。

| 触发器        | 详细说明                  |
|---------------|---------------------------|
| 插入后        | 插入单条记录后             |
| 更新后        | 更新单条记录后             |
| 删除后        | 删除单条记录后             |
| 批量插入后    | 批量插入记录后             |
| 批量更新后    | 批量更新记录后             |
| 批量删除后    | 批量删除记录后             |

3. 方法和 URL：配置 Webhook 触发的端点。支持的请求方法有 GET、POST、DELETE、PUT、HEAD、PATCH。
4. 请求头和参数：配置请求的头和参数（可选）。
5. 条件：仅符合条件的记录会触发 Webhook（可选）。
6. 测试 Webhook（使用示例负载）以验证参数配置是否正确（可选）。
7. 保存 Webhook。

### 带条件的 Webhook

如果配置了条件，仅满足条件的记录会触发 Webhook。例如，当 `状态` 为 `完成` 时触发 Webhook。可以使用 `AND` 或 `OR` 操作符配置多个条件。例如，当 `状态` 为 `完成` 且 `优先级` 为 `高` 时触发 Webhook。

Webhook 仅在记录更新前未满足条件且更新后满足条件时触发。例如，若配置的条件为 `状态` 为 `完成` 且 `优先级` 为 `高`，当记录的 `状态` 从 `完成` 且 `优先级` 从 `低` 更新为 `高` 时，Webhook 会被触发。但是，如果更新了具有 `状态` 为 `完成` 且 `优先级` 为 `高` 的记录中的其他字段，则不会触发 Webhook。

简而言之，只有当 `条件（旧记录）= false` 且 `条件（新记录）= true` 时，Webhook 才会触发。

### Webhook 响应示例

- 插入后
- 更新后
- 删除后
- 批量插入后
- 批量更新后
- 批量删除后

```json
{
  "type": "records.after.insert",
  "id": "9dac1c54-b3be-49a1-a676-af388145fa8c",
  "data": {
    "table_id": "md_xzru7dcqrecc60",
    "table_name": "Film",
    "view_id": "vw_736wrpoas7tr0c",
    "view_name": "Film",
    "records": [
      {
        "FilmId": 1011,
        "Title": "FOO",
        "Language": {
          "LanguageId": 1,
          "Name": "English"
        }
      }
    ]
  }
}
```

### 自定义负载的 Webhook

在企业版中，可以为 Webhook 设置个性化负载。前往 `Body` 标签以进行必要配置。用户可以使用 [Handlebar 语法](https://handlebarsjs.com/guide/#simple-expressions)，轻松访问和处理数据。

使用 `{{ json event }}` 访问事件数据。示例响应如下：

```json
{
  "type": "records.after.insert",
  "id": "0698517a-d83a-4e72-bf7a-75f46b704ad1",
  "data": {
    "table_id": "m969t01blwprpef",
    "table_name": "Table-2",
    "view_id": "vwib3bvfxdqgymun",
    "view_name": "Table-2",
    "rows": [
      {
        "Id": 1,
        "Tags": "Sample Text",
        "CreatedAt": "2024-04-11T10:40:20.998Z",
        "UpdatedAt": "2024-04-11T10:40:20.998Z"
      }
    ]
  }
}
```

### Discord Webhook

Discord Webhook 可配置为向 Discord 频道发送消息。Discord 请求体应包含内容、嵌入或附件，否则请求将失败。以下是 Discord Webhook 负载示例。更多详细信息请参见 [此处](https://birdie0.github.io/discord-webhooks-guide/discord_webhook.html)。

```json
{
  "content": "Hello, this is a webhook message",
  "embeds": [
    {
      "title": "Webhook",
      "description": "This is a webhook message",
      "color": 16711680
    }
  ]
}
```

要向 Discord 发送完整的事件数据，请使用以下负载：

```json
{
  "content": "{{ json ( json event ) }}"
}
```

您还可以根据需求自定义负载。例如，仅向 Discord 发送 `Title` 字段：

```json
{
  "content": "{{ event.data.rows.[0].Title }}"
}
```

## 环境变量

在自托管版本中，可以配置以下环境变量以自定义 Webhook 行为。

- `NC_ALLOW_LOCAL_HOOKS`: 允许基于本地地址的链接触发。默认值：false。

更多环境变量信息请参见 [此处](https://docs.nocodb.com/getting-started/self-hosted/environment-variables)。