class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # base case
        # n = 1, k
        # n = 2, 2.1 k * 1                ----same
        #       2.2 k * (k - 1)          ----diff

        # build up
        # n = 3, from 2.1, same * (k - 1) ----diff
        #       from 2.2, diff * 1       ----same => same = diff * 1,   diff = same * (k - 1) + diff * (k - 1)
        #                  diff * (k - 1) ----diff

        #0 fence
        if n == 0:
            return 0
        #1 fence
        if n == 1:
            return k

        #2 fences
        same, diff = k, k * (k - 1)

        #3 fences ~ n fences
        for i in range(3, n + 1):
            same, diff = diff, (same + diff) * (k - 1)
        return same + diff
