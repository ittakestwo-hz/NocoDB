# 编写文档

本文讨论在编写文档时应遵循的协议和约定。

## 文件夹结构[](https://docs.nocodb.com/views/views-overview/#folder-structure "直接链接到文件夹结构")

- 文档遵循面向对象的方法。每个文件夹代表一个对象，每个文件代表与该对象相关的过程。
- 每个文件夹包含一个 `_category_.json` 文件，包含该对象的元数据。

```
{  "label": "工程",  "collapsible": true,  "collapsed": true}
```

## 文件结构[](https://docs.nocodb.com/views/views-overview/#file-structure "直接链接到文件结构")

- 在每个文件的顶部添加以下元数据。

```
---title: "编写文档"description: "编写文档概述"tags: ['工程']keywords: ['工程', '编写文档', '文档规范']---
```

- `title` 是文章的标题，显示在侧边栏和文章顶部。
- `description` 是文章的描述，出现在搜索结果中。
- `tags` 是与文章关联的标签。标签用于将文章分组。例如，所有带有 `工作区` 标签的文章将被归为一组。
- `keywords` 是与文章关联的关键字。关键字用于提高搜索结果的准确性。例如，如果用户搜索 `创建工作区`，则包含关键字 `创建工作区` 的文章将出现在搜索结果中。

## 命名规则[](https://docs.nocodb.com/views/views-overview/#nomenclature "直接链接到命名规则")

- 文件夹名和文件名：
  - 使用连字符（kebab-case）。
  - 以数字前缀表示在侧边栏中的显示顺序。
  - 前缀数字始终为3位数。
  - 例如，`010.account-settings`。
- 文件夹或文件名的第一个字母大写。第二个字母开始仅在是专有名词时才大写。

## 标签[](https://docs.nocodb.com/views/views-overview/#tags "直接链接到标签")

- 每个标签的第一个字母大写。
- 标签通常是对象或动作。仅在我们确定标签会在多个地方使用时才添加。例如，'创建' - 我们可以有 `创建项目`、`创建用户`、`创建API令牌`等。

### 活跃标签[](https://docs.nocodb.com/views/views-overview/#active-tags "直接链接到活跃标签")

当前文档中正在使用的标签如下。在添加新标签前，查看是否可以重用这些标签。

## 描述[](https://docs.nocodb.com/views/views-overview/#description "直接链接到描述")

- 描述应简洁明了，最好是一句话。
- 参考与标签相关的描述，以了解描述的写法。
- 描述出现在搜索结果中（按标签搜索时）。因此，它应该足够描述性，以便让用户了解文章的主题。

![按标签搜索](https://docs.nocodb.com/assets/images/engineering-search-by-tags-9453d5cf2d1534c2f812c7aee697fe43.png)

## 图片[](https://docs.nocodb.com/views/views-overview/#images "直接链接到图片")

- 注释图片应放置在 `img/v2` 文件夹中。
- 每个注释图片都应有一个对应的未注释图片，放置在 `img/v2-unannotated` 文件夹中。
- 图片按与文档相同的文件夹结构存放。
- 使用 `Skitch` 进行注释。

## 提交前[](https://docs.nocodb.com/views/views-overview/#before-you-commit "直接链接到提交前")

- 使用 `npm run build` 来构建文档。
- 确保构建成功且没有与缺失链接、图片等相关的错误/警告。