# class Solution:
#     # @param {string} s a string
#     # @param {set[str]} wordDict a set of words
#     def wordBreak(self, s, wordDict):
#         # Write your code here
#         if len(s) == 0 and len(wordDict) == 0:
#             return [""]
#
#         n = len(s)
#         dp = [False for i in range(n + 1)]
#         dp[0] = True
#
#         maxLen = max([len(w) for w in wordDict])
#         for i in range(1, n + 1):
#             for j in range(1, min(i, maxLen) + 1):
#                 if dp[i - j] and s[i - j: i] in wordDict:
#                     dp[i] = True
#
#         res = []
#         self.dfs(s, wordDict, dp[1:], 0, [], res)
#         return res
#
#     def dfs(self, s, wordDict, dp, index, tmp, res):
#         if index == len(s) and self.check:
#             res.append(self.transform(tmp))
#             return
#
#         for i in range(index, len(s)):
#             if not dp[i]:
#                 continue
#
#             sub = s[index: i + 1]
#
#             if sub not in wordDict:
#                 continue
#
#             tmp.append(sub)
#             self.dfs(s, wordDict, dp, i + 1, tmp, res)
#             del tmp[-1]
#
#     def check(self, s, tmp):
#         sum_len = sum([len(sub) for sub in tmp])
#         return sum_len == len(s)
#
#     def transform(self, tmp):
#         s = ""
#         for i in range(len(tmp) - 1):
#             s += tmp[i] + " "
#
#         s += tmp[-1]
#         return s
class Solution:
    # @param {string} s a string
    # @param {set[str]} wordDict a set of words
    def wordBreak(self, s, wordDict):
        # Write your code here
        if len(s) == 0 and len(wordDict) == 0:
            return ['']

        if len(s) == 0 or len(wordDict) == 0:
            return []

        # 这个二维的矩阵是为了优化,是的查看s[i:j]是否是word的时间为O(1)
        n = len(s)
        isWord = [[False for j in range(n)] for i in range(n)]

        for i in range(n):
            for j in range(i, n):
                if s[i: j + 1] in wordDict:
                    isWord[i][j] = True

        dp = [False for i in range(n + 1)]
        dp[0] = True


        # 因为isWord初始化的是上方斜半个矩阵
        # 因此此处i, j也要在上半个斜举证里
        for i in range(n):
            for j in range(i, n):
                if dp[i] and isWord[i][j]:
                    dp[j + 1] = True
                    break

        res = []
        self.dfs(s, isWord, dp, 0, [], res)
        return res

    def dfs(self, s, isWord, dp, index, tmp, res):
        if index == len(s):
            res.append(self.transform(tmp))
            return

        # 如果之前都不是word,那么肯定不能连成句子
        # 直接砍掉这个branch返回
        if not dp[index]:
            return

        for i in range(index, len(s)):
            if not isWord[index][i]:
                continue

            tmp.append(s[index: i + 1])
            self.dfs(s, isWord, dp, i + 1, tmp, res)
            del tmp[-1]

    def transform(self, tmp):
        s = ''

        for i in range(len(tmp) - 1):
            s += tmp[i] + ' '
        s += tmp[-1]

        return s

s = Solution()
print s.wordBreak("catsanddog", ["cat","cats","and","sand","dog"])