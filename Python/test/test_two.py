# coding: utf-8
__author__ = 'lau.wenbo'


class Solution(object):
    def twoSum(self, nums, target):
        strs = {}
        for i in range(len(nums)):
            print(i)
            if nums[i] in strs:
                return [strs[nums[i]], i]
            else:
                print(target, nums[i ])
                strs[target - nums[i]] = i
        # if len(nums) <= 1:
        #     return False
        # buff_dict = {}
        # for i in range(len(nums)):
        #     if nums[i] in buff_dict:
        #         return [buff_dict[nums[i]], i]
        #     else:
        #         buff_dict[target - nums[i]] = i


a = Solution()
c = a.twoSum(nums=[2, 7, 11, 15], target=22)
print(c)