# Okta

本文简要介绍了将 Okta 配置为 NocoDB 身份服务提供者的步骤。

### NocoDB，检索 `重定向 URL` [](https://docs.nocodb.com/views/views-overview/#nocodb-retrieve-redirect-url "直接链接到 nocodb-retrieve-redirect-url")

1.  转到 `账户设置`
2.  选择 `身份验证 (SSO)`
3.  点击 `新建提供者` 按钮
4.  在弹出的模态框中，为提供者指定一个 `显示名称`；请注意，此名称将在登录页面上显示提供者
5.  检索 `重定向 URL`；此信息稍后需要与身份提供者进行配置

![OIDC SSO 配置](https://docs.nocodb.com/assets/images/SSO-1-aa9135167c7a7cfb680e4fa5e50c86a4.png) ![OIDC SSO 配置](https://docs.nocodb.com/assets/images/OIDC-2-9ca271e8b627eaa9e44eaf8b34c010d1.png) ![OIDC SSO 配置](https://docs.nocodb.com/assets/images/OIDC-3-71b373c47b6affa93db2d447c52c77d6.png)

### Okta，将 NocoDB 配置为应用程序 [](https://docs.nocodb.com/views/views-overview/#okta-configure-nocodb-as-an-application "直接链接到 Okta，将 NocoDB 配置为应用程序")

1.  登录到您的 [Okta 账户](https://www.okta.com/)，并导航到“开始使用 Okta”页面。
    -   点击单点登录选项的 `添加应用`。
    -   在 `浏览应用集成目录` 页面，选择 `创建新应用`
2.  在标题为 `创建新的应用集成` 的弹出窗口中
    -   选择 `OIDC - OpenID Connect` 作为登录方法
    -   选择 `Web 应用程序` 作为应用程序类型
3.  在 `新 Web 应用集成` 页面转到 `常规设置`
    -   提供您的应用程序名称。
    -   在 `允许的授权类型` 部分的选项中，选择 `授权码` 和 `刷新令牌`
    -   在 `登录重定向 URI` 下添加 `重定向 URL`。
    -   在 `分配部分`，选择 `受控访问` 中的一个选项，以设置此应用程序的所需访问配置。
    -   `保存`
4.  在您的新应用程序上，
    -   转到 `常规` 选项卡
    -   从 `客户端凭证` 部分复制 `客户端 ID` 和 `客户端密钥`。
5.  在导航栏的 `账户` 下拉菜单中
    -   复制 `Okta 域`
6.  将 "./well-known/openid-configuration" 附加到 `Okta 域` URL 并访问它
    -   示例: [https://dev-123456.okta.com/.well-known/openid-configuration](https://dev-123456.okta.com/.well-known/openid-configuration)
    -   从 JSON 响应中复制 `authorization_endpoint`、`token_endpoint`、`userinfo_endpoint` 和 `jwks_uri`

### NocoDB，将 Okta 配置为身份提供者 [](https://docs.nocodb.com/views/views-overview/#nocodb-configure-okta-as-an-identity-provider "直接链接到 NocoDB，将 Okta 配置为身份提供者")

在 NocoDB 中，打开 `账户设置` > `身份验证` > `OIDC`。在“注册 OIDC 身份提供者”模态框中，插入以下信息：

-   将步骤（6）中检索到的 `客户端 ID` 插入为 `客户端 ID`
-   将步骤（6）中检索到的 `客户端密钥` 插入为 `客户端密钥`
-   将步骤（8）中检索到的 `authorization_endpoint` 插入为 `授权 URL`
-   将步骤（8）中检索到的 `token_endpoint` 插入为 `令牌 URL`
-   将步骤（8）中检索到的 `userinfo_endpoint` 插入为 `用户信息 URL`
-   将步骤（8）中检索到的 `jwks_uri` 插入为 `JWK 集 URL`
-   将 `范围` 设置为 `openid` `profile` `email` `offline_access`
-   在用户名属性字段中，指明代表用户电子邮件的声明名称。默认值设置为 "email."

对于登录，用户现在应该能够看到 `使用 <SSO> 登录` 选项。

![SAML SSO 配置](https://docs.nocodb.com/assets/images/SSO-SignIn-1221ec860763be25257e0e80e24891ec.png)

注意

如果您没有看到 `使用 <SSO> 登录` 选项，请在注销后刷新页面（第一次）。

有关 Okta API 范围的信息，请参考 [这里](https://developer.okta.com/docs/reference/api/oidc/#scopes)。