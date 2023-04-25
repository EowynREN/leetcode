"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the root of the minimum subtree

    # 思路：与在数组中找一个最小值是一样的
    #       需要一个全局的min flag来记录最小的值（这里是node和值）
    #       然后遍历一遍

    def __init__(self):
        self.min_subtree = None
        self.min_sum = 2147483647

    def findSubtree(self, root):
        # Write your code here
        self.helper(root)
        return self.min_subtree

    def helper(self, node):
        if not node:
            return 0

        sum = self.helper(node.left) + self.helper(node.right) + node.val

        if sum < self.min_sum:
            self.min_sum = sum
            self.min_subtree = node

        return sum