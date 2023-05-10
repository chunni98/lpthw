## 类型注解

### 变量注解

例：

```python
a: int = 3
b: float = 3.14
c: str = 'abc'
d: bool = False
```

### 函数注解

```python
def add(first: int = 10, second: float = 5.5) -> float:
    return first + second

def bar() -> None:
    pass
```

### 容器类型

列表、字典、元组等包含元素的复合类型，用简单的 list，dict，tuple 不能够明确说明内部元素的具体类型。

因此要用到 typing 模块提供的复合注解功能：

```python
from typing import List, Dict, Tuple

# 参数1: 元素为 int 的列表
# 参数2: 键为字符串，值为 int 的字典
# 返回值: 包含两个元素的元组
def mix(scores: List[int], ages: Dict[str, int]) -> Tuple[int, int]:
    return (0, 0)
```

如果你用的是 Python 3.9+ 版本，甚至连 typing 模块都不需要了，内置的容器类型就支持了复合注解：

```python
def mix(scores: list[int], ages: dict[str, int]) -> tuple[int, int]:
    return (0, 0)
```

在某些情况下，不需要严格区分参数到底是列表还是元组（这种情况还蛮多的）。这时候就可以将它们的特征抽象为更泛化的类型（泛型），比如 Sequence（序列）。

下面是例子：

```python
# Python 3.8 之前的版本
from typing import Sequence as Seq1

def foo(seq: Seq1[str]):
    for item in seq:
        print(item)


# Python 3.9+ 也可以这么写
from collections.abc import Sequence as Seq2

def bar(seq: Seq2[str]):
    for item in seq:
        print(item)
```

### 类型别名

有时候对象的类型可能会非常复杂，或者你希望给类型赋予一个有意义的名称，那么你可以这样定义类型的别名：

```python
from typing import Tuple

# 类型别名
Vector2D = Tuple[int, int]

def foo(vector: Vector2D):
    print(vector)

foo(vector=(1, 2))
# Output: (1, 2)
```

## 参考

[Python类型注解，你需要知道的都在这里了][1]

[1]: https://zhuanlan.zhihu.com/p/419955374
