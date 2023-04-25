#-*- coding:utf8 -*-
#coding=utf-8
import sys


class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """

        # dp[j]，代表着如果我们在区间 [i , j] 内进行查找，所需要的最少 cost 来保证找到结果

        # 如果以 top-down recursion 的方式分析这个问题，可以发现对于区间 [i, j] ，我们的猜测 i <= k <= j 我们可能出现以下三种结果：
        #    1. k 就是答案，此时子问题的额外 cost = 0 ，当前位置总 cost  = k + 0;
        #    2. k 过大，此时我们的有效区间缩小为 [i , k - 1] 当前操作总 cost  = k + dp[k - 1];
        #    3. k 过小，此时我们的有效区间缩小为 [k + 1 , j] 当前操作总 cost  = k + dp[k + 1][j];

        dp = [[0 for j in xrange(n + 1)] for i in xrange(n + 1)]

        # 如果只有一个数字，那么不用猜，cost为0
        for i in xrange(n + 1):
            dp[i][i] = 0

        for i in xrange(n - 1, 0, -1):
            for j in xrange(i + 1, n + 1):
                min_cost = sys.maxint
                for k in xrange(i, j):
                    min_cost = min(min_cost, k + max(dp[i][k - 1], dp[k + 1][j]))
                dp[i][j] = min_cost
        return dp[1][n]


s = Solution()
print s.getMoneyAmount(4)