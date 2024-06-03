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
        """
        # 经典问题了，先给出递归函数的定义：给该函数输入三个参数 root，p，q，它会返回一个节点：

        # 情况 1，如果 p 和 q 都在以 root 为根的树中，函数返回的即使 p 和 q 的最近公共祖先节点。
        # 情况 2，那如果 p 和 q 都不在以 root 为根的树中怎么办呢？函数理所当然地返回 null 呗。
        # 情况 3，那如果 p 和 q 只有一个存在于 root 为根的树中呢？函数就会返回那个节点。

        # 根据这个定义，分情况讨论：

        # 情况 1，如果 p 和 q 都在以 root 为根的树中，那么 left 和 right 一定分别是 p 和 q（从 base case 看出来的）。
        # 情况 2，如果 p 和 q 都不在以 root 为根的树中，直接返回 null。
        # 情况 3，如果 p 和 q 只有一个存在于 root 为根的树中，函数返回该节点。
        """

        # base case
        if not root:
            return None

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if p == root or q == root:
            return root

        # 情况 1
        if left and right:
            return root
        # 情况 2
        if not left and not right:
            return None
        # 情况 3
        return right if not left else left
