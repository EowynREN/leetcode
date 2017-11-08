class Solution:
    """
    @param: A: An integer matrix
    @return: an integer
    """

    DIRECTIONS = [(1, 0), (0, 1), (0, -1), (-1, 0)]

    def longestIncreasingContinuousSubsequenceII(self, A):
        # write your code here
        if not A or not A[0]:
            return 0

        n, m = len(A), len(A[0])
        dp = [[0] * m for i in xrange(n)]
        visited = [[False] * m for i in xrange(n)]
        res = 0

        for i in range(n):
            for j in range(m):
                dp[i][j] = self.search(i, j, dp, visited, A)
                res = max(res, dp[i][j])
        return res

    def search(self, x, y, dp, visited, A):
        n, m = n, m = len(A), len(A[0])

        if visited[x][y]:
            return dp[x][y]

        res = 1
        for dx, dy in self.DIRECTIONS:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 如果还有比当前更大的，就继续找
            if A[x][y] < A[nx][ny]:
                res = max(res, self.search(nx, ny, dp, visited, A) + 1)

        # 第一次执行到这一行的时候，A[x][y]应该是矩阵中最大的元素
        # 因为4个方向都没有比它大的了，for循环结束，递归达到最底层（出口）
        visited[x][y] = True
        dp[x][y] = res

        return dp[x][y]

s = Solution()
print s.longestIncreasingContinuousSubsequenceII([[1,2,3,4,5],[16,17,24,23,6],[15,18,25,22,7],[14,19,20,21,8],[13,12,11,10,9]])