# 大 O 记法

试图摆脱程序或计算机的影响而描述算法的效率时，量化算法的操作或步骤很重要。

如果将每一步看成基本计算单位，那么可以将算法的执行时间描述成解决问题所需的步骤数。

确定合适的基本计算单位很复杂，也依赖于算法的实现。

对于累加算法，计算总和所用的赋值语句的数目就是一个很好的基本计算单位。

回顾：

```
def sumOfN(n): 
    theSum = 0
    for i in range(1, n+1):
        theSum = theSum + i 

    return theSum
```

在 `sumOfN` 函数中，赋值语句数是 `1`（`theSum = 0`）加上 `n`（`theSum = theSum + i` 的运行次数）。可以将其定义成函数 $T$，令 $T(n) = 1 + n$ 。参数 `n` 常被称作问题规模，可以将函数解读为“当问题规模为 `n` 时，解决问题所需的时间是 $T(n)$，即需要 `1 + n` 步。

在前面给出的累加函数中，用累加次数定义问题规模是合理的。这样一来，就可以说处理前 100000 个整数的问题规模比处理前 1000 个整数的大。鉴于此，前者花的时间要比后者长。接下来的目标就是揭示算法的执行时间如何随问题规模而变化。 