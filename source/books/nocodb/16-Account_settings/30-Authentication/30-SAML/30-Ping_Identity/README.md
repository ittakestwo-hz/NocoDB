# Ping Identity

本文简要介绍了将 Auth0 配置为 NocoDB 身份服务提供者的步骤。

### NocoDB，获取 `SAML SSO` 配置信息

1. 进入 `账户设置`
2. 选择 `身份验证 (SSO)`
3. 点击 `新建提供者` 按钮
4. 在弹出的对话框中，为提供者指定一个 `显示名称`；请注意，此名称将在登录页面上显示
5. 获取 `重定向 URL` 和 `受众 / 实体 ID`；这些信息将在稍后与身份提供者进行配置时使用

![SAML SSO 配置](https://docs.nocodb.com/assets/images/SSO-1-aa9135167c7a7cfb680e4fa5e50c86a4.png) ![SAML SSO 配置](https://docs.nocodb.com/assets/images/SAML-2-9ad2e18f3eb498cd699d0f627fb2bb65.png) ![SAML SSO 配置](https://docs.nocodb.com/assets/images/SAML-3-3f208fb861d8e91cb30ecba18c9d7ae8.png)

### Ping Identity，将 NocoDB 配置为应用程序

1. 访问您的 [PingOne 账户](https://www.pingidentity.com/en/account/sign-on.html) 并导航到首页。
2. 点击右上角的 `添加环境`。
3. 在 `创建环境` 页面上，
   - 选择 `构建自己的解决方案`
   - 在 `为您的环境选择解决方案` 部分，从 `云服务` 中选择 `PingOne SSO`
   - 点击 `下一步`
   - 为环境提供名称和描述，
   - 点击 `下一步`
4. 访问新创建的环境，从侧边栏进入 `连接` > `应用程序`。
5. 在应用程序首页，通过点击 "+" 图标开始创建新应用程序。
6. 在 "添加应用程序" 面板上：
   - 输入应用程序名称和描述。
   - 选择 "SAML 应用程序" 作为应用程序类型，然后点击 "配置"。
   - 在 SAML 配置面板中，选择 "手动输入"。
   - 在 `ACS URLs` 字段中填写从第 (2) 步中获取的 `重定向 URL`
   - 将从第 (2) 步中获取的 `受众 URI` 插入到 `实体 ID` 字段中
   - 点击 `保存`
7. 在您的应用程序中，
   - 导航到 `配置` 选项卡
   - 复制 `IDP 元数据 URL`
8. 在您的应用程序面板上，通过切换右上角的开关激活用户访问该应用程序。

### NocoDB，将 Ping Identity 配置为身份提供者

1. 进入 `账户设置` > `身份验证` > `SAML`
2. 输入上述步骤中获取的 `元数据 URL`；或者您也可以直接配置 XML
3. 点击 `保存`

![SAML SSO 配置](https://docs.nocodb.com/assets/images/SAML-4-f2e6f8c1cb091f01fbc7c0901bf1fc84.png)

在登录时，用户现在应该能够看到 `使用 <SSO> 登录` 的选项。

![SAML SSO 配置](https://docs.nocodb.com/assets/images/SSO-SignIn-1221ec860763be25257e0e80e24891ec.png)

注意：

注销后，如果您第一次刷新页面时没有看到 `使用 <SSO> 登录` 的选项，请刷新页面。