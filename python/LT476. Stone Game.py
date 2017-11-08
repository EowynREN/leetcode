# import sys
#
#
# class Solution:
#     """
#     @param: A: An integer array
#     @return: An integer
#     """
#     def stoneGame(self, A):
#         # write your code here
#         n = len(A)
#
#         sums = [[0 for j in range(n + 1)] for i in range(n + 1)]
#         for i in range(1, n + 1):
#             sums[i][i] = A[i - 1]
#             for j in range(i + 1, n + 1):
#                 sums[i][j] = sums[i][j - 1] + A[j - 1]
#
#         dp = [[0 for j in range(n + 1)] for i in range(n + 1)]
#         self.memorial_search(1, n, dp, sums)
#
#         return dp[1][n]
#
#     def memorial_search(self, i, j, dp, sums):
#         if i >= j:
#             return 0
#
#         if dp[i][j] != 0:
#             return dp[i][j]
#
#         dp[i][j] = sys.maxint
#         for k in range(i, j):
#             left = self.memorial_search(i, k, dp, sums)
#             right = self.memorial_search(k + 1, j, dp, sums)
#
#             dp[i][j] = min(dp[i][j], left + right + sums[i][j])
#
#         return dp[i][j]
#
# s = Solution()
# print s.stoneGame([3,4,3])

import sys


class Solution:
    """
    @param: A: An integer array
    @return: An integer
    """
    def stoneGame(self, A):
        # write your code here
        if not A:
             return 0

        n = len(A)

        sums = [0 for i in range(n + 1)]
        for i in range(1, n + 1):
            sums[i] = sums[i - 1] + A[i - 1]

        dp = [[0 for j in range(n + 1)] for i in range(n + 1)]

        for i in range(n - 1, 0, -1):
            for j in range(i + 1, n + 1):
                dp[i][j] = sys.maxint
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + sums[j] - sums[i - 1])

        return dp[1][n]

s = Solution()
print s.stoneGame([3,4,3])