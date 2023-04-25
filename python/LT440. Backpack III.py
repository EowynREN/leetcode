#-*- coding:utf8 -*-
#coding=utf-8
# Solution 1: 完全按照题目要求一步一步做下来,会超时
class Solution:
    """
    @param: A: an integer array
    @param: V: an integer array
    @param: m: An integer
    @return: an array
    """
    def backPackIII(self, A, V, m):
        # write your code here
        if not A or not V:
            return 0

        # dp[i][j]: 在i容量时装A的前j种item的最大价值
        # dp[i][j] = max(dp[i][j - 1], dp[i - k * A[j]][j - 1] + V[j])
        n = len(A)
        dp = [[0 for j in xrange(n + 1)] for i in xrange(m + 1)]

        # 容量为0时，什么也放不下
        for i in xrange(n + 1):
            dp[0][i] = 0

        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):

                # 不放
                dp[i][j] = dp[i][j - 1]

                # k * A[j] <= i
                # 放，那么放几个
                for k in xrange(1, i / A[j - 1] + 1):
                    dp[i][j] = max(dp[i][j], dp[i - k * A[j - 1]][j - 1] + k * V[j - 1])
        return dp[m][n]


class Solution2:

    def backPackIII(self, A, V, m):
        # write your code here
        if not A or not V:
            return 0

        # dp[i][j]: 在i容量时装A的前j种item的最大价值
        # dp[i][j] = max(dp[i][j - 1], dp[i - k * A[j]][j - 1] + V[j])
        n = len(A)
        dp = [[0 for j in xrange(n + 1)] for i in xrange(m + 1)]

        # 容量为0时，什么也放不下
        for i in xrange(n + 1):
            dp[0][i] = 0

        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):

                # 不放
                dp[i][j] = dp[i][j - 1]

                # 放，直接在dp[i - A[j - 1]][j]叠加即可
                # dp[i - A[j - 1]][j]表示在容量为i - A[j - 1]放到第j个item是的最大值，直接在第j个item上累积就可以达到无限取个数的目的
                if i - A[j - 1] >= 0:
                    dp[i][j] = max(dp[i][j], dp[i - A[j - 1]][j] + V[j - 1])
        return dp[m][n]

s = Solution()
print s.backPackIII([2,3,5,7], [1,5,2,4], 10)