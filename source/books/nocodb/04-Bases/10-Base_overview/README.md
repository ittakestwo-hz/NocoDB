# Base概述

在 NocoDB 中，Base是包含表、视图、表单和 Webhook 的基本元素，为数据组织和协作工作提供了结构化框架。重要的是要理解，每个Base都固有地与特定的工作区相关联，无法在不同工作区之间转移。Base的创建者被称为“Base拥有者”。一个Base可以有多个拥有者，每个拥有者都有权管理Base的设置和访问权限。每个Base至少需要一个拥有者才能保持其正常运作。

Base还配备了其独特的成员和访问权限，这些权限优先于工作区级别设置的任何权限。这种细粒度的控制允许在每个Base内进行定制化的协作和数据管理。值得注意的是，邀请到Base的成员数量没有限制，促进了开放的团队合作。类似地，您可以在单个Base内自由创建所需的多个表，提供了所需的可扩展性，以适应各种数据集和项目。

要开始使用，如果您想从头开始，可以[创建一个空Base](https://docs.nocodb.com/bases/create-base)。如果您已经在使用 Airtable，我们可以轻松地[导入您的Base](https://docs.nocodb.com/bases/import-base-from-airtable)。在与团队协作时，您可以[邀请他们](https://docs.nocodb.com/bases/base-collaboration)共同工作。如果您想将数据分享给更广泛的受众，可以[将Base设为公开](https://docs.nocodb.com/bases/share-base)。如果您需要重命名Base，可以使用[重命名Base](https://docs.nocodb.com/bases/actions-on-base#rename-base)功能。并且，如果您发现某个Base特别有用，可以[将其添加到收藏](https://docs.nocodb.com/bases/actions-on-base#star-base)以便快速访问。然而，当您需要删除一个Base时，可以[将其删除](https://docs.nocodb.com/bases/actions-on-base#delete-base)。

## Base仪表板[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#base-dashboard "直接链接到Base仪表板")

Base仪表板作为Base的主要登录页面，为用户提供其内容和功能的简要摘要。这个中央中心为用户提供了快速访问Base设置和协作工具等基本功能。要访问Base仪表板，只需单击左侧边栏中的Base名称。

![image](https://docs.nocodb.com/assets/images/base-dashboard-1c778031a554f46f75392fc786212606.png)

Base仪表板分为三个关键部分，每个部分有其特定目的：

1. **表列表**：此部分提供Base内所有表的综合列表，包括来自外部数据存储库的表。用户可以通过单击表名称便捷地访问特定表。来自外部来源的表在列表中清晰突出，便于识别。
2. **Base成员**：在此部分，用户可以查看与Base相关联的成员名单及其相应的权限级别。值得注意的是，属于工作区的成员自动继承Base级别的访问权限。然而，Base拥有者仍保留调整这些权限的能力，可以增加或减少它们。有关协作管理的更多详细信息，请参见专门的[Base协作](https://docs.nocodb.com/bases/base-collaboration)部分。
3. **数据源**：NocoDB 提供连接外部数据源并将其无缝集成为本地表的功能。此部分提供已连接数据源的列表，为即将介绍的[数据源](https://docs.nocodb.com/data-sources/data-source-overview)部分奠定基础。这一功能使用户能够像处理内部数据表一样轻松处理外部数据，增强了Base内数据管理的灵活性和广度。
## 相关文章[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#related-articles "直接链接到相关文章")

- [创建一个空Base](https://docs.nocodb.com/bases/create-base)
- [从 Airtable 导入Base](https://docs.nocodb.com/bases/import-base-from-airtable)
- [邀请团队成员共同工作](https://docs.nocodb.com/bases/base-collaboration)
- [公开分享Base](https://docs.nocodb.com/bases/share-base)
- [重命名Base](https://docs.nocodb.com/bases/actions-on-base#rename-base)
- [复制Base](https://docs.nocodb.com/bases/actions-on-base#duplicate-base)
- [添加Base收藏](https://docs.nocodb.com/bases/actions-on-base#star-base)
- [删除Base](https://docs.nocodb.com/bases/actions-on-base#delete-base)