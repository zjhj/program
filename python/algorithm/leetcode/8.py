#!/usr/bin/python3
# -*- coding:utf-8 -*-

class Solution:
	def myAtoi( self,str ):
		res_data = list()
		for i in str:
			if 33<=ord(i)<=126 or len(res_data)>0:
				res_data.append( i )

			print( res_data,ord(res_data[0]),len(res_data) )

			if len(res_data) == 1:
				if res_data[0] != '-' and res_data[0] != '+' and ( ord(res_data[0])>57 or ord(res_data[0])<48 ):
					return 0
				else:
					continue

			if len(res_data) > 0:
				if ord(i)<48 or ord(i)>57:
					print( "---",res_data )
					if len(res_data) == 1 and ( res_data[0] == '-' or res_data[0] == '+' ):
						return 0
					else:
						res_data.pop(-1)
						break

		if len(res_data) == 0 or ( len(res_data)==1 and ( res_data[0]=='-' or res_data[0]=='+' ) ):
			return 0
	
		else:
			currNum = int( ''.join(res_data) )
			if currNum < -2**31:
				return -2**31
			elif currNum > 2**31-1:
				return 2**31-1
			else:
				return currNum
		
a = Solution()
# print( a.myAtoi('42') )
# print( a.myAtoi('4193 with words') )
# print( a.myAtoi('words and 987') )
# print( a.myAtoi('-91283472332') )
# print( a.myAtoi('3.14159') )
# print( a.myAtoi('-') )
print( a.myAtoi('+') )
