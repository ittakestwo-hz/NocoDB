# Azure AD（Entra）

本文简要介绍了将 Azure AD 配置为 NocoDB 的身份服务提供者的步骤。

### NocoDB，获取 `Redirect URL` [](https://docs.nocodb.com/views/views-overview/#nocodb-retrieve-redirect-url "直接链接到 nocodb-retrieve-redirect-url")

1.  转到 `账户设置`
2.  选择 `身份验证 (SSO)`
3.  点击 `新建提供者` 按钮
4.  在弹出窗口中，为提供者指定一个 `显示名称`；注意，此名称将在登录页面上显示
5.  获取 `Redirect URL`；稍后需要将此信息配置到身份提供者中

![OIDC SSO 配置](https://docs.nocodb.com/assets/images/SSO-1-aa9135167c7a7cfb680e4fa5e50c86a4.png) ![OIDC SSO 配置](https://docs.nocodb.com/assets/images/OIDC-2-9ca271e8b627eaa9e44eaf8b34c010d1.png) ![OIDC SSO 配置](https://docs.nocodb.com/assets/images/OIDC-3-71b373c47b6affa93db2d447c52c77d6.png)

### Azure AD，将 NocoDB 配置为应用程序 [](https://docs.nocodb.com/views/views-overview/#azure-ad-configure-nocodb-as-an-application "直接链接到 Azure AD，将 NocoDB 配置为应用程序")

1.  登录到您的 [Azure 账户](https://portal.azure.com/#allservices)，并在 `Azure 服务` 下导航到 `Azure Active Directory`。
2.  从导航栏访问 `管理租户`，选择您的目录，然后点击 `切换`。
3.  在您目录的主页上，从导航栏点击 `+ 添加` > `应用注册`。
4.  在 `注册应用程序` 页面上，
    -   输入您的应用程序名称。
    -   将 `仅限该组织目录中的帐户` 设置为 `支持的帐户类型`。
    -   选择 `Web` 作为应用程序类型。
    -   在 `重定向 URI` 下添加 `Redirect URL`。
    -   `注册`
5.  在您应用程序的主页上，
    -   复制 `应用程序（客户端）ID`
    -   在 `客户端凭据` 部分点击 `添加证书或秘密`
    -   在 `证书和秘密` 页面，转到 `客户端秘密` 部分
    -   点击 `新建客户端秘密`
    -   在 `添加客户端秘密` 页面上，
        -   为秘密添加描述
        -   根据需要设置到期时间
        -   `添加`
    -   复制新创建的秘密的 `值`
6.  在您应用程序的主页上，
    -   转到 `端点` 标签
    -   打开 `OpenID Connect 元数据文档` URL，并从 JSON 响应中复制 `authorization_endpoint`、`token_endpoint`、`userinfo_endpoint` 和 `jwks_uri`
7.  配置作用域
    -   转到 `API 权限` 标签
    -   点击 `添加权限`
    -   在 `请求 API 权限` 页面上，
        -   从 `Microsoft APIs` 中选择 `Microsoft Graph`
        -   选择 `委托权限`
        -   从 `选择权限` 下拉菜单中选择 `openid`、`profile`、`email` 和 `offline_access`
        -   从 `用户` 下拉菜单中选择 `User.Read`
        -   `添加权限`
    -   在 `API 权限` 页面上点击 `授予此目录的管理员同意`

### NocoDB，将 Azure AD 配置为身份提供者 [](https://docs.nocodb.com/views/views-overview/#nocodb-configure-azure-ad-as-an-identity-provider "直接链接到 NocoDB，将 Azure AD 配置为身份提供者")

在 NocoDB 中，打开 `账户设置` > `身份验证` > `OIDC`。在 "注册 OIDC 身份提供者" 模态框中，插入以下信息：

-   将在步骤 (7) 中获取的 `应用程序（客户端）ID` 插入为 `客户端 ID`
-   将在步骤 (7) 中获取的新创建秘密的 `值` 插入为 `客户端秘密`
-   将在步骤 (8) 中获取的 `authorization_endpoint` 插入为 `授权 URL`
-   将在步骤 (8) 中获取的 `token_endpoint` 插入为 `令牌 URL`
-   将在步骤 (8) 中获取的 `userinfo_endpoint` 插入为 `用户信息 URL`
-   将在步骤 (8) 中获取的 `jwks_uri` 插入为 `JWK 集合 URL`
-   将 `作用域` 设置为 `openid`、`profile`、`email` 和 `offline_access`

在登录时，用户现在应该能够看到 `使用 <SSO> 登录` 选项。

![SAML SSO 配置](https://docs.nocodb.com/assets/images/SSO-SignIn-1221ec860763be25257e0e80e24891ec.png)

注意

注销后，如果您没有看到 `使用 <SSO> 登录` 选项，请刷新页面（第一次）。

有关 Azure AD API 作用域的信息，请参阅 [这里](https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-permissions-and-consent#offline_access)。