class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsets(self, S):
        # write your code here
        # 1. input: a set of numbers
        # 2. output: a list of lists
        # 3. ket concept: all possible subset ----> recursion / dfs
        #                 recursion interface ----> helper(self, index, res, tmp, S)
        #                 end of recursion ----> run out all element in S
        #                 recursion breaking blocks --->
        # 4. edge case: []
        # 5. TDD - test case: [5,4,2,3]
        res = []
        if S:
            # sort S to ensure all subsets are in non-descending order
            self.helper(0, res, [], sorted(S))
        return res

    def helper(self, index, res, tmp, S):
        # reminder: must be list(tmp) instead of tmp
        #           create a new space, otherwise res content will change when tmp changes
        res.append(list(tmp))

        # dfs
        for i in range(index, len(S)):
            tmp.append(S[i])
            self.helper(i + 1, res, tmp, S)
            del tmp[-1]
