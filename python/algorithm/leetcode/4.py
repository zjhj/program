#!/usr/bin/python3
# -*- coding:utf-8 -*-

class Solution:
	def findMedianSortedArrays(self, nums1, nums2):
		i = j = cnt = 0

		curr_num  = last_num = -1
		total_len = len(nums1) + len(nums2)
		is_odd = False if total_len%2==0 else True

		while i<len(nums1) and j<len(nums2):
			if nums1[i] < nums2[j]:
				curr_num = nums1[i]
				i += 1
			else:
				curr_num = nums2[j]
				j += 1
			cnt += 1

			if is_odd and cnt == total_len//2+1:
				return curr_num
			if not is_odd and cnt == total_len//2+1:
				return (last_num+curr_num)/2

			last_num = curr_num

		if i<len(nums1):
			for k in range( i,len(nums1) ):
				curr_num = nums1[k]
				cnt += 1
				if is_odd and cnt == total_len//2+1:
					return curr_num
				if not is_odd and cnt == total_len//2+1:
					return (last_num+curr_num)/2
				last_num = curr_num

		if j<len(nums2):
			for k in range( j,len(nums2) ):
				curr_num = nums2[k]
				cnt += 1
				if is_odd and cnt == total_len//2+1:
					return curr_num
				if not is_odd and cnt == total_len//2+1:
					return (last_num+curr_num)/2
				last_num = curr_num

a = Solution()
print( a.findMedianSortedArrays( [1,2],[3,4] ) )
print( a.findMedianSortedArrays( [1,3],[2] ) )
print( a.findMedianSortedArrays( [1,1],[1,2] ) )
print( a.findMedianSortedArrays( [1,2],[1,2] ) )
