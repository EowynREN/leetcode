from heapq import heappush, heappop


class Solution(object):
    def valid(self, x, y, matrix, visit):
        if x < len(matrix) and y < len(matrix[0]) and not visit[x][y]:
            return True
        return False

    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        #edge case
        if not matrix or len(matrix) == 0:
            return -1

        if len(matrix) * len(matrix[0]) < k:
            return -1

        dx = [0, 1]
        dy = [1, 0]
        heap = [(matrix[0][0], 0, 0)]
        visit = [[False for j in range(len(matrix[0]))] for i in range(len(matrix))]
        visit[0][0] = True

        for i in range(k - 1):
            smallest = heappop(heap)

            for j in range(2):
                nx = smallest[1] + dx[j]
                ny = smallest[2] + dy[j]
                if self.valid(nx, ny, matrix, visit):
                    heappush(heap, (matrix[nx][ny], nx, ny))
                    visit[nx][ny] = True
        return heap[0][0]

s = Solution()
print s.kthSmallest([[1,5,7],[3,7,8],[4,8,9]], 4)
