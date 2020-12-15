#-*- coding:utf8 -*-
#coding=utf-8

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
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if not wordDict:
            return []

        n = len(s)
        # 这个二维的矩阵是为了优化,使得查看s[i:j]是否是word的时间为O(1)
        isWord = [[False for j in xrange(n)] for i in xrange(n)]

        for i in xrange(n):
            for j in xrange(i, n):
                if s[i:j + 1] in wordDict:
                    isWord[i][j] = True

        # dp[i]表示i~n是否可以组成valid sentence
        # 这个dp数组将用于dfs的剪枝, 与word break I dp数组的方向相反
        #            （word break I中dp[i]表示0~i是否可以组成valid sentence）
        dp = [False for i in range(n + 1)]
        dp[n] = True

        for i in xrange(n - 1, -1, -1):
            for j in xrange(i, n):
                if dp[j + 1] and isWord[i][j]:
                    dp[i] = True
                    break

        res = []
        self.dfs(s, 0, [], dp, isWord, res)
        return res

    def dfs(self, s, index, path, dp, isWord, res):
        if index == len(s):
            res.append(self.transform(path))
            return

        # 如果之前都不是word,那么肯定不能连成句子
        # 直接砍掉这个branch返回
        if not dp[index]:
            return

        for i in xrange(index, len(s)):
            if not isWord[index][i]:
                continue

            path.append(s[index: i + 1])
            self.dfs(s, i + 1, path, dp, isWord, res)
            del path[-1]

    def transform(self, path):
        s = ""
        for i in xrange(len(path) - 1):
            s += path[i] + " "
        s += path[-1]

        return s


s = Solution()
print s.wordBreak("catsanddog", ["cat","cats","and","sand","dog", "ddog", "san", "an"])
print s.wordBreak("aaaaaaaaaaaaaaaaaabaaaaaaaaaaaaa",["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])