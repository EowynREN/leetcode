class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        # Write your code here
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        if m == 0:
            return 0

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    count += 1
                    self.dfs(grid, i, j)
        return count

    def dfs(self, grid, i, j):
        n, m = len(grid), len(grid[0])
        if i < 0 or i >= n or j < 0 or j >= m or not grid[i][j]:
            return

        grid[i][j] = False
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i, j + 1)
