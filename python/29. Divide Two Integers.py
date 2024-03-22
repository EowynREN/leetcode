import sys


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        # 基本思路是利用减法, 看看被除数可以减去多少次除数
        #
        # 使用倍增的思想优化, 可以将减法的次数优化到对数时间复杂度
        #
        # 我们将除数左移一位(或者让它加上自己), 即得到了二倍的除数, 这时一次减法相当于减去了2个除数.不断倍增, 时间效率很优秀
        #
        # 与此同时还需要一个变量记录此时的除数是最初的除数的多少倍, 每次减法后都加到结果上即可

        if divisor == 0:
            return sys.maxsize

        sign = -1 if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0) else 1
        a = abs(dividend)
        b = abs(divisor)
        res = 0

        while a >= b:
            shift = 0
            while a >= (b << shift):
                shift += 1

            # now a < b
            a -= b << (shift - 1)
            res += 1 << (shift - 1)

        return res if sign >= 0 else -res
