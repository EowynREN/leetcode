class Solution:
    # @param word1 & word2: Two string.
    # @return: The minimum number of steps.
    def minDistance(self, word1, word2):
        # write your code here
        if len(word1) == 0 and len(word2) == 0:
            return 0
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)

        n, m = len(word1), len(word2)
        dp = [[0 for j in range(m + 1)] for i in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = i

        for j in range(m + 1):
            dp[0][j] = j

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])
                if word1[i - 1] != word2[j - 1]:
                    dp[i][j] += 1
        return dp[n][m]

s = Solution()
print s.minDistance("sea", "ate")