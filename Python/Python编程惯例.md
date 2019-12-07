# Python编程惯例

* 为什么要关心Python编程惯例？因为能让你的代码更加***Pythonic***！

## 1.  让代码既能当模块被import又能直接执行

```python
if __name__ = '__main__':
```

## 2. 用下面的方式判断逻辑 "真"或"假"

```python
if x:
if not x:
```

```python
name = 'Qiangsheng He'
fruits = ['apple', 'orange']
scores = {'Jim': 88, 'Mary': 78}

# GOOD
if name and fruits and scores:
    print(True)
# NOT SO GOOD
if name != '' and fruits != [] and scores != {}:
    print(True)
```

* What's is Truth?

|                True                |               False                |
| :--------------------------------: | :--------------------------------: |
|             非空字符串             |              空字符串              |
|              非0数字               |               数字0                |
|    非空的container：len(x) > 0     |     空的container：len(x) == 0     |
|                 -                  |                None                |
|              布尔True              |             布尔False              |
| __nonzero__ (2.x) / __bool__ (3.x) | __nonzero__ (2.x) / __bool__ (3.x) |

## 3. 善用***in***运算符

```python
if x in items: # Contains
for x in items: # Iteration

title = 'Python idioms'
# GOOD
if 'd' in title:
    print('Title contains char d')
# NOT SO GOOD
if title.find('d') != -1:
    print('Title not contains char d')

names = ['Jim', 'Mary']
# GOOD
for name in names:
    print(name)
# NOT SO GOOD
i = 0
while i < len(names):
    print(names[i])
```

## 4. 不借用临时变量交换值

```python
a, b = 'Jim', 'Mary'

# GOOD
a, b = b, a
# NOT SO GOOD
temp = a
a = b
b = a
```

## 5. 用sequence构建字符串

```python
letters = ['J', 'o', 'h', 'n', 's', 'o', 'n']
# GOOD
name = ''.join(letters) # 时间复杂度O(n)
# NOT SO GOOD
name = ''
for letter in letters: # 时间复杂度O(n**2)
    name += letter
```

## 6. EAFP is preferable to LBYL

* EAFP - Easier to Ask Forgiveness than Permission.
* LBYL - Look Before You Leap.

```python
# Python中抛出异常的代价不像其他语言那么大
try: v. if ...: except:

scores = {'Jim': '87'}
# GOOD
try:
    score = int(scores['Jim'])
except (KeyError, TypeError, ValueError):
    score = None
# NOT SO GOOD
if 'Jim' in scores and isinstance(scores['Jim'], str)
    and scores['Jim'].isdigit():
    score = int(scores['Jim'])
else:
    score = None
```

## 7. 使用***enumerate***

```python
names = ['Jim', 'Mary', 'Tom']
# GOOD
for i, name in enumerate(names):
    print(i, name)
# NOT SO GOOD
i = 0
for name in names:
    print(i, name)
    i += 1
```

## 8. 用列表推导式式构建lists

```python
nums = list(range(10))
# GOOD
odd_nums = [x for x in nums if x % 2 == 1]
# NOT SO GOOD
odd_nums = []
for num in nums:
    if num % 2 == 1:
        odd_nums.append(num)
```

## 9. 通过***zip***函数组合键和值构建字典

```python
# d = dict(zip(keys, values))

students = ['Jim', 'Mary', 'Tom']
scores = [89, 34, 56]
# GOOD
student_scores = dict(zip(students, scores))
# NOT SO GOOD
student_scores = []
for i, name in enumerate(students):
    student_scores[name] = scores[i]
```

## 10. 其他

* 使用Generators（生成器） and generator expressions

* 避免使用 from module import *
好的写法: import numpy as np; import pandas as pd

* 使用 _ 作为一次性变量 e.g.:
for k, _ in [('a', 1), ('b', 2), ('c', 3)]

* dict.get() and dict.setdefault()
* collections.defaultdict

* 用 l.sort(key=key_func)进行列表排序

> **说明**：这篇文章的内容来自于网络，有兴趣的读者可以阅读[原文](http://safehammad.com/downloads/python-idioms-2014-01-16.pdf)

------

转载请标明来源

如果文章对你有所把帮助，请动动小手点个赞👍！有任何疑问和建议，可以在下面评论留言。

祝生活愉快！
