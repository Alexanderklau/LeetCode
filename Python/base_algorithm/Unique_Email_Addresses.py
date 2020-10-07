# coding: utf-8
__author__ = 'lau.wenbo'


class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        memo = set()
        for email in emails:
            loc, dom = email.split("@")
            if "+" in loc:
                loc = loc[:loc.index("+")]
            loc = "".join(loc.split("."))
            print(loc+dom)
            memo.add(loc+dom)
        return len(memo)


a = Solution()
a.numUniqueEmails(emails=["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])