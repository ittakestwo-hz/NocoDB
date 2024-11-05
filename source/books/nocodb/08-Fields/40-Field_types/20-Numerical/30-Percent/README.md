# 货币

`Currency` 字段类型用于存储货币值。它是一个数值字段，额外提供了在显示中设置货币符号的功能。

## 创建字段

1. 点击 `Fields header` 右侧的 `+` 图标
2. 在下拉模态框中输入字段名称（可选）。
3. 从下拉列表中选择字段类型为 `Currency`。
4. 配置 `Currency Locale`：默认值为 `en-US`
5. 配置 `Currency Symbol`：默认值为 `$`
6. 设置字段的默认值（可选）。
7. 点击 `Save Field` 按钮。

![image](https://docs.nocodb.com/assets/images/currency-97e11fde0e86cf5aa78c6e3117bd9ee8.png)

### 单元格显示

![image](https://docs.nocodb.com/assets/images/currency-cell-display-d3e0309151ff2bb7cc72a48861a565bd.png)

### 支持的地区

[https://www.npmjs.com/package/locale-codes#locale-list](https://www.npmjs.com/package/locale-codes#locale-list)

注

NocoDB 遵循 ISO639-1 标准进行地区代码的定义。

### 支持的货币

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| AED | AFN | ALL | AMD | ANG | AOA |
| ARS | AUD | AWG | AZN | BAM | BBD |
| BDT | BGN | BHD | BIF | BMD | BND |
| BOB | BOV | BRL | BSD | BTN | BWP |
| BYR | BZD | CAD | CDF | CHE | CHF |
| CHW | CLF | CLP | CNY | COP | COU |
| CRC | CUP | CVE | CYP | CZK | DJF |
| DKK | DOP | DZD | EEK | EGP | ERN |
| ETB | EUR | FJD | FKP | GBP | GEL |
| GHC | GIP | GMD | GNF | GTQ | GYD |
| HKD | HNL | HRK | HTG | HUF | IDR |
| ILS | INR | IQD | IRR | ISK | JMD |
| JOD | JPY | KES | KGS | KHR | KMF |
| KPW | KRW | KWD | KYD | KZT | LAK |
| LBP | LKR | LRD | LSL | LTL | LVL |
| LYD | MAD | MDL | MGA | MKD | MMK |
| MNT | MOP | MRO | MTL | MUR | MVR |
| MWK | MXN | MXV | MYR | MZN | NAD |
| NGN | NIO | NOK | NPR | NZD | OMR |
| PAB | PEN | PGK | PHP | PKR | PLN |
| PYG | QAR | ROL | RON | RSD | RUB |
| RWF | SAR | SBD | SCR | SDD | SEK |
| SGD | SHP | SIT | SKK | SLL | SOS |
| SRD | STD | SYP | SZL | THB | TJS |
| TMM | TND | TOP | TRY | TTD | TWD |
| TZS | UAH | UGX | USD | USN | USS |
| UYU | UZS | VEB | VND | VUV | WST |
| XAF | XAG | XAU | XBA | XBB | XBC |
| XBD | XCD | XDR | XFO | XFU | XOF |
| XPD | XPF | XPT | XTS | XXX | YER |
| ZAR | ZMK | ZWD |  |  |  |

## 相似的数值字段

以下是 NocoDB 中其他可用的数值字段，具有一些自定义的附加功能。

- [数字](https://docs.nocodb.com/fields/field-types/numerical/number)
- [小数](https://docs.nocodb.com/fields/field-types/numerical/decimal)
- [百分比](https://docs.nocodb.com/fields/field-types/numerical/percent)