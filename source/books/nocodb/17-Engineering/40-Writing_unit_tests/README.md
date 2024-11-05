# 发布与构建

## NocoDB 构建类型

NocoDB 中有 3 种 Docker 构建：

- **发布构建** [nocodb/nocodb](https://hub.docker.com/r/nocodb/nocodb) : 在 NocoDB 发布时构建。
- **每日构建** [nocodb/nocodb-daily](https://hub.docker.com/r/nocodb/nocodb-daily) : 从开发分支每 6 小时构建一次。
- **及时构建** [nocodb/nocodb-timely](https://hub.docker.com/r/nocodb/nocodb-timely): 为每个 PR 和手动触发的 PR 构建。

以下是构建方法及其背后流程概述。

## 发布构建

### 如何进行发布构建？

1. 点击 [NocoDB 发布动作](https://github.com/nocodb/nocodb/actions/workflows/release-nocodb.yml)。
2. 在“使用工作流程”中选择“分支: master”。错误选择分支会导致工作流程终止。
3. 可以将目标标签和先前标签留空，或手动输入一些值。目标标签表示目标部署版本，而先前标签用于显示版本间的文件或提交差异。

### 标签命名规则

假设实际发布标签为 `0.100.0`，则命名规则如下：

- `0.100.0-beta.0` (预发布的第一个版本)
- `0.100.0-beta.1` (包含上一个版本的错误修复)
- `0.100.0` (正式发布)
- `0.100.1` (小错误修复版本)

### 情况 1: 留空输入

- 如果先前标签为空，则会从 [latest](https://github.com/nocodb/nocodb/releases/latest) 获取最新值。
- 如果目标标签为空，则目标标签为先前标签加 `0.0.1`。

### 情况 2: 手动输入

有时可能需要手动输入，因为 NPM 不允许重复发布同一标签。在这种情况下，需使用先前标签加 `2`，手动配置后点击 `运行工作流`。

- 查看总结和总体任务状态。
- 当 `release-draft-note` 和 `release-executables` 完成后，编辑草稿并保存。
- `release-docker` 完成后，先在本地测试，然后发布发布说明。

### 发布动作的工作方式

#### validate-branch

检查 `github.ref` 是否为 master，否则不接受其他分支。

#### process-input

在必要时丰富目标标签或先前标签。

#### pr-to-master

从开发分支自动创建 PR 到 master，以便了解标签差异。

#### release-npm

构建前后端并发布到 NPM，创建并合并自动 PR 到 master。

#### release-draft-note

生成草稿发布说明，供进一步编辑。

#### release-docker

构建并发布 Docker 镜像到 Docker Hub，约需 15 - 30 分钟。

#### close-issues

自动关闭带有“已修复”标签的问题，注明修复所在版本。

#### publish-docs

发布文档。

#### update-sdk-path

在部署时更新 `nocodb-sdk` 的路径。

#### sync-to-develop

同步 master 分支的最新更改到开发分支，保持一致。

## 每日构建

### 什么是每日构建？

- 从开发分支每 6 小时创建并发布到 `nocodb/nocodb-daily`。

### Docker 镜像

- Docker 镜像构建并推送到 Docker Hub (参见 [nocodb/nocodb-daily](https://hub.docker.com/r/nocodb/nocodb-daily/tags) 查看完整列表)。

## 及时构建

### 什么是及时构建？

NocoDB 使用 GitHub Actions 为每个 PR 创建 Docker 和二进制文件，可在 PR 最后提交的评论中找到。

- 进入 PR 并点击评论中的链接复制 Docker 镜像并在本地运行。

### Docker 镜像

当非草稿的 PR 被创建、重新打开或同步时，会触发及时构建。

- Docker 镜像构建并推送到 Docker Hub (参见 [nocodb/nocodb-timely](https://hub.docker.com/r/nocodb/nocodb-timely/tags) 查看完整列表)。

## 可执行文件或二进制文件

为非 Docker 用户提供及时构建，将源代码构建并打包为二进制文件，推送至 GitHub (参见 [nocodb/nocodb-timely](https://github.com/nocodb/nocodb-timely/releases) 查看完整列表)。

支持以下目标：

- `node16-linux-arm64`
- `node16-macos-arm64`
- `node16-win-arm64`
- `node16-linux-x64`
- `node16-macos-x64`
- `node16-win-x64`

一旦可执行文件准备好，GitHub bot 会在 PR 中添加包含命令的评论。

NocoDB 为每个 PR 创建 Docker 和二进制文件，以缩短 PR 循环时间并方便问题报告人/审查人验证修复。