# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {int} the length of the longest consecutive sequence path

    # 思路: 与在一个数组里找最大一样
    #      遍历一颗树, 用一个成员变量来储存最大值
    #      这里唯一需要注意的地方是
    #                          当不再连续的时候,需要把当前子树的seq的值变成0

    def __init__(self):
        self.max_seq = 0

    def longestConsecutive(self, root):
        # Write your code here
        seq = self.helper(root)
        return self.max_seq

    def helper(self, node):
        if not node:
            return 0

        left_seq = self.helper(node.left)
        right_seq = self.helper(node.right)

        if node.left and left_seq != 0:
            # 不再连续的时候,需要把当前子树的seq的值变成0
            if node.left.val - 1 != node.val:
                self.max_seq = max(self.max_seq, left_seq)
                left_seq = 0
            # 仍然连续, 更新最大值, 把当前的父节点也算上
            else:
                self.max_seq = max(self.max_seq, left_seq + 1)

        if node.right and right_seq != 0:
            # 不再连续的时候,需要把当前子树的seq的值变成0
            if node.right.val - 1 != node.val:
                self.max_seq = max(self.max_seq, right_seq)
                right_seq = 0
            # 仍然连续, 更新最大值, 把当前的父节点也算上
            else:
                self.max_seq = max(self.max_seq, right_seq + 1)

        seq = max(left_seq, right_seq)
        return seq + 1

# simplified version 2
class Solution2:
    # @param {TreeNode} root the root of binary tree
    # @return {int} the length of the longest consecutive sequence path

    def __init__(self):
        self.longest = 0

    def longestConsecutive(self, root):
        # Write your code here
        self.helper(root)
        return self.longest

    def helper(self, node):
        if not node:
            return 0

        left = self.helper(node.left)
        right = self.helper(node.right)

        subtree_longest = 1  # at least we have root
        if node.left and node.left.val - 1 == node.val:
            subtree_longest = max(subtree_longest, left + 1)

        if node.right and node.right.val - 1 == node.val:
            subtree_longest = max(subtree_longest, right + 1)

        if subtree_longest > self.longest:
            self.longest = subtree_longest

        return subtree_longest

t0 = TreeNode(2)
t1 = TreeNode(3)
t0.right = t1
t2 = TreeNode(2)
t1.left = t2
t3 = TreeNode(1)
t2.left = t3

s = Solution()
print s.longestConsecutive(t0)