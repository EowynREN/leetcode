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

        # dp[i]表示s前i个字符能否由字典里的word组成改一个valid sentence
        dp = [False] * (n + 1)
        dp[0] = True  # 表示空串,一句空的话,当然是valid的

        maxLen = max([len(word) for word in wordDict])

        for i in xrange(1, n + 1):
            # 从i向左扫,最长的一个单词
            for j in xrange(1, min(i, maxLen) + 1):
                if dp[i - j] and s[i - j: i] in wordDict:
                    dp[i] = True
        return dp[n]