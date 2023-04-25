class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        if not nums or len(nums) <= 1:
            return

        left, right = 0, len(nums) - 1
        i = 0
        while i <= right:
            if nums[i] == 0:
                self.swap(nums, left, i)
                left += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                self.swap(nums, right, i)
                right -= 1
        return nums

    def swap (self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

s = Solution()
print s.sortColors([2,0,0,1,2,0,2])