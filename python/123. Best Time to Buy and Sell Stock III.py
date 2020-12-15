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


s = Solution()
print s.maxProfit([2,4,1])