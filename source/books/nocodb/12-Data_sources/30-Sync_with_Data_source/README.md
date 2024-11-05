# 与数据源同步

要将外部数据源中的更改与 NocoDB 同步，请在基本设置中打开 [数据源](https://docs.nocodb.com/data-sources/data-source-overview#accessing-data-sources) 选项卡，选择您要同步元数据的数据源，然后按以下步骤操作：

1. 点击 `Meta Sync` 选项卡
2. 点击 `Reload` 按钮以刷新同步状态（可选）
3. 识别出的任何元数据更改将显示在 `Sync State` 列中
4. 点击 `Sync Now` 按钮以同步元数据更改
5. 同步完成后，您可以在 `Sync State` 列中查看更新后的状态

![同步元数据](https://docs.nocodb.com/assets/images/data-source-meta-sync-1-aef2f4b8c4939fb494857d19f1f48c00.png)

![同步元数据](https://docs.nocodb.com/assets/images/data-source-meta-sync-2-6a03a0f5352aaee35f7bdd6a3ab7283f.png)

同步完成后，您可以在 `Sync State` 列中查看更新后的状态。
同步窗口的标题还会标记为 `Tables metadata is in Sync`。