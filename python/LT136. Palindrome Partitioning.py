class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        # write your code here
        # 思路：
        # 1. input: string
        # 2. output: list of list
        # 3. key concept: all possible palindrome partition of s ----> dfs
        #                 interface of recursion: dfs(s, index, each_patition, res)
        #                 end of recursion: recursion level == s length
        #                 recursion blocks: end ---> to add patition in res
        #                                   for loop to iterate all in cur level
        #                                   return val
        # 4. edge case: None, ""
        # 5. TDD - test case: "sffaftbt"
        # 6. can add a hashmap to avoid the repeating calling for isPalindrome()
        if s is None or len(s) == 0:
            return []
        res = []
        map = {}
        self.dfs(s, 0, [], res)
        return res


    def dfs(self, s, index, path, res):
        if index == len(s):
            res.append(list(path))
            return

        for i in range(index, len(s)):
            prefix = s[index : i + 1]
            if not self.isPalindrome(prefix):
                continue
            path.append(prefix)
            self.dfs(s, i + 1, path, res)
            del path[-1]

    def isPalindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True