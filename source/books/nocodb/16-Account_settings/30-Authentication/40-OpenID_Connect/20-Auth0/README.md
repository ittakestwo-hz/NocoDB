# Auth0

本文简要介绍了将 Auth0 配置为 NocoDB 身份服务提供者的步骤。

### NocoDB，获取 `Redirect URL` [](https://docs.nocodb.com/views/views-overview/#nocodb-retrieve-redirect-url "直接链接到 nocodb-retrieve-redirect-url")

1.  转到 `账户设置`
2.  选择 `身份验证 (SSO)`
3.  点击 `新建提供者` 按钮
4.  在弹出窗口中，为提供者指定一个 `显示名称`；请注意，该名称将在登录页面上显示提供者
5.  获取 `Redirect URL`；此信息稍后需要与身份提供者进行配置

![OIDC SSO 配置](https://docs.nocodb.com/assets/images/SSO-1-aa9135167c7a7cfb680e4fa5e50c86a4.png) ![OIDC SSO 配置](https://docs.nocodb.com/assets/images/OIDC-2-9ca271e8b627eaa9e44eaf8b34c010d1.png) ![OIDC SSO 配置](https://docs.nocodb.com/assets/images/OIDC-3-71b373c47b6affa93db2d447c52c77d6.png)

### Auth0，配置 NocoDB 作为一个应用程序 [](https://docs.nocodb.com/views/views-overview/#auth0-configure-nocodb-as-an-application "直接链接到 Auth0，配置 NocoDB 作为应用程序")

1.  访问您的 [Auth0 账户](https://auth0.com/)
    -   导航到 `应用程序` > `创建应用程序`。
2.  在 `创建应用程序` 弹窗中，
    -   选择 `常规 Web 应用程序`
    -   点击 `创建`
3.  在快速启动界面，转到 `设置` 选项卡
    -   从 `基本信息` 部分复制 `客户端 ID` 和 `客户端密钥`。
4.  转到 `应用程序 URIs` 部分
    -   在 `允许的回调 URL` 下添加步骤（2）复制的 `Redirect URL`。
    -   点击 `保存更改`
5.  在 `设置` 选项卡中，转到 `高级设置` 部分并点击 `端点` 选项卡。
    -   复制 `OAuth 授权 URL`、`OAuth 令牌 URL`、`OAuth 用户信息 URL` 和 `JSON Web 密钥集 URL`

### NocoDB，配置 Auth0 作为身份提供者 [](https://docs.nocodb.com/views/views-overview/#nocodb-configure-auth0-as-an-identity-provider "直接链接到 NocoDB，配置 Auth0 作为身份提供者")

1.  在 NocoDB 中，打开 `账户设置` > `身份验证` > `OIDC`。在“注册 OIDC 身份提供者”弹窗中，输入以下信息：
    -   将步骤（5）中获取的 `客户端 ID` 作为 `客户端 ID` 输入
    -   将步骤（5）中获取的 `客户端密钥` 作为 `客户端密钥` 输入
    -   将步骤（7）中获取的 `OAuth 授权 URL` 作为 `授权 URL` 输入
    -   将步骤（7）中获取的 `OAuth 令牌 URL` 作为 `令牌 URL` 输入
    -   将步骤（7）中获取的 `OAuth 用户信息 URL` 作为 `用户信息 URL` 输入
    -   将步骤（7）中获取的 `JSON Web 密钥集 URL` 作为 `JWK 集合 URL` 输入
    -   将 `Scope` 设置为 `openid` `profile` `email` `offline_access`
    -   在用户名属性字段中，指明代表用户电子邮件的声明名称。默认值设置为 "email"。

对于登录，用户现在应该能够看到 `使用 <SSO> 登录` 选项。

![SAML SSO 配置](https://docs.nocodb.com/assets/images/SSO-SignIn-1221ec860763be25257e0e80e24891ec.png)

注意

在注销后，如果您未看到 `使用 <SSO> 登录` 选项，请刷新页面（第一次刷新）。

有关 Auth0 API 范围的信息，请参见 [此处](https://auth0.com/docs/secure/tokens/refresh-tokens)。