#-*- coding:utf8 -*-
#coding=utf-8

# 这道「最大子数组和」就和「最长递增子序列」非常类似，dp 数组的定义是「以 nums[i] 为结尾的最大子数组和/最长递增子序列为 dp[i]」。
# 因为只有这样定义才能将 dp[i+1] 和 dp[i] 建立起联系，利用数学归纳法写出状态转移方程

import sys
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 常规dp解法
        dp = [nums[i] for i in range(len(nums))]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])

        res = -sys.maxsize - 1
        for i in range(len(dp)):
            res = max(res, dp[i])
        return res

# 上述解法,状态压缩
class Solution2(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_ending_here = nums[0]
        max_so_far = nums[0]

        for i in range(1, len(nums)):
            max_ending_here = max(max_ending_here + nums[i], nums[i])
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far