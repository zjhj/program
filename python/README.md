## python的使用记录

### WEB类
#### requests
requests+beautifulsoup抓bing的背景图
```python
#!/usr/bin/python3
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup

import requests

base_url = 'https://cn.bing.com'
r = requests.get( base_url )
if r.status_code == 200:
	b = BeautifulSoup( r.text, 'lxml' )
	image_url =  b('div')[1].findChildren()[0].get('data-ultra-definition-src')
	image_name = b('div')[49].findChildren()[13].get('title').split()[0]

	r = requests.get( base_url + image_url )
	print( r.raw.getheaders()['Content-Type'] )
	with open(image_name+'.jpg','wb') as fp:
		fp.write( r.content )
```
部分方法和属性：
```
>>> cs = {'token': '12345', 'status': 'working'}
>>> r = requests.get( 'https://cn.bing.com', headers={'User-Agent': 'Mozilla/5.0 AppleWebKit'}, params={'a':'1','b':'2'}, cookies=cs, timeout=2 )
>>> r.url
'https://cn.bing.com/?a=1&b=2'
>>> r.encoding
'utf-8'
>>> r.headers  # 获取响应头，dict类型
>>> r.content  # 获取响应内容的bytes对象
>>> r.json()   # 响应内容为json数据，可直接解析
>>> r = requests.post( 'https://cn.bing.com', data={'a':'1','b':'2'} )
>>> r = requests.post(url, json=params)  # params为dict，内部自动序列化为JSON?

#文件上传
>>> upload_files = {'file': open('report.xls', 'rb')}
>>> r = requests.post(url, files=upload_files)
```

#### curl

### 网络类
#### scapy
#### pwn

### 图形类
#### PIL

### 数据类
#### numpy
numpy求解方程组代码，二元一次方程组及求解代码示例如下：
```
x + 2y = 3
4x + 5y = 6

import numpy as np
A = np.mat('1,2; 4,5')
b = np.mat('3,6').T
r = np.linalg.solve(A,b)
print( r )
```

#### pandas

### 类型转换
#### binascii
