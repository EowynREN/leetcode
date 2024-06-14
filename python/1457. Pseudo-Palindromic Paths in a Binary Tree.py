# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
如果一组数字中，只有最多一个数字出现的次数为奇数，剩余数字的出现次数均为偶数，那么这组数字可以组成一个回文串

1、用到异或运算的特性，1 ^ 1 = 0, 0 ^ 0 = 0, 1 ^ 0 = 1。

2、其次用到 n & (n - 1) 去除二进制最后一个 1 的技巧
"""


class Solution(object):
    def __init__(self):
        self.res = 0

    def pseudoPalindromicPaths(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.traverse(root, 0)
        return self.res

    def traverse(self, node, count):
        if not node:
            return

        if not node.left and not node.right:
            count = count ^ (1 << node.val)  # XOR除去所有偶数次出现的value
            # 判断奇数次出现的value是否最多只有一个，如果出现两个以上的value，其出现次数都是奇数次，则无法构成palindrome
            if count & (count - 1) == 0:
                self.res += 1
            return

        self.traverse(node.left, count ^ (1 << node.val))
        self.traverse(node.right, count ^ (1 << node.val))
