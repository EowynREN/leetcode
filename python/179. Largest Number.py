class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        n = len(nums)
        if not nums:
            return 0

        if n == 1:
            return str(nums[0])

        self.split(nums, 0, n - 1)

        i= 0
        while i < n and nums[i] == 0:
            i += 1

        if i == n:
            return "0"
        return ''.join(str(num) for num in nums[i:])

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

        while i <= mid and j <= right:
            if int(str(nums[i]) + str(nums[j])) - int(str(nums[j]) + str(nums[i])) > 0:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1

        while i <= mid:
            temp.append(nums[i])
            i += 1

        while j <= right:
            temp.append(nums[j])
            j += 1

    def copyArray(self, nums, temp, left, right):
        for i in range(left, right + 1):
            nums[i] = temp[i - left]

s = Solution()
print s.largestNumber([0, 0])