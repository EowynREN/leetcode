class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # dp[i]: number of qualified sub-arrays that ending at ith position
        if len(nums) == 0:
            return 0

        sums = [0]  # length = n + 1, make it easy for index manipulation with dp array
        for i in range(1, len(nums) + 1):
            sums.append(sums[i - 1] + nums[i - 1])

        res = 0
        dp = [0 for i in range(len(nums) + 1)]
        for i in range(1, len(nums) + 1):
            for j in range(i - 1, -1, -1):
                if (sums[i] - sums[j]) % k == 0:  # d[j] is dividable and [j, i] is dividable
                    dp[i] = dp[j] + 1
                    res += dp[i]

                    # the first dividable [j, i] is the max number of qualified sub-arrays
                    #        j is the max now and dp[j] will contains more that dp[less that j]
                    break
        return res

s = Solution()
print(s.subarraysDivByK([1, 11, 12, 23, 5], 12))