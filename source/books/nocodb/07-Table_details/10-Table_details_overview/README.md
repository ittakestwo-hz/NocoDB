# 表详情概述

`Details` 部分包含了多种工具和实用程序，用于管理和处理您的表模式和数据。这里本质上是一个供“创建者”快速构建和管理表的地方。`Details`部分可以通过顶部导航栏中的 `Data` - `Details` 切换开关访问。

![image](https://docs.nocodb.com/assets/images/details-tab-8aeca1f70ead223a641ead51b82e97f5.png)

本文分为四个部分：

## 字段[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#fields "直接链接到字段")

字段是一个多字段表模式编辑器，可以让您快速轻松地从一个地方添加、编辑、删除和重新排序字段。有关多字段编辑器的更多详细信息，请访问 [这里](https://docs.nocodb.com/fields/multi-fields-editor)。

![image](https://docs.nocodb.com/assets/images/details-field-editor-6b80e39a53b09c20af27e53b9777ea9a.png)

## 关系[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#relations "直接链接到关系")

关系对于管理数据库中的数据连接至关重要。在复杂的模式中，清晰理解这些连接是必不可少的，因为它们：

1.  维护数据准确性。
2.  提高查询效率。
3.  有助于逻辑模式设计。
4.  支持数据分析。
5.  促进应用程序开发。

通过实体关系图（ERD）可视化这些关系，有助于简化它们的理解和管理，尤其是随着数据库复杂性的增加。

![image](https://docs.nocodb.com/assets/images/details-relations-0716794b3e749928f581e2a2f78931a3.png)

> 💡 **小贴士**
> 
> 您可以拖放表以在图中重新排列它们。请注意，此类重新排序在会话之间不会持久保存。

## API 代码片段[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#api-snippet "直接链接到 API 代码片段")

NocoDB 提供通过 REST API 访问数据的程序化接口。NocoDB 中的 API 代码片段提供了各种编程语言的现成代码示例，简化了将数据与外部应用程序集成的过程。这些代码片段通过提供快速和简单的参考，节省了开发人员的时间和精力，使他们能够以编程方式与 NocoDB 数据库进行交互，而无需从头编写代码。

本文列出了不同脚本和语言的快速代码片段。

![image](https://docs.nocodb.com/assets/images/details-api-snippet-78906ef3b2248845b8955eed84a3031e.png)

### 示例代码片段[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#sample-snippets "直接链接到示例代码片段")

- Shell
- Javascript
- Node
- NocoDB SDK
- PHP
- Python
- Ruby
- Java
- C

```
curl --request GET \
  --url 'http://localhost:8080/api/v1/db/data/noco/p18h72lcfwzpsvu/Customer/views/Customer?offset=0&limit=25&where=' \
  --header 'xc-auth: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InVzZXJAbm9jb2RiLmNvbSIsImRpc3BsYXlfbmFtZSI6IlJpY2hhcmQiLCJhdmF0YXIiOm51bGwsInVzZXJfbmFtZSI6bnVsbCwiaWQiOiJ1c3ExbGNpeWp4ejh5bzY4Iiwicm9sZXMiOnsib3JnLWxldmVsLXZpZXdlciI6dHJ1ZX0sInRva2VuX3ZlcnNpb24iOiI0ZjUyOTUxZGQwOTZmMTVjMTY0Y2U5MDM1OTk1YzlmMDE1MTJjMGNjOThkYmRiMDU2ZmFhM2JhZWE1OWY4Y2QzMTcyN2FjOWZkMTJjNDA2ZiIsImlhdCI6MTY5NTk5MTg0NywiZXhwIjoxNjk2MDI3ODQ3fQ.I7P5caoiDSO4j_3D032XxWxxXwyEju6pL5y3Mnu_MNU'
```

## 支持的代码片段[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#supported-snippet "直接链接到支持的代码片段")

### Shell[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#shell "直接链接到 Shell")

- cURL
- wget

### Javascript[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#javascript "直接链接到 Javascript")

- Axios
- Fetch
- jQuery
- XHR

### Node[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#node "直接链接到 Node")

- Axios
- Fetch
- Request
- Native
- Unirest

### NocoDB SDK[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#nocodb-sdk "直接链接到 NocoDB SDK")

- Javascript
- Node

### PHP[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#php "直接链接到 PHP")

### Python[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#python "直接链接到 Python")

- http.client
- request

### Ruby[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#ruby "直接链接到 Ruby")

### Java[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#java "直接链接到 Java")

### C[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#c "直接链接到 C")

## Webhook[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#webhook "直接链接到 Webhook")

Webhook 对于 NocoDB 和外部系统之间的实时通信和自动化至关重要。它们具有几个重要目的：

1.  **即时通知：** 当 NocoDB 数据库中发生变化时，Webhook 使您能够立即接收通知。这些实时信息对于及时响应重要事件（如新数据条目、更新或删除）至关重要。 
2.  **自动化：** 它们通过根据数据库事件触发外部系统中的操作来促进流程的自动化。例如，您可以在 NocoDB 发生变化时自动执行发送电子邮件、更新电子表或与其他应用程序同步数据等任务。   
3.  **集成：** Webhook 使您能够无缝集成 NocoDB 与其他工具和服务，从而增强数据库的整体功能。这种集成可以简化工作流程，提高数据一致性，减少手动数据输入。  
4.  **批量操作：** NocoDB 对批量端点的支持使其能够高效处理多个记录。这在处理大型数据集或需要在外部系统中执行批量操作时特别有用。
    
总之，NocoDB 中的 Webhook 使您能够通过保持外部系统与数据库活动的同步来创建动态、响应性和互联的工作流程。

![image](https://docs.nocodb.com/assets/images/details-webhook-834a408cf5a6b9d711ac6ab63a1eaa4a.png)


> 💡 **小贴士**
> 
> 请注意，目前 Webhook 是特定于关联表的。有关 Webhook 的其他程序性细节，请访问 [这里](https://docs.nocodb.com/automation/webhook/webhook-overview)。