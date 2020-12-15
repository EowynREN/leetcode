#-*- coding:utf8 -*-
#coding=utf-8
# class Solution(object):
#     def minCostII(self, costs):
#         """
#         :type costs: List[List[int]]
#         :rtype: int
#         """
#         if not costs or not costs[0]:
#             return 0
#
#         n, k = len(costs), len(costs[0])
#         dp = [[0 for j in xrange(k)] for i in xrange(n)]
#         for j in xrange(k):
#             dp[0][j] = costs[0][j]
#
#         for i in xrange(1, n):
#             min1 = 2147483647  # 最小
#             min2 = 2147483647  # 次小
#
#             for j in xrange(k):
#                 if dp[i - 1][j] < min1:
#                     min2 = min1
#                     min1 = dp[i - 1][j]
#                 else:
#                     if dp[i - 1][j] < min2:
#                         min2 = dp[i - 1][j]
#
#             for j in xrange(k):
#                 if dp[i - 1][j] == min1:
#                     dp[i][j] = costs[i][j] + min2
#                 else:
#                     dp[i][j] = costs[i][j] + min1
#
#         res = 2147483647
#         for j in xrange(k):
#             res = min(res, dp[n - 1][j])
#         return res
class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or not costs[0]:
            return 0

        n, k = len(costs), len(costs[0])
        dp = [[0 for j in xrange(k)] for i in xrange(n)]
        for j in xrange(k):
            dp[0][j] = costs[0][j]

        for i in xrange(1, n):
            leftmin = [2147483647] * k
            rightmin = [2147483647] * k

            for j in xrange(k):
                if j == 0:
                    leftmin[j] = dp[i - 1][j]
                else:
                    leftmin[j] = min(leftmin[j - 1], dp[i - 1][j])

            for j in xrange(k - 1, -1, -1):
                if j == k - 1:
                    rightmin[j] = dp[i - 1][j]
                else:
                    rightmin[j] = min(rightmin[j + 1], dp[i - 1][j])

            for j in xrange(k):
                if j == 0:
                    dp[i][j] = costs[i][j] + rightmin[j + 1]
                elif j == k - 1:
                    dp[i][j] = costs[i][j] + leftmin[j - 1]
                else:
                    dp[i][j] = costs[i][j] + min(leftmin[j - 1], rightmin[j + 1])

        res = 2147483647
        for j in xrange(k):
            res = min(res, dp[n - 1][j])
        return res


s = Solution()
print s.minCostII([[7, 2,3,5]])