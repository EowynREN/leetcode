import heapq


class Solution:
    """
    @param {int} n an integer.
    @return {int} the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        if n <= 1:
            return n

        uglys = [2, 3, 5]
        heap = []
        for i in range(3):
            heapq.heappush(heap, (uglys[i], i))

        val = uglys[0]
        while n - 1  > 0:
            val, index = heapq.heappop(heap)

            while index < 3:
                new_val = uglys[index] * val
                heapq.heappush(heap, (new_val, index))
                index += 1
            n -= 1
        return val

s = Solution()
print s.nthUglyNumber(9)