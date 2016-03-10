class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        n = len(nums)
        if n < 1:
            return []
        if n == 1:
            return [str(nums[0])]

        nums.append(-1)
        p = nums[0]
        res = []
        for i in range(n):
            if nums[i + 1] - nums[i] > 1 or i == n - 1:
                if p == nums[i]:
                    res.append(str(p))
                else:
                    res.append(str(p) + "->" + str(nums[i]))
                p = nums[i + 1]
        return res
s = Solution()
print s.summaryRanges([1, 3, 4, 6, 7, 8])