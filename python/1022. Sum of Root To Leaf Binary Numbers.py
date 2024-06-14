# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
二叉树的递归分为「遍历」和「分解问题」两种思维模式，这道题需要用到「遍历」的思维。

用 path 变量维护每一条从根节点到叶子节点的路径形成的二进制数，到了叶子节点之后将这条路径的二进制数累加到 res 中即可
"""

class Solution(object):
    def __init__(self):
        self.res = 0

    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.traverse(root, 0)
        return self.res

    def traverse(self, node, path):
        if not node:
            return

        if not node.left and not node.right:
            path = path << 1 | node.val  # 重点在这里，二进制加法
            self.res += path
            return

        self.traverse(node.left, path << 1 | node.val)
        self.traverse(node.right, path << 1 | node.val)