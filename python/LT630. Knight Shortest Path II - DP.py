#思路: 2-d棋盘,worst case 全部走一遍 --> O(n^2)


class Solution:
    # @param {boolean[][]} grid a chessboard included 0 and 1
    # @return {int} the shortest path
    def shortestPath2(self, grid):
        # Write your code here
        if not grid or not grid[0]:
            return -1

        n, m = len(grid), len(grid[0])

        dp = [[2147483647 for j in range(m)] for i in range(n)]
        dp[0][0] = 0

        # 马走的规则
        dx = [-1, -2, 1, 2]
        dy = [-2, -1,-2,-1]

        for j in range(m):
            for i in range(n):
                # 当前这个点如果不可达(1表示有障碍)
                if grid[i][j] == 1:
                    continue

                # 马可以总四个位置,走到当前这个点
                for s in range(4):
                    x = i + dx[s]
                    y = j + dy[s]

                    if x < 0 or x >= n or y < 0 or y >= m:
                        continue

                    # (i, j)是到达点, (x, y)是出发点
                    # 出发点如果是障碍,也跳过
                    if grid[x][y] == 1:
                        continue

                    # dp[i][j]表示从(0, 0)到(i, j)这个点的最少步骤
                    # (x, y)是能到(i, j)的点
                    dp[i][j] = min(dp[i][j], dp[x][y] + 1)

        return dp[n - 1][m - 1] if dp[n - 1][m - 1] != 2147483647 else -1