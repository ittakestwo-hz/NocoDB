# 更新密钥

## 更新密钥[](https://docs.nocodb.com/views/views-overview/#updating-secrets "直接链接至更新密钥")

要在 NocoDB 中更新密钥，可以使用 `nc-secret-mgr` 包。按照以下步骤更新密钥：

### 使用命令行界面 (CLI)[](https://docs.nocodb.com/views/views-overview/#using-the-command-line-interface-cli "直接链接至使用命令行界面 (CLI)")

1. 如果还未安装 `nc-secret-mgr` 包，可通过在终端中运行以下命令进行安装：
    
    ```
    npm install -g nc-secret-mgr
    ```
    
2. 安装完成后，可以通过运行以下命令更新密钥：
    
    ```
    NC_DB="pg://host:port?u=user&p=password&d=database" nc-secret-mgr update --prev <previous-secret> --new <new-secret>
    ```
    
    或者
    
    ```
    NC_DB="pg://host:port?u=user&p=password&d=database" nc-secret-mgr <previous-secret> <new-secret>
    ```
    
    将 `<previous-secret>` 替换为之前使用的密钥名称，`<new-secret>` 替换为新的密钥值。
    
3. 运行命令后，密钥将会在 NocoDB 中更新。
    

### 使用可执行文件[](https://docs.nocodb.com/views/views-overview/#using-executables "直接链接至使用可执行文件")

或者，可以使用 `nc-secret-mgr` 可执行文件来更新密钥。

1. 从 [NocoDB Github](https://github.com/nocodb/nc-secret-mgr/releases/latest) 下载 `nc-secret-mgr` 可执行文件。
    
2. 使用以下命令运行可执行文件：
    
    ```
    NC_DB="pg://host:port?u=user&p=password&d=database" ./nc-secret-mgr-macos-arm64 update --prev <previous-secret> --new <new-secret>
    ```
    
    将 `<previous-secret>` 替换为之前使用的密钥名称，`<new-secret>` 替换为新的密钥值。
    
3. 运行命令后，密钥将会在 NocoDB 中更新。
    

注意：支持所有环境变量，包括 `NC_DB`、`NC_DB_JSON`、`NC_DB_JSON_FILE`、`DATABASE_URL` 和 `DATABASE_URL_FILE`。您可以使用这些变量之一来指定数据库连接。或者，可以使用下表中的等效参数。

| 环境变量 | CLI 参数 |
| --- | --- |
| `NC_DB` | `--nc-db` |
| `NC_DB_JSON` | `--nc-db-json` |
| `NC_DB_JSON_FILE` | `--nc-db-json-file` |
| `DATABASE_URL` | `--database-url` |
| `DATABASE_URL_FILE` | `--database-url-file` |