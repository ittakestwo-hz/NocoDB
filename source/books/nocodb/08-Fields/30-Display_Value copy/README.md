# 显示值

`显示值`顾名思义，作为表格中记录的主要或主值，通常是我们用来识别或关联特定记录的属性。虽然建议将显示值与唯一标识符的字段（如主键）相关联，但需要注意的是，这种唯一性并不总是在数据库级别得到强制执行。

<iframe width="560" height="315" src="https://www.youtube.com/embed/GAPAec6zXQ8?si=G_61hrI3gV_xYTrt?&amp;start=13" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"></iframe>

## 显示值的使用 [](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#use-of-display-value "直接链接到显示值的使用")

- 在电子表格中，`显示值`始终被高亮显示，以便更容易识别我们正在处理的记录。
- 当在两个表之间创建`链接`时，出现在`链接记录`对话框中的就是显示值。

示例：在演员表中高亮显示的显示值

![显示值](https://docs.nocodb.com/assets/images/display-value-90a8f4b70e88e428acbff6e49a339325.png)

在链接字段中关联的显示值  
在添加新链接时，`链接记录`对话框中显示的值与关联记录的`显示值`相对应。

![显示值- 链接字段](https://docs.nocodb.com/assets/images/display-value-in-linked-record-a2d5ae449c2be23c1b31d60beb97d063.png)

## 设置显示值 [](https://docs.nocodb.com/getting-started/self-hosted/installation/aws-ecs/#set-display-value "直接链接到设置显示值")

在目标字段中点击下拉图标 (🔽)。然后点击`设为显示值`。

![设置显示值](https://docs.nocodb.com/assets/images/set-as-display-value-dcd56ac34c7d3e79a72b2abcab08f1f8.png)

💡 问答

> **如何识别现有数据库表的显示值？**
> - 通常是在主键之后的第一个非数字字段。
> - 如果没有非数字字段，则选择与主键相邻的字段。

> **我可以将显示值更改为表中的另一个字段吗？**
> - 是的，您可以使用上述相同的方法设置显示值。