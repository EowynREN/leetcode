"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Result:
    def __init__(self):
        self.sum = -2147483648
        self.num = 0

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the root of the maximum average of subtree

    # 思路: 与minimum subtree一样的思路
    #       唯一此处需要注意的是: avg (sum / num)会得到一个浮点数
    #       而浮点数的比较比较麻烦
    #       最好是直接保存sum和num在一个类里
    #       在比较的时候转换成乘法来计算, 这样就是整数的比较了
    def __init__(self):
        self.max_subtree = None
        self.result = Result()

    def findSubtree2(self, root):
        # Write your code here
        self.helper(root, 0)
        return self.max_subtree

    def helper(self, node, num):
        if not node:
            return 0, 0

        left_sum, left_num = self.helper(node.left, num)
        right_sum, right_num = self.helper(node.right, num)

        num = left_num + right_num + 1

        sum = left_sum + right_sum + node.val

        # 因为用avg来进行比较, (sum/num)会产生浮点数
        # 浮点数的比较麻烦, 最好使用相乘的办法
        # 例: sum0 / num0 > sum1 / num1
        #     等同于 sum0 * num1 > sum1 * num0
        if self.result.sum * num < sum * self.result.num:
            self.result.sum = sum
            self.result.num = num

            self.max_subtree = node

        return sum, num