class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    # @param A: Given an integer array with no duplicates.
    # @return: The root of max tree.
    def maxTree(self, A):
        # write your code here
        if not A:
            return None

        stack = []
        for i in range(len(A)):
            if not stack or stack[-1].val > A[i]:
                stack.append(TreeNode(A[i]))
            else:
                new_node = TreeNode(A[i])

                node1 = stack.pop()
                while stack and stack[-1].val < A[i]:
                    node2 = stack.pop()
                    node2.right = node1
                    node1 = node2

                new_node.left = node1
                stack.append(new_node)

        root = stack.pop()
        while stack:
            node = stack.pop()
            node.right = root
            root = node
        return root