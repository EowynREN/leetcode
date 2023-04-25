class Solution:
    # @paramn n: An integer
    # @return: An integer
    def numTrees(self, n):
        # write your code here
        # dp[i]表示当n = i时，能有多少种BST
        dp = [0] * (n + 2)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            # 枚举每一个节点，当一这个节点为root时：
            # 左边有几个节点，右边有几个节点
            # 左边的可能 * 右边的可能 = 以这个节点为root时BST的可能数
            # The case for 3 elements example
            # Count[3] = Count[0]*Count[2]  (1 as root)
            #               + Count[1]*Count[1]  (2 as root)
            #               + Count[2]*Count[0]  (3 as root)
            for j in range(i + 1):
                # j表示左边的节点数
                # i- j - 1：表示所有节点数-左边的节点数-root
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[n]