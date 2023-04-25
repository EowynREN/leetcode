class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        # variant of LCS (NO. 1143)
        # The result after deletion of two string is LCS
        # dp[i][j] means the lowest accmulated ACSII value for substring s1 end on i and substring s2 end on j

        n, m = len(s1), len(s2)
        dp = [[0 for j in range(m + 1)] for i in range(n + 1)]

        # init cases
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])

        for j in range(1, m + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])


        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]: # this char should remain in LCS, no deletion
                    dp[i][j] = dp[i - 1][j - 1]
                else: # deletion occur, accmulated ACSII value and record the lower value
                    dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]), dp[i][j - 1] + ord(s2[j - 1]))
        return dp[n][m]


s = Solution()
print(s.minimumDeleteSum("ab", "abc"))