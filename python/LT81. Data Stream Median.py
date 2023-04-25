import heapq


class Solution:
    """
    @param nums: A list of integers.
    @return: The median of numbers
    """
    def medianII(self, nums):
        # write your code here
        if not nums:
            return []

        res = [nums[0]]
        # left side <= median <= right side
        minHeap, maxHeap, median = [], [], nums[0]
        for i in range(1, len(nums)):
            if nums[i] > median:
                heapq.heappush(minHeap, nums[i])
            else:
                heapq.heappush(maxHeap, nums[i] * -1)

            # left side is over weight
            if len(maxHeap) > len(minHeap):
                heapq.heappush(minHeap, median)
                median = heapq.heappop(maxHeap) * -1

            # right side is over weight
            if len(maxHeap) + 1 < len(minHeap):
                heapq.heappush(maxHeap, median * -1)
                median = heapq.heappop(minHeap)

            res.append(median)
        return res