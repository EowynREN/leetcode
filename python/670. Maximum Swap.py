class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        nums = [int(d) for d in str(num)]
        digit_position = {int(nums[0]): 0}
        for i in range(1, len(nums)):  # record the right most position for the same digit
            digit = int(nums[i])
            digit_position[digit] = i

        for i, d1 in enumerate(nums):
            for d2 in range(9, d1, -1):
                if d2 in digit_position and digit_position[d2] > i:
                    j = digit_position[d2]
                    nums[i], nums[j] = nums[j], nums[i]
                    return self.convertListToInt(nums)
        return num

    def convertListToInt(self, nums):
        res = 0
        for i in range(len(nums)):
            res = res * 10 + nums[i]
        return res
s = Solution()
print(s.maximumSwap(2736))

# digit_position = {2: 0, 7: 1, 3: 2, 8: 3}
# i = [0, ]
# d1 = [2, ]
# d2 = [7]
# j = [1, ]