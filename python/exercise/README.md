## 一些练习

### 一行代码实现1--100之和
```python
from functools import reduce
reduce( lambda x,y:x+y, range(1,101) )
```

### 函数内部修改全局变量
使用global关键字：
```python
>>> def hello():
...     global a
...     a = 4
... 
>>> a
5050
>>> hello()
>>> a
4
```

### 字典的合并与删除
```python
>>> a = {'a':1}
>>> b = {'b':2}
>>> a.update(b)
>>> a
{'a': 1, 'b': 2}
>>> del a['b']
>>> a
{'a': 1}
>>> 
```

### range在python2、3的区别
python2
```
>>> type( range(100) )
<type 'list'>
```
python3
```
>>> type( range(100) )
<class 'range'>
```

### 变参
函数传参使用*、**，分别对应tuple和dict结构。
