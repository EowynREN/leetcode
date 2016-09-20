class Solution:
    # @param {integer[]} nums
    # @return {integer[]} nums

    def sortIntegers(self, nums):
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, nums, left, right):
        if left >= right:
            return

        i, j = left, right
        pivot = nums[(left + right) / 2]

        while i <= j:
            while i <= j and nums[i] < pivot:
                i += 1

            while i <= j and nums[j] > pivot:
                j -= 1

            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        self.quickSort(nums, left, j)
        self.quickSort(nums, i, right)

s = Solution()
print s.sortIntegers([5, 6, 7, 3, 5, 10, 29, 3, 0, 4])