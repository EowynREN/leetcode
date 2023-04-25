class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    # @param A: Given an integer array with no duplicates.
    # @return: The root of max tree.
    def maxTree(self, A):
        # write your code here
        stk = []
        for ele in A:
            node = TreeNode(ele)
            while stk and ele > stk[-1].val:
                node.left = stk.pop()
            if stk:
                stk[-1].right = node
            stk.append(node)
        return stk[0]

s = Solution()
print s.maxTree([2, 5, 6, 0, 3, 1])