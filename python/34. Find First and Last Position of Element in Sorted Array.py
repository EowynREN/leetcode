#-*- coding:utf8 -*-
#coding=utf-8

# 这道二分的题,两种写法,根据搜索区间分为:
#       1. 左闭右开
#       2. 两端都闭

# =================== 1. 左闭右开的写法 =================== #
class Solution1(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        start, end = -1, -1

        # 寻找start -> 收紧右侧，逼近左端
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) / 2

            if nums[mid] == target:
                right = mid #注意！收缩右侧
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid

        # 没找到target的start,不用继续找,没有start也就没有ending,直接返回[-1, -1]
        if left == len(nums) or nums[left] != target:
            return [-1, -1]

        start = left

        # 寻找ending -> 收紧左侧，逼近右端
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) / 2

            if nums[mid] == target:
                left = mid + 1 #注意！收缩左侧
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid

        # 因为已经有start了，那么一定有ending。所以此处可以不判断是否存在了
        # if right == 0 or nums[right] != target:
        #     return [-1, -1]

        # 这里可以这样记忆:因为右侧是开的,所以这里需要right减一
        end = right - 1

        return [start, end]

# =================== 2. 两端都闭的写法 =================== #
class Solution2(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        start, end = -1, -1

        # 寻找start -> 收紧右侧，逼近左端
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2

            if nums[mid] == target:
                right = mid - 1 #注意！收缩右侧
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        # 没找到target的start,不用继续找,没有start也就没有ending,直接返回[-1, -1]
        if left >= len(nums) or nums[left] != target:
            return [-1, -1]

        start = left

        # 寻找ending -> 收紧左侧，逼近右端
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2

            if nums[mid] == target:
                left = mid + 1 #注意！收缩左侧
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        # 因为已经有start了，那么一定有ending。所以此处可以不判断是否存在了
        # if right < 0 or nums[right] != target:
        #     return [-1, -1]

        end = right

        return [start, end]