import heapq

class Solution:
    '''
    @param {int[]} nums an integer array
    @param {int} k an integer
    @return {int[]} the top k largest numbers in array
    '''
    # Thanks to geek4u for suggesting this method.
    #
    # 1) Build a Min Heap MH of the first k elements ----> O(k)
    #
    # 2) For each element, after the kth element (arr[k] to arr[n-1]), compare it with root. ----> O((n-k) * logk)
    #     a) If the element is greater than the root then make it root and call heapify.
    #     b) Else ignore it.

    # 3) Finally, MH has k largest elements and root of the MH is the kth largest element.
    #
    # Time Complexity: O(k + (n-k)Logk) without sorted output.
    #                  If sorted output is needed then O(k + (n-k)Logk + kLogk)

    # All of the above methods can also be used to find the kth largest (or smallest) element.



    def topk(self, nums, k):
        # Write your code here
        heap = []
        for i in range(k):
            heapq.heappush(heap, nums[i])

        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, nums[i])
        return sorted(heap, reverse=True)