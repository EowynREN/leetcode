# class Solution:
#     # @param {int[][]} grid a 2D grid
#     # @return {int} an integer
#     def shortestDistance(self, grid):
#         # Write your code here
#         if not grid or not grid[0]:
#             return -1
#
#         n, m = len(grid), len(grid[0])
#         # if n == 0 or m == 0:
#         #     return -1
#
#         x, y = [], []
#         sum_x, sum_y = [0], [0]
#
#         for i in range(n):
#             for j in range(m):
#                 if grid[i][j] == 1:
#                     x.append(i)
#                     y.append(j)
#
#         x = sorted(x)
#         y = sorted(y)
#         total = len(x)
#
#         # no house around
#         if total == 0:
#             return 0
#
#         for i in range(total):
#             sum_x.append(sum_x[i] + x[i])
#             sum_y.append(sum_y[i] + y[i])
#
#         smallest = 2147483647
#         for i in range(n):
#             for j in range(m):
#                 if grid[i][j] == 0:
#                     x_cost = self.get_cost(x, sum_x, i, total)
#                     y_cost = self.get_cost(y, sum_y, j, total)
#
#                     if x_cost + y_cost < smallest:
#                         smallest = x_cost + y_cost
#         return smallest
#
#
#     def get_cost(self, x, sum, pos, n):
#         if x[0] > pos:
#             return sum[n] - pos * n
#
#         left, right = 0, n - 1
#         while left < right:
#             mid = left + (right - left) / 2 + 1
#
#             if x[mid] <= pos:
#                 left = mid
#             else:
#                 right = mid - 1
#
#         index = 0
#         if x[left] <= pos:
#             index = left
#         else:
#             index = left - 1
#         return (index + 1) * pos - sum[index + 1] + sum[n] - sum[index + 1] - (n - index - 1) * pos

class Solution:
    # @param {int[][]} grid a 2D grid
    # @return {int} an integer
    def shortestDistance(self, grid):
        # Write your code here
        if not grid or not grid[0] or not self.isAllZero(grid):
            return -1

        n, m = len(grid), len(grid[0])

        row = [0] * n
        column = [0] * m

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    column[j] += 1
                    row[i] += 1

        x_cost = [0] * n
        y_cost = [0] * m
        self.get_cost(row, n, x_cost)
        self.get_cost(column, m, y_cost)

        smallest = 2147483647
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 and x_cost[i] + y_cost[j] < smallest:
                    smallest = x_cost[i] + y_cost[j]
        return smallest

    def get_cost(self, a, n, res):
        prefixSum = [0] * n
        prefixSumSum = [0] * n


        prefixSum[0] = a[0]
        for i in range(1, n):
            prefixSum[i] = prefixSum[i - 1] + a[i]

        prefixSumSum[0] = 0
        for i in range(1, n):
            prefixSumSum[i] = prefixSumSum[i - 1] + prefixSum[i - 1]

        for i in range(n):
            res[i] = prefixSumSum[i]



        prefixSum[n - 1] = a[n - 1]
        for i in range(n - 2, -1, -1):
            prefixSum[i] = prefixSum[i + 1] + a[i]

        prefixSumSum[n - 1] = 0
        for i in range(n - 2, -1, -1):
            prefixSumSum[i] = prefixSumSum[i + 1] + prefixSum[i + 1]

        for i in range(n):
            res[i] += prefixSumSum[i]

        return res

    def isAllZero(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    return True
        return False

s = Solution()
print s.shortestDistance([[0,1,0,0],[1,0,1,1],[0,1,0,0]])