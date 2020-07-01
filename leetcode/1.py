#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
brute force

1. start from the pointer points to the 1st element
2. compare the summary of the element pointed and the elements behind it
3. if not found, pointer moves forward, repeat 2 until reach last element
"""

class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums, target):
        for loc1,i in enumerate(nums):
            for loc2,j in enumerate(nums[loc1+1:]):
                if i+j == target:
                    return [loc1,loc1+1+loc2]
        return []

a = Solution()
print( a.twoSum( [2, 7, 11, 15],9 ) )
print( a.twoSum( [3, 2, 4],6 ) )
