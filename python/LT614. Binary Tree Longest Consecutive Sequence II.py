# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class ResultType:
    def __init__(self, longest, increase, decrease):
        self.longest = longest
        self.increase = increase
        self.decrease = decrease

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {int} the length of the longest consecutive sequence path
    def longestConsecutive2(self, root):
        # Write your code here
        rt = self.helper(root)
        return rt.longest

    def helper(self, node):
        if not node:
            return ResultType(0, 0, 0)

        left = self.helper(node.left)
        right = self.helper(node.right)


        # 如果左分支为increase，那么它就不可能是decrease
        # 如果右分支为increase，那么它就不可能是decrease
        increase, decrease = 0, 0

        # left subtree increase (from top to bottom)
        if node.left and node.left.val - 1 == node.val:
            increase = max(increase, left.increase + 1)

        # right subtree increase
        if node.right and node.right.val - 1 == node.val:
            increase = max(increase, right.increase + 1)

        # left subtree decrease
        if node.left and node.left.val + 1 == node.val:
            decrease = max(decrease, left.decrease + 1)

        # right subtree decrease
        if node.right and node.right.val + 1 == node.val:
            decrease = max(decrease, right.decrease + 1)

        # longest sequence for current node as root
        longest = increase + 1 + decrease

        # 保证最长的sequence永远能保留下来
        longest = max(longest, max(left.longest, right.longest))

        return ResultType(longest, increase, decrease)