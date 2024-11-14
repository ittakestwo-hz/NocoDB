# 提议更新

一旦发布，稳定版（Stable）的更新大约每 2 个月进行一次。`proposed-updates` 仓库是用来准备预期更新的地方（在稳定版发布经理的监督下）。

前面章节中提到的安全更新和稳定版更新总是包含在这个仓库中，但这里还有更多内容，因为软件包维护者也有机会修复那些不需要立即发布的重要错误。

任何人都可以使用这个仓库来测试这些更新，在它们正式发布之前。以下摘录使用了 `bullseye-proposed-updates` 别名，这样更明确且更一致，因为 `buster-proposed-updates` 也存在（用于旧稳定版的更新）：

```
deb https://deb.debian.org/debian bullseye-proposed-updates main contrib non-free
```