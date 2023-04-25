class Solution:
    # @param {int[]} nums an integer array
    # @param {int} target an integer
    # @return {int} the difference between the sum and the target
    def twoSumCloset(self, nums, target):
        # Write your code here
        if not nums:
            return 2147483647

        if len(nums) == 1:
            return 2147483647

        nums = sorted(nums)
        minDiff = 2147483647
        left, right = 0, len(nums) - 1
        while left < right:
            minDiff = min(minDiff, abs(nums[left] + nums[right] - target))
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
        return minDiff

s = Solution()
print s.twoSumCloset([-1,2,1,-4], 4)