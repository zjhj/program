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
