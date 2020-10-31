#!/usr/bin/python3
# -*- coding:utf-8 -*-

import sys
import math
import traceback

sys.setrecursionlimit(20000)

def newton_recusive( a,b=1 ):
	return b if math.fabs(b*b-a)<1e-20 else newton( a,(b+a/b)/2 )

def newton( a ):
	b = a
	while b*b-a>1e-30:
		b = ( b+a/b )/2
	return b

def do_main():
	try:
		if len(sys.argv)<2:
			raise Exception( "Please input number!" )

		# print( newton( int(sys.argv[1]),int(sys.argv[1]) ) )
		print( newton( int(sys.argv[1]) ) )
	except Exception as ex:
		print( ex )
		traceback.print_exc()


if __name__ == '__main__':
	do_main()
