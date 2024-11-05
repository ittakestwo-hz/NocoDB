# 编写单元测试

## 单元测试

-   所有单独的单元测试相互独立。我们不在测试之间使用任何共享状态。
-   测试环境包括 `sakila` 示例数据库，测试对其的任何更改都会在运行其他测试之前被还原。
-   在运行单元测试时，它会尝试连接到运行在 `localhost:3306` 的 MySQL 服务器，使用用户名 `root` 和密码 `password`（可进行配置），如果找不到，则会使用 `sqlite` 作为后备，因此运行测试不需要任何 SQL 服务器。

### 先决条件

-   优先使用 MySQL，然而测试也可以回退到 SQLite。

### 设置

```
pnpm --filter=-nocodb install
# 添加 .env 文件
cp tests/unit/.env.sample tests/unit/.env
# 打开 .env 文件
open tests/unit/.env
```

配置以下变量：

> DB\_HOST : 主机  
DB\_PORT : 端口  
DB\_USER : 用户名  
DB\_PASSWORD : 密码  

### 运行测试

### 文件结构

单元测试的根文件夹为 `packages/nocodb/tests/unit`。

-   `rest` 文件夹包含所有 REST API 的测试套件。
-   `model` 文件夹包含所有模型的测试套件。
-   `factory` 文件夹包含所有创建测试数据的辅助函数。
-   `init` 文件夹包含配置测试环境的辅助函数。
-   `index.test.ts` 是根测试套件文件，导入所有测试套件。
-   `TestDbMngr.ts` 是一个辅助类，用于管理测试数据库（即创建、删除等）。

### 工厂模式

-   使用工厂来创建/更新/删除数据。测试中不应直接创建/更新/删除数据。
-   编写工厂时确保尽可能少的参数，并对其他参数使用默认值。
-   使用命名参数作为工厂的参数。

    ```
    createUser({ email, password })
    ```
    
-   每个工厂使用一个文件。

### 编写单元测试的步骤

我们将创建一个 `Table` 测试套件作为示例。

#### 配置测试

我们将配置 `beforeEach`，该函数在每个测试执行之前调用。我们将使用 `nocodb/packages/nocodb/tests/unit/init/index.ts` 中的 `init` 函数，它是一个配置测试环境的辅助函数（即重置状态等）。

`init` 执行以下操作：

-   初始化一个 `Noco` 实例（在所有测试中重用）。
-   恢复 `meta` 和 `sakila` 数据库到其初始状态。
-   创建根用户。
-   返回 `context`，其中包含为创建用户生成的 `auth token`、节点服务器实例（`app`）和 `dbConfig`。

我们将使用 `createProject` 和 `createTable` 工厂来创建一个项目和一个表。

```
let context;
beforeEach(async function () {  
  context = await init();  
  project = await createProject(context);  
  table = await createTable(context, project);
});
```

#### 测试用例

我们将使用 `it` 函数创建一个测试用例。我们将使用 `supertest` 向服务器发起请求。使用 `expect`（`chai`）来断言响应。

```
it('获取表列表', async function () {  
  const response = await request(context.app)    
    .get(`/api/v1/db/meta/projects/${project.id}/tables`)    
    .set('xc-auth', context.token)    
    .send({})    
    .expect(200);  
  expect(response.body.list).to.be.an('array').not.empty;
});
```

信息

我们也可以通过在 `describe` 或 `it` 函数中使用 `.only` 来单独运行测试，并运行测试命令。

```
it.only('获取表列表', async () => {
```

#### 集成新的测试套件

我们在 `packages/nocodb/tests/unit/rest/tests` 目录中创建一个新文件 `table.test.ts`。

```
import 'mocha';
import request from 'supertest';
import init from '../../init';
import { createTable, getAllTables } from '../../factory/table';
import { createProject } from '../../factory/project';
import { defaultColumns } from '../../factory/column';
import Model from '../../../../src/lib/models/Model';
import { expect } from 'chai';

function tableTest() {  
  let context;  
  let project;  
  let table;  
  
  beforeEach(async function () {    
    context = await init();    
    project = await createProject(context);    
    table = await createTable(context, project);  
  });  
  
  it('获取表列表', async function () {    
    const response = await request(context.app)      
      .get(`/api/v1/db/meta/projects/${project.id}/tables`)      
      .set('xc-auth', context.token)      
      .send({})      
      .expect(200);    
    expect(response.body.list).to.be.an('array').not.empty;  
  });
}

export default function () {  
  describe('Table', tableTest);
}
```

然后我们可以将 `Table` 测试套件导入到 `packages/nocodb/tests/unit/rest/index.test.ts` 文件中的 `Rest` 测试套件中（`Rest` 测试套件被导入到根测试套件文件 `packages/nocodb/tests/unit/index.test.ts` 中）。

### 填充示例数据库（Sakila）

```
function tableTest() {  
  let context;  
  let sakilaProject: Project;  
  let customerTable: Model;  
  
  beforeEach(async function () {    
    context = await init();        

    /******* 开始 : 填充示例数据库 **********/
    sakilaProject = await createSakilaProject(context);    
    /******* 结束 : 填充示例数据库 **********/        

    customerTable = await getTable({ project: sakilaProject, name: 'customer' });  
  });  
  
  it('获取表数据列表', async function () {    
    const response = await request(context.app)      
      .get(`/api/v1/db/data/noco/${sakilaProject.id}/${customerTable.id}`)      
      .set('xc-auth', context.token)      
      .send({})      
      .expect(200);    
    expect(response.body.list[0]['FirstName']).to.equal('MARY');  
  });
}
```