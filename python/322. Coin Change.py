#-*- coding:utf8 -*-
#coding=utf-8

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 因为凑成 amount 金额的硬币数最多只可能等于 amount（全用 1 元面值的硬币），所以初始化为 amount + 1 就相当于初始化为正无穷，便于后续取最小值。
        INF = amount + 1

        dp = [INF for _ in range(amount + 1)] # 当目标金额为i时，至少需要 dp[i] 枚硬币凑出。
        dp[0] = 0 # 当amount为0的时候，最少数量硬币凑出为0

        for i in xrange(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[amount] == INF:
            return -1
        return dp[amount]

s = Solution()
print s.coinChange([1, 2, 5], 11)