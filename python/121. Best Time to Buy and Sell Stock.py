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
