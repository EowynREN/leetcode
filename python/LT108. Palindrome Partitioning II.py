class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        # write your code here
        if s is None:
            return 0

        n = len(s)
        # dp[i]表示前i个字符的最小cut
        # 此处为何要初始化成i - 1 ---> 因为"a"   1个字符，只需要切0刀
        #                                  "ab"  2个字符，只需要切1刀
        dp = [i - 1 for i in range(n + 1)]
        # preparation
        isPalindrome = self.getIsPalindrome(s)

        for i in range(n + 1):
            for j in range(i):
                if isPalindrome[j][i - 1]:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[n]


    def getIsPalindrome(self, s):
        n = len(s)
        isPalindrome = [[False for i in range(n)] for i in range(n)]

        # init
        for i in range(n):
            isPalindrome[i][i] = True

        # init for avoiding overflow
        for i in range(n - 1):
            isPalindrome[i][i + 1] = s[i] == s[i + 1]

        for length in range(2, n):
            # left + length < len(s) ---> left < len(s) - length
            for left in range(n - length):
                # right < left + length = n - length + length = n
                right = left + length
                isPalindrome[left][right] = isPalindrome[left + 1][right - 1] and s[left] == s[right]
        return isPalindrome