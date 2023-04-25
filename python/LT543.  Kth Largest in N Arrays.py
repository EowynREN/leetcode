import heapq


class Solution:
    # @param {int[][]} arrays a list of array
    # @param {int} k an integer
    # @return {int} an integer, K-th largest element in N arrays
    def KthInArrays(self, arrays, k):
        # Write your code here
        if not arrays:
            return 0

        if k <= 0:
            return 0

        heap = []

        for i in range(len(arrays)):
            arrays[i] = sorted(arrays[i])

            n = len(arrays[i])
            if n > 0:
                # largest element in each array
                val = arrays[i][n - 1] * -1  # change min heap to max heap
                from_id = i
                index = n - 1
                heapq.heappush(heap, (val, from_id, index))

        for i in range(k):
            elem = heapq.heappop(heap)
            val = elem[0]
            from_id = elem[1]
            index = elem[2]

            if i == k - 1:
                return val * -1

            # not the first element in array
            if index > 0:
                index -= 1
                val = arrays[from_id][index] * -1  # change min heap to max heap
                heapq.heappush(heap, (val, from_id, index))

        return -1
