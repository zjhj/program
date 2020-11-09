## Note for Fluent Python

### 第一节
- %r可用于获取对象各个属性的标准字符串表示形式
- __repr__ 和 __str__ 的区别在于，后者是在 str() 函数被使用，或是在用 print 函数打印一个对象的时候才被调用的，并且它返回的字符串对终端用户更友好。
- bool(x)默认总返回True，除非类对 __bool__ 或者 __len__ 函数有自己的实现，如果不存在 __bool__ 方法，那么 bool(x) 会尝试调用 x.__len__()。若返回 0，则 bool 会返回 False；否则返回True。
- 特殊方法一览表：https://docs.python.org/3/reference/datamodel.html。
- python3中reload可以通过`from importlib import reload`后使用。（the imp module is deprecated in favour of importlib）
- 延申：https://docs.python.org/3/reference/datamodel.html。

### 第二节
- *运算符可用于将可迭代对象拆开，作为函数的参数，比如： 
```python
>>> x = (16,4)
>>> divmod(*x)
(4, 0)
```
