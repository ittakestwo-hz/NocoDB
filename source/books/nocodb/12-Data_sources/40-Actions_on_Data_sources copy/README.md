# 数据源操作

## 编辑数据源参数

-   在基本设置主页中打开 [数据源](https://docs.nocodb.com/data-sources/data-source-overview#accessing-data-sources) 选项卡
-   点击您希望编辑的数据源
-   根据需要重新配置数据源参数，可以编辑以下参数：
    1.  数据源名称
    2.  数据库和架构
    3.  数据源访问权限
-   点击 `提交` 按钮保存更改

备注

要更改数据库连接配置参数（如主机、端口等），请使用 [编辑连接](https://docs.nocodb.com/integrations/actions-on-connection#edit) 选项。编辑连接选项仅对具有“工作区创建者+”权限的用户开放。

![编辑数据源](https://docs.nocodb.com/assets/images/data-source-edit-5d12627884da6af6843315c3d4a77229.png)

## 删除数据源

在基本设置主页中打开 [数据源](https://docs.nocodb.com/data-sources/data-source-overview#accessing-data-sources) 选项卡

1.  点击您希望删除的数据源旁的操作按钮（三个点）
2.  从下拉菜单中选择 `删除` 选项

![数据源解除关联](https://docs.nocodb.com/assets/images/data-source-remove-92f4cbe575b6829905563d10c6fef079.png)

![数据源解除关联](https://docs.nocodb.com/assets/images/data-source-remove-2-938c8c654453fcfb18836327fd82e92d.png)

备注

删除数据源不会删除外部数据源，它仅会将数据源从当前库中移除。

## 数据源可见性

-   在基本设置主页中打开 [数据源](https://docs.nocodb.com/data-sources/data-source-overview#accessing-data-sources) 选项卡
-   切换您希望隐藏/显示的数据源的 `可见性` 列下的单选按钮

![数据源可见性](https://docs.nocodb.com/assets/images/data-source-visibility-fd43ae2a715b65d4e3df928e46513fdc.png)

## 界面访问控制

信息

界面访问控制仅在 NocoDB 的开源版本中可用。

在基本设置主页中打开 [数据源](https://docs.nocodb.com/data-sources/data-source-overview#accessing-data-sources) 选项卡，选择您希望配置 UI ACL 的数据源，并按以下步骤操作：

1.  选择 `UI ACL` 选项卡
2.  您可以查看数据源中可用的视图和表格列表（作为行）及角色（作为列）。切换复选框以为特定角色启用/禁用表的访问。
3.  点击 `保存` 按钮保存更改

![界面访问控制](https://docs.nocodb.com/assets/images/data-source-uiacl-ad7f673a3f7e2074534b899219ea312a.png)

## 审计日志

-   在基本设置主页中打开 [数据源](https://docs.nocodb.com/data-sources/data-source-overview#accessing-data-sources) 选项卡
-   点击 `默认` 数据源，然后
-   访问 `审计` 选项卡查看审计日志

![审计](https://docs.nocodb.com/assets/images/data-source-audit-a37d4f5cdc9ae377941d2baf4942daad.png)

信息

审计日志不适用于外部数据源连接。

## 关系

-   在基本设置主页中打开 [数据源](https://docs.nocodb.com/data-sources/data-source-overview#accessing-data-sources) 选项卡
-   选择您希望访问 ERD（关系视图）的数据源
-   点击 `ERD 视图` 选项卡

![关系](https://docs.nocodb.com/assets/images/data-source-erd-297c127608dc70ab77674cbd7e9b1beb.png)