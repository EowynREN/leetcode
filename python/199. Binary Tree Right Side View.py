# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
二叉树的递归分为「遍历」和「分解问题」两种思维模式，这道题需要用到「遍历」的思维。

1、用 BFS 层序遍历算法，每一层的最后一个节点就是二叉树的右侧视图。我们可以把 BFS 反过来，从右往左遍历每一行，进一步提升效率。
2、用 DFS 递归遍历算法，同样需要反过来，先递归 root.right 再递归 root.left，同时用 res 记录每一层的最右侧节点作为右侧视图。
"""

# 1、BFS 层遍历
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        res = []
        queue = [root]
        while queue:
            count = len(queue)

            for i in range(count):
                node = queue.pop(0)
                if i == 0:
                    res.append(node.val)

                if node.right:
                    queue.append(node.right)

                if node.left:
                    queue.append(node.left)
        return res

# DFS 递归遍历
class Solution2(object):
    def __init__(self):
        self.res = []

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.traverse(root, 1)
        return self.res

    def traverse(self, node, depth):
        if not node:
            return

        if len(self.res) < depth:
            self.res.append(node.val)

        self.traverse(node.right, depth + 1)
        self.traverse(node.left, depth + 1)
