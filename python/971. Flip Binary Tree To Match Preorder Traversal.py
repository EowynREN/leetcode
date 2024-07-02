# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
用 traverse 函数遍历整棵二叉树，对比前序遍历结果，如果节点的值对不上，就无解；如果子树对不上 voyage，就尝试翻转子树
"""


class Solution(object):
    def __init__(self):
        self.res = []
        self.i = 0
        self.canFlip = True

    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        self.traverse(root, voyage)

        if not self.canFlip:
            return [-1]
        return self.res

    def traverse(self, node, voyage):
        # 一旦发现无解，立刻返回
        if not node or not self.canFlip:
            return

        # 节点的 val 对不上，必然无解
        if node.val != voyage[self.i]:
            self.canFlip = False
            return

        # 此处的i是voyage array的index，所以必须一直增加，才能走遍此处的i是voyage array
        # 不能设在参数里，因为递归函数返回后，i会恢复之前的值
        self.i += 1

        # 前序遍历结果不对，尝试翻转左右子树
        if node.left and node.left.val != voyage[self.i]:
            # 记录翻转节点
            self.res.append(node.val)

            temp = node.left
            node.left = node.right
            node.right = temp

        self.traverse(node.left, voyage)
        self.traverse(node.right, voyage)


