class Solution:
    # @param heights: a list of integers
    # @return: a integer
    def trapRainWater(self, heights):
        # write your code here
        if not heights or len(heights) == 1:
            return 0

        # 如果最左和最有的墙为0, 跳过这些墙
        # 因为外侧不可能有别的墙与左边(和右边)组成pair来围水
        left, right = 0, len(heights) - 1
        while heights[left] == 0:
            left += 1
        while heights[right] == 0:
            right -= 1

        # 此处很重要, 在左右两侧分别维护一个左右墙的max height
        v, lh_max, rh_max = 0, heights[left], heights[right]
        while left < right:
            if heights[left] > heights[right]:
                right -= 1
                # 右边的指针被移动
                # if   新的墙比右边的max height小
                #      水可以被围住, 更新volumn
                # else 新的墙壁右边的max height还要高
                #      围不住水,更新右边最高墙高
                if heights[right] < rh_max:
                    v += rh_max - heights[right]
                else:
                    rh_max = heights[right]
            else:
                left += 1
                if heights[left] < lh_max:
                    v += lh_max - heights[left]
                else:
                    lh_max = heights[left]
        return v