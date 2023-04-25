class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number
             and the index of the last number
    """
    # 思路: 当一个sum已经出现过一次了,那么从这个sum出现的后一个数开始到当前位置,相加的值一定是0
    #      sum表示: 从零到当前这个数的总和
    #      因此如果sum = 2已经出现在record里,那么record[2]所指的位置的下一位,到当前前位置的和一定是零
    #      因为cur sum = 2, sum_was = 2, cur_sum - sum_was = 0
    #                                   这公式的意思就是: 从record[2]所指的位置的下一位,到当前前位置的和一定是零
    def subarraySum(self, nums):
        # write your code here
        # 点睛之处!!!
        record = {0: -1}
        sum = 0

        for i in range(len(nums)):
            sum += nums[i]
            if sum in record:
                return [record[sum] + 1, i]
            record[sum] = i
        return [-1, -1]