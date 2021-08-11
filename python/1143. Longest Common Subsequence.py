class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """

        n, m = len(text1), len(text2)

        # dp[i][j] means the length of LCS for substring end with i in text1 and substring end with j in text2
        dp = [[0 for j in range(m + 1)] for i in range(n + 1)]

        # base case: text1 to "", LCS is 0
        #            "" to text2, LCS is 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # current char are same in text1 and text2, +1 for LCS
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else: # find the longest so far
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[n][m]