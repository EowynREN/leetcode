#-*- coding:utf8 -*-
#coding=utf-8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 与105几乎一模一样,只有递归时的index manipulation有差别
# worst case: O(n^2) -> 每一层只有左节点或只有有节点,层数是n,每层搜max value最坏可能每次都在最后O(n)  -> O(n^2)
# avg: O(nLogn) -> 每次最大值都在中间, half to left sub tree, half to right sub tree (类似快排的平均复杂度),树的平均深度是logn,每层搜max value右用时O(n)-> O(nLogn)
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None

        # 后序遍历,root在末端
        root = TreeNode(postorder[-1])

        # 找到root在中序中的位置
        position = 0
        for i in range(len(inorder)):
            if root.val == inorder[i]:
                position = i
                break

        root.left = self.buildTree(inorder[: position], postorder[: position])
        root.right = self.buildTree(inorder[position + 1: ], postorder[position: len(postorder) - 1])

        return root

s = Solution()
print s.buildTree([9,3,15,20,7], [9,15,7,20,3])