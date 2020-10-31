# [Note for Fluent Python 2015](fluent_python/)

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

## zip
python2中，zip会返回list；而python3中返回的zip对象，只能支持一次iteration。

## int & bytes 转换
```
num = 6957464
fp.write( num.to_bytes(4,'little',signed=True) )   # mode='wb', b'\x98)j\x00'
b= '98296a00'
int.from_bytes( bytes.fromhex(b),'little' )
# int.from_bytes( b'\x98)j\x00','little' )
```

# [并发相关](concurrency.md)

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
>>> r = requests.get( url,allow_redirects=True )    # 自动重定向
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

## django
如果pip或者通过其他的方式无法安装MySQLdb，可以使用pymysql代替，django主项目的__init__.py头部加一行即可：
```
import pymysql
pymysql.install_as_MySQLdb()
```

# 内容解析
## BeautifulSoup
抓bing的背景图的两个例子 [国内地址](get_bingbg.py) [国外地址](get_bing_i18n.py)
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

# 数据处理相关

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
列类型转换：`df['example'] = df['example'].astype("int64")`<br>
读取压缩文件示例：`df = pd.read_csv( gzip.open('creditcard.csv.gz') )`<br>

## tensorflow
安装完毕后导入，出现类似以下的提示：
```
>>> import tensorflow
/usr/local/lib/python3.7/dist-packages/tensorflow/python/framework/dtypes.py:516: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.
  _np_qint8 = np.dtype([("qint8", np.int8, 1)])
  /usr/local/lib/python3.7/dist-packages/tensorflow/python/framework/dtypes.py:517: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.
```
是由于numpy版本导致（过高过低都不行），换成1.16.4版本解决`pip3 install numpy==1.16.4`。

## matplotlib
设置中文，先将windows的fonts目录下的文件（这里用了雅黑）复制到/usr/share/fonts/目录下，为了便于管理，建立一个chinese目录：
```
from matplotlib.font_manager import FontProperties
chinese_font = FontProperties(fname='/usr/share/fonts/chinese/msyh.ttc' )
plt.text(0.5,0.5,'江苏', fontsize=12, fontproperties=chinese_font)
plt.show()
```
