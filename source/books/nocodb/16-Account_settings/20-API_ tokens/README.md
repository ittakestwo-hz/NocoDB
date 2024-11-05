# API 令牌

## 创建 API 令牌

从侧边栏左下角的用户菜单中打开账户设置页面。

1. 点击侧边栏左下角的 `用户菜单`，
2. 从下拉菜单中选择 `账户设置`。

![个人资料页面](https://docs.nocodb.com/assets/images/account-settings-3f8b281c933be2349ddb19f0fa8660e8.png)

按照以下步骤创建 API 令牌：

1. 在 `账户设置` 页面中点击 `令牌` 标签。
2. 点击 `添加新 API 令牌`。
3. 输入 API 令牌的名称。
4. 点击 `保存` 按钮以保存更改。
5. 通过点击 `操作` 菜单下显示的 `复制` 按钮复制 API 令牌。
6. 在需要身份验证的服务中将 API 令牌作为 `xc-token` 使用，放在请求头中。

```
{  "headers": {    "xc-token": "在引号内复制的 API 令牌"  }}
```

![创建 API 令牌](https://docs.nocodb.com/assets/images/api-token-1-6806c5ece8a92717e786e0fa4e824081.png)

![创建 API 令牌](https://docs.nocodb.com/assets/images/api-token-2-378e04140d53a68be86d17d3561c8591.png)

信息

- 每个用户只能创建一个令牌。
- API 令牌不会过期，但可以随时删除。

创建的 API 令牌将被添加到列表中。通过点击 `操作` 菜单下的 `复制` 按钮复制 API 令牌。

![创建 API 令牌](https://docs.nocodb.com/assets/images/api-token-3-493d6baa74b64ec5d6a00c20d6806fd4.png)

## 删除 API 令牌

警告

请注意，一旦 API 令牌被删除，所有使用该 API 令牌的服务将停止工作。

从侧边栏左下角的用户菜单中打开账户设置页面。

1. 点击侧边栏左下角的 `用户菜单`，
2. 从下拉菜单中选择 `账户设置`。

![个人资料页面](https://docs.nocodb.com/assets/images/account-settings-3f8b281c933be2349ddb19f0fa8660e8.png)

1. 在 `账户设置` 页面中点击 `令牌` 标签。
2. 在 `操作` 菜单中，点击与要删除的 API 令牌关联的 `删除` 按钮。

![删除 API 令牌](https://docs.nocodb.com/assets/images/api-token-4-1a6120f496ccdfca799987a4dc8f9027.png)