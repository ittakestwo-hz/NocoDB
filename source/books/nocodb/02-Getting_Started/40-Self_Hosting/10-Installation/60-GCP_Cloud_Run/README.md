# GCP Cloud Run

## 在 GCP Cloud Run 上部署 NocoDB

本指南将帮助您在 Google Cloud Platform 上使用 Cloud Run 部署 NocoDB。

## 先决条件

- 已安装并配置 Google Cloud SDK
- [Docker](https://docs.docker.com/get-docker/)

## 部署步骤

1. 拉取 NocoDB Docker 镜像：
```
docker pull nocodb/nocodb:latest
```
2. 将镜像标记为 Google 容器注册表 (GCR)：
```
docker tag nocodb/nocodb:latest gcr.io/<MY_PROJECT_ID>/nocodb/nocodb:latest
``` 
3. 将镜像推送到 GCR：
```
docker push gcr.io/<MY_PROJECT_ID>/nocodb/nocodb:latest
``` 
4. 在 Cloud Run 上部署 NocoDB：
```
gcloud run deploy --image=gcr.io/<MY_PROJECT_ID>/nocodb/nocodb:latest \
    --region=us-central1 \
    --allow-unauthenticated \
    --platform=managed
```

## 重要说明

- Cloud Run 仅支持来自 Google 容器注册表 (GCR) 或 Artifact 注册表的镜像。因此，我们从 Docker Hub 拉取镜像并将其推送到 GCR。
- 确保您的 GCP 项目已启用必要的 API（Cloud Run、容器注册表）。
- `--allow-unauthenticated` 标志用于允许对服务的未经身份验证的访问。如果您希望限制访问，可以移除此标志。