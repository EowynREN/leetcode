#-*- coding:utf8 -*-
#coding=utf-8

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[i]表示以nums[i]为结尾的最长递增子序列(LIS)的长度

        # 根据刚才我们对 dp 数组的定义，现在想求 dp[5] 的值，也就是想求以 nums[5] 为结尾的最长递增子序列。
        #   nums[5] = 3，既然是递增子序列，我们只要找到前面那些结尾比 3 小的子序列，然后把 3 接到最后，
        #   就可以形成一个新的递增子序列，而且这个新的子序列长度加一。

        # base case: 每个字符的最长递增子序列都是自己,因此为1
        dp = [1 for i in range(len(nums))]

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        lenOfLIS = 0
        for i in range(len(nums)):
            lenOfLIS = max(lenOfLIS, dp[i])
        return lenOfLIS

class Solution2(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 耐心排序(patience sort) + binary search的解法

        top = [0] * len(nums)
        piles = 0 # 牌堆数初始化为 0
        for i in range(len(nums)):
            left, right = 0, piles
            poker = nums[i] # 要处理的扑克牌

            # ***** 搜索左侧边界的二分查找 *****
            while left < right:
                mid = left + (right - left) / 2
                if top[mid] < poker:
                    left = mid + 1
                else:
                    right = mid

            # 没找到合适的牌堆，新建一堆
            if left == piles:
                piles += 1

            # 把这张牌放到选中的牌堆顶
            top[left] = poker

        # 牌堆数就是 LIS 长度
        return piles

