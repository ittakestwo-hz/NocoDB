# Keycloak

本文简要介绍了将 Keycloak 配置为 NocoDB 身份服务提供者的步骤。

### NocoDB，获取 `SAML SSO` 配置详情

1. 前往 `账户设置`
2. 选择 `身份验证 (SSO)`
3. 点击 `新建提供者` 按钮
4. 在弹出窗口中，为提供者指定一个 `显示名称`；请注意，此名称将用于在登录页面上显示提供者
5. 获取 `重定向 URL` 和 `受众 / 实体 ID`；这些信息将在后续配置身份提供者时需要

![SAML SSO 配置](https://docs.nocodb.com/assets/images/SSO-1-aa9135167c7a7cfb680e4fa5e50c86a4.png) ![SAML SSO 配置](https://docs.nocodb.com/assets/images/SAML-2-9ad2e18f3eb498cd699d0f627fb2bb65.png) ![SAML SSO 配置](https://docs.nocodb.com/assets/images/SAML-3-3f208fb861d8e91cb30ecba18c9d7ae8.png)

### Keycloak，将 NocoDB 配置为应用程序

1. 访问你的 Keycloak 帐户
    - 转到 `客户端` 菜单
    - 选择 `客户端列表` 标签 > 点击 `创建客户端` 按钮
2. 在 `创建客户端` 窗口中，`常规设置` 标签：
    - 选择 `SAML` 作为 `客户端类型`
    - 将从 NocoDB 获取的 `受众/实体 ID` 指定为 `客户端 ID`
    - 点击 `下一步`
3. 在 `创建客户端` 窗口中，`登录设置` 标签：
    - 将从 NocoDB 获取的 `重定向 URL` 指定为 `有效重定向 URI`
    - 将从 NocoDB 获取的 `重定向 URL` 指定为 `有效注销后重定向 URI`
    - 点击 `保存`
4. 在 `客户端详情`，`设置` 标签：
    - 转到 `SAML 功能` 部分
    - 将 `名称 ID 格式` 指定为 `email`
    - 启用 `强制名称 ID 格式` 和 `强制 POST 绑定`
    - 转到 `签名和加密` 部分
    - 启用 `签名声明`
    - 点击 `保存`
5. 在 `客户端详情`，`密钥` 标签：
    - 禁用 `签名密钥配置` > `客户端签名必需`
6. 转到 `领域设置` > `端点`
    - 复制 `SAML 2.0 身份提供者元数据` URL

### NocoDB，将 Azure AD 配置为身份提供者

1. 前往 `账户设置` > `身份验证` > `SAML` 密钥
2. 插入在上述步骤中获取的 `元数据 URL`；或者，你也可以直接配置 XML
3. 点击 `保存`

![SAML SSO 配置](https://docs.nocodb.com/assets/images/SAML-4-f2e6f8c1cb091f01fbc7c0901bf1fc84.png)

用户现在应该能够在登录时看到 `使用 <SSO> 登录` 选项。

![SAML SSO 配置](https://docs.nocodb.com/assets/images/SSO-SignIn-1221ec860763be25257e0e80e24891ec.png)

注意

如果你在注销后第一次刷新页面时没有看到 `使用 <SSO> 登录` 选项，请刷新页面。