# NocoDB Python 客户端概述

NocoDB Python 客户端为 Python 开发者提供了一种简便的方式与 NocoDB API 交互，NocoDB 是一个多功能的 Airtable 替代方案。该客户端支持基本的 CRUD 操作、过滤和项目管理功能。

## 安装

使用 pip 安装 NocoDB 客户端：

```python
pip install nocodb
```

## 客户端配置

要使用客户端，可以通过 API Token 或 JWT Token 初始化：

```python
from nocodb.nocodb import APIToken, JWTAuthToken
from nocodb.infra.requests_client import NocoDBRequestsClient

# 使用 API Token 示例
client = NocoDBRequestsClient(
    APIToken("YOUR-API-TOKEN"),
    "http://localhost:8080"  # NocoDB 根 URL
)

# 使用 JWT Token 示例
client = NocoDBRequestsClient(
    JWTAuthToken("your.jwt.token"),
    "http://localhost:8080"
)
```

## 项目管理

**创建新项目**：可以使用默认数据库或自定义配置数据库（以下以 PostgreSQL 为例）：
  ```python
  project_body = {"title": "My new project"}
  
  # 或使用 PostgreSQL
  project_body = {
      "title": "MyProject",
      "bases": [
          {
              "type": "pg",
              "config": {
                  "client": "pg",
                  "connection": {
                      "host": "localhost",
                      "port": "5432",
                      "user": "postgres",
                      "password": "postgres",
                      "database": "postgres"
                  },
                  "searchPath": ["public"]
              },
              "inflection_column": "camelize",
              "inflection_table": "camelize"
          }
      ],
      "external": True
  }
  
  project = client.project_create(body=project_body)
  ```

**选择已有项目**：指定组织名称和项目名称（区分大小写）：

  ```python
  from nocodb.nocodb import NocoDBProject
  
  project = NocoDBProject("noco", "myproject")
  ```

## 表操作

**获取行数据**：从表中获取一页或指定行数的数据，并支持过滤和分页：

  ```python
  table_name = "tablename"
  
  # 获取一页行数据
  table_rows = client.table_row_list(project, table_name)

  # 获取前 10,000 行
  table_rows = client.table_row_list(project, table_name, params={'limit': 10000})
  ```

**过滤行数据**：使用 `LikeFilter`、`EqFilter` 或逻辑组合（如 `And`、`Or`）进行过滤：

  ```python
  from nocodb.filters import LikeFilter, EqFilter, And

  table_rows = client.table_row_list(project, table_name, LikeFilter("name", "%sam%"))
  table_rows = client.table_row_list(project, table_name, And(LikeFilter("name", "%sam%"), EqFilter("age", 26)))
  ```

**统计行数据**：

  ```python
  count = client.table_count(project, table_name, EqFilter("Id", 100))
  ```

**创建、更新和删除行**：

  ```python
  row_info = {
      "name": "my thoughts",
      "content": "i'm going to buy samuel a beer 🍻 because I 💚 this module",
      "mood": ":)"
  }
  
  # 创建新行
  client.table_row_create(project, table_name, row_info)
  
  # 更新现有行
  client.table_row_update(project, table_name, row_id=2, row_info={"content": "new content"})
  
  # 删除行
  client.table_row_delete(project, table_name, row_id=10)
  ```

## 过滤器

可用的过滤器包括 `EqFilter`、`NotEqualFilter`、`GreaterThanFilter`、`LessThanFilter` 等，支持逻辑组合：

```python
from nocodb import filters

# 基本过滤器
nickname_filter = filters.EqFilter("nickname", "elchicodepython")
country_filter = filters.EqFilter("country", "es")

# 逻辑组合
combined_filter = filters.And(nickname_filter, country_filter)
table_rows = client.table_row_list(project, table_name, combined_filter)
```

## 自定义过滤器

如果所需操作尚未提供，可以创建自定义过滤器：

```python
from nocodb.filters.factory import basic_filter_class_factory

# 基本自定义过滤器示例
BasicFilter = basic_filter_class_factory('=')
table_rows = client.table_row_list(project, table_name, BasicFilter('age', '16'))
```

借助 NocoDB 的灵活 API 和此 Python 客户端，开发者可以轻松将 NocoDB 的功能集成到应用程序中，实现强大且可定制的数据管理解决方案。