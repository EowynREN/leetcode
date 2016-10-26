class Solution:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, S):
        # write your code here
        # 1. input: a set of numbers
        # 2. output: a list of lists
        # 3. key concept: all possible subsets ----> recursion / dfs
        #                 recursion interface ----> help(self, index, res, S)
        #                 end of recursion ----> run out all element in S
        #                 where to append res ----> begin of func
        # 4. edge case: S = []
        # 5. TDD - test case: [1,2,2,3]
        res = []
        if S:
            res = []
            # sort S to ensure all subsets are in non-descending order.
            self.help(0, res, [], sorted(S))
        return res

    def help(self, index, res, tmp, S):
        # dfs
        res.append(list(tmp))
        for i in range(index, len(S)):
            # skip the duplicates
            if i > index and S[i] == S[i - 1]:
                continue
            tmp.append(S[i])
            self.help(i + 1, res, tmp, S)
            del tmp[-1]