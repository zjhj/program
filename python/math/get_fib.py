#!/usr/bin/python3
# -*- coding:utf-8 -*-

import sys
import time
import traceback

def p_time( func ):
	# def wrapper( *args,**kwargs ):
	def wrapper( *args,**kwargs ):
		start_time = time.time()
		res = func( *args,**kwargs )
		end_time = time.time()
		print( "Time elpased: {0}".format(end_time-start_time) )
		return res
	return wrapper

@p_time
def fib_recursive( n ):
	if n<2:
		return 1
	return fib_recursive(n-1)+fib_recursive(n-2)

@p_time
def fib( n ):
	f0 = 0
	f1 = 1
	for i in range(n):
		f1,f0 = f1+f0,f1
	return f1

def do_main():
	try:
		if len(sys.argv)<2:
			raise Exception( "Wrong parameters!" )

		print( fib_recursive(int(sys.argv[1])) )
		print( fib(int(sys.argv[1])) )

	except Exception as ex:
		print( ex )
		traceback.print_exc()

if __name__ == '__main__':
	do_main()
