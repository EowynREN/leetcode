class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 首先求出nums的前缀和数组 然后将前缀和数组扫一遍
        # 每扫到一个位置就将答案加上前面(k-prefixSum)出现次数（出现次数可以用dict维护） 再将当前前缀和prefixSum在出现的次数+1

        prefix = [0] * (len(nums) + 1)
        prefix[0] = 0
        count = {0: 1}  # 什么都没有的时候sum是0，这个情况算1个instance
        res = 0
        for i in range(1, len(nums) + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]

            need = prefix[i] - k
            if need in count:
                res += count[need]

            if prefix[i] in count:
                count[prefix[i]] += 1
            else:
                count[prefix[i]] = 1
        return res