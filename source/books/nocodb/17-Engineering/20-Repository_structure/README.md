# 仓库结构

我们使用 `Lerna` 来管理多个包。我们有以下[包](https://github.com/nocodb/nocodb/tree/master/packages)。

- `packages/nc-cli`：用于创建 NocoDB 应用的 CLI。
  
- `packages/nocodb-sdk`：NocoDB 的 API 客户端 SDK。
  
- `packages/nc-gui`：NocoDB 前端。
  
- `packages/nc-lib-gui`：`nc-gui` 的构建版本，将在 `packages/nocodb` 中使用。
  
- `packages/noco-blog`：NocoDB 博客，将自动发布到 [nocodb/noco-blog](https://github.com/nocodb/noco-blog)。
  
- `packages/noco-docs`：NocoDB 文档，将自动发布到 [nocodb/noco-docs](https://github.com/nocodb/noco-docs)。
  
- `packages/nocodb`：NocoDB 后端，托管在 [NPM](https://www.npmjs.com/package/nocodb) 上。