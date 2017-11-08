import sys

class Solution:
    # @param {int[]} nums an array with positive and negative numbers
    # @param {int} k an integer
    # @return {double} the maximum average
    def maxAverage(self, nums, k):
        # Write your code here
        left, right = sys.maxint, -sys.maxint - 1

        for num in nums:
            if num < left:
                left = num

            if num > right:
                right = num

        while right - left >= 1e-6:
            mid = left + (right - left) / 2.0
            if self.check(nums, mid, k):
                left = mid
            else:
                right = mid

        return left

    def check(self, nums, mid, k):
        sums = [0 for i in range(len(nums))]
        sums[0] = nums[0] - mid
        min_pre = 0

        for i in range(1, k):
            sums[i] = sums[i - 1] + (nums[i] - mid)

        if sums[k - 1] >= 0:
            return True

        for i in range(k,len(nums)):
            sums[i] = sums[i - 1] + (nums[i] - mid)

            min_pre = min(min_pre, sums[i - k])
 
            if sums[i] - min_pre >= 0:
                return True

        return False

s = Solution()
print s.maxAverage([1, 12, -5, -6, 50, 3], 3)