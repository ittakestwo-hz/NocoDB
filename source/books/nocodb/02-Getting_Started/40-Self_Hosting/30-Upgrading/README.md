# 升级

默认情况下，如果在[安装](https://docs.nocodb.com/getting-started/self-hosted/installation/auto-upstall)时未指定 `NC_DB`，则将使用 SQLite 存储元数据。我们建议用户将元数据和用户数据分开存储在不同的数据库中，如我们[架构](https://docs.nocodb.com/engineering/architecture)中所示。

## Docker [](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#docker "直接链接到 Docker")

### 查找、停止和删除 NocoDB Docker 容器 [](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#find-stop--delete-nocodb-docker-container "直接链接到查找、停止和删除 NocoDB Docker 容器")

```
# 查找 NocoDB 容器 ID
docker ps

# 停止 NocoDB 容器
docker stop <YOUR_CONTAINER_ID>

# 删除 NocoDB 容器
docker rm <YOUR_CONTAINER_ID>
```

注意：在未设置 `NC_DB` 或未挂载到持久卷以用于默认 SQLite 数据库的情况下删除 Docker 容器将导致数据丢失。请参见以下示例。

### 查找和删除 NocoDB Docker 镜像 [](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#find--remove-nocodb-docker-image "直接链接到查找和删除 NocoDB Docker 镜像")

```
# 查找 NocoDB 镜像
docker images

# 删除 NocoDB 镜像
docker rmi <YOUR_IMAGE_ID>
```

### 使用相同环境变量拉取最新的 NocoDB 镜像 [](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#pull-the-latest-nocodb-image-with-same-environment-variables "直接链接到使用相同环境变量拉取最新的 NocoDB 镜像")

```
docker run -d -p 8080:8080 \
    -e NC_DB="<YOUR_NC_DB_URL>" \
    -e NC_AUTH_JWT_SECRET="<YOUR_NC_AUTH_JWT_SECRET_IF_GIVEN>" \
    nocodb/nocodb:latest
```

更新 NocoDB Docker 容器的过程类似于更新[任何其他 Docker 容器](https://www.whitesourcesoftware.com/free-developer-tools/blog/update-docker-images/)。

### 示例：Docker 升级 [](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#example-docker-upgrade "直接链接到示例：Docker 升级")

```
# 之前的 Docker 运行命令
# 终端
% docker run -d --name myNocoDB \
-v "$(pwd)"/nocodb:/usr/app/data/ \
-p 8080:8080 \
-e NC_DB="pg://host.docker.internal:5432?u=postgres&p=password&d=d1" \
-e NC_AUTH_JWT_SECRET="569a1821-0a93-45e8-87ab-eb857f20a010" \
nocodb/nocodb:0.111.0

Unable to find image 'nocodb/nocodb:0.111.0' locally
0.111.0: Pulling from nocodb/nocodb
...
Status: Downloaded newer image for nocodb/nocodb:0.111.0

# 查找、停止和删除 NocoDB Docker 容器
# 终端
% docker ps
CONTAINER ID   IMAGE                   COMMAND                  CREATED          STATUS                 PORTS                    NAMES
afdc8edd1005   nocodb/nocodb:0.111.0   "/usr/bin/dumb-init …"   18 seconds ago   Up 18 seconds          0.0.0.0:8080->8080/tcp   myNocoDB
...
# 停止和删除 NocoDB 容器
% docker stop afdc8edd1005
% docker rm afdc8edd1005

# 查找和删除 NocoDB Docker 镜像
# 终端
% docker images
REPOSITORY      TAG       IMAGE ID       CREATED        SIZE
nocodb/nocodb   0.111.0   34609411e87c   5 weeks ago    132MB
...

% docker rmi 34609411e87c
Untagged: nocodb/nocodb:0.111.0
...

# 使用与之前相同的环境变量拉取并运行最新的 NocoDB 镜像
# 终端
% docker run -d --name myNocoDB \
-v "$(pwd)"/nocodb:/usr/app/data/ \
-p 8080:8080 \
-e NC_DB="pg://host.docker.internal:5432?u=postgres&p=password&d=d1" \
-e NC_AUTH_JWT_SECRET="569a1821-0a93-45e8-87ab-eb857f20a010" \
nocodb/nocodb:latest

Unable to find image 'nocodb/nocodb:latest' locally
latest: Pulling from nocodb/nocodb
...
Status: Downloaded newer image for nocodb/nocodb:latest
```

## Node [](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#node "直接链接到 Node")

更新 Docker 容器的过程类似于更新 npm 包。

从您的根文件夹

#### 卸载 NocoDB 包 [](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#uninstall-nocodb-package "直接链接到卸载 NocoDB 包")
```
npm uninstall nocodb
```

#### 安装 NocoDB 包 [](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#install-nocodb-package "直接链接到安装 NocoDB 包")

```
npm install --save nocodb
```

## Homebrew [](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#homebrew "直接链接到 Homebrew")

运行以下命令以升级 Homebrew 中的 Nocodb 版本。

```
# 更新本地 Homebrew 公式
brew update

# 升级 Nocodb 包
brew upgrade nocodb
```