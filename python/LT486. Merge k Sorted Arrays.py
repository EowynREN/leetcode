import heapq


class Node:
    def __init__(self, from_id, index, val):
        self.from_id = from_id
        self.index = index
        self.val = val

    def __cmp__(self, other):
        return cmp(self.val, other.val)


class Solution:
    # @param {int[][]} arrays k sorted integer arrays
    # @return {int[]} a sorted array
    def mergekSortedArrays(self, arrays):
        # Write your code here
        res = []
        heap = []

        for i in range(len(arrays)):
            if arrays[i]:
                heapq.heappush(heap, Node(i, 0, arrays[i][0]))

        while heap:
            node = heapq.heappop(heap)
            res.append(node.val)

            if node.index + 1 < len(arrays[node.from_id]):
                from_id = node.from_id
                index = node.index + 1
                val = arrays[from_id][index]
                heapq.heappush(heap, Node(from_id, index, val))
        return res
s = Solution()
print s.mergekSortedArrays([[1,3,5,7],[2,4,6],[0,8,9,10,11]])