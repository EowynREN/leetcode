# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
二叉树的递归分为「遍历」和「分解问题」两种思维模式，这道题需要用到「遍历」的思维。

遍历的过程中记录父节点的值和连续序列的长度，并更新全局最大值即可
"""

import sys


class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {int} the length of the longest consecutive sequence path
    def __init__(self):
        self.maxLength = 0

    def longestConsecutive(self, root):
        self.traverse(root, 0, -sys.maxsize)
        return self.maxLength

    def traverse(self, node, length, parentVal):
        if not node:
            return

        # 记录连续递增序列长度，如果递增，长度+1，如果非递增，从当前node开始重新算长度
        if parentVal < node.val:
            length += 1
        else:
            length = 1
        # 更新全局最长连续序列的长度
        self.maxLength = max(self.maxLength, length)

        self.traverse(node.left, length, node.val)
        self.traverse(node.right, length, node.val)