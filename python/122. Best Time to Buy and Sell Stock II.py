#-*- coding:utf8 -*-
#coding=utf-8

# greedy
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in xrange(1, len(prices)):
            # greedy的思想，第一天买进，第二天卖出
            # 如果是亏本就不加(max函数会选0)，如果有收益就加
            profit += max(0, prices[i] - prices[i - 1])
        return profit


import sys
# dp - 通杀版
# k = inifity, 交易次数k不参与状态变化，即k的状态和k - 1的状态是一样的 ->消掉k这个维度
class Solution1(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 通杀模板
        # init
        dp = [[0 for j in range(2)] for i in range(len(prices) + 1)]

        # base case
        dp[0][0] = 0
        dp[0][1] = -sys.maxsize - 1

        for i in range(1, len(prices) + 1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i - 1])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i - 1])

        return dp[len(prices)][0]

# dp - 简化版: 压缩空间
# 基于通杀版给出一个空间更高效的解法:
# 观察得出,dp的状态转移只跟相邻的状态相关,因此不需要数组来存储中间状态,直接用变量交替存储相邻状态即可
class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # init
        # nothing here

        # base case
        dp_i_0 = 0
        dp_i_1 = -sys.maxsize - 1

        for i in range(len(prices)):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_i_0 - prices[i])

        return dp_i_0