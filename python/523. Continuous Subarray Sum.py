class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # 子数组的和：preSum[j] - preSum[i]
        # 是否为K倍：(preSum[j] - preSum[i])% k == 0
        # (preSum[j] - preSum[i]) % k == 0   等价于   preSum[j] % k == preSum[i] % k
        if not nums:
            return False

        prefix = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]

        valToIndex = {}
        for i in range(len(prefix)):
            val = prefix[i] % k
            if val not in valToIndex:
                valToIndex[val] = i

        for j in range(1, len(prefix)):
            need = prefix[j] % k
            if need in valToIndex and j - valToIndex[need] >= 2:
                return True
        return False
