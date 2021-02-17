#-*- coding:utf8 -*-
#coding=utf-8

class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        # left和right指针之间,夹有一个山峰
        # 一定会先单调增(山峰的左边),然后单调减(山峰的右边)
        left, right = 0, len(nums) - 1

        while left + 1 < right:
            mid = left + (right - left) / 2

            # 山峰
            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return nums[mid]
            # 单调增(山峰的左边)
            elif nums[mid - 1] < nums[mid] < nums[mid + 1]:
                left = mid
            # 单调减(山峰的右边)
            elif nums[mid - 1] > nums[mid] > nums[mid + 1]:
                right = mid

        return max(nums[left], nums[right])

s = Solution()
print s.mountainSequence([10,9,8,7])