#!/usr/bin/python3
# -*- coding:utf-8 -*-
import random

file_convert = { 10:'10', 100:'100', 1000:'1k', 10000:'10k', 100000:'100k', 1000000:'1m' }
file_prefix = 'need_sort_'

for curr_num in file_convert:
	curr_file = file_prefix + file_convert[curr_num]
	with open( curr_file, 'w' ) as fp:
		for i in range( curr_num ):
			num = random.randint( -curr_num*3,curr_num*3 )
			fp.write( str(num)+'\n' )
