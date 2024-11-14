# MOSFET 的结构

近年来，数字电路基本上都是由 MOSFET 场效应管构成的。MOSFET 是一种在施加电压后可以像开关一样工作的半导体器件。MOSFET 有 P 型 MOSFET 和 N 型 MOSFET 两种。

P 型 MOSFET 的构造如下图所示：

<p align="center">
    <img src="P 型 MOSFET 的构造.png" alt="P 型 MOSFET 的构造">
</p>

N 型 MOSFET 的构造如下图所示：

<p align="center">
    <img src="N 型 MOSFET 的构造.png" alt="N 型 MOSFET 的构造">
</p>

MOSFET 有源极、漏极和栅极 3 个电极。功能上，源极、漏极和栅极分别作为电流输入、电流输出和电流控制使用。

MOSFET 的源极和漏极采用相同类型的半导体材料，而栅极下的通道则填入不同类型半导体材料。

P 型 MOSFET 的源极和漏极使用 P 型半导体，栅极下的通道使用 N 型半导体。

N 型 MOSFET 材料的构成与 P 型 MOSFET 相反。 

下面以 N 型 MOSFET 为例说明其工作原理。

在不给控制电流的栅极施加电压时，源极和漏极间填充了异种半导体材料，因此电流无法流过。

当给栅极施加正电压时，源极和漏极中 N 型半导体材料里的自由电子被栅极吸引，使通道中充满电子，源极和漏极间的电流从而能够流动。

<p align="center">
    <img src="N 型 MOSFET 的动作原理.png" alt="N 型 MOSFET 的动作原理">
</p>

N 型 MOSFET 在栅极施加电源电压（H）时电流可以流通，接地（L）时电流无法流通。反之，P 型 MOSFET 的栅极接地时电流可以通过，施加电源电压时电流无法流过。

这种持有相反特性的 N 型 MOSFET 和 P 型 MOSFET 互补使用形成的门电路称为 CMOS （Complementary Metal Oxide Semiconductor，互补金属氧化物半导体）。CMOS 可以用来制作各种各样的逻辑电路。

