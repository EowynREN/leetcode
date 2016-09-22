class Solution:
    # @param {integer[]} nums
    # @return {string}
    def sortIntegers(self, nums):
        self.split(nums, 0, len(nums) - 1)
        return nums

    def split(self, nums, left, right):
        if left == right:
            return

        mid = left + (right - left) / 2
        self.split(nums, left, mid)
        self.split(nums, mid + 1, right)

        temp = [] #work array
        self.merge(nums, temp, left, mid, right)
        self.copyArray(nums, temp, left, right)


    def merge(self, nums, temp, left, mid, right):

        i, j = left, mid + 1
        for k in range(left, right + 1):

            if i <= mid and (j > right or nums[i] < nums[j]):
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1

    def copyArray(self, nums, temp, left, right):
        for i in range(left, right + 1):
            nums[i] = temp[i - left]

s = Solution()
print s.sortIntegers([10,9,8,7,6,5,4,3,2,1])
