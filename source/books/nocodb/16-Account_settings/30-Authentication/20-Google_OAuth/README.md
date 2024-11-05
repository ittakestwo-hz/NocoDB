# 概述

本节提供了 NocoDB 中可用的不同身份验证机制的概述。

## 基于电子邮件和密码

这是 NocoDB 中默认的基于表单的身份验证机制。用户可以使用电子邮件和密码注册，然后使用相同的凭据登录。

## 单点登录 (SSO)

单点登录是一种会话和用户身份验证服务，允许用户使用一组登录凭据访问多个应用程序。该服务对用户拥有权限的所有应用程序进行身份验证，并在用户在同一会话期间切换应用程序时消除进一步的提示。

单点登录功能通过与身份提供者（IdP）建立连接实现，IdP 是用于管理用户数字身份的存储库，存在于数字或基于云的生态系统中。通过使用如安全声明标记语言（SAML 2.0）等协议，例如在 NocoDB 的情况下，单点登录促进了身份提供者与服务提供者之间身份验证数据的安全交换。

### Google OAuth

Google OAuth（开放授权）是一种广泛使用的标准化协议，促进安全的身份验证和授权过程，尤其是在 Web 和移动应用程序的上下文中。由 Google 开发，OAuth 使用户能够授权第三方应用程序有限访问其资源，而无需暴露其凭据。该授权框架基于基于令牌的身份验证，用户可以使用其 Google 凭据登录，开发者可以获得访问令牌以代表用户与 Google API 进行交互。

请按照文章中的详细说明集成 [Google OAuth](https://docs.nocodb.com/account-settings/authentication/google-oauth)。

### 安全声明标记语言 (SAML)

安全声明标记语言（SAML）在安全身份验证和授权过程中是一个关键协议。它旨在启用单点登录（SSO）功能，SAML 促进身份提供者（IdP）与服务提供者（SP）之间身份验证和授权数据的交换。该基于 XML 的协议确保用户身份信息的安全传输，使个人能够使用一组凭据访问多个应用程序和服务。SAML 基于信任模型，身份提供者向服务提供者声明用户的身份，后者根据提供的声明授予或拒绝访问权限。

请按照下面文章中的详细说明与各种流行的 SAML 提供商进行集成。

1. [Okta](https://docs.nocodb.com/account-settings/authentication/SAML-SSO/okta)
2. [Auth0](https://docs.nocodb.com/account-settings/authentication/SAML-SSO/auth0)
3. [Ping Identity](https://docs.nocodb.com/account-settings/authentication/SAML-SSO/ping-identity)
4. [Active Directory](https://docs.nocodb.com/account-settings/authentication/SAML-SSO/azure-ad)
5. [Keycloak](https://docs.nocodb.com/account-settings/authentication/SAML-SSO/keycloak)

### OpenID Connect (OIDC)

OpenID Connect（OIDC）协议是建立在 OAuth 2.0 框架之上的现代身份验证层，旨在解决 Web 和移动应用程序中的用户身份验证和授权挑战。OIDC 为应用程序提供了一种标准化和安全的方法来验证最终用户的身份。OIDC 利用 JSON Web Tokens（JWTs），使身份提供者（IdP）与服务提供者（通常是 Web 应用程序）之间交换用户身份信息成为可能。

请按照下面文章中的详细说明与各种流行的 OIDC 提供商进行集成。

1. [Okta](https://docs.nocodb.com/account-settings/authentication/OIDC-SSO/okta)
2. [Auth0](https://docs.nocodb.com/account-settings/authentication/OIDC-SSO/auth0)
3. [Ping Identity](https://docs.nocodb.com/account-settings/authentication/OIDC-SSO/ping-identity)
4. [Active Directory](https://docs.nocodb.com/account-settings/authentication/OIDC-SSO/azure-ad)