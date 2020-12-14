#-*- coding:utf8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 这道题求最大路径和,因为路径可以由任一节点开始,在任一节点结束, 那么最大路径和有可能不经过root
# 那么对于'当前'节点来说最大路径和可能出现在:
# 1. 左子树中
# 2. 右子树中
# 3. 横跨了左右子树(图像上呈现路径拐弯)
# 另外因为求的是最大路径'和', 所以一旦某个sub path之和为负数,那么就需要舍弃这个sub path (i.e.,加负数,不如不加)

import sys
class Solution(object):
    def __init__(self):
        self.maxSum = -sys.maxint - 1

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.helper(root)

        # 最终返回全局最大
        return self.maxSum

    def helper(self, node):
        if not node:
            return 0
        # 寻找左子树中的最大sub path之和, 出现负数,就清零
        left = max(0, self.helper(node.left))
        # 寻找右子树中的最大sub path之和, 出现负数,就清零
        right = max(0, self.helper(node.right))

        # self.maxSum是一个全局变量,用来追踪全局最大值, 这里的式子其实涵盖了1-3所有case
        # left + right + node.val这个式子其实涵盖了case1-3, 因为在上一步,如果左子树sub path之后或右子树sub path之和为负数的话,会被清零
        # 因为left和right有0的情况,所以这个式子可以看成:
        #       left + node.val
        #       right + node.val
        #       left + right + node.val
        self.maxSum = max(self.maxSum, left + right + node.val)

        # 返回的值是可供上一层父节点接龙的值, 不会涉及路径拐弯
        return max(left, right) + node.val

a = TreeNode(-10)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)

a.left = b
a.right = c
c.left = d
c.right = e

s = Solution()
print "final:" + str(s.maxPathSum(a))