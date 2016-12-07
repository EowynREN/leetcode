class Solution:
    '''
    @param {int[]} nums an integer array
    @param {int} k an integer
    @return {int[]} the top k largest numbers in array
    '''
    def topk(self, nums, k):
        # Write your code here
        self.quickSort(nums, 0, len(nums) - 1, k)
        return nums

    def quickSort(self, nums, left, right, k):
        if left >= right:
            return

        i, j = left, right
        pivot = (left + right) / 2

        while i <= j:
            while i <= j and nums[i] > nums[pivot]:
                i += 1

            while i <= j and nums[j] < nums[pivot]:
                j -= 1

            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        self.quickSort(nums, left, j, k)
        self.quickSort(nums, i, right, k)

s = Solution()
print s.topk([3,10,1000,-99,4,100], 3)