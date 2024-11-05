# 字符串函数

本备忘单提供了数据分析和编程中常用的各种字符串函数的快速参考指南。每个函数都附有其语法、示例用法和简要描述。

## CONCAT

CONCAT 函数将一个或多个字符串连接成一个单一字符串。

#### 语法

#### 示例

```
CONCAT('John', ' ', 'Doe') => 'John Doe'
```

## LEFT

LEFT 函数从输入字符串的开头检索指定的前 'n' 个字符。

#### 语法

#### 示例

```
LEFT('123-456-7890', 3) => '123'
```

## LEN

LEN 函数计算并返回提供的字符串中的总字符数。

#### 语法

#### 示例

```
LEN('Product Description') => 19
```

## LOWER

LOWER 函数将输入字符串中的所有字符转换为小写字母。

#### 语法

#### 示例

```
LOWER('User INPUT') => 'user input'
```

## MID

MID 函数从输入字符串中提取子字符串，从指定位置开始并扩展到指定的字符数。

#### 语法

```
MID(text, position, [count])
```

#### 示例

```
MID('This is a sentence', 5, 3) => 'is '
```

REGEX_EXTRACT 函数在输入字符串中搜索指定的正则表达式模式的首次出现，并返回匹配的子字符串。

#### 语法

```
REGEX_EXTRACT(text, pattern)
```

#### 示例

```
REGEX_EXTRACT('Error: Something went wrong', 'Error: (.*)') => 'Something went wrong'
```

## REGEX_MATCH

REGEX_MATCH 函数评估输入字符串是否与指定的正则表达式模式匹配，如果匹配则返回 1，否则返回 0。

#### 语法

```
REGEX_MATCH(text, pattern)
```

#### 示例

```
REGEX_MATCH('123-45-6789', '\d{3}-\d{2}-\d{4}') => 1
```

## REGEX_REPLACE

REGEX_REPLACE 函数识别输入字符串中指定正则表达式模式的所有出现，并用提供的替换字符串替代。

#### 语法

```
REGEX_REPLACE(text, pattern, replacer)
```

#### 示例

```
REGEX_REPLACE('Replace all bugs', 'bug', 'feature') => 'Replace all features'
```

## REPEAT

REPEAT 函数将提供的字符串复制指定的次数，以便创建重复的模式或序列。

#### 语法

#### 示例

```
REPEAT('😃', 3) => '😃😃😃'
```

## REPLACE

REPLACE 函数识别给定字符串中某个子字符串的所有实例，并用另一个指定的子字符串替代。

#### 语法

```
REPLACE(text, srchStr, rplcStr)
```

#### 示例

```
REPLACE('Replace old text', 'old', 'new') => 'Replace new text'
```

## RIGHT

RIGHT 函数从输入字符串的末尾检索最后 'n' 个字符，允许从右侧提取子字符串。

#### 语法

#### 示例

```
RIGHT('file_name.txt', 3) => 'txt'
```

## SEARCH

SEARCH 函数识别输入字符串中指定子字符串的位置，如果找到则返回索引，否则返回 0。

#### 语法

#### 示例

```
SEARCH('user@example.com', '@') => 5
```

## SUBSTR

SUBSTR 函数从输入字符串中提取子字符串，从指定位置开始，并可选择扩展到指定的字符数。

#### 语法

```
SUBSTR(text, position, [count])
```

#### 示例

```
SUBSTR('Extract this text', 9, 4) => 'this'
```

## TRIM

TRIM 函数去除输入字符串中的任何前导或尾随空格。

#### 语法

#### 示例

```
TRIM('   Trim this   ') => 'Trim this'
```

## UPPER

UPPER 函数将输入字符串中的所有字符转换为大写字母。

#### 语法

#### 示例

```
UPPER('title') => 'TITLE'
```

## URL

URL 函数检查输入字符串是否为有效 URL，并将其转换为超链接。

#### 语法

#### 示例

```
URL('https://www.example.com') => 可点击链接 https://www.example.com
```

## URLENCODE

URLENCODE 函数对字符串中的特殊字符进行百分号编码，以便可以作为查询参数替换到 URL 中。

它类似于 JavaScript 的 `encodeURIComponent()` 函数，只编码根据 RFC 3986 第 2.2 节具有特殊含义的字符，以及百分号和空格；其他非拉丁字母的字符不会被编码。与 `encodeURIComponent()` 一样，它仅用于编码 URL 组件，而不是整个 URL。

#### 语法

#### 示例

```
'https://example.com/q?param=' & URLENCODE('Hello, world') => 'https://example.com/q?param=Hello%2C%20world'
```

## ISBLANK

ISBLANK 函数检查给定输入是否不为空或为 null，如果输入有值则返回 FALSE，否则返回 TRUE。

#### 语法

#### 示例

```
ISBLANK('') => true
ISBLANK('Hello') => false
```

## ISNOTBLANK

ISNOTBLANK 函数检查给定输入是否不为空或为 null，如果输入有值则返回 TRUE，否则返回 FALSE。

#### 语法

#### 示例

（此部分未完整提供示例）