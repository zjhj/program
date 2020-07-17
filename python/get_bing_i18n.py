#!/usr/bin/python3
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup

import requests

base_url = 'https://cn.bing.com'
r = requests.get( base_url )
if r.status_code == 200:
	b = BeautifulSoup( r.text, 'lxml' )
	image_url = b.find_all( name='div',attrs={'class':'img_cont'} )[0].attrs['style']
	image_url = base_url + image_url[image_url.index('url')+4:image_url.index('1080')+8]

	image_name = b.find_all( attrs={'class':'title'} )[0].text

	r = requests.get( image_url )
	print( r.raw.getheaders()['Content-Type'] )
	with open(image_name+'.jpg','wb') as fp:
		fp.write( r.content )
