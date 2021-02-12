#-*- coding:utf8 -*-
#coding=utf-8
import sys


# dp - 通杀版，交易次数不限制k = inifity, 因此可消除k这个维度
        # 只需在每次卖出时，把手续费从利润里扣除或加进买入的价格就可以
        # dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        # dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i] - fee)
        # 解释：相当于买入股票的价格升高了
        # 在第一个式子里减也是一样的，相当于卖出股票的价格减小了
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """

        # init
        dp = [[0 for j in range(2)] for i in range(len(prices) + 1)]

        # base case
        dp[0][0] = 0
        dp[0][1] = -sys.maxsize - 1

        for i in range(1, len(prices) + 1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i - 1])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i - 1] - fee)

        return dp[len(prices)][0]

# dp - 简化版:压缩空间
# 观察上面的通杀版可得, dp的状态转移只跟相邻的状态相关,因此可以直接用变量交替存储相邻状态即可
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """

        # init
        # nothing here

        # base case: 第i = 0天
        dp_i_0 = 0
        dp_i_1 = -sys.maxsize - 1

        for i in range(len(prices)):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_i_0 - prices[i] - fee)

        return dp_i_0