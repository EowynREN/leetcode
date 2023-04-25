import heapq


class Solution:
    """
    @param nums: A list of integers.
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        # write your code here
        if not nums:
            return []

        res = []
        maxHeap = []
        for i in range(k):
            heapq.heappush(maxHeap, nums[i] * -1)
        res.append(maxHeap[0] * -1)

        for i in range(k, len(nums)):
            maxHeap.remove(nums[i - k] * -1)
            heapq.heapify(maxHeap)
            heapq.heappush(maxHeap, nums[i] * -1)
            res.append(maxHeap[0] * -1)
        return res

s = Solution()
print s.maxSlidingWindow([1, 2, 7, 7, 8], 3)