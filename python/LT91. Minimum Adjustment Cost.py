import sys


# class Solution:
#     """
#     @param: A: An integer array
#     @param: target: An integer
#     @return: An integer
#     """
#     def MinAdjustmentCost(self, A, target):
#         # write your code here
#         if not A:
#             return 0
#
#         B = list(A)
#

#         M = [[-1 for j in xrange(100)] for i in xrange(len(A))]
#         s = self.dfs(A, B, 0, target, M)
#         return s
#     def dfs(self, A, B, index, target, M):
#         if index >= len(A):
#             return 0
#
#         mn = sys.maxint
#         for val in xrange(1, 101):
#             if index != 0 and abs(val - B[index - 1]) > target:
#                 continue
#
#             if M[index][val - 1] != -1:
#                 diff = M[index][val - 1]
#                 mn = min(mn, diff)
#                 continue
#
#             B[index] = val
#
#             diff = abs(A[index] - val) + self.dfs(A, B, index + 1, target, M)
#             M[index][val - 1] = diff
#             mn = min(mn, diff)
#
#             B[index] = A[index]
#
#         return mn
class Solution:
    """
    @param: A: An integer array
    @param: target: An integer
    @return: An integer
    """
    def MinAdjustmentCost(self, A, target):
        # write your code here
        if not A:
            return 0

        # 对于B数组，每一位都可以从1取到100，B数组一共有n位
        # dp记录B数组每一个可能的取值所带来的最小cost
        n = len(A)
        dp = [[sys.maxint] * (100 + 1) for i in xrange(n)]

        # initial
        # 改第0个位置上的数可能的cost
        for j in xrange(1, 100 + 1):
            dp[0][j] = abs(A[0] - j)


        # dp[i][j]：前i位中,把index = i的值修改为j，所需要的最小花费
        # dp[i][j] = min(dp[i - 1][k] + A[i] - j)
        # 在当前i位取了j以后，k是前一位(i - 1)取从1~100的值，min是在所有的dp[i - 1][k]中间找到最小的那个
        for i in xrange(1, n):
            # 把index = i位的值修改为j
            for j in xrange(1, 100 + 1):
                # 前面i - 1位可能的取值与当前j值所能带来的最小cost
                for k in xrange(1, 100 + 1):
                    if abs(j - k) > target:
                        continue

                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + abs(A[i] - j))

        res = sys.maxint
        for j in xrange(1, 100 + 1):
            res = min(res, dp[n - 1][j])
        return res


s = Solution()
print s.MinAdjustmentCost([11,11,3,5,11,16,12,11,15,11,16,16,16,16,16,11,16], 0)