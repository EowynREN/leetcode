class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        i, n = 0, len(nums)
        res = []
        while i < n:
            p = nums[i]

            #i = n - 1最有项特殊处理
            while i < n - 1 and nums[i + 1] - nums[i] == 1:
                i += 1

            if p == nums[i]:
                res.append(str(p))
            else:
                res.append(str(p) + "->" + str(nums[i]))
            i += 1
        return res