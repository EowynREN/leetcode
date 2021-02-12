#-*- coding:utf8 -*-
#coding=utf-8
import sys

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 划分型dp
        # Maximum Subarray II这题的马甲题
        # 套用prefixSum的模板

        if not prices:
            return 0

        n = len(prices)
        left = [0] * n  # 从最左面到 i 所能获得的最大利益（单次交易）
        right = [0] * n  # 从 i 到最右面所能获得的最大利益（单次交易）

        localMin = prices[0]
        globalMax = -sys.maxint - 1
        for i in xrange(1, n):
            globalMax = max(globalMax, max(0, prices[i] - localMin))
            localMin = min(localMin, prices[i])
            left[i] = globalMax

        localMax = prices[n - 1]
        globalMax = -sys.maxint - 1
        for i in xrange(n - 2, -1, -1):
            globalMax = max(globalMax, max(0, localMax - prices[i]))
            localMax = max(localMax, prices[i])
            right[i] = globalMax

        res = 0
        for i in xrange(n - 1):
            res = max(res, left[i] + right[i + 1])

        # 不是非要做 “两次交易” 不可，因此 left[end] 作为一次交易的代表，也要考虑在内
        return max(res, left[n - 1])

# dp - 通杀版
# 交易次数 k = 2
class Solution1(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # init
        k = 2
        dp = [[[0 for n in xrange(2)] for j in xrange(k + 1)] for i in xrange(len(prices) + 1)]

        # base case
        for i in xrange(len(prices) + 1):
            dp[i][0][0] = 0
            dp[i][0][1] = -sys.maxsize - 1

        for j in xrange(k + 1):
            dp[0][j][0] = 0
            dp[0][j][1] = -sys.maxsize - 1

        for i in xrange(1, len(prices) + 1):
            for j in xrange(k, 0, -1): # [1, k]
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i - 1])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i - 1])

        return dp[len(prices)][k][0]

# dp - 简化版:压缩空间
# 给出空间更高效的优化:
# dp的状态转移,只跟相邻的状态有关,那么就不需要用数组来存储,直接改为变量更高效
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 这里 k 取值范围比较小，所以可以不用 for 循环，直接把 k = 1 和 2 的情况全部列举出来：
        # dp[i][2][0] = max(dp[i-1][2][0], dp[i-1][2][1] + prices[i])
        # dp[i][2][1] = max(dp[i-1][2][1], dp[i-1][1][0] - prices[i])
        # dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i])
        # dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0] - prices[i])
        #             = max(dp[i-1][1][1], 0 - prices[i])
        #             = max(dp[i-1][1][1], -prices[i])

        # init
        # nothing here

        # base case: 第i = 0天
        dp_i_2_0 = 0
        dp_i_2_1 = -sys.maxsize - 1
        dp_i_1_0 = 0
        dp_i_1_1 = -sys.maxsize - 1

        for i in range(len(prices)):
            dp_i_2_0 = max(dp_i_2_0, dp_i_2_1 + prices[i])
            dp_i_2_1 = max(dp_i_2_1, dp_i_1_0 - prices[i])
            dp_i_1_0 = max(dp_i_1_0, dp_i_1_1 + prices[i])
            dp_i_1_1 = max(dp_i_1_1, -prices[i])

        return dp_i_2_0

s = Solution()
print s.maxProfit([2,4,1])