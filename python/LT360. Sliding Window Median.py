import heapq


class Solution:
    """
    @param nums: A list of integers.
    @return: The median of element inside the window at each moving.
    """
    def medianSlidingWindow(self, nums, k):
        # write your code here
        # 1. input: a list of integer, an integer
        # 2. output: a list of integer
        # 3. key: min & max heap, int median (median is the number part of the result)
        #         if nums[i] == median --> do nothing
        #         if nums[i] > median --> add in minHeap
        #         if nums[i] < median --> add in maxHeap
        #
        #         pop the number out of the window num[i - k]
        #         if nums[i - k] == median --> if nums[i] == median -> pop either form min or max
        #         if nums[i - k] > median --> minHeap.remove[nums[i - k]]
        #         if nums[i - k] < median --> maxHeap.remove[nums[i - k]]
        #
        #          if len(maxHeap) > len(minHeap) --> median = maxHeap.pop
        #          if len(maxHeap) + 1 < len(minHeap) --> median = minheap.pop
        # 4. edge case: nums = [] --> return []
        #               k = 0 --> return []
        #               len = 1 --> return [nums[0]]
        # 5. TDD - test case: [2, 1, 7, 8, 5]

        if not nums or k == 0:
            return []
        if len(nums) == 1:
            return [nums[0]]

        # if k = 1, the first number must in result set
        res = [] if k > 1 else [nums[0]]
        minHeap, maxHeap = [], []
        median = nums[0]
        for i in range(1, len(nums)):
            # left side <= median <= right side
            # push the num in either side
            if nums[i] > median:
                heapq.heappush(minHeap, nums[i])
            else:
                heapq.heappush(maxHeap, nums[i] * -1)

            # pop num which is out of the window size
            if i >= k:
                if nums[i - k] > median:
                    minHeap.remove(nums[i - k])
                    heapq.heapify(minHeap)
                elif nums[i - k] < median:
                    maxHeap.remove(nums[i - k] * -1)
                    heapq.heapify(maxHeap)
                else:
                    # get the adjust medain when the new coming nums[i] is equal to the old median
                    if maxHeap:
                        median = heapq.heappop(maxHeap) * -1
                    elif minHeap:
                        median = heapq.heappop(minHeap)

            # adjust the median
            # left side is over weight
            if len(maxHeap) > len(minHeap):
                # shift median to right
                heapq.heappush(minHeap, median)
                median = heapq.heappop(maxHeap) * -1

            # right side is over weight
            if len(maxHeap) + 1 < len(minHeap):
                # shift median to left
                heapq.heappush(maxHeap, median * -1)
                median = heapq.heappop(minHeap)

            if i >= k - 1:
                res.append(median)

        return res

s = Solution()
print s.medianSlidingWindow([1,2,7,7,2], 1)