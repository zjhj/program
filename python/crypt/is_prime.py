#!/usr/bin/python3
# -*- coding:utf-8 -*-

import sys
import math

def is_prime_sqrt( num ):
	if num%2 == 0:
		return False
	for i in range(3,int(math.sqrt(num))+2,2):
		# print( i )
		if num%i == 0:
			return False
	return True

def do_main():
	try:
		if len(sys.argv)<2:
			raise Exception( "Please input the number!" )

		curr_judge = 'is not'
		if is_prime_sqrt( int(sys.argv[1]) ):
			curr_judge = 'is'
			
		print( "{0} {1} a prime number.".format(sys.argv[1],curr_judge) )

	except Exception as ex:
		print( ex )

if __name__ == '__main__':
    do_main()
