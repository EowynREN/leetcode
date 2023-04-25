"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

import copy
class Solution:
    """
    @param {TreeNode} root The root of the binary tree.
    @param {TreeNode} A and {TreeNode} B two nodes
    @return Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        possible = self.helper(root, A, B)

        if not possible:
            return None

        if self.check(possible, A) and self.check(possible, B):
            return possible
        return None


    def helper(self, node, A, B):
        if node is None or node == A or node == B:
            return node

        left = self.helper(node.left, A, B)
        right = self.helper(node.right, A, B)

        if left and right:
            return node

        if left:
            return left

        if right:
            return right

        return None

    def check(self, node, either):
        if node is None or either == node:
            return node

        left = self.check(node.left, either)
        right = self.check(node.right, either)

        if left:
            return left

        if right:
            return right

        return None




###################################################
##################### version 2 ###################
###################################################


class ResultType:
    def __init__(self, a_exist, b_exist, node):
        self.a_exist = a_exist
        self.b_exist = b_exist
        self.node = node

class Solution2:
    """
    @param {TreeNode} root The root of the binary tree.
    @param {TreeNode} A and {TreeNode} B two nodes
    @return Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        rt = self.helper(root, A, B)

        if rt.a_exist and rt.b_exist:
            return rt.node
        return None

    def helper(self, node, A, B):
        # 到底了
        if node is None:
            return ResultType(False, False, None)

        # 分别问左右分支：是否有A或B
        left_rt = self.helper(node.left, A, B)
        right_rt = self.helper(node.right, A, B)

        # 在当前节点，或其左右分支里存在A
        a_exist = left_rt.a_exist or right_rt.a_exist or node == A

        # 在当前节点，或其左右分支里存在B
        b_exist = left_rt.b_exist or right_rt.b_exist or node == B

        # 如果当前节点就是A（或B
        # 把当前节点放到结果里，然后标记a_exist（或b_exist）为true
        if node == A or node == B:
            return ResultType(a_exist, b_exist, node)

        # 如果当前节点的左右分支里都找到了A和B，那么返回当前节点作为LCA
        if left_rt.node and right_rt.node:
            return ResultType(a_exist, b_exist, node)

        # 如果只在左分支里找到了A（或B），
        # 把左分支里的A（或B）放到结果里，然后标记a_exist（或b_exist）为true
        if left_rt.node:
            return ResultType(a_exist, b_exist, left_rt.node)

        # 如果只在右分支里找到了A（或B），
        # 把右分支里的A（或B）放到结果里，然后标记a_exist（或b_exist）为true
        if right_rt.node:
            return ResultType(a_exist, b_exist, right_rt.node)

        # 如果左右分支里都没有找到，返回null，并标记A和B 在当当前的分支里没找到
        return ResultType(a_exist, b_exist, None)


t0 = TreeNode(1)
t1 = TreeNode(2)
t0.left = t1

s = Solution()
print s.lowestCommonAncestor3(t0, t1, TreeNode(3))