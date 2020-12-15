class Solution:
    # @param {boolean[][]} matrix, a list of lists of boolean
    # @return {int} an integer
    def maximalRectangle(self, matrix):
        # Write your code here
        if not matrix or not matrix[0]:
            return 0

        n, m = len(matrix), len(matrix[0])

        # int[][] height = new int[n][m + 1];
        # 这里之所以m + 1，是为了函数largestRectangleInHistogram中，在最后人为的加入一个最小值
        # 使得stack无论是否为空，里面的元素都必须全部出栈
        heights = [[0 for j in range(m + 1)] for i in range(n)]

        for j in range(m):
            heights[0][j] = matrix[0][j]

        for i in range(1, n):
            for j in range(m):
                if matrix[i][j] == 0:
                    heights[i][j] = 0
                else:
                    heights[i][j] = heights[i - 1][j] + 1

        maxArea = 0
        for i in range(n):
            area = self.largestRectangleInHistogram(heights[i])
            maxArea = max(maxArea, area)
        return maxArea

    def largestRectangleInHistogram(self, height):
        stack = []

        i, maxArea = 0, 0
        while i < len(height):

            if not stack or height[stack[-1]] <= height[i]:
                stack.append(i)
                i += 1
            else:
                h = height[stack.pop()]
                w = i if not stack else i - stack[-1] - 1

                maxArea = max(maxArea, h * w)

        return maxArea

s = Solution()
print s.maximalRectangle([[1]])