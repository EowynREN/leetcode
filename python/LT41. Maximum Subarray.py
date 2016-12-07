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

s = Solution()
print s.maxSubArray([-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-1000])