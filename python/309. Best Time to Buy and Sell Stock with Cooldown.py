#-*- coding:utf8 -*-
#coding=utf-8
import sys

# dp - 通杀版，只需一下改进，完全套用模板
        # 每次 sell 之后要等一天才能继续交易。只要把这个特点融入上一题的状态转移方程即可：
        # dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        # dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])   <------ 改变
        # 解释：第 i 天选择 buy 的时候，cooldown 1 day, 要从 i-2 的状态转移，而不是 i-1
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # init
        dp = [[0 for j in range(2)] for i in range(len(prices) + 1)]

        # base case
        dp[0][0] = 0
        dp[0][1] = -sys.maxsize - 1
        if len(prices) > 0:
            dp[1][0] = 0
            dp[1][1] = -prices[0]

        for i in range(1, len(prices) + 1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i - 1])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i - 1]) # <------ 改变

        return dp[len(prices)][0]

# dp - 简化版:空间压缩
# 根据上面通杀版的解法,给出空间更高效的优化:
# dp的状态转移,只跟相邻的状态i- 1以及i- 2有关,那么就不需要用数组来存储,直接改为变量更高效
class Solution1(object):
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
        dp_pre_0 = 0 # 代表dp[i - 1][0]

        for i in range(len(prices)):
            temp = dp_i_0 # <------ 注意
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i]) # <------ 改变
            dp_pre_0 = temp # <------ 注意

        return dp_i_0