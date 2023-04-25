# 思路: 一个DFS, 搜索最大的'1'的边界
#      用全局的left, right, top, bottom去保存最大边界
#      为了防止访问已经访问过的点, 可以将访问过的'1'都置为'0'
#      当然如果不允许改变数组的话还可以用hash来存储已经访问过的点

# 这种方法lintcode会报MLE, 占用系统栈空间太大

class Solution(object):
    # @param image {List[List[str]]}  a binary matrix with '0' and '1'
    # @param x, y {int} the location of one of the black pixels
    # @return an integer
    def __init__(self):
        self.left = 2147483647
        self.right = -2147483648
        self.top = 2147483647
        self.bottom = -2147483648

    def minArea(self, image, x, y):
        # Write your code here
        if not image or len(image) == 0 or len(image[0]) == 0:
            return 0

        self.dfs(image, x, y)
        return (self.right - self.left + 1) * (self.bottom - self.top + 1)

    def dfs(self, image, x, y):
        n, m = len(image), len(image[0])
        if x < 0 or x >= n or y < 0 or y >= m or image[x][y] == '0':
            return

        image[x][y] = '0'
        self.left = min(self.left, x)
        self.right = max(self.right, x)
        self.top = min(self.top, y)
        self.bottom = max(self.bottom, y)

        self.dfs(image, x - 1, y)
        self.dfs(image, x + 1, y)
        self.dfs(image, x, y - 1)
        self.dfs(image, x, y + 1)