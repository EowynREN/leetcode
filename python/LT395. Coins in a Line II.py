class Solution:
    """
    @param: values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def firstWillWin(self, values):
        # write your code here
        n = len(values)

        if n <= 2:
            return True

        dp = [0] * (n + 1)
        dp[1] = values[n - 1]
        dp[2] = values[n - 1] + values[n - 2]
        dp[3] = values[n - 3] + values[n - 2]

        for i in range(4, n + 1):
            dp[i] = max(min(dp[i - 2], dp[i - 3]) + values[n - i], min(dp[i - 3], dp[i - 4]) + values[n - i] + values[n - i + 1])
        return dp[n] > sum(values) - dp[n]

s = Solution()
print s.firstWillWin([100,200,400,300,400,800,500,600,1200])