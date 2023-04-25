from heapq import heappop, heappush

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Pair(object):

    def __init__(self, num, frequency):
        self.num = num
        self.frequency = frequency

    def __lt__(self, other):
        return self.frequency < other.frequency


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freqPair = {}

        # O(n)
        for num in nums:
            if num in freqPair:
                freqPair[num].frequency += 1
            else:
                freqPair[num] = Pair(num, 1)

        # O(nlog(k))
        minHeap = []
        for pair in freqPair.values():
            if len(minHeap) >= k and pair.frequency > minHeap[0].frequency:
                heappop(minHeap)
                heappush(minHeap, pair)

            if len(minHeap) < k:
                heappush(minHeap, pair)

        # O(klog(k))
        res = []
        for i in range(k):
            cur = heappop(minHeap)
            res.append(cur.num)
        return res

s = Solution()
res = s.topKFrequent([-1,1,4,-4,3,5,4,-2,3,-1], 3)
print(res)