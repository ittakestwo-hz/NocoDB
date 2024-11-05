# Docker

Docker 安装 - 大约需要三分钟！

Docker 提供了一种简单的方式来安装和运行 NocoDB。按照以下步骤使用 Docker 启动 NocoDB。

## 前提条件

-   [Docker](https://www.docker.com/get-started)

## 安装步骤

1.  选择您喜欢的数据库：
<details open>
<summary>SQLite</summary>

```
docker run -d --name nocodb \
-v "$(pwd)"/nocodb:/usr/app/data/ \
-p 8080:8080 \
nocodb/nocodb:latest    
```

</details>
<details open>
<summary>Postgres</summary>

```
docker run -d --name nocodb-postgres \
-v "$(pwd)"/nocodb:/usr/app/data/ \
-p 8080:8080 \
-e NC_DB="pg://host.docker.internal:5432?u=root&p=password&d=d1" \
-e NC_AUTH_JWT_SECRET="569a1821-0a93-45e8-87ab-eb857f20a010" \
nocodb/nocodb:latest
```

</details>

2.  一旦容器运行，您可以通过在网页浏览器中打开 [http://localhost:8080](http://localhost:8080/) 来访问 NocoDB。

> **提示**
> 为了持久化数据，请始终将卷挂载到 `/usr/app/data/`。如果没有这样做，容器被移除时您的数据将会丢失。对于 0.10.6 之前的版本，请将卷挂载到 `/usr/src/app`。

## 故障排除

- 如果您在安装后无法访问 NocoDB，请检查 Docker 容器是否正在运行。
- 如果容器未运行，请检查日志以查看是否有错误。

## 安装视频

<iframe width="100%" height="500" src="https://www.youtube.com/embed/K-UEecQyiOk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen=""></iframe>