class Solution:
    """
    @param {int} n an integer.
    @return {int} the nth prime number as description.
    """

    # time: O(n)
    def nthUglyNumber(self, n):
        # write your code here
        uglys = [0] * n
        uglys[0] = 1

        p2, p3, p5 = 0, 0, 0
        for i in range(1, n):
            last = uglys[i - 1]
            # 只要p2指向的这个值 * 2 刚好大于目前最大的ugly num, 那么它就成为一个备选
            while uglys[p2] * 2 <= last:
                p2 += 1
            # 同理p3
            while uglys[p3] * 3 <= last:
                p3 += 1
            while uglys[p5] * 5 <= last:
                p5 += 1

            # 在三个备选中,选出最小的那个,放在uglys数组的最后(这样uglys数组就是排好序的)
            uglys[i] = min(min(uglys[p2] * 2, uglys[p3] * 3), uglys[p5] * 5)
        return uglys[n - 1]

s = Solution()
print s.nthUglyNumber(9)