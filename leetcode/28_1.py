#!/usr/bin/python3
# -*- coding:utf-8 -*-
# strstr，暴力法
class Solution:
	def strStr(self, haystack, needle):
		if len(needle) == 0:
			return 0

		if len(needle) > len(haystack):
			return -1

		m = 0
		for i in range( len(haystack)-len(needle)+1 ):
			for j in range( len(needle) ):
				if haystack[i+j] == needle[j]:
					m += 1
				else:
					m = 0
					break
			if m == len(needle):
				return i

		return -1

a = Solution()
print( a.strStr('Hello','ll') )
print( a.strStr('mississippi','issipi') )
