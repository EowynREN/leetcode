# 思路: 二分法 - 分别对上下左右四条边界进行夹逼

class Solution(object):
    # @param image {List[List[str]]}  a binary matrix with '0' and '1'
    # @param x, y {int} the location of one of the black pixels
    # @return an integer
    def minArea(self, image, x, y):
        # Write your code here
        if not image or len(image) == 0 or len(image[0]) == 0:
            return 0

        left, right, top, bottom = 0, 0, 0, 0

        n, m = len(image), len(image[0])

        # 夹逼左边界
        start, end = 0, y
        while start < end:
            mid = start + (end - start) / 2
            if (self.checkColumn(image, mid)):
                end = mid
            else:
                start = mid + 1
        left = start

        # 夹逼右边界
        start, end = y, m - 1
        while start < end:
            mid = start + (end - start) / 2 + 1
            if (self.checkColumn(image, mid)):
                start = mid
            else:
                end = mid - 1
        right = start

        # 夹逼上边界
        start, end = 0, x
        while start < end:
            mid = start + (end - start) / 2
            if (self.checkRow(image, mid)):
                end = mid
            else:
                start = mid + 1
        top = start

        # 夹逼下边界
        start, end = x, n - 1
        while start < end:
            mid = start + (end - start) / 2 + 1
            if (self.checkRow(image, mid)):
                start = mid
            else:
                end = mid - 1
        bottom = start

        return (right - left + 1) * (bottom - top + 1)

    def checkColumn(self, image, col):
        for i in range(len(image)):
            if image[i][col] == '1':
                return True
        return False

    def checkRow(self, image, row):
        for j in range(len(image[0])):
            if image[row][j] == '1':
                return True
        return False