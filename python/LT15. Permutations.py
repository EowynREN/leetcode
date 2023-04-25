class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        # 1. input: a list of numbers
        # 2. output: a list of lists
        # 3. key concept: all possible permutations. ----> recursion
        #                 recursion interface ----> helper(self, index, res, tmp, nums)
        #                 end if recursion ----> ru out all the elements in nums
        #                 recursion blocks ---->
        #                 when to append ----> when each candidate permutation is valid (means has the same length with nums)
        # 4. edge case: [] ----> return [[]]
        # 5. TDD - test case: [1, 2, 3, 4, 5]

        res = []

        self.helper(res, [], nums)
        return res

    def helper(self, res, tmp, nums):
        if len(tmp) == len(nums):
            # reminder: must be list(tmp) instead of tmp
            #           create a new space, otherwise res content will change when tmp changes
            res.append(list(tmp))
            return

        # DFS
        for i in range(len(nums)):
            if nums[i] in tmp:
                continue
            tmp.append(nums[i])
            self.helper(res, tmp, nums)
            del tmp[-1]
        return