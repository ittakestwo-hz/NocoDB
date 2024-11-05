# Okta

-   [](https://docs.nocodb.com/)
-   [账户设置](https://docs.nocodb.com/category/account-settings)
-   [身份验证 ☁](https://docs.nocodb.com/category/authentication-)
-   [SAML](https://docs.nocodb.com/category/saml)
-   Okta

版本：最新

本文简要介绍了将 Okta 配置为 NocoDB 的身份服务提供者的步骤。

### NocoDB，获取 `SAML SSO` 配置信息 [](https://docs.nocodb.com/views/views-overview/#nocodb-retrieve-saml-sso-configuration-details "直接链接到 nocodb-retrieve-saml-sso-configuration-details")

1.  转到 `账户设置`
2.  选择 `身份验证 (SSO)`
3.  点击 `新建提供者` 按钮
4.  在弹出的对话框中，为提供者指定一个 `显示名称`；请注意，这个名称将用于在登录页面上显示提供者
5.  获取 `重定向 URL` 和 `受众 / 实体 ID`；这些信息将在稍后与身份提供者配置时需要用到

![SAML SSO 配置](https://docs.nocodb.com/assets/images/SSO-1-aa9135167c7a7cfb680e4fa5e50c86a4.png) ![SAML SSO 配置](https://docs.nocodb.com/assets/images/SAML-2-9ad2e18f3eb498cd699d0f627fb2bb65.png) ![SAML SSO 配置](https://docs.nocodb.com/assets/images/SAML-3-3f208fb861d8e91cb30ecba18c9d7ae8.png)

### Okta，配置 NocoDB 作为应用程序 [](https://docs.nocodb.com/views/views-overview/#okta-configure-nocodb-as-an-application "直接链接到 Okta，配置 NocoDB 作为应用程序")

1.  登录到您的 [Okta 账户](https://www.okta.com/)
    -   导航到 `应用程序` > `应用程序`
    -   点击 `创建应用集成`
2.  在标题为 `创建新的应用集成` 的弹出窗口中，选择 `SAML 2.0` 作为登录方法
3.  在 `创建 SAML 集成` 页面，在常规设置中提供您的应用名称；点击 `下一步`
4.  在 `配置 SAML` 部分：
    -   在 `单点登录 URL` 字段中输入从 NocoDB 复制的 `重定向 URL`。
    -   在 `受众 URI (SP 实体 ID)` 字段中添加从 NocoDB 复制的 `受众 URI`。
    -   从 `名称 ID 格式` 选项中选择 `电子邮件地址`。
    -   从 `应用程序用户名` 选项中选择 `电子邮件`。
    -   点击 `下一步`
5.  在最后一步完成任何附加信息，然后点击 `完成`
6.  在您的应用主页上，
    -   导航到 `登录` 选项卡
    -   从 `SAML 2.0` 部分复制 `元数据 URL`
7.  转到 `分配` 选项卡，点击 `分配` 将人员或组分配给此应用程序。

### NocoDB，配置 Okta 作为身份提供者 [](https://docs.nocodb.com/views/views-overview/#nocodb-configure-okta-as-an-identity-provider "直接链接到 NocoDB，配置 Okta 作为身份提供者")

1.  转到 `账户设置` > `身份验证 (SSO)` > `SAML`
2.  在“注册 SAML 身份提供者”对话框中，插入在上一步中获取的 `元数据 URL`；您也可以直接配置 XML
3.  `保存`

![SAML SSO 配置](https://docs.nocodb.com/assets/images/SAML-4-f2e6f8c1cb091f01fbc7c0901bf1fc84.png)

对于登录，用户现在应该能够看到 `使用 <SSO> 登录` 选项。

![SAML SSO 配置](https://docs.nocodb.com/assets/images/SSO-SignIn-1221ec860763be25257e0e80e24891ec.png)

注意

注销后，如果您没有看到 `使用 <SSO> 登录` 选项，请刷新页面（第一次刷新）。

[

上一个

SAML

](https://docs.nocodb.com/category/saml)[

下一个

Auth0

](https://docs.nocodb.com/account-settings/authentication/SAML-SSO/auth0)