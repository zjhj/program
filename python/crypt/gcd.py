#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def euclid( a,b ):
	"""
	if b == 0:
		return a
	else:
		return euclid(b,a%b)
	"""

	return a if b==0 else euclid(b,a%b)

def euclid1( a,b ):
	while b != 0:
		# print( "{0},{1}".format(a,b) )
		a,b = b,a%b
	
	return a

def do_main():
	try:
		if len(sys.argv) < 3:
			raise Exception( "wrong parameters!" )

		print( "The gcd of {0} and {1} is: {2} (euclid,recursive)".format( sys.argv[1],sys.argv[2],euclid( int(sys.argv[1]),int(sys.argv[2]) ) ) )
		print( "The gcd of {0} and {1} is: {2} (euclid)".format( sys.argv[1],sys.argv[2],euclid1( int(sys.argv[1]),int(sys.argv[2]) ) ) )

	except Exception as ex:
		print( ex )

if __name__ == '__main__':
	do_main()
