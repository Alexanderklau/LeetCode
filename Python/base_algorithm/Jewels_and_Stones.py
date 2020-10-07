# coding: utf-8
__author__ = 'lau.wenbo'

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        s = 0
        for i in J:
            for z in S:
                if i == z:
                    s += 1

        return s


a = Solution()
J = "aA"
S = "aAAbbbb"
k = a.numJewelsInStones(J=J, S=S)
print(k)
