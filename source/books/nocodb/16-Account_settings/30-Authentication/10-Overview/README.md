# Google OAuth

NocoDB 提供了一项功能，允许用户通过 Google OAuth 2.0 进行连接，使他们能够使用 Google 身份验证凭据登录到 NocoDB 账户。本文提供了将 Google OAuth 2.0 与 NocoDB 集成的分步指南。

1.  从 NocoDB 复制 `Redirect URL`
    -   转到 `账户设置` > `身份验证` > `Google OAuth`
    -   从 `Google OAuth` 部分复制 `Redirect URL`
2.  前往 [Google Cloud Console](https://console.cloud.google.com/) 并创建一个新项目。
3.  在 `API 和服务` 部分访问 `OAuth 同意屏幕`。  
    a) 决定您应用程序的配置和注册偏好，指定预期的用户群体  
    b) 点击 `创建` 按钮
4.  通过提供有关应用程序的详细信息并指定您托管 NocoDB 的授权域来设置 OAuth 同意屏幕。
5.  进入 `凭据` 屏幕，然后点击 `创建凭据`。从可用选项中选择 `OAuth 客户端 ID` 以生成 OAuth 凭据。
6.  从 `应用类型` 下拉菜单中选择 `Web 应用程序`。
7.  配置以下内容  
    a) `授权的 JavaScript 源` 指的是您的 Web 应用程序托管的 HTTP 源，例如 [https://app.nocodb.com](https://app.nocodb.com/)  
    b) `授权的重定向 URI` 指的是用户在成功与 Google 进行身份验证后被重定向到的 URI。将步骤（1）中从 NocoDB 复制的 _Redirect URL_ 粘贴到此处。
8.  点击 `创建` 按钮以生成 OAuth 凭据。从 OAuth 2.0 客户端 ID 部分复制 `客户端 ID` 和 `客户端密钥`。
9.  在 NocoDB 中转到 `账户设置` > `身份验证` > `Google OAuth`，并将 `客户端 ID` 和 `客户端密钥` 粘贴到相应的字段中。