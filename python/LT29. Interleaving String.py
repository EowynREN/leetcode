class Solution:
    """
    @params s1, s2, s3: Three strings as description.
    @return: return True if s3 is formed by the interleaving of
             s1 and s2 or False if not.
    @hint: you can use [[True] * m for i in range (n)] to allocate a n*m matrix.
    """
    def isInterleave(self, s1, s2, s3):
        # write your code here
        n, m, k = len(s1), len(s2), len(s3)

        if n + m != k:
            return False

        # 定义为s1 (前i个字符) s2(前j个字符) s3(i+j 个字符) 是不是交叉字符
        dp = [[False for j in range(m + 1)] for i in range(n + 1)]
        dp[0][0] = True  # s1 = "", s2 = "", s3 = ""

        for i in range(1, n + 1):
            # s1前i - 1个字符与s3是交叉字符
            # and s1第i个字符 == s3第i个字符
            if dp[i - 1][0] and s1[i - 1] == s3[i - 1]:
                dp[i][0] = True

        for j in range(1, m + 1):
            # s2前i - 1个字符与s3是交叉字符
            # and s2第i个字符 == s3第i个字符
            if dp[0][j - 1] and s2[j - 1] == s3[j - 1]:
                dp[0][j] = True

        # 递推公式： (s1.i == s3.(i+j) and dp[i-1][j]) or (s2.j == s3.(i+j) and dp[i][j - 1])
        # 分别从s1,s2两种可能性来匹配 ，两者有一个成立就行了。
        #   s1 s3 首字母相同，继续查s1第i -1 与 s3第 i + j -1 是否isInterleave1
        #   s2 s3 首字母相同，继续查s2第j -1 与 s3第 i + j -1 是否isInterleave1
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # s1前i - 1个字符与s3是交叉字符, 并且s1第i个字符与s3第i + j - 1个字符相同
                # s2前i - 1个字符与s3是交叉字符, 并且s2第i个字符与s3第i + j - 1个字符相同
                if (dp[i - 1][j] and s3[i + j - 1] == s1[i - 1]) or (dp[i][j - 1] and s3[i + j - 1] == s2[j - 1]):
                    dp[i][j] = True
        return dp[n][m]