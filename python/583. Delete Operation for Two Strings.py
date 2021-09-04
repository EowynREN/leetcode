#-*- coding:utf8 -*-
#coding=utf-8

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        #最后这两个字符串的删除结果就是它俩的最长公共子序列

        # The final result of after deleting add chars in either string is
        # the longest common subsequence of these two strings(LCS)
        # so the solution refers to LCS

        n, m = len(word1), len(word2)
        dp = [[0 for j in range(m + 1)] for i in range(n + 1)]

        # base case: text1 to "", LCS is 0
        #            "" to text2, LCS is 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        LCS = dp[n][m]
        return n - LCS + m - LCS
