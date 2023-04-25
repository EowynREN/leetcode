class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or not costs[0]:
            return 0

        n = len(costs)
        dp = [[0 for j in xrange(3)] for i in xrange(2)]
        dp[0][0], dp[0][1], dp[0][2] = costs[0][0], costs[0][1], costs[0][2]


        for i in xrange(1, n):
            dp[i % 2][0] = costs[i][0] + min(dp[(i - 1) % 2][1], dp[(i - 1) % 2][2])
            dp[i % 2][1] = costs[i][1] + min(dp[(i - 1) % 2][0], dp[(i - 1) % 2][2])
            dp[i % 2][2] = costs[i][2] + min(dp[(i - 1) % 2][0], dp[(i - 1) % 2][1])
        return min(dp[(n - 1) % 2][0], dp[(n - 1) % 2][1], dp[(n - 1) % 2][2])

s = Solution()
print s.minCost([[7,6,2]])