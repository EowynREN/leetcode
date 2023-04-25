class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        if not nums:
            return []

        self.quickSort(0, len(nums) - 1, nums)
        return nums

    def quickSort(self,start, end, nums):
        if start >= end:
            return

        pivot = nums[(start + end) / 2]
        i, j = start, end

        while i <= j:
            while i <= j and nums[i] < pivot:
                i += 1

            while i <= j and nums[j] > pivot:
                j -= 1

            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        self.quickSort(start, j, nums)
        self.quickSort(i, end, nums)

s = Solution()

print s.sortColors([2,0,0,1,2,0,2])