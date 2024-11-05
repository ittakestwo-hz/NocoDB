# 自动安装

自动安装是以最快的方式在 2 分钟内安装带 SSL 的 NocoDB，随每个版本自动升级，并自动续订您的 SSL！

```
bash <(curl -sSL http://install.nocodb.com/noco.sh) <(mktemp)
```

## 关于自动安装的说明

自动安装是一个单一的命令，它：

-   🐳 首先自动在您的 Linux 服务器上安装所有前置条件（Docker、Docker Compose）。
-   🚀 然后自动安装：
    -   🇳 NocoDB，
    -   🐘 PostgreSQL，
    -   ⚡ Redis，
    -   🗄 Minio，
    -   🌐 Traefik 网关。
-   🔄 还会在新版本可用时自动升级 NocoDB。
-   🔒 最后自动设置 SSL，并自动续订！

## 安装视频

<iframe width="560" height="315" src="https://www.youtube.com/embed/AkOWLk7e_hk?si=5A1BMLlQHBtj_pHH" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"></iframe>

## 快速安装指南

以下是使用自动安装脚本安装 NocoDB 的快速指南。

- **步骤 1** : 🔐 SSH 登录到您的服务器（基于 Linux 的系统 - Ubuntu、Debian、CentOS 等）。
- **步骤 2** : 🚀 运行以下命令： 
    ```
    bash <(curl -sSL http://install.nocodb.com/noco.sh) <(mktemp)
    ``` 
- **步骤 3** : 🌐 打开浏览器并访问以下网址：
    - 对于 🌍 HTTP: `http://<您的域名或 IP>`
    - 对于 🔒 HTTPS: `https://<您的域名或 IP>`
- **步骤 4** : 🐦 不要保守这个命令的秘密。发推特分享它有多简单。这一步是必须的！

## 详细安装指南

1.  在终端中运行以下命令：
    ```
    bash <(curl -sSL http://install.nocodb.com/noco.sh) <(mktemp)
    ```   
2.  按照安装提示操作：
    -   **域名**：输入您的 NocoDB 实例的 IP 地址或域名。
    -   **SSL 配置**：如果您输入了有效的域名，系统会询问您是否希望配置 SSL。
    -   **高级选项**：您可以选择显示高级选项或使用默认设置。
3.  如果选择了高级选项：
    -   选择社区版 (CE) 或企业版 (EE)
    -   输入许可证密钥（对于 EE）
    -   启用/禁用 Redis 以进行缓存
    -   启用/禁用 Minio 以进行文件存储
    -   配置 Minio 域和 SSL
    -   启用/禁用 Watchtower 以进行自动更新
    -   设置运行的 NocoDB 实例数量
4.  等待安装完成 - 大约需要 2-5 分钟。完成后，您将看到成功消息，并包含访问您的 NocoDB 实例的 URL。  
5.  访问 NocoDB  
    在浏览器中打开提供的 URL 以访问 NocoDB。
6.  恭喜！您现在应该有一个正常工作的 NocoDB 安装。享受使用您的新无代码数据库平台吧！
    
安装后，系统会询问您是否要启动管理菜单。该菜单允许您：

-   启动 NocoDB
-   停止 NocoDB
-   查看日志
-   重启 NocoDB
-   升级 NocoDB
-   扩展 NocoDB（更改运行实例的数量）
-   监控 NocoDB（查看 Docker 统计信息）

![服务管理菜单](https://docs.nocodb.com/img/v2/engineering/service-mgmt-menu.png)

## 额外说明

-   该脚本在安装目录中创建一个 update.sh 文件。您可以使用此文件在未来更新 NocoDB。
-   如果您在安装过程中遇到任何问题，请检查日志以获取错误消息。