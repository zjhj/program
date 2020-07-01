#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
1. sort the list
2. set two bounds -- bound_min and bound_max
3. scan for the summary from the last element to the firest element, if the last element is bigger than the minus result of target and the first element, bound_max-1, repeat until the result is equal or less than
4. if the result is equal, return the result, need to deal with the situation exist same elements
5. if the result is less than, bound_min+1, repeat 3
"""

class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums, target):
        sorted_nums = sorted( nums )

        bound_min = 0
        bound_max = len(nums)-1

        while bound_min<bound_max:
            while target-sorted_nums[bound_max]<=sorted_nums[bound_min] and bound_min<bound_max:
                if target-sorted_nums[bound_max] == sorted_nums[bound_min]:
					# for same elements exist
                    if sorted_nums[bound_min] == sorted_nums[bound_max]:
                        return sorted( [nums.index(sorted_nums[bound_min]),nums[nums.index(sorted_nums[bound_min])+1:].index(sorted_nums[bound_min])+nums.index(sorted_nums[bound_min])+1] )
                    else:
                        return sorted( [nums.index(sorted_nums[bound_min]),nums.index(sorted_nums[bound_max])] )
                bound_max -= 1

            bound_min += 1

        return []

a = Solution()
print( a.twoSum( [2, 7, 11, 15],9 ) )
print( a.twoSum( [3, 2, 4],6 ) )
print( a.twoSum( [3, 3],6 ) )
