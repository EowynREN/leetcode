#-*- coding:utf8 -*-
#coding=utf-8
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return []

        n, m = len(matrix), len(matrix[0])

        dp = [[n + m + 1 if matrix[i][j] else 0 for j in xrange(m)] for i in xrange(n)]
        visited = set()

        for i in xrange(n):
            for j in xrange(m):
                visited.add((i, j))
                dp[i][j] = self.dfs(matrix, i, j, dp, visited)
                visited.remove((i, j))
        return dp

    def dfs(self, matrix, i, j, dp, visited):
        n, m = len(matrix), len(matrix[0])

        if dp[i][j] != n + m + 1:
            return dp[i][j]

        if matrix[i][j] == 0:
            return 0

        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x = i + dx
            y = j + dy

            if x < 0 or x >= n or y < 0 or y >= m:
                continue

            if (x, y) in visited:
                continue

            visited.add((x, y))
            dp[i][j] = min(dp[i][j], self.dfs(matrix, x, y, dp, visited) + 1)
            visited.remove((x, y))

        return dp[i][j]


s = Solution()
print s.updateMatrix([[0, 0, 1, 0, 1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 0, 0, 0, 1, 1], [1, 0, 1, 0, 1, 1, 1, 0, 1, 1], [0, 0, 1, 1, 1, 0, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1, 0, 0, 1, 1], [1, 1, 1, 0, 1, 1, 0, 1, 0, 1], [1, 0, 1, 1, 1, 0, 1, 1, 1, 0]])