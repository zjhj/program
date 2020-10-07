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

### __new__与__init__
1. __new__至少要有一个参数cls，代表当前类，此参数在实例化时由Python解释器自动识别。
2. __new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，可以return父类（通过super(当前类名, cls)）__new__出来的实例，或者直接是object的__new__出来的实例。
3. __init__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化的动作，__init__不需要返回值。
4. 如果__new__创建的是当前类的实例，会自动调用__init__函数，通过return语句里面调用的__new__函数的第一个参数是cls来保证是当前类实例，如果是其他类的类名，；那么实际创建返回的就是其他类的实例，其实就不会调用当前类的__init__函数，也不会调用其他类的__init__函数。

### 列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数
[ i for i in map( lambda x:x*x, [1,2,3,4,5] ) if i>10 ]

### 生成5个随机小数
import numpy as np
np.random.randn(5)

### <div class="nam">中国</div>，用正则匹配出标签里面的内容（“中国”），其中class的类名是不确定的
`(.*?)`可用于提取文本
```python
import re
str = '<div class="nam">中国</div>'
res = re.findall( r'<div class=".*">(.*?)</div>',str )
```

### 可变、不可变类型及原理
- 不可变数据类型：数值型、字符串型string和元组tuple   
不允许变量的值发生变化，如果改变了变量的值，相当于是新建了一个对象，而对于相同的值的对象，在内存中则只有一个对象（一个地址），如下图用id()方法可以打印对象的id
- 可变数据类型：列表list和字典dict   
允许变量的值发生变化，即如果对变量进行append、+=等这种操作后，只是改变了变量的值，而不会新建一个对象，变量引用的对象的地址也不会变化，不过对于相同的值的不同对象，在内存中则会存在不同的对象，即每个对象都有自己的地址，相当于内存中对于同值的对象保存了多份，这里不存在引用计数，是实实在在的对象。

### [[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
`[ j for i in a for j in i ]`

### try except else finally
try..except..else没有捕获到异常，执行else语句
try..except..finally不管是否捕获到异常，都执行finally语句

### [i for i in range(3)]改成生成器
1. [] 改为 ()，即变成生成器
2. 返回值的时候使用yield
