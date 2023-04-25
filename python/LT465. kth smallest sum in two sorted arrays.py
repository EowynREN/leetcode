import heapq


class Solution:
    # @param {int[]} A an integer arrays sorted in ascending order
    # @param {int[]} B an integer arrays sorted in ascending order
    # @param {int} k an integer
    # @return {int} an integer
    def valid(self, x, y, A, B, visit):
        if x < len(A) and y < len(B) and (x, y) not in visit:
            return True
        return False

    def kthSmallestSum(self, A, B, k):
        # Write your code here
        if not A and not B:
            return 0
        if not B:
            return A[k - 1]
        if not A:
            return B[k - 1]

        heap = [(A[0] + B[0], 0, 0)]
        visit = set()  # 此处用set,而不用2-d array,否则会MLE
        visit.add((0, 0))  # 一对二元组,就可以唯一确定一个位置

        dx = [0, 1]
        dy = [1, 0]
        for i in range(k - 1):
            smallest = heapq.heappop(heap)
            for j in range(2):
                nx = smallest[1] + dx[j]
                ny = smallest[2] + dy[j]
                if self.valid(nx, ny, A, B, visit):
                    heapq.heappush(heap, (A[nx] + B[ny], nx, ny))
                    visit.add((nx, ny))
        return heap[0][0]