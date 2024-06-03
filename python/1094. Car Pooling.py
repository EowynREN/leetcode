class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        """
        差分数组的神奇指出
        """
        nums = [0] * 1001
        df = Difference(nums)

        for trip in trips:
            val = trip[0]
            i = trip[1]
            j = trip[2] - 1

            df.increment(i, j, val)

        res = df.result()
        for i in range(len(res)):
            if res[i] > capacity:
                return False
        return True


class Difference(object):
    def __init__(self, nums):
        self.diff = [0] * len(nums)
        self.diff[0] = nums[0]

        for i in range(1, len(nums)):
            self.diff[i] = nums[i] - nums[i - 1]

    def increment(self, i, j, val):
        self.diff[i] += val
        if j + 1 < len(self.diff):
            self.diff[j + 1] -= val

    def result(self):
        res = [0] * len(self.diff)
        res[0] = self.diff[0]

        for i in range(1, len(self.diff)):
            res[i] = res[i - 1] + self.diff[i]
        return res

