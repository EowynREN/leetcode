#-*- coding:utf8 -*-
#coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 一个值得注意的地方:这道题中,前序/后序遍历都可以得到正确答案
#                 但中序遍历会出错
#                 因为在left与right子树交换后,再遍历的right的子树实际上是原来的left子树,而真正的right并没有被switch
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        # pre-order traversal
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        # post-order traversal也是可以的
        # root.left, root.right = root.right, root.left

        return root