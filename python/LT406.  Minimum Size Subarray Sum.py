class Solution:
     # @param nums: a list of integers
     # @param s: an integer
     # @return: an integer representing the minimum size of subarray
    def minimumSize(self, nums, s):
        # write your code here
        if not nums:
            return -1

        i, j = 0, 0
        sum, res = 0, 2147483647
        while i < len(nums):
            while j < len(nums) and sum < s:
                sum += nums[j]
                j += 1

            if sum >= s:
                res = min(res, j - i)
            sum -= nums[i]
            i += 1
        return res if res != 2147483647 else -1

s = Solution()
print s.minimumSize([2,3,1,2,4,3], 7)