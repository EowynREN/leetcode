class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n < 3:
            return 0

        count = 0
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            left, right = i + 1, n - 1

            while left < right:
                #if nums[i] + nums[left] + nums[right] < target, each item k between left and right
                # its sum nums[i] + nums[left] + nums[k]  must < target
                if nums[i] + nums[left] + nums[right] < target:
                    count += right - left
                    left += 1
                else:
                    right -= 1
        return count