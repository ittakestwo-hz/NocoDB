# 架构概述

默认情况下，如果未指定 `NC_DB`，则将使用 SQLite 来存储您的元数据。我们建议用户将元数据和用户数据分开存储在不同的数据库中。

![image](https://docs.nocodb.com/assets/images/architecture-0ae1ed245ed474936af018fb5fa06792.png)

| 项目类型 | 元数据存储在 | 数据存储在 |
| --- | --- | --- |
| 创建新基础 | NC\_DB | NC\_DB |
| 使用外部数据库创建新基础 | NC\_DB | 外部数据库 |
| 从 Excel 创建新基础 | NC\_DB | NC\_DB |