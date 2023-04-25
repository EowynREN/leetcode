#-*- coding:utf8 -*-
#coding=utf-8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # 思路: 思考当前这个节点应该做什么?
    #       1. 以这个节点为root的subtree长什么样
    #       2. 以其他节点为root的subtree长什么样
    #       3. 如何让他们被比较
    # 方法: 将每个以当前节点为root的subtree都序列化成字符串,存在一个map里
    #      因为有逗号分隔,因此后续遍历的顺序可以唯一确定一个子树
    #      e.g.,    2          2
    #              /            \
    #             4              4
    #      以上述方法序列化后,分别是 "4,#,2"和"#,4,2",是不一样的

    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        res = []
        self.helper(root, {}, res)
        return res

    def helper(self, node, duplicacy, res):
        if not node:
            return '#'

        left = self.helper(node.left, duplicacy, res)
        right = self.helper(node.right, duplicacy, res)

        # serialize the subtree so it can be compared with each other
        # with ',', a subtree can be uniquely indentified by the following string
        subtree = left + ',' + right + ',' + str(node.val)
        freq = 0 if subtree not in duplicacy else duplicacy[subtree]

        # only append the duplicate subtree when it appear on the second time to avoid multiple appending
        if freq == 1:
            res.append(node)

        duplicacy[subtree] = freq + 1

        return subtree

root = TreeNode(1)
left = TreeNode(2)
right = TreeNode(3)
root.left = left
root.right = right
s = Solution()
print s.findDuplicateSubtrees(root)