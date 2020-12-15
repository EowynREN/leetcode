class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number
             and the index of the last number
    """
    # 思路: 跟subarray sum类似，用一个array存从0到i的sum,然后sort一下，相邻两个找最小的差值
    def subarraySumClosest(self, nums):
        # write your code here
        if not nums:
            return [-1, -1]

        if len(nums) == 1:
            return [0, 0]

        # sum[i]表示从0 -> i的sum
        # tuple表示(sum, index)
        sum = [(0, 0)] * len(nums)
        sum[0] = (nums[0], 0)
        for i in range(1, len(nums)):
            sum[i] = (sum[i - 1][0] + nums[i], i)

        # SUM中的和啦sort
        # 现在sum中所有的已经有序
        res = [0, 0]
        sum.sort()
        minDiff = 2147483647
        # 找相邻的和,并比较差值, 因为已经sort了,相邻和的差值一定比不相邻的差值小
        # 找到较小的minDiff, 就更新一下答案
        for i in range(1, len(nums)):
            if sum[i][0] - sum[i - 1][0] < minDiff:
                minDiff = sum[i][0] - sum[i - 1][0]
                res[0] = min(sum[i - 1][1], sum[i][1]) + 1
                res[1] = max(sum[i - 1][1], sum[i][1])
        return res

s = Solution()
print s.subarraySumClosest([-3,1,1,-3,5])