class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    # 思路: 严格的说，这个算法是递推，而不是动态规划，但是可以用动态规划的四要素去分析换个解答。
    #      为什么不是动态规划？因为最暴力的方式也就是 O(n^3) 可以找到A所有的Substring然后看看在不在B里。
    def longestCommonSubstring(self, A, B):
        # state: f[i][j] is the length of the longest lcs
        # init f[n][m] is 0 by default
        n, m = len(A), len(B)
        f = [[0 for j in range(m + 1)] for i in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if A[i - 1] == B[j - 1]:
                    f[i][j] = f[i - 1][j - 1] + 1
                else:
                    f[i][j] = 0

        res = 0
        # answer: max{f[i][j]}
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                res = max(res, f[i][j])
        return res