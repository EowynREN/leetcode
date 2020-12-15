class Solution:
    #@param n, m: Two integer
    #@param i, j: Two bit positions
    #return: An integer
    def updateBits(self, n, m, i, j):
        # write your code here
        a = [0] * 32
        for i in range(31, -1, -1):
            a[i] = n & 1
            n >>= 1

        b = [0] * 32
        for i in range(31, -1, -1):
            b[i] = m & 1
            m >>= 1

        for index in range(i, j + 1):
            a[index] = b[index]

        res = ''.join(a)
        return int(res)

s = Solution()
print s.updateBits(35,41,3,9)