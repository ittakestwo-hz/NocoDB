# 分享 Base

要分享一个 Base，请按照以下步骤操作：

1. 在顶部导航栏的右上角点击“分享”按钮。
2. 在“共享 Base”部分，切换开关以启用公共访问，从而激活共享 Base 功能。
3. 生成的共享 Base 链接将显示在上方，可用于与他人分享此 Base。要复制 URL，只需点击“复制链接”选项。

![分享 Base](https://docs.nocodb.com/assets/images/share-base-1-b9c4bddb603c184a16da76c4e1e08edb.png)

![分享 Base](https://docs.nocodb.com/assets/images/share-base-2-07354533111aa13a608996b10640f468.png)

## 修改共享 Base

修改 `共享 Base` 设置将使之前生成的 `共享 Base` 链接失效，并生成一个新的链接。以下是修改的步骤：

1. 点击位于工具栏右上角的“分享”按钮。
2. 切换标记为 `启用公共访问` 的选项，以停用 Base 分享。
3. 再次切换相同的选项 `启用公共访问`，以重新激活 Base 分享，从而生成一个新链接。

![启用公共访问](https://docs.nocodb.com/assets/images/share-base-enable-public-access-70567245aad03d619b620d838cbdb21a.png)

## 禁用共享 Base

禁用“共享 Base”将使之前生成的“共享 Base”链接失效。以下是禁用的步骤：

1. 点击位于工具栏右上角的“分享”按钮。
2. 切换标记为“启用公共访问”的选项，以停用 Base 分享。

## 共享 Base 访问权限

“共享 Base”可以配置为两种模式：

1. 只读 - 具有提供链接的用户将只能读取 Base 数据。
2. 可编辑 - 具有提供链接的用户将可以读取和写入 Base 数据。

切换 `启用编辑访问` 按钮以按需配置权限。

![共享 Base 编辑访问](https://docs.nocodb.com/assets/images/share-base-edit-access-b293bc0349998853d6de8a9784ae9e54.png)

## 可嵌入框架

NocoDB 界面可以通过使用 [HTML IFRAME](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe) 属性无缝集成到现有应用程序中。此功能使用户能够将 NocoDB 界面嵌入到其应用程序中，从而实现统一的用户体验。要生成可嵌入的 HTML 代码，请按照以下步骤操作：

**生成可嵌入 HTML 代码：**

1. 点击位于工具栏右上角的“分享”按钮。
2. 在“共享 Base 链接”选项卡中，选择按钮将 `可嵌入 HTML 代码` 复制到剪贴板。

![分享 Base iFrame](https://docs.nocodb.com/assets/images/share-base-iframe-5cf906c782389e1cf39b132cd1ab62ac.png)

示例：

```
<iframe
    class="nc-embed"
    src="https://nocodb-nocodb-rsyir.ondigitalocean.app/dashboard/#/nc/base/e3bba9df-4fc1-4d11-b7ce-41c4a3ad6810?embed"
    frameBorder="0"
    width="100%"
    height="700"
    style="background: transparent; border: 1px solid #ddd"
>
</iframe>
```

#### 嵌入到应用程序的 HTML 主体中

**使用上述生成的嵌入 iframe 的示例代码**

```
<!DOCTYPE html>
<html>
<head>
    <title>示例 iFrame 示例</title>
</head>
<body style="height:100vh; margin:0">
<iframe src="http://localhost:3000/#/base/035c5207-501a-48b8-8dbe-67742b78323e" width="100%" height="100%" style="border: none;"></iframe>
</body>
</html>
```

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