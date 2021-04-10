#-*- coding:utf8 -*-
#coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # base case
        if not root:
            return None

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # condition 1: 当前节点是不是p或者q
        if p == root or q == root:
            return root

        # condition 2: p和q分别在左右子树里, 那么当前节点就是最近公共祖先
        if left and right:
            return root

        # condition 3:
        # p或q在左子树里,返回任何左子树返回的节点
        if left:
            return left

        # condition 3:
        # p或q在右子树里,返回任何右子树返回的节点
        if right:
            return right

        # 啥都没找到,返回none,表示一无所获
        return None
