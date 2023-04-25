#-*- coding:utf8 -*-
#coding=utf-8

import sys
# 解析: https://labuladong.github.io/algo/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E7%B3%BB%E5%88%97/%E5%9B%A2%E7%81%AD%E8%82%A1%E7%A5%A8%E9%97%AE%E9%A2%98.html

# 买入、卖出、无操作，我们用 buy, sell, rest 表示这三种选择
# 但问题是，并不是每天都可以任意选择这三种选择的,因为 sell 必须在 buy 之后，buy 必须在 sell 之后
# 那么 rest 操作还应该分两种状态，一种是 buy 之后的 rest（持有了股票），一种是 sell 之后的 rest（没有持有股票
# 而且别忘了，我们还有交易次数 k 的限制，就是说你 buy 还只能在 k > 0 的前提下操作。
# 而且我们可以用自然语言描述出每一个状态的含义，比如说:
#       dp[3][2][1] 的含义就是：今天是第三天，我现在手上持有着股票，至今最多进行 2 次交易
#       dp[2][3][0] 的含义：今天是第二天，我现在手上没有持有股票，至今最多进行 3 次交易

# 我们想求的最终答案是 dp[n - 1][K][0]，即最后一天，最多允许 K 次交易，最多获得多少利润
# 为什么不是 dp[n - 1][K][1]？
# 因为 [1] 代表手上还持有股票，[0] 表示手上的股票已经卖出去了，很显然后者得到的利润一定大于前者

# 这个问题的「状态」有三个，第一个是天数，第二个是允许交易的最大次数，第三个是当前的持有状态（即之前说的 rest 的状态，我们不妨用 1 表示持有，0 表示没有持有
# 我们用一个三维数组就可以装下这几种状态的全部组合：
# dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
#               max(   选择 rest  ,             选择 sell      )
#
# 解释：今天我没有持有股票，有两种可能：
# 要么是我昨天就没有持有，然后今天选择 rest，所以我今天还是没有持有；
# 要么是我昨天持有股票，但是今天我 sell 了，所以我今天没有持有股票了。
#
# dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
#               max(   选择 rest  ,           选择 buy         )
#
# 解释：今天我持有着股票，有两种可能：
# 要么我昨天就持有着股票，然后今天选择 rest，所以我今天还持有着股票
# 要么我昨天本没有持有，但今天我选择 buy，所以今天我就持有股票了

# Base Case
# dp[-1][k][0] = 0
# 解释：因为 i 是从 0 开始的，所以 i = -1 意味着还没有开始，这时候的利润当然是 0
# dp[-1][k][1] = -infinity
# 解释：还没开始的时候，是不可能持有股票的，用负无穷表示这种不可能
# dp[i][0][0] = 0
# 解释：因为 k 是从 1 开始的，所以 k = 0 意味着根本不允许交易，这时候利润当然是 0
# dp[i][0][1] = -infinity
# 解释：不允许交易的情况下，是不可能持有股票的，用负无穷表示这种不可能

# dp - 通杀模板
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        # init
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

# dp - 解决朝内存错误的 通杀版
# 当传入k 值非常大时，dp 数组太大了
# 解法: 一次交易由买入和卖出构成，至少需要两天
#      有效的限制 k 应该不超过 n/2，如果超过，就没有约束作用了，相当于 k = +infinity(这种情况是之前解决过的,就是股票系列的II)
class Solution1(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        # 解决朝内存错误
        # if k > len(prices) / 2:
        #     return maxProfitINF(prices)   ---> 就是股票系列的II

        # ---------- 以下都一样 ---------- #
        # init
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