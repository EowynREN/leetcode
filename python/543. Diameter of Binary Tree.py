# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def __init__(self):
        # 记录最大直径的长度
        self.maxDiameter = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 关键在于，每一条二叉树的「直径」长度，就是一个节点的左右子树的最大深度之和
        self.maxDepth(root)
        return self.maxDiameter

    def maxDepth(self, root):
        if not root:
            return 0

        leftMaxDepth = self.maxDepth(root.left)
        rightMaxDepth = self.maxDepth(root.right)

        self.maxDiameter = max(self.maxDiameter, leftMaxDepth + rightMaxDepth)

        return max(leftMaxDepth, rightMaxDepth) + 1