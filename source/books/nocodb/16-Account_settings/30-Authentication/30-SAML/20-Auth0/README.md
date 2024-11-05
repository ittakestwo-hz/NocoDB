# Auth0

本文简要介绍了将 Auth0 配置为 NocoDB 身份服务提供者的步骤。

### NocoDB，检索 `SAML SSO` 配置详情

1.  转到 `账户设置`
2.  选择 `身份验证 (SSO)`
3.  点击 `新建提供者` 按钮
4.  在弹出窗口中，为提供者指定一个 `显示名称`；请注意，此名称将在登录页面上显示提供者
5.  检索 `重定向 URL` 和 `受众 / 实体 ID`；这些信息将在后续与身份提供者配置时需要

![SAML SSO 配置](https://docs.nocodb.com/assets/images/SSO-1-aa9135167c7a7cfb680e4fa5e50c86a4.png) ![SAML SSO 配置](https://docs.nocodb.com/assets/images/SAML-2-9ad2e18f3eb498cd699d0f627fb2bb65.png) ![SAML SSO 配置](https://docs.nocodb.com/assets/images/SAML-3-3f208fb861d8e91cb30ecba18c9d7ae8.png)

### Auth0，配置 NocoDB 为应用程序

1.  访问您的 [Auth0 账户](https://auth0.com/)
    
    -   导航到 `应用程序` > `创建应用程序`。
2.  在 `创建应用程序` 窗口中，
    
    -   选择 `常规 Web 应用程序`
    -   点击 `创建`
3.  创建成功后，您将被引导到 `快速入门` 界面。
    
    -   转到 `插件` 选项卡。
    -   启用 `SAML2 Web 应用程序`
4.  在 `SAML2 Web 应用程序` 窗口中，
    
    -   将上述步骤中复制的 `重定向 URL` 粘贴到 `应用程序回调 URL` 字段中
    -   在设置中，保留 `nameIdentifierProbes` 为 `["http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress"]`；如果有其他探测器，请删除它们
    
    ```
    {  "nameIdentifierProbes": [    "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress"  ]}
    ```
    
    -   点击 `启用` 保存设置
5.  在 `设置` 选项卡中，
    
    -   移动到 `高级设置` > `端点` > `SAML` 部分，
    -   复制 SAML `元数据 URL`

### NocoDB，配置 Auth0 为身份提供者

1.  转到 `账户设置` > `身份验证` > `SAML`
2.  插入在上述步骤中检索到的 `元数据 URL`；您也可以直接配置 XML
3.  `保存`

![SAML SSO 配置](https://docs.nocodb.com/assets/images/SAML-4-f2e6f8c1cb091f01fbc7c0901bf1fc84.png)

对于登录，用户现在应该能够看到 `使用 <SSO> 登录` 选项。

![SAML SSO 配置](https://docs.nocodb.com/assets/images/SSO-SignIn-1221ec860763be25257e0e80e24891ec.png)

注意

注销后，如果您没有看到 `使用 <SSO> 登录` 选项，请刷新页面（第一次刷新）。