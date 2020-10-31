#!/usr/bin/python3
# -*- coding:utf-8 -*-

class Solution:
	def findMedianSortedArrays( self, nums1, nums2 ):
		# return biSearch( (len(nums1)+len(nums2))//2,nums1,nums2 )

		wantLoc = ( len(nums1)+len(nums2)-1 ) // 2
		i = j = currLoc = 0
		while True:
			currLoc = ( wantLoc -currLoc ) // 2
			if currLoc == 0:
				break

			if len(nums1)-currLoc-i>=0 and len(nums2)-currLoc-j>=0:
				if nums1[i+currLoc] < nums2[j+currLoc]:
					i += currLoc
				else:
					j += currLoc
			else:
				break


a = Solution()
print( a.findMedianSortedArrays( [1,2],[3,4] ) )
print( a.findMedianSortedArrays( [1,3],[2] ) )
print( a.findMedianSortedArrays( [1,1],[1,2] ) )
print( a.findMedianSortedArrays( [1,2],[1,2] ) )
