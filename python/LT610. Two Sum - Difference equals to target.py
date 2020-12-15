class Pair:
    def __init__(self, i, num):
        self.index = i
        self.num = num

class Solution:
    """
    @param nums {int[]} n array of Integer
    @param target {int} an integer
    @return {int[]} [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum7(self, nums, target):
        # Write your code here
        if len(nums) < 2:
            return [0, 0]

        n = len(nums)
        target = abs(target)
        pairs = [Pair(i, nums[i]) for i in range(n)]

        pairs = sorted(pairs, key=lambda x: x.num)

        i, j = 0, 1
        while i < n:
            if i == j:
                j += 1

            while j < n and pairs[j].num - pairs[i].num < target:
                j += 1

            if pairs[j].num - pairs[i].num == target:
                if pairs[j].index > pairs[i].index:
                    return [pairs[i].index + 1, pairs[j].index + 1]
                else:
                    return [pairs[j].index + 1, pairs[i].index + 1]

            i += 1
        return [0, 0]

s = Solution()
print s.twoSum7([1,2,5,6,7,3,51,8,-33,-5,-72,12,-34,100,99], -77)