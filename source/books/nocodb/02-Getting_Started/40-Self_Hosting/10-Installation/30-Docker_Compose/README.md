# Docker Compose

## 使用 Docker Compose 安装 NocoDB

Docker Compose 允许您定义和运行多容器的 Docker 应用程序。这是将 NocoDB 及其数据库在一个配置文件中设置的好方法。

## 前提条件

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## 安装步骤

1. 从 GitHub 克隆 NocoDB 仓库。
    ```
    git clone https://github.com/nocodb/nocodb
    ```
2. 导航到 docker-compose 目录
    ```
    cd nocodb/docker-compose/2_pg
    ```
3. 使用 Docker Compose 启动服务：这将启动 NocoDB 以及一个 PostgreSQL 数据库。
4. 通过访问 `http://localhost:8080` 在浏览器中访问 NocoDB。

## 重要说明

- 提供的 `docker-compose.yml` 文件已配置为持久化数据。确保卷正确挂载。
- 您可以自定义 `docker-compose.yml` 文件以更改端口、环境变量或添加其他服务。

## 故障排除

- 如果您遇到任何问题，请使用以下命令检查日志：
- 如果您需要停止服务，请使用以下命令：
- 确保您的主机机器上所有所需端口均可用。
- 对于数据库连接问题，请验证数据库服务是否正在运行：