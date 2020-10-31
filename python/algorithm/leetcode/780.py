#!/usr/bin/python3
# -*- coding:utf-8 -*-

class Solution:
	def reachingPoints(self, sx, sy, tx, ty):
		nodeList = list()
		nodeList.append( (sx,sy) )

		p = 0
		while p<len(nodeList):
			(a,b) = nodeList[p]
			p += 1
			# print( "({},{})".format(a,b) )

			if a>tx or b>ty:
				continue

			if (a+b,b) == (tx,ty) or (a,b+a) == (tx,ty):
				return True

			nodeList.append( (a+b,b) )
			nodeList.append( (a,b+a) )

		return False

a = Solution()
# print( a.reachingPoints(1,1,3,5) )
# print( a.reachingPoints(1,1,2,2) )
# print( a.reachingPoints(35,13,455955547,420098884) )
print( a.reachingPoints(1,1,1000000000,1) )
