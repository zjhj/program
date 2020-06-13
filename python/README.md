## python的使用记录

### WEB类
#### request
初始化：
设置HEAD、POST数据：

#### curl

### 网络类
#### scapy
#### pwn

### 图形类
#### PIL

### 数据类
#### numpy
numpy求解方程组代码，设有二元一次方程组如下：
$$
x + 2y = 3
4x + 5y = 6
$$
```
import numpy as np
A = np.mat('1,2; 4,5')
b = np.mat('3,6').T
r = np.linalg.solve(A,b)
print( r )
```

#### pandas
