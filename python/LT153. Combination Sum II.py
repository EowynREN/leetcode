class Solution:
    """
    @param candidates: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, candidates, target):
        # write your code here
        res = []
        if candidates:
            self.dfs(sorted(candidates), target, len(candidates), 0, [], res)
        return res

    def dfs(self, candidates, target, n, level, tmp, res):
        if target == 0:
            res.append(list(tmp))
            return

        for i in range(level, n):
            # remove duplicates
            if i != level and candidates[i] == candidates[i - 1]:
                continue

            if target - candidates[i] < 0:
                break

            tmp.append(candidates[i])
            self.dfs(candidates, target - candidates[i], n, i + 1, tmp, res)
            del tmp[-1]

s = Solution()
print s.combinationSum2([7,1,2,5,1,6,10], 8)