# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
用 traverse 函数遍历到对应行，进行插入即可
"""


class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """
        # 插入到第一行的话特殊对待一下
        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot
        self.traverse(root, val, depth, 1)
        return root

    def traverse(self, node, val, target_depth, cur_depth):
        if not node:
            return

        if cur_depth + 1 == target_depth:
            new_left = TreeNode(val)
            new_right = TreeNode(val)

            new_left.left = node.left
            new_right.right = node.right

            node.left = new_left
            node.right = new_right
            return

        self.traverse(node.left, val, target_depth, cur_depth + 1)
        self.traverse(node.right, val, target_depth, cur_depth + 1)