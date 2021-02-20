#!/usr/bin/python3
# -*- coding:utf-8 -*-
# strstr

from time import sleep

class Solution:
	def strStr(self, haystack, needle):
		needle_len = len(needle)
		if needle_len == 0:
			return 0

		haystack_len = len(haystack)
		if needle_len > haystack_len:
			return -1

		next = dict()
		for i in range(256):
			next[i] = -1
		for i in range( needle_len ):
			next[ord(needle[i])] = i

		i = 0
		while i<=haystack_len-needle_len:
			m = 0
			for j in range( needle_len ):
				# print( "***i={},j={},m={}".format(i,j,m) )
				if haystack[i+j] == needle[j]:
					m += 1
				else:
					k = 1
					if next[ord(haystack[i+j])] == -1:
						k += m
					else:
						if m>next[ord(haystack[i+j])]:
							k = m - next[ord(haystack[i+j])]
					# i += k if k>0 else 1
					i += k
					# print( "i={},k={},m={}".format(i,k,m) )
					# sleep(0.5)
					break
			if m == len(needle):
				return i

		return -1

a = Solution()
print( a.strStr('Hello','ll') )
print( a.strStr('mississippi','issipi') )
print( a.strStr('mississippi','issi') )
print( a.strStr('aabaabbbaabbbbabaaab','abaa') )
print( a.strStr('mississippi','issip') )
print( a.strStr('aabaaabaaac','aabaaac') )
print( a.strStr('babbbbbabb','bbab') )
