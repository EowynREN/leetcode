class Solution:
    # @param {int[]} nums a set of distinct positive integers
    # @return {int[]} the largest subset
    def largestDivisibleSubset(self, nums):
        # Write your code here
        if not nums:
            return []

        n = len(nums)
        nums = sorted(nums)

        # 从0到i位置最大的divisible subset（两个数可以整除，整除操作是1次，但是是两个数，所以初始化为1）
        dp = [1] * n
        # 从0到i位置的最大值是基于哪个位置得来的
        pre_record = [-1] * n

        for i in range(n):
            for j in range(i):

                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    pre_record[i] = j

        index_for_max_val = dp.index(max(dp))

        res = []

        # 从最右侧回朔,根据pre_record的记录找到历次的最大值
        while index_for_max_val != -1:
            res.append(nums[index_for_max_val])
            index_for_max_val = pre_record[index_for_max_val]

        # 返回升序的结果
        return list(reversed(res))