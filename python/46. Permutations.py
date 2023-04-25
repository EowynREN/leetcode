class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        visited, res = set(), []
        self.dfs(nums, [], visited, res)
        return res

    def dfs(self, nums, path, visited, res):
        if len(path) == len(nums):
            res.append(list(path))
            return

        for i in xrange(len(nums)):
            if nums[i] in visited:
                continue

            path.append(nums[i])
            visited.add(nums[i])
            self.dfs(nums, path, visited, res)
            visited.remove(nums[i])
            path.pop()