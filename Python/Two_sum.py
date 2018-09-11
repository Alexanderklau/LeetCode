# coding: utf-8

__author__ = 'lau.wenbo'

"""
题目：
Given an array of integers, 
return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

举例：
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

"""
解题思路：
传入一个列表和数字，数字等于列表中某两项的和，需要你输出两个量的下标，比较简单。
"""

class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i


a = Solution()
c = a.twoSum(nums=[2, 7, 11, 15], target=18)
print(c)
