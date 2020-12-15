import heapq


class Solution:

    # @param {int} k an integer
    def __init__(self, k):
        # initialize your data structure here.
        self.minHeap = []
        self.k = k

    # @param {int} num an integer
    def add(self, num):
        # Write your code here
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, num)
            return

        if num > self.minHeap[0]:
            heapq.heappop(self.minHeap)
            heapq.heappush(self.minHeap, num)

    # @return {int[]} the top k largest numbers
    def topk(self):
        # Write your code here
        return sorted(self.minHeap, reverse=True)


s = Solution(3)
s.add(9)
print s.topk()
s.add(3)
print s.topk()
s.add(2)
print s.topk()
s.add(4)
print s.topk()
s.add(8)
print s.topk()