#!/usr/bin/python3
#  -*- coding:utf-8 -*-

# p=61,q=53,n=3233
# 3120 17

import sys

def ex_gcd( a,b ):
	if b == 0:
		return (1,0,a)

	(x,y,d) = ex_gcd( b,a%b )
	# print( "x:{0}, y:{1}, d:{2}".format( x,y,d ) )
	x,y = y,x-int(a/b)*y
	return (x,y,d)

def do_main():
	try:
		if len(sys.argv) < 3:
			raise Exception( "Wrong parameters!" )

		a = int(sys.argv[1])
		b = int(sys.argv[2])
		(x0,y0,d) = ex_gcd( a,b )

		curr_factor = 0
		if x0<0:
			curr_factor = -x0//b + 1

		x0 = x0 + b*curr_factor
		y0 = y0 - a*curr_factor

		solve_num = 10
		if len(sys.argv) == 4:
			solve_num = int(sys.argv[3])

		for i in range(solve_num):
			print( "x:{:<10d}, y:{:<10d}".format( x0+i*b,y0-i*a ) )

	except Exception as ex:
		print( ex )

if __name__ == '__main__':
	do_main()
