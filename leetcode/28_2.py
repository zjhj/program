#!/usr/bin/python3
# -*- coding:utf-8 -*-
# strstr，暴力法-again
class Solution:
	def strStr(self, haystack, needle):
		needle_len = len(needle)
		if needle_len == 0:
			return 0

		haystack_len = len( haystack )
		if needle_len > haystack_len:
			return -1

		for i in range( len(haystack)-len(needle)+1 ):
			if haystack[i:i+len(needle)] == needle:
				return i

		return -1

a = Solution()
print( a.strStr('Hello','ll') )
print( a.strStr('mississippi','issipi') )
