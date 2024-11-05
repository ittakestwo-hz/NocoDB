# 附件

`Attachment` 字段允许您将文件上传到您的记录中。您可以上传任何类型的文件，并且该文件将与记录关联。您还可以将多个文件上传到单个 `Attachment` 字段记录中。

## 创建附件字段[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#create-an-attachment-field "直接链接到创建附件字段")

1. 点击 `Fields header` 右侧的 `+` 图标
2. 在下拉模态中，输入字段名称（可选）。
3. 从下拉菜单中选择字段类型为 `Attachment`。
4. 点击 `Save Field` 按钮。

![image](https://docs.nocodb.com/assets/images/attachment-68efc9fbeb85c49731a9d441cd90bda8.png)

信息

附件文件的最大大小目前限制为 5 MB

### 单元格显示[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#cell-display "直接链接到单元格显示")

`Attachment` 字段的单元格显示为可点击的预览（如果文件是可识别格式的图像）或文件类型图标。  
![image](https://docs.nocodb.com/assets/images/attachment-cell-63aeff518251334ef9ebdd018c752b1b.png)

### 上传文件[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#upload-files "直接链接到上传文件")

要上传文件到 `Attachment` 字段，

- 点击单元格中的 `+` 图标，选择要上传的文件，然后点击 `Upload` 按钮。或者
- 拖放文件到单元格中。或者
- 点击扩展图标 `<>`，选择要上传的文件或拖放文件；点击 `Upload` 按钮。

## 扩展模态[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#expand-modal "直接链接到扩展模态")

`Attachment` 字段的扩展模态显示已上传到该字段的文件列表。您也可以从扩展模态上传文件。要访问扩展模态，请点击单元格中的扩展图标 `<>`。

![image](https://docs.nocodb.com/assets/images/attachment-expand-bf0a44f3b002a3efa120b55211ac4d3c.png)

扩展模态支持以下操作：

### 附加文件[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#attach-files "直接链接到附加文件")

- 点击 `Attach file(s)` 按钮 <1>
- 选择要上传的文件

### 删除文件[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#delete-file "直接链接到删除文件")

- 点击图像卡片左上角的 `x` 图标 <2> 以删除文件

### 下载文件[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#download-file "直接链接到下载文件")

- 点击 `Download` 按钮 <5> 下载文件

### 批量下载文件[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#bulk-download-files "直接链接到批量下载文件")

- 通过点击图像卡片左上角的复选框 <3> 选择文件
- 点击 `Bulk Download` 按钮 <4> 下载所选文件

### 重命名文件[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#rename-file "直接链接到重命名文件")

- 点击 `Rename` 按钮 <5> 以重命名文件
- 在输入框中输入新名称
- 点击 `Rename` 按钮以保存新名称

注意

重命名文件仅在 NocoDB 显示中重命名文件（扩展记录和悬停工具提示）。它不会在存储中重命名文件。

## 环境变量[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#environment-variables "直接链接到环境变量")

在自托管版本中，您可以配置以下环境变量以自定义 `Attachment` 字段的行为：

- `NC_ATTACHMENT_FIELD_SIZE`：附件文件的最大大小（以字节为单位）。默认值：`20971520`（20 MiB）
- `NC_MAX_ATTACHMENTS_ALLOWED`：每个单元格允许的最大附件数量。默认值：`10`
- `NC_SECURE_ATTACHMENTS`：仅允许通过预签名的 URL 访问附件。默认值：`false`
- `NC_ATTACHMENT_EXPIRE_SECONDS`：预签名 URL 的过期时间。默认值：`7200`（2 小时）

所有支持的环境变量在 [这里](https://docs.nocodb.com/getting-started/self-hosted/environment-variables) 描述。

## 相关文章[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#related-articles "直接链接到相关文章")

- [从移动设备附加文件](https://docs.nocodb.com/views/view-types/form#attaching-a-file-from-mobile-device)