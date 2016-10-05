import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #思路：k大小的min heap
        #      先遍历k个数，假设为k个最大的数
        #      遍历剩下的n - k个数，x， 如果比堆顶的最大数kmax大，则替换x与kmax，否则不更新
        #      结束，第k大的数就在堆顶

        if not nums:
            return 0
        
        if k <= 0:
            return 0
        
        heap = []
        for i in range(len(nums)):
            if i < k:
                heapq.heappush(heap, nums[i])
                continue
            if nums[i] > heap[0]:
                heap[0] = nums[i]
                heapq.heapify(heap)
        return heap[0]
            

s = Solution()
print s.findKthLargest([-1,2,0], 2)