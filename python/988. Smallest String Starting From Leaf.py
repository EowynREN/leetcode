# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
二叉树的递归分为「遍历」和「分解问题」两种思维模式，这道题需要用到「遍历」的思维。

思路非常简单：用 path 维护递归遍历的路径，到达叶子节点的时候判断字典序最小的路径。

不要忘了在叶子节点的时候也要正确维护 path 变量，而且要把 path 中的字符串反转才是题目想要的答案
"""

import sys


class Solution(object):
    def __init__(self):
        self.res = ""

    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        self.traverse(root, "")
        return self.res

    def traverse(self, node, path):
        if not node:
            return

        if not node.left and not node.right:
            path += chr(node.val + 97)
            path = path[::-1]
            if self.res == "" or path < self.res:
                self.res = path
            return

        self.traverse(node.left, path + chr(node.val + 97))
        self.traverse(node.right, path + chr(node.val + 97))
