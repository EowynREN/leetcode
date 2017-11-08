#-*- coding:utf8 -*-
#coding=utf-8
class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # 思路：把每个单词单独拿出来作为s，剩下的作为worDict，这就是一道需要做N次的word Break I
        #      时间复杂度是n^3，如果纯做n次word break的话会TLE
        # 优化：把words按长度排序，因为长度短的word是不可能有长的word的组成的（应该是反过来）
        #      这样对于短的word来说，它的wordDict会少很多
        if not words:
            return []

        words.sort(key = len)

        res = []
        wordDict = set()
        for word in words:
            if self.wordBreak(word, wordDict):
                res.append(word)
            # 把短的word放进来，以备之后长的word用
            wordDict.add(word)
        return res

    def wordBreak(self, s, wordDict):
        if not s or not wordDict:
            return False

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in xrange(1, n + 1):
            for j in xrange(i):
                if dp[j] and s[j: i] in wordDict:
                    dp[i] = True
                    break
        return dp[n]


s = Solution()
print s.findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"])