---
author: xiaohe
date: 2018/2/25
---

> # datetime

[代码参考](https://github.com/michaelliao/learn-python3/blob/master/samples/commonlib/use_datetime.py)

```python
    datetime.now()
    datetime.fromtimestamp()
    dt.timestamp()
    timedelta
```

> # collections

[代码参考](https://github.com/michaelliao/learn-python3/blob/master/samples/commonlib/use_collections.py)

### 1. namedtuple

```
    namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，
并可以用属性而不是索引来引用tuple的某个元素。
```

### 2. deque

```
    使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
```
### 3. defaultdict

```
    使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict.
```

### 4. OrderedDict

```
    使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
    如果要保持Key的顺序，可以用OrderedDict：
```

### 5. Counter

```
    Counter是一个简单的计数器，例如，统计字符出现的个数.
```

># base64

[代码参考](https://github.com/michaelliao/learn-python3/blob/master/samples/commonlib/do_base64.py)
```
    Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。
```

># struct

```
```

># hashlib
```
```

># hmac

># itertools

># contextlib

># urllib

># XML

># HTMLParser






















