#-*- coding:utf8 -*-
#coding=utf-8

# greedy
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        maxProfit = 0
        cheapest = prices[0]
        for cur in prices:
            maxProfit = max(maxProfit, cur - cheapest)
            cheapest = min(cheapest, cur)
        return maxProfit

# dp - 通杀版 k = 1
# 完全利用模板,一处不改
import sys
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # init
        k = 1 # 注意
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

# dp - 简化版
# 根据题意,限制了总共的交易次数,即k = 1,只能交易一次,因此关于交易次数的维度就可以flat掉,dp数组变成二维
class Solution2(object):
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

        for i in range(1, len(prices) + 1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i - 1])
            dp[i][1] = max(dp[i - 1][1], -prices[i - 1]) # 注意这里,不能是dp[i - 1][0] - prices[i - 1],
                                                         # 因为限制了交易次数(k=1),当已经完成一次交易后,再要进行交易时,要么保留上一次的profit,要么放弃,直接从新买(即: -prices[i - 1])

        return dp[len(prices)][0]

# dp - 简化版:压缩空间
# 给出空间更高效的优化:
# 根据简化版可见,dp的状态转移,只跟相邻的状态有关,那么就不需要用数组来存储,直接改为变量更高效

class Solution3(object):
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
            dp_i_1 = max(dp_i_1, -prices[i])

        return dp_i_0


s = Solution3()
print s.maxProfit([7,1,5,3,6,4])