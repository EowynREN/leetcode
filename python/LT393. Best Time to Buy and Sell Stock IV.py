class Solution:
    """
    @param: K: An integer
    @param: prices: An integer array
    @return: Maximum profit
    """
    def maxProfit(self, k, prices):
        # write your code here
        if k == 0:
            return 0

        n = len(prices)
        if k >= n / 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]

            return profit

        mustsell = [[0 for j in range(k + 1)]for i in range(n + 1)]
        globalbest = [[0 for j in range(k + 1)]for i in range(n + 1)]

        mustsell[0][0] = 0
        globalbest[0][0] = 0
        for i in range(1, k + 1):
            mustsell[0][i] = 0
            globalbest[0][i] = 0

        for i in range(1, n):
            gainorlose = prices[i] - prices[i - 1]
            mustsell[i][0] = 0
            for j in range(1, k + 1):
                mustsell[i][j] = max(globalbest[i - 1][j - 1] + gainorlose,
                                            mustsell[i - 1][j] + gainorlose)
                globalbest[i][j] = max(globalbest[i - 1][j], mustsell[i][j])

        return globalbest[n - 1][k]

s = Solution()
print s.maxProfit(2, [4,6,6,1,1,4,2,5])