#-*- coding:utf8 -*-
#coding=utf-8
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        if len(wordDict) == 0:
            return n == 0

        dp = [False] * (n + 1)
        dp[0] = True

        maxLen = max([len(word) for word in wordDict])

        for i in xrange(1, n + 1):
            for j in xrange(1, min(i, maxLen) + 1):
                if not dp[i - j]:
                    continue

                if s[i - j: i] in wordDict:
                    dp[i] = True
        return dp[n]
