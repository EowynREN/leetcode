#-*- coding:utf8 -*-
#coding=utf-8
class Solution(object):
    # 这道题跟44. Wildcard Matching很像，只是一些细节上的处理不太一样
    #
    # 题目中要求：
    #     '.' Matches any single character.
    #     '*' Matches zero or more of the preceding element.
    #
    # Init: s = ""时，p和s的是否可以匹配
    #
    # 对于'.'时， 因为只通配一个字符，因此
    #   if s[i] == p[j] or p[j] == '.' :
    #         dp[i][j] = dp[i- 1][j- 1]]
    #
    # 对于'*'处理时，题目中的要求是可以match0个或者多个preceding element。对于0个preceding element就是dp[i][j] = dp[i][j- 2]，例如s = ""ac"", p = ""acf*""，那么对于p中的f就是match了0次。因此对于'*'的处理分两种情况就可以了：match 了0次， 和match里至少一次
    #
    #     dp[i][j] = dp[i][j - 2]  # 0次
    #
    #     # 至少一次
    #     if s[i - 1] == p[j - 2] or p[j - 2] == '.':
    #             dp[i][j] |= dp[i - 1][j]

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n, m = len(s), len(p)
        dp = [[False for j in xrange(m + 1)] for i in xrange(n + 1)]
        dp[0][0] = True

        for j in xrange(2, m + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in xrange(1, n + 1):
            for j in xrange(1, m + 1):
                if p[j - 1] == '*':
                    if j == 1:
                        continue
                    dp[i][j] = dp[i][j - 2]

                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                        dp[i][j] |= dp[i - 1][j]
                else:
                    if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                        dp[i][j] = dp[i - 1][j - 1]
        return dp[n][m]

s = Solution()
print s.isMatch("a", ".*..a*")