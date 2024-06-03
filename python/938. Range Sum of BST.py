# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
遍历的思路
"""
class Solution(object):
    def __init__(self):
        self.sum = 0
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        self.traverse(root, low, high)
        return self.sum

    def traverse(self, root, low, high):
        if not root:
            return

        if root.val < low:
            self.traverse(root.right, low, high)
        elif root.val > high:
            self.traverse(root.left, low, high)
        else: # low <= root.val <= high
            self.sum += root.val
            self.traverse(root.right, low, high)
            self.traverse(root.left, low, high)

"""
分解的思路
"""
class Solution(object):
    def rangeSumBST(self, root, low, high):
        if not root:
            return 0

        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            return self.rangeSumBST(root.left, low, high)
        else:  # low <= root.val <= high
            return root.val + self.rangeSumBST(root.right, low, high) + self.rangeSumBST(root.left, low, high)


