# sum[i][j]: sum of submatrix [(0, 0), (i, j)]
    # 1. 建立sum矩阵，为n＋1行，m＋1列。将第0行和第0列都初始化为0。
    #
    # 2. 遍历matrix，计算所有sum
    #   - sum[i][j] = matrix[i][j] + sum[i][j - 1] + sum[i - 1][j]  -sum[i - 1][j - 1] 。
    #
    # 3. 然后取两个row：l1, l2。用一个线k从左到右扫过l1和l2，每次都用diff = sum[l1][k]-sum[l2][k]来表示l1-l2和0-k这个矩形元素的sum。
    #    如果在同一个l1和l2中，有两条线（k1，k2）的diff相等，则表示l1-l2和k1-k2这个矩形中的元素和为0。


class Solution:
    # @param {int[][]} matrix an integer matrix
    # @return {int[][]} the coordinate of the left-up and right-down number
    def submatrixSum(self, matrix):
        # Write your code
        if not matrix or not matrix[0]:
            return [[0, 0], [0, 0]]

        n, m = len(matrix), len(matrix[0])
        sums = [[0 for j in xrange(m + 1)] for i in xrange(n + 1)]

        for j in xrange(m + 1):
            sums[0][j] = 0

        for i in xrange(n + 1):
            sums[i][0] = 0

        for i in xrange(1, n + 1):
            for j in xrange(1, m + 1):
                sums[i][j] = matrix[i - 1][j - 1] + sums[i][j - 1] + sums[i - 1][j] - sums[i - 1][j - 1]

        for l1 in xrange(n + 1):
            for l2 in xrange(l1 + 1, n + 1):
                map = {}
                for k in xrange(m + 1):
                    diff = sums[l2][k] - sums[l1][k]

                    if diff in map:
                        prev_k = map[diff]
                        return [[l1, prev_k], [l2 - 1, k - 1]]
                    else:
                        map[diff] = k
        return [[0, 0], [0, 0]]

s = Solution()
print s.submatrixSum([[2,-2],[-4,4]])