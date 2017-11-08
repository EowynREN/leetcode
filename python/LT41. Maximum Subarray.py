class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        if not nums:
            return -2147483648

        maxSum, sum = -2147483648, 0
        for i in range(len(nums)):
            if sum >= 0 and sum + nums[i] > 0:
                sum += nums[i]
                maxSum = max(maxSum, sum)
            else:
                sum = 0
                maxSum = max(maxSum, nums[i])
        return maxSum

    # version 2  2017.11.08
    def maxSubArray(self, nums):
        # write your code here
        # 如果没有数,那么和就是0,意味没有
        if not nums:
            return 0

        mx = sums = nums[0]
        for i in xrange(1, len(nums)):
            sums = max(nums[i], sums + nums[i])
            mx = max(mx, sums)
        return mx


s = Solution()
print s.maxSubArray([-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-1000])