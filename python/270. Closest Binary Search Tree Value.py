# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        closest = root.val
        while root:

            if abs(target - root.val) < abs(target - closest):
                closest = root.val

            root = root.right if target > root.val else root.left
        return closest


class Solution2(object):
    def __init__(self):
        self.closest = 0

    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.closest = root.val
        self.traverse(root, target)
        return self.closest

    def traverse(self, node, target):
        if not node:
            return

        if target < node.val:
            self.traverse(node.left, target)

            if abs(target - node.val) < abs(target - self.closest):
                self.closest = node.val
        else:
            if abs(target - node.val) < abs(target - self.closest):
                self.closest = node.val

            self.traverse(node.right, target)

