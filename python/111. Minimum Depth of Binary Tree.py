#-*- coding:utf8 -*-
#coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS层遍历
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        q = [root]
        depth = 1 # root也算一层,所以depth为1

        while q:
            count = len(q) # 层遍历的精髓
            for i in xrange(count):
                cur = q.pop(0)

                if cur.left == None and cur.right == None:
                    return depth

                if cur.left:
                    q.append(cur.left)

                if cur.right:
                    q.append(cur.right)
            depth += 1
        return depth