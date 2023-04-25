#-*- coding:utf8 -*-
#coding=utf-8
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n, m = len(t), len(s)
        dp = [[0 for j in xrange(m + 1)] for i in xrange(n + 1)]

        for j in xrange(m + 1):
            dp[0][j] = 1

        for i in xrange(1, n + 1):
            dp[i][0] = 0

        for i in xrange(1, n + 1):
            for j in xrange(1, m + 1):
                # 如果s前j的最后一个，与t前i的最后一个，不相等
                # 那么s[:j]所包含的t[:i]，就等于s[:j - 1]所包含的t[:i]的个数
                # 因为最后一位不一样，所以不会产生新的disct seq
                dp[i][j] = dp[i][j - 1]

                if s[j - 1] == t[i - 1]:
                    # 最后一位一样，那么s[:j - 1]所包含的t[:i - 1]里的disct seq再匹配上相同的最后一位
                    # 就会产生新的disct seq
                    dp[i][j] += dp[i - 1][j - 1]
        return dp[n][m]

s = Solution()
print s.numDistinct("b", "a")
