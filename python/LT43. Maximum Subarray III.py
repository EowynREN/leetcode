#-*- coding:utf8 -*-
#coding=utf-8
import sys


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k == 0:
            return 0

        n = len(prices)
        if k >= n / 2:
            return self.maxProfit2(k, prices)

        # 动态规划，循环引用的状态数组(local/global数组)
        # mustSell[i][k] 表示前i天，至多进行k次交易，第i天必须sell的最大获益
        # globalBest[i][k] 表示前i天，至多进行k次交易，第i天可以不sell的最大获益
        
        # 这里为什么初始化成int[n][k + 1]:
        # 因为题干中使用prices数组的i来表示第几天，因此一共n天从第0天开始（如果不是题干中用prices隐藏的暗示了天数，应该也是从第一天开始比较合理）
        # 而k + 1是因为，表示几次交易，要从1开始
        mustSell = [[0 for j in range(k + 1)]for i in range(n)]
        globalBest = [[0 for j in range(k + 1)]for i in range(n)]

        mustSell[0][0] = 0
        globalBest[0][0] = 0
        # 在第0天不管进行什么操作都是没有收益的，因为要么买进（不挣钱），要么没买（还是不挣钱）
        for j in range(1, k + 1):
            mustSell[0][j] = 0
            globalBest[0][j] = 0

        for i in range(1, n):
            gainOrLose = prices[i] - prices[i - 1]
            mustSell[i][0] = 0
            for j in range(1, k + 1):
                mustSell[i][j] = max(globalBest[i - 1][j - 1], mustSell[i - 1][j]) + gainOrLose
                globalBest[i][j] = max(globalBest[i - 1][j], mustSell[i][j])

        return globalBest[n - 1][k]

    def maxProfit2(self, k, prices):
        n = len(prices)
        profit = 0
        for i in range(1, n):
            # Best Time to Buy and Sell Stock II
            # greedy的思想，第一天买进，第二天卖出
            # 如果是亏本就不加(max函数会选0)，如果有收益就加
            profit += max(0, prices[i] - prices[i - 1])

        return profit
