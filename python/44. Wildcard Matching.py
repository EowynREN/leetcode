#-*- coding:utf8 -*-
#coding=utf-8
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # string类的dp，几乎都是dp[i][j]表示s的前i个字符和p的前j个字符***(可达到的情况)
        #
        # 题目中要求：
        #     '?' Matches any single character.
        #     '*' Matches any sequence of characters (including the empty sequence).
        #
        # 这里dp[i][j]表示s的前i个字符和p的前j个字符是否可以匹配
        #
        # init: s  = '' 时，p和s的是否可以匹配
        #
        # 对于'?'很好处理，因为通配一个字符，因此
        #         if s[i] == p[j] or p[j] == '?':
        #             dp[i][j] = dp[i- 1][j- 1]
        #
        # 对于'*'的处理，稍微复杂一些，'*'即可以mantch空串(就是一个都不匹配)，也可以match一个多个，也可以match一个，因此
        # dp[i][j] = dp[i][j - 1] or dp[i - 1][j] or dp[i - 1][j - 1]

        n, m = len(s), len(p)

        # dp[i][j]表示s的前i个字符和p的前j个字符是否可以匹配
        dp = [[False for j in xrange(m + 1)] for i in xrange(n + 1)]
        dp[0][0] = True  # 空串对空串

        # init: '*' Matches any sequence of characters (including the empty sequence)
        # 表示s = ""时，p和s的是否可以匹配
        for j in xrange(1, m + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        for i in xrange(1, n + 1):
            for j in xrange(1, m + 1):
                if p[j - 1] == '*':
                    #           '*'匹配了0个      匹配了多个        匹配了1个
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j] or dp[i - 1][j - 1]
                else:
                    if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                        dp[i][j] = dp[i - 1][j - 1]
        return dp[n][m]
s = Solution()
print s.isMatch("aab", "c*a*b")