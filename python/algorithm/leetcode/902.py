#!/usr/bin/python3
# -*- coding:utf-8 -*-

class Solution(object):
	def atMostNGivenDigitSet(self, D, N):
		lenOfN = len( str(N) )

		n1 = 0
		for i in range( 1,lenOfN ):
			n1 += pow( len(D),i )

		# print( "n1=",n1 )

		offset = 0
		while offset<lenOfN:
			print( "offset={}".format(offset) )
			n2 = 0
			for i in D:
				if i>str(N)[offset]:
					break
				elif i == str(N)[offset]:
					n2 += 1
					if i == str(N)[offset]:
						if offset == lenOfN-1:
							n1 += 1
						break
				else:
					n1 += pow( len(D),lenOfN-offset-1 )
			if n2 == 0:
				break
			offset += 1

		return n1

a = Solution()
print( a.atMostNGivenDigitSet( ["3","4","8"],4 ) )
print( a.atMostNGivenDigitSet( ["1","3","5","7"], 100 ) )
print( a.atMostNGivenDigitSet( ["5","6"], 19 ) )
print( a.atMostNGivenDigitSet( ["5","7","8"],59 ) )
print( a.atMostNGivenDigitSet( ["1"],834 ) )
