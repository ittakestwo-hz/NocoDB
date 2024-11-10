# 访问 API

## 认证令牌（Auth Token）

认证令牌是基于已登录用户生成的 JWT 令牌。默认情况下，令牌的有效期为 10 小时。但您可以通过定义环境变量 `NC_JWT_EXPIRES_IN` 来更改有效期。如果您传递了认证令牌，请确保请求头为 `xc-auth`。

- 进入 NocoDB 项目，点击最右侧按钮，然后点击“Copy Auth Token”（复制认证令牌）。

![image](https://user-images.githubusercontent.com/35857179/194856397-b2e194e8-5ca1-420e-8b46-e1345d1d91d3.png)

## API 令牌

API 令牌允许我们与第三方应用无缝集成。有关更多信息，请参阅 [API Tokens Management](https://docs.nocodb.com/0.109.7/setup-and-usages/team-and-auth#api-tokens-management)（API 令牌管理）。

## Swagger UI

您可以通过 Swagger UI 与 API 资源进行交互。

- 进入 NocoDB 项目，点击最右侧按钮，然后点击“Swagger APIs Doc”（Swagger API 文档）。

![image](https://user-images.githubusercontent.com/35857179/194856535-c81bfc2a-8cdd-41aa-8aa6-9c667c972fa4.png)

- 点击“Authorize”（授权），将您在上面步骤中复制的令牌粘贴进去，然后点击“Authorize”来保存。

![image](https://user-images.githubusercontent.com/35857179/164874471-29fc1630-ab99-4c25-8ce2-b41e5415e4be.png)