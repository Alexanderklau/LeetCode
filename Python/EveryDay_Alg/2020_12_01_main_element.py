# coding: utf-8

__author__ = "lau.wenbo"

"""
数组中占比超过一半的元素称之为主要元素。给定一个整数数组，找到它的主要元素。若没有，返回-1。

示例 1：
输入：[1,2,5,9,5,9,5,5,5]
输出：5

示例 2：
输入：[3,2]
输出：-1

涉及到了摩尔投票法
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 遍历去重的nums列表
        for i in set(nums):
            # 如果出现的数量 大于 总数的二分之一
            if nums.count(i) > len(nums) / 2:
                return i
        return -1



if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([1,2,5,9,5,9,5,5,5]))
