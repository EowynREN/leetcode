"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths
    def binaryTreePathSum(self, root, target):
        # Write your code here
        res = []
        if root:
            self.dfs(root, target - root.val, [root.val], res)
        return res

    def dfs(self, node, target, tmp, res):
        # 达到叶子节点
        if not node.left and not node.right:
            # 路径上的值相加为target, 纳入结果集
            if target == 0:
                res.append(list(tmp))
                return

        # 可能会有target为负数的情况
        # if target < 0:
        #     return

        if node.left:
            tmp.append(node.left.val)
            self.dfs(node.left, target - node.left.val, tmp, res)
            del tmp[-1]

        if node.right:
            tmp.append(node.right.val)
            self.dfs(node.right, target - node.right.val, tmp, res)
            del tmp[-1]

t0 = TreeNode(1)
t1 = TreeNode(2)
t2 = TreeNode(2)
t3 = TreeNode(4)
t4 = TreeNode(3)

t0.left = t1
t0.right = t3

t1.left = t2
t1.right = t4

s = Solution()
print s.binaryTreePathSum(t0, 5)