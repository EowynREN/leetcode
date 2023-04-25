"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""

# 思路:
#      dfs(findsum) in dfs(dfs)
#      对于每一个node, 都将他作为root进行(上, 左, 右)遍历 ---- dfs function
#      在当前node作为root的时候,要注意不要走回头路,这样可能导致死循环,或者某一个node的值在一个solution里重复出现

#      如树{1, 2, 3, 4}, target = 6
#      正确答案是: [[2, 1, 3], [3, 1, 2], [2, 4], [4, 2]]
#      但如果走回头路,则可能出现 [1, 2, 1, 2]这样的解出现

#      为了保证不走回头路, 可以用一个变量father来记录上一层的节点
#      如果指针在find sum是等于father了,说明走回头路了
class Solution:
    # @param {ParentTreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths
    def binaryTreePathSum3(self, root, target):
        # Write your code here
        res = []
        if root:
            self.dfs(root, target, res)
        return res

    def dfs(self, node, target, res):
        if not node:
            return

        self.findSum(node, target, None, [], res)

        self.dfs(node.left, target, res)
        self.dfs(node.right, target, res)

    def findSum(self, node, target, father, path, res):
        path.append(node.val)
        target -= node.val

        if target == 0:
            res.append(list(path))

        if node.parent not in [None, father]:
            self.findSum(node.parent, target, node, path, res)

        if node.left not in [None, father]:
            self.findSum(node.left, target, node, path, res)

        if node.right not in [None, father]:
            self.findSum(node.right, target, node, path, res)

        del path[-1]