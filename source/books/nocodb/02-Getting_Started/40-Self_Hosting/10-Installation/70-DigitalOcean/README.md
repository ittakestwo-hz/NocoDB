# DigitalOcean

## 在 DigitalOcean 上部署 NocoDB

按照以下步骤在 DigitalOcean 上使用其应用平台部署 NocoDB。

## 部署步骤

1. 在 DigitalOcean 主页上，点击“创建”图标并选择“应用程序（部署您的代码）”。
![DigitalOcean 创建应用](https://user-images.githubusercontent.com/86527202/154790558-f8fe5580-5a58-412c-9c2e-145587712bf2.png)  
2. 选择“Docker Hub”作为源。
![DigitalOcean Docker Hub](https://user-images.githubusercontent.com/86527202/154790563-b5b6d5b4-0bdc-4718-8cea-0a7ee52f283b.png)
3. 将源代码库设置为 nocodb/nocodb。如果您想要特定的 NocoDB 版本，可以选择指定发布标签。
![DigitalOcean Docker Hub](https://user-images.githubusercontent.com/86527202/154790564-1dcb5e33-3a57-471a-a44c-835a410a0cb7.png)
4. 根据需要配置其他设置。
![DigitalOcean Docker Hub](https://user-images.githubusercontent.com/86527202/154790565-c0234b2e-ad50-4042-90b6-4f8798f1d585.png)
5. 为您的网络服务命名并选择离您最近的云托管区域。
![DigitalOcean Docker Hub](https://user-images.githubusercontent.com/86527202/154790567-a6e65e4e-9aa0-4edb-998e-da8803ad6e23.png)
6. 选择您偏好的托管计划并点击“启动基本应用”。
![DigitalOcean Docker Hub](https://user-images.githubusercontent.com/86527202/154790570-62044713-5cca-4d06-82ec-f3cc257218a1.png)

您的应用程序将开始构建，URL 将很快上线。URL 看起来类似于 [https://your-app-name.ondigitalocean.app/](https://your-app-name.ondigitalocean.app/)。

## 重要提示

- 如果需要，请确保为数据库连接配置环境变量。
- 为您的 NocoDB 数据设置持久存储。
- 您可以根据需要使用 DigitalOcean 的应用平台扩展您的应用。
- 考虑启用自动部署，以便于更新。