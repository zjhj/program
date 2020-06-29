## 1.两数之和
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
```python
#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
bruteforce to resolve
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
```
