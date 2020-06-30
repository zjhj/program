#!/usr/bin/python3
# -*- coding:utf-8 -*-

class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums, target):
        nums_d = dict()
        for k,v in enumerate(nums):
            if v not in nums_d:
                nums_d[v] = list()
            nums_d[v].append(k)

        for k,v in nums_d.items():
            if target-k in nums_d:
                if target == k*2:
                    if len(nums_d[k]) == 1:
                        continue
                    else:
                        return nums_d[k][:2]
                else:
                    return sorted( [nums_d[k][0],nums_d[target-k][0]] )
        return []

a = Solution()
print( a.twoSum( [2, 7, 11, 15],9 ) )
print( a.twoSum( [3, 2, 4],6 ) )
print( a.twoSum( [3, 3],6 ) )
