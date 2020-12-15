class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, height):
        # write your code here
        if not height:
            return 0

        max_area = height[0]
        stack = [0] # stack store the indexes
        height.append(-1) # to ensure all height pop out

        for i in range(1, len(height)):
            cur = height[i]
            # cur < height[stack[-1]] is ok
            while stack and cur <= height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1 if stack else i

                max_area = max(max_area, h * w)
            stack.append(i)
        return max_area