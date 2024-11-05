# Homebrew

## 使用 Homebrew 安装 NocoDB

Homebrew 为在 macOS 和 Linux 系统上安装 NocoDB 提供了一种简单的方法。按照以下步骤使用 Homebrew 安装 NocoDB。

## 前提条件

-   [Homebrew](https://brew.sh/)

## 安装步骤

1.  将 NocoDB 添加到 Homebrew 的源中：
    ```
    brew tap nocodb/nocodb
    ```
2.  安装 NocoDB：
    ```
    brew install nocodb
    ```    
3.  启动 NocoDB：
    ```
    nocodb
    ```    
4.  在浏览器中访问 NocoDB，网址为 `http://localhost:8080`。    

## 更新 NocoDB

要将 NocoDB 更新到最新版本，请使用以下命令：

```
brew upgrade nocodb
```

## 故障排除

-   如果遇到权限问题，请确保您拥有使用 Homebrew 安装软件包的必要权限。
-   如果 NocoDB 无法启动，请检查默认端口（8080）是否已经在使用中。您可以使用环境变量指定不同的端口。