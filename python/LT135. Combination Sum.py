class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        # write your code
        res = []
        if not candidates or target > 0:
            self.dfs(sorted(candidates), target, 0, 0, [], res)
        return res

    def dfs(self, candidates, target, index, sum, tmp, res):
        # 递归的出口
        if sum == target:
            res.append(list(tmp))
            return

        # 递归饿出口
        if sum > target:
            return

        i = index
        while i < len(candidates):
            # dfs加一个
            tmp.append(candidates[i])
            # dfs
            self.dfs(candidates, target, index, sum + candidates[i], tmp, res)
            # dfs 删一个
            del tmp[-1]

            # avoid duplicate
            if i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            # avoid looking back
            index = i + 1
            i += 1

s = Solution()
print s.combinationSum([2,2,3], 7)