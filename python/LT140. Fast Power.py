class Solution:
    """
    @param a, b, n: 32bit integers
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        if n <= 0:
            return 0
        return self.helper(a, b, n)

    def helper(self, a, b, n):
        if n == 0:
            return 1 % b

        if n == 1:
            return a % b

        mod = self.helper(a, b, n / 2)
        mod = (mod * mod) % b
        if (n % 2 == 1):
            mod = (mod * a) % b
        return mod

s = Solution()
print s.fastPower(3, 7, 5)
