class Solution:
    """
    @param nums: A list of integers.
    @return: A list of unique permutations.
    """
    def permuteUnique(self, nums):
        # write your code here
        # 1. input: a list of numbers
        # 2. output: a list of lists
        # 3. key concept: all unique permutations ----> recursion / dfs
        #                 recursion interface ----> helper(self, res, tmp, nums, visited)
        #                 end of recursion ----> run out all elements in nums every recursion
        #                 recursion blocks ----> each recursion level append a num
        #                 when to append ----> each candidate permutation is valid (means has the same length with nums)
        #                 how to skip duplicates ----> visited[]!!!!!
        # 4. edge case: [] ----> return [[]]
        # 5. TDD - test case: [1, 2, 2, 2]
        # 6. reminder: duplicate numbers exist

        res = []
        visited = [0 for i in range(len(nums))]
        # 注意: 此处sort是为了使duplicate能够紧挨着,这样才能使用line 46的while条件来skip
        self.helper(res, [], sorted(nums), visited)
        return res

    def helper(self, res, tmp, nums, visited):
        if len(tmp) == len(nums):
            # reminder: must be list(tmp) instead of tmp
            #           create a new space, otherwise res content will change when tmp changes
            res.append(list(tmp))
            return

        #DFS
        i = 0
        while i < len(nums):
            if visited[i] == 1:
                i += 1
                continue

            tmp.append(nums[i])
            visited[i] = 1
            self.helper(res, tmp, nums, visited)
            visited[i] = 0
            del tmp[-1]

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return
s = Solution()
print s.permuteUnique([3, 3, 0, 3])