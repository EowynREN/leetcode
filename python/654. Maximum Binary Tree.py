#-*- coding:utf8 -*-
#coding=utf-8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 与105,106同一套模板
# worst case: O(n^2) -> 每一层只有左节点或只有有节点,层数是n,每层搜max value右用时O(n) -> O(n^2)
# avg: O(nLogn) -> 每次最大值都在中间, half to left sub tree, half to right sub tree (类似快排的平均复杂度),树的平均深度是logn,每层搜max value右用时O(n)-> O(nLogn)

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums, left, right):
        if left > right:
            return None

        maxVal = nums[left]
        position = left
        for i in range(left, right + 1):
            if nums[i] > maxVal:
                maxVal = nums[i]
                position = i

        root = TreeNode(maxVal)
        root.left = self.helper(nums, left, position - 1)
        root.right = self.helper(nums, position + 1, right)

        return root

s = Solution()
print s.constructMaximumBinaryTree([3,2,1,6,0,5])