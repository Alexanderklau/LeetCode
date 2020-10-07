# coding: utf-8
__author__ = 'lau.wenbo'

"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

"""
给定两个非空链表来表示两个非负整数。
位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。
你可以假设除了数字 0 之外，这两个数字都不会以零开头
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 表示进位
        res = None
        res_end = None
        temp = 0
        while l1 is not None or l2 is not None or temp ==1:
            if l1 is not None:
                temp +=l1.val
                l1 = l1.next
            if l2 is not None:
                temp += l2.val
                l2= l2.next
            if res is None:
                res = ListNode(temp%10)
                res_end = res
            else:
                res_end.next = ListNode(temp%10)
                res_end = res_end.next
            temp = temp//10
        return res