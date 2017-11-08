class Solution:
    """
    @param: prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if not prices or len(prices) <= 1:
            return 0

        n = len(prices)
        left = [0] * n
        right = [0] * n

        left[0] = 0
        mn = prices[0]
        for i in xrange(1, n):
            mn = min(mn, prices[i])
            left[i] = max(left[i - 1], prices[i] - mn)

        right[n - 1] = 0
        mx = prices[n - 1]
        for i in xrange(n - 2, -1, -1):
            mx = max(mx, prices[i])
            t = prices[i]
            right[i] = max(right[i + 1], mx - prices[i])

        profit = 0
        for i in xrange(n):
            profit = max(profit, left[i] + right[i])
        return profit

s = Solution()
print s.maxProfit([4,4,6,1,1,4,2,5])