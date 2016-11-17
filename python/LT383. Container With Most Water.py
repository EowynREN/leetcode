class Solution:
    # @param heights: a list of integers
    # @return: an integer
    def maxArea(self, heights):
        # write your code here
        if not heights:
            return 0

        res = 0
        i, j = 0, len(heights) - 1
        while i < j:
            res = max(res, min(heights[i], heights[j]) * (j - i))
            if heights[i] > heights[j]:
                j -= 1
            elif heights[i] < heights[j]:
                i += 1
            else:
                i += 1
                j -= 1
        return res