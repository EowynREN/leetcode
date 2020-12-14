#-*- coding:utf8 -*-
#coding=utf-8

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