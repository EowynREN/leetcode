import heapq


class Solution:
    # @param heights: a matrix of integers
    # @return: an integer
    def trapRainWater(self, heights):
        # write your code here
        heap = []
        n, m = len(heights), len(heights[0])
        visited = [[0 for j in range(m)] for i in range(n)]

        for i in range(n):
            heapq.heappush(heap, (heights[i][0], i, 0))
            heapq.heappush(heap, (heights[i][m - 1], i, m - 1))
            visited[i][0] = 1
            visited[i][m - 1] = 1

        for j in range(m):
            heapq.heappush(heap, (heights[0][j], 0, j))
            heapq.heappush(heap, (heights[n - 1][j], n - 1,j))
            visited[0][j] = 1
            visited[n - 1][j] = 1

        vol = 0
        while heap:
            cell = heapq.heappop(heap)

            for k in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                x = cell[1] + k[0]
                y = cell[2] + k[1]

                if x >= 0 and x < n and y >= 0 and y < m and visited[x][y] == 0:
                    heapq.heappush(heap, (max(heights[x][y], cell[0]), x, y))
                    vol += max(0, cell[0] - heights[x][y])
                    visited[x][y] = 1
        return vol