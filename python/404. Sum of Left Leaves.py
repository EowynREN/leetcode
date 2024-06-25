# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
遍历一遍二叉树，然后找到那些左叶子节点，累加它们的值
"""
class Solution(object):
    def __init__(self):
        self.sum = 0

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.traverse(root)
        return self.sum

    def traverse(self, node):
        if not node:
            return

        if node.left and not node.left.left and not node.left.right:
            self.sum += node.left.val

        self.traverse(node.left)
        self.traverse(node.right)