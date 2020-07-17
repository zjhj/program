# 基本语法
## list/dict/...
两个list合并为一个dict的方法：
```python
>>> a = ['a','b']
>>> b = [1,2]
>>> dict( zip(a,b) )
{'a': 1, 'b': 2}
```
dict合并可以使用`dict.update`

## int & bytes 转换
```
num = 6957464
fp.write( num.to_bytes(4,'little',signed=True) )   # mode='wb', b'\x98)j\x00'
b= '98296a00'
int.from_bytes( bytes.fromhex(b),'little' )
# int.from_bytes( b'\x98)j\x00','little' )
```

# 网络相关
## requests
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

## curl
设置文件上传：
```
c.setopt( pycurl.HTTPPOST, [('file',(pycurl.FORM_FILE,'11.php', pycurl.FORM_FILENAME, '11.php'))])
```
设置POST方法：`c.setopt( pycurl.POST, True )`
设置head方法：`c.setopt( c.NOBODY, True )`

## scapy
模拟syn flood攻击：
```
from scapy.all import *
pkt = IP(dst='121.40.205.55',src='218.2.135.1')/TCP(dport=22,flags="S")
send(pkt)
```
解析pcap，下面是一个从easycap.pcap中抓取flag的示例：
```python
#!/usr/bin/python3
# -*- coding:utf-8 -*-

from scapy.all import *

import sys

packets = rdpcap( sys.argv[1] )

data = b''
for curr_packet in packets:
	if hasattr( curr_packet,'load' ):
		data += curr_packet.load

print( data )
```
packets可以通过layers方法查看报文中数据层级，通过iterpayloads方法可以把每一层级的数据遍历出来。

# 内容解析
## BeautifulSoup
```
r = requests.get( base_url )
from bs4 import BeautifulSoup
b = BeautifulSoup( r.text, 'lxml' )
b.find_all( name='div',attrs={'class':'title'} )
```

# Hacker
## pwn

# 图形处理
## PIL

# AI相关

## numpy
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

## pandas
