class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        n, m = len(matrix), len(matrix[0])
        dp = [[0 for j in xrange(m)] for i in xrange(n)]

        maxLen = 0
        for j in xrange(m):
            dp[0][j] = int(matrix[0][j])
            maxLen = max(maxLen, dp[0][j])

        for i in xrange(n):
            dp[i][0] = int(matrix[i][0])
            maxLen = max(maxLen, dp[i][0])

        for i in xrange(1, n):
            for j in xrange(1, m):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + int(matrix[i][j])
                    maxLen = max(maxLen, dp[i][j])
        return maxLen * maxLen

        

s = Solution()
print s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])