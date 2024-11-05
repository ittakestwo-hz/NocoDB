# 其他安装方法

## 在其他平台上安装 NocoDB

本指南涵盖在多个平台上安装 NocoDB 的方法，包括 Cloudron、CapRover、Railway、FreeBSD/FreeNAS/TrueNAS Jail 和 SealOs。

## Cloudron

Cloudron 提供了一种简单的方式来安装和管理 NocoDB。

### 安装步骤

1. 登录到您的 Cloudron 控制面板。
2. 导航到应用商店。
![应用商店截图](https://user-images.githubusercontent.com/35857179/194700146-aae90503-a8fd-4bc5-8397-39f0bc279606.png)
3. 搜索 NocoDB。
![搜索 NocoDB 截图](https://user-images.githubusercontent.com/35857179/194700181-b5303919-70b8-4cf8-bebe-7e75aca601f3.png)
4. 点击 NocoDB 应用，然后点击“安装”。
![安装 NocoDB 截图](https://user-images.githubusercontent.com/35857179/194700192-d702f5c2-2afa-45c5-9823-4ebe9e141b01.png) 
5. 根据需要配置 NocoDB 设置。
![配置 NocoDB 设置截图](https://user-images.githubusercontent.com/35857179/194700230-c35e934f-bd93-4948-8f31-935483b30571.png) 
6. 安装完成后，转到“我的应用”并启动 NocoDB。
    ![启动 NocoDB 截图](https://user-images.githubusercontent.com/35857179/194700464-50098cb1-bf94-42bb-a63a-cc0aad671913.png)

### 重要说明

- 确保您的 Cloudron 服务器满足运行 NocoDB 的最低要求。
- 通过 Cloudron 的备份系统为您的 NocoDB 实例配置备份。
- 保持 Cloudron 和 NocoDB 应用的更新，以获得最新的功能和安全补丁。

## CapRover

### 部署步骤

1. 登录到您的 CapRover 控制面板。
2. 转到“应用程序”，然后点击“一键应用/数据库”。
![CapRover 应用程序截图](https://user-images.githubusercontent.com/35857179/194701420-7fe5c396-a488-456c-98de-6f2ee1151fc5.png)
3. 搜索 NocoDB 并点击它。
![NocoDB 截图](https://user-images.githubusercontent.com/35857179/194701537-63e7efc5-013b-4ca9-8659-56e9d536e7d0.png)
4. 点击 NocoDB 以开始配置过程。
5. 根据需要配置 NocoDB 设置，然后点击“部署”。
![配置 NocoDB 设置截图](https://user-images.githubusercontent.com/35857179/194701576-19519df5-2aa4-435d-8fc6-7bc684b9cfe1.png) 
6. 部署完成后，您可以通过提供的 URL 访问 NocoDB。

### 重要说明

- 确保您的 CapRover 服务器有足够的资源来运行 NocoDB。
- 为您的 NocoDB 数据配置持久存储。
- 设置 SSL 以安全访问您的 NocoDB 实例。
- 定期更新您的 CapRover 服务器和 NocoDB 应用，以获得最新的功能和安全补丁。

## Railway

### 部署步骤

1. 转到 Railway 模板。
2. 在模板列表中搜索“ NocoDB”。
    ![Railway 模板搜索截图](https://user-images.githubusercontent.com/35857179/194702833-1bea22ee-6dfa-4024-ac27-e33fe56e5500.png)
3. 点击 NocoDB 模板，然后点击“部署”。
4. 根据需要配置您的 NocoDB 设置。
![配置 NocoDB 设置截图](https://user-images.githubusercontent.com/35857179/194702960-149393fe-b00f-4d84-9e54-22cb7616ba44.png)
5. Railway 将自动部署您的 NocoDB 实例。

### 重要说明

- 如果需要，请确保配置数据库连接的环境变量。
- 为您的 NocoDB 数据设置持久存储。
- 定期更新您的 NocoDB 实例以获取最新功能和安全补丁。

## FreeBSD/FreeNAS/TrueNAS Jail 安装

有关在 FreeBSD、FreeNAS 或 TrueNAS Jail 上安装 NocoDB 的详细说明，请参阅 [C. R. Zamana 提供的指南](https://gist.github.com/Zamana/e9281d736f9e9ce5882c6f4b140a590e)。

## SealOs

_[![在 SealOs 上部署](https://raw.githubusercontent.com/labring-actions/templates/main/Deploy-on-Sealos.svg)](https://cloud.sealos.io/?openapp=system-template%3FtemplateName%3Dnocodb)_

## Elestio

_[![在 Elestio 上部署](https://elest.io/images/logos/deploy-to-elestio-btn.png)](https://elest.io/open-source/nocodb)_

## RepoCloud

_[![在 RepoCloud 上部署](https://d16t0pc4846x52.cloudfront.net/deploy.png)](https://repocloud.io/details/?app_id=100)_