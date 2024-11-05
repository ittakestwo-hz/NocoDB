# Azure AD (Entra)

本文简要介绍了将 Active Directory 配置为 NocoDB 身份服务提供商的步骤。

### NocoDB，获取 `SAML SSO` 配置信息 [](https://docs.nocodb.com/views/views-overview/#nocodb-retrieve-saml-sso-configuration-details "直接链接到 nocodb-retrieve-saml-sso-configuration-details")

1. 转到 `账户设置`
2. 选择 `身份验证 (SSO)`
3. 点击 `新建提供商` 按钮
4. 在弹出窗口中，为提供商指定一个 `显示名称`；请注意，此名称将在登录页面上显示
5. 获取 `重定向 URL` 和 `受众 / 实体 ID`；这些信息稍后需要与身份提供商进行配置

![SAML SSO 配置](https://docs.nocodb.com/assets/images/SSO-1-aa9135167c7a7cfb680e4fa5e50c86a4.png) ![SAML SSO 配置](https://docs.nocodb.com/assets/images/SAML-2-9ad2e18f3eb498cd699d0f627fb2bb65.png) ![SAML SSO 配置](https://docs.nocodb.com/assets/images/SAML-3-3f208fb861d8e91cb30ecba18c9d7ae8.png)

### Azure AD，配置 NocoDB 作为应用程序 [](https://docs.nocodb.com/views/views-overview/#azure-ad-configure-nocodb-as-an-application "直接链接到 Azure AD，配置 NocoDB 作为应用程序")

1. 登录到您的 [Azure 账户](https://portal.azure.com/#allservices)，并导航到 `Microsoft Entra 管理中心` > `身份` > `企业应用程序`
2. 点击 `+ 新应用程序`
3. 在 `浏览 Microsoft Entra 画廊` 页面中，从导航栏选择 `创建您自己的应用程序`
   a. 提供您的应用程序名称。  
   b. 选择 `集成您在画廊中找不到的任何其他应用程序 (非画廊)`  
   c. `创建`
4. 在您的应用程序页面中，导航到 `管理` > `单点登录` > `SAML`
5. 转到 `SAML 设置单点登录` 下的 `基本 SAML 配置` 部分并点击 `编辑`  
   a. 在 `标识符 (实体 ID)` 下添加 `受众 URI`。  
   b. 在 `重放 URL (断言消费服务 URL)` 下添加 `重定向 URL`。  
   c. 点击 `保存`
6. 在 `属性和声明` 部分，点击 `编辑`  
   a. 编辑 "唯一用户标识符 (名称 ID)" 声明：
   - 从 `名称标识符格式` 下拉菜单中选择 `电子邮件地址`
   - 选择 `属性` 作为 `源`
   - 在 `源属性` 中选择 `user.mail`
   - 点击 `保存`  
   \[//\]: # ( b. (可选) 对于自定义声明:)  
   \[//\]: # ( - 点击添加新声明，提供详细信息并保存。)  
   \[//\]: # ( - 确保该声明在附加声明部分可见。)  
   \[//\]: # ( - 复制声明名称以便在 NocoDB SAML 配置中使用。)
7. 转到 `SAML 证书` 部分并复制 `应用程序联邦元数据 URL`
8. 在应用程序的概述页面上，  
   - 点击 `用户和组`，  
   - 将所需的用户或组添加到应用程序中。

### NocoDB，配置 Azure AD 作为身份提供商 [](https://docs.nocodb.com/views/views-overview/#nocodb-configure-azure-ad-as-an-identity-provider "直接链接到 NocoDB，配置 Azure AD 作为身份提供商")

1. 转到 `账户设置` > `身份验证` > `SAML`
2. 插入上一步中检索到的 `元数据 URL`；或者您也可以直接配置 XML
3. `保存`

![SAML SSO 配置](https://docs.nocodb.com/assets/images/SAML-4-f2e6f8c1cb091f01fbc7c0901bf1fc84.png)

用户现在应该能够看到 `使用 <SSO> 登录` 选项。

![SAML SSO 配置](https://docs.nocodb.com/assets/images/SSO-SignIn-1221ec860763be25257e0e80e24891ec.png)

注意

如果您在注销后第一次刷新页面时没有看到 `使用 <SSO> 登录` 选项，请刷新页面。