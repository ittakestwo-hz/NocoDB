# 分享基础

要分享基础，请按照以下步骤操作：

1. 在顶部导航栏的右上角点击 `分享` 按钮。
2. 在 `共享基础` 部分，将开关切换为 `启用公开访问` 以激活共享基础功能。
3. 生成的共享基础链接将显示在上方，可以用来与他人分享此基础。要复制 URL，只需点击 `复制链接` 选项。

![分享基础](https://docs.nocodb.com/assets/images/share-base-1-b9c4bddb603c184a16da76c4e1e08edb.png)

![分享基础](https://docs.nocodb.com/assets/images/share-base-2-07354533111aa13a608996b10640f468.png)

## 复制基础 [](https://docs.nocodb.com/views/views-overview/#copy-base "直接链接到复制基础")

`复制基础` 功能允许用户将基础（导入基础）复制到他们自己的工作区。此功能也适用于希望将基础用作未来基础模板的用户。要复制基础，请按照以下步骤操作：

1. 访问您希望复制的共享基础 URL。
2. 点击工具栏右上角的 `复制基础` 按钮。
3. 将出现一个模态框，提示您选择要复制到的工作区。选择所需的工作区。
4. 配置是否希望复制带有或不带数据/视图的基础。
5. 点击 `复制基础` 按钮完成操作。

![复制基础](https://docs.nocodb.com/assets/images/share-base-copy-base-d3104cd78770d32c4c70d8a585ec3d00.png) ![复制基础](https://docs.nocodb.com/assets/images/share-base-copy-base-2-6284b3e7a0c196202d52377af31abae0.png)

修改 `共享基础` 设置将使之前生成的 `共享基础` 链接失效，并生成一个新链接。以下是修改步骤：

1. 点击工具栏右上角的 `分享` 按钮。
2. 切换标记为 `启用公开访问` 的选项以停用基础共享。
3. 切换相同的选项 `启用公开访问` 以重新激活基础共享，随后生成一个新链接。

![启用公开访问](https://docs.nocodb.com/assets/images/share-base-enable-public-access-70567245aad03d619b620d838cbdb21a.png)

禁用 `共享基础` 将使之前生成的 `共享基础` 链接失效。以下是禁用步骤：

1. 点击工具栏右上角的 `分享` 按钮。
2. 切换标记为 `启用公开访问` 的选项以停用基础共享。

![启用公开访问](https://docs.nocodb.com/assets/images/share-base-enable-public-access-70567245aad03d619b620d838cbdb21a.png)

“共享基础”可以配置为两种模式：

1. **查看者** - 拥有提供链接的用户将获得**只读**访问基础数据的权限。
2. **编辑者** - 拥有提供链接的用户将获得**读写**访问基础数据的权限。

注意：

- 默认访问权限设置为 `查看者`
- 具有 `编辑者` 访问权限的共享基础当前仅在自托管版本中可用

切换 `启用编辑访问` 按钮以根据需要配置权限！  
![共享基础编辑访问](https://docs.nocodb.com/assets/images/share-base-edit-access-b293bc0349998853d6de8a9784ae9e54.png)

## 可嵌入的框架 [](https://docs.nocodb.com/views/views-overview/#embeddable-frame "直接链接到可嵌入的框架")

NocoDB 界面可以通过利用 [HTML IFRAME](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe) 属性无缝集成到现有应用程序中。此功能使用户能够将 NocoDB 界面嵌入到他们的应用程序中，从而实现统一的用户体验。要生成可嵌入的 HTML 代码，请按照以下步骤操作：

**生成可嵌入的 HTML 代码：**

1. 点击工具栏右上角的 `分享` 按钮。
2. 在 `共享基础链接` 选项卡中，选择按钮将 `可嵌入 HTML 代码` 复制到剪贴板。

![分享基础 iFrame](https://docs.nocodb.com/assets/images/share-base-iframe-5cf906c782389e1cf39b132cd1ab62ac.png)

示例：

```
<iframe        class="nc-embed"        src="https://nocodb-nocodb-rsyir.ondigitalocean.app/dashboard/#/nc/base/e3bba9df-4fc1-4d11-b7ce-41c4a3ad6810?embed"        frameBorder="0"        width="100%"        height="700"        style="background: transparent; border: 1px solid #ddd"></iframe>
```

### 嵌入到应用程序的 HTML 正文中 [](https://docs.nocodb.com/views/views-overview/#embed-into-applications-html-body "直接链接到嵌入到应用程序的 HTML 正文中")

使用上面生成的嵌入 iframe 的示例代码

```
<!DOCTYPE html><html><body><iframe        class="nc-embed"        src="http://localhost:3000/#/nc/base/7d4b551c-b5e0-41c9-a87b-f3984c21d2c7?embed"        frameBorder="0"        width="100%"        height="700"        style="background: transparent; "></iframe></body></html>
```