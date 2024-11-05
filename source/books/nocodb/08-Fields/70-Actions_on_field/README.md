# 字段操作

可以通过点击字段名称旁边的下拉图标 (🔽) 访问字段上下文菜单。  
![字段上下文菜单](https://docs.nocodb.com/assets/images/fields-context-menu-bdaf40426dd6cee3e064967ef9c0e1bd.png)

### 编辑[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#edit "直接链接到编辑")

#### 重命名字段[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#rename-field "直接链接到重命名字段")

1. 打开字段上下文菜单。
2. 点击 `编辑` 选项。
3. 在 `字段名称` 字段中输入所需的新字段名称。
4. 点击 `保存字段` 按钮。

![重命名字段](https://docs.nocodb.com/assets/images/fields-edit-2-565e86f68e89b2c0d5a009e26825586b.png)

#### 更改字段类型[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#change-field-type "直接链接到更改字段类型")

1. 打开字段上下文菜单。
2. 点击 `编辑` 选项。
3. 从 `字段类型` 下拉菜单中选择新字段类型。
4. 点击 `保存字段` 按钮。

![更改字段类型](https://docs.nocodb.com/assets/images/fields-edit-3-9f36d47020d18da0b1f30c893bc62b73.png)

#### 更改默认值[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#change-default-value "直接链接到更改默认值")

1. 打开字段上下文菜单。
2. 点击 `编辑` 选项。
3. 在 `默认值` 字段中输入新的默认值。要禁用默认值，请点击 `x` 图标。
4. 点击 `保存字段` 按钮。

![更改默认值](https://docs.nocodb.com/assets/images/fields-edit-4-5eb8140cd39f4ee2364081b214612861.png)

### 更改字段宽度[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#change-field-width "直接链接到更改字段宽度")

要调整字段的宽度，将鼠标悬停在字段边缘并拖动以调整宽度。

![更改字段宽度](https://docs.nocodb.com/assets/images/fields-width-b843c90fee1c762db57dd39a37c931cf.png)

### 隐藏字段[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#hide-field "直接链接到隐藏字段")

1. 打开字段上下文菜单。
2. 点击 `隐藏字段` 选项。

注意

- 隐藏字段在表格视图中不可见，但仍然可以用于公式、排序、过滤等。
- 要取消隐藏字段，请使用 `工具栏 > 字段` 菜单。
- 也可以通过 `工具栏 > 字段` 菜单将字段标记为隐藏。

### 设置为显示值[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#set-as-display-value "直接链接到设置为显示值")

1. 打开字段上下文菜单。
2. 点击 `设置为显示值` 选项。

有关更多详细信息，请参阅 [显示值](https://docs.nocodb.com/fields/display-value)。

### 升序排序[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#sort-ascending "直接链接到升序排序")

1. 打开字段上下文菜单。
2. 点击 `升序排序` 选项。

### 降序排序[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#sort-descending "直接链接到降序排序")

1. 打开字段上下文菜单。
2. 点击 `降序排序` 选项。

### 复制字段[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#duplicate-field "直接链接到复制字段")

1. 打开字段上下文菜单。
2. 点击 `复制` 选项。

将创建一个不带数据的复制字段，其名称后缀为 `_copy`，并将其放置在原字段的右侧。

### 在字段后插入[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#insert-after-a-field "直接链接到在字段后插入")

1. 打开字段上下文菜单。
2. 点击 `在后面插入` 选项。

新字段将在原字段的右侧创建。

### 在字段前插入[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#insert-before-a-field "直接链接到在字段前插入")

1. 打开字段上下文菜单。
2. 点击 `在前面插入` 选项。

新字段将在原字段的左侧创建。

### 删除字段[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#delete-field "直接链接到删除字段")

信息

**此操作无法撤消。**

要删除字段，请按照以下步骤操作：

1. 通过点击下拉图标 (🔽) 打开字段上下文菜单。
2. 点击 **删除**。
3. 在确认模态中点击 **删除字段** 确认删除。

### 添加/编辑字段描述[](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#add--edit-field-description "直接链接到添加/编辑字段描述")

可以通过点击字段创建模态中的 `添加描述` 按钮或通过点击字段上下文菜单中的 `编辑描述` 按钮添加字段描述。

![添加字段描述](https://docs.nocodb.com/assets/images/add-field-description-b930daa8867dda6d76070d2d5fe5c5a8.png) ![编辑字段描述](https://docs.nocodb.com/assets/images/edit-field-description-91e8183d07ebf4d317405e4dadff90ca.png)

字段的描述将在悬停在字段名称旁边的 `信息` 图标时作为工具提示可见。

![字段描述](https://docs.nocodb.com/assets/images/fields-description-cd054aa8023db594ea1d08e9ddee0949.png)