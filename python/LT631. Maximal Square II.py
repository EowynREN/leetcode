class Solution:
    #param {int[][]} matrix a matrix of 0 and 1
    #return {int} an integer
    def maxSquare2(self, matrix):
        # write your code here
        if not matrix or not matrix[0]:
            return 0

        n, m = len(matrix), len(matrix[0])

        up = [[0] * m for i in range(n)]
        left = [[0] * m for i in range(n)]
        dp = [[0] * m for i in range(n)]

        for j in range(m):
            if matrix[0][j] == 1:
                dp[0][j] = 1
            else:
                up[0][j] = 1

        for i in range(n):
            if matrix[i][0] == 0:
                left[i][0] = 1

        mx = max(dp[0])
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j]:
                    dp[i][j] = min(dp[i - 1][j - 1], up[i - 1][j], left[i][j - 1]) + 1
                    up[i][j] = 0
                    left[i][j] = 0
                else:
                    dp[i][j] = 0

                    up[i][j] = up[i - 1][j] + 1
                    left[i][j] = left[i][j - 1] + 1

                mx = max(mx, dp[i][j])

        return mx * mx

s = Solution()
print s.maxSquare2([[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]])