# coding: utf-8
__author__ = 'lau.wenbo'


class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        transformations = set()
        encoding = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for word in words:
          string = ""
          for char in word:
            string += encoding[ord(char) - 97]
          transformations.add(string)
        return len(transformations)

a = Solution()
print(a.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
