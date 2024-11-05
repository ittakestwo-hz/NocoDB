# i18n 翻译

-   NocoDB 支持 30 多种外语，并且通过 [Crowdin](https://crowdin.com/) 的社区贡献现已简化。

## 如何添加 / 编辑翻译？[](https://docs.nocodb.com/views/views-overview/#how-to-add--edit-translations- "直接链接到如何添加 / 编辑翻译？")

### 使用 GitHub[](https://docs.nocodb.com/views/views-overview/#using-github "直接链接到使用 GitHub")

-   对于英语，请直接更改 [en.json](https://github.com/nocodb/nocodb/blob/develop/packages/nc-gui/lang/en.json) 文件并提交到 `develop` 分支。
-   对于其他语言，请使用 `Crowdin` 选项。

### 使用 Crowdin[](https://docs.nocodb.com/views/views-overview/#using-crowdin "直接链接到使用 Crowdin")

-   注册 [Crowdin](https://crowdin.com/) 账户
-   加入 [NocoDB](https://crowdin.com/project/nocodb) 项目

![屏幕截图 2022-09-08 于 10:26:23 PM](https://user-images.githubusercontent.com/86527202/189181511-51b8671e-bee8-45d5-8216-a4a031bc6309.png)

-   点击您希望贡献的语言

![屏幕截图 2022-09-08 于 10:29:56 PM](https://user-images.githubusercontent.com/86527202/189182132-0eed7d5a-eaa1-43e1-929d-688f375763c1.png)

-   点击 `Translate` 按钮；这将打开 `Crowdin Online Editor`

![屏幕截图 2022-09-08 于 10:32:17 PM](https://user-images.githubusercontent.com/86527202/189182450-999124e8-566c-40af-9d3c-731a11c1b6aa.png)

-   在左侧菜单栏中选择 `English` 字符串 \[1\]
-   提出修改意见 \[2\]
-   保存 \[3\] 注意：Crowdin 提供翻译推荐 \[4\]，如合适可直接点击使用

![屏幕截图 2022-09-08 于 10:37:38 PM](https://user-images.githubusercontent.com/86527202/189184278-69d688ed-4e5a-4d5a-b629-9f6d10d79346.png)

GitHub 拉取请求将自动触发（周期为 6 小时）。我们将跟进剩余的集成工作项。

#### 参考[](https://docs.nocodb.com/views/views-overview/#reference "直接链接到参考")

请参阅以下文章以获取更多关于 Crowdin 门户的使用细节：

-   [翻译人员介绍](https://support.crowdin.com/crowdin-intro/)
-   [志愿翻译人员介绍](https://support.crowdin.com/for-volunteer-translators/)
-   [在线编辑器](https://support.crowdin.com/online-editor/)

## 如何添加新语言？[](https://docs.nocodb.com/views/views-overview/#how-to-add-a-new-language- "直接链接到如何添加新语言？")

#### GitHub 更改[](https://docs.nocodb.com/views/views-overview/#github-changes "直接链接到 GitHub 更改")

-   更新 `enums.ts` 中的枚举项 \[packages/nc-gui/lib/enums.ts\]
-   在 `a.i18n.ts` 中映射 JSON 路径 \[packages/nc-gui/plugins/a.i18n.ts\]

#### Crowdin 更改 \[仅限管理员\][](https://docs.nocodb.com/views/views-overview/#crowdin-changes-admin-only "直接链接到 Crowdin 更改 [仅限管理员]")

-   打开 `NocoDB` 项目
-   点击首页标签上的 `Language`
-   选择目标语言，`Update`
-   更新 `tests/playwright/tests/language.spec.ts` 中的数组

![屏幕截图 2022-09-08 于 10:52:59 PM](https://user-images.githubusercontent.com/86527202/189186570-5c1c7cad-6d3f-4937-ab4d-fa7ebe022cb1.png)

![屏幕截图 2022-09-08 于 10:54:04 PM](https://user-images.githubusercontent.com/86527202/189186632-0b9f5f55-0550-4d8f-a8ae-7e9b9076774e.png)

## 字符串类别[](https://docs.nocodb.com/views/views-overview/#string-categories "直接链接到字符串类别")

-   **General**：简单和通用的词汇（如保存、取消、提交、打开、关闭、主页等）
-   **Objects**：NocoDB 视角下的对象（如项目、表、字段、视图、页面等）
-   **Title**：屏幕标题（简洁的）（菜单标题、模式窗口标题）
-   **Labels**：文本框/单选/字段标题（简短）（文本框、单选按钮上的标签等）
-   **Activity**/动作：工作项目（简短）（创建项目、删除表格、添加记录等）
-   **Tooltip**：与工作项目相关的附加信息（通常较长）（为活动提供的附加信息）
-   **Placeholder**：与各种文本框相关的占位符（文本占位符）
-   **Msg**
    -   Info：一般/成功类信息
    -   Error：警告和错误
    -   Toast：弹出式提示消息

> 注意：字符串名称应使用驼峰命名法。如有歧义，请按照上述列表的优先级排列。