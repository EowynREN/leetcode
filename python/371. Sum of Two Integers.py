class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 32-bit max positive integer value
        MAX = 0x7FFFFFFF #全等于1111111...1111(32 bits binary)

        # 32-bit min negetive integer value
        # no use here, just for clarification
        MIN = 0x80000000

        # 1 in Python would look like 0x0000000000000001, but it looks like 0x00000001 in 32-bit format
        #-1 in Python would look like 0xFFFFFFFFFFFFFFFF, but it looks like 0xFFFFFFFF in 32-bit format.
        # input given is in 32-bit format.
        # Since Python would treat it as positive with 1 on the 32 position, we have to use mask to treat it as negative
        # python是64位的，会把32位的负数（最高位32位是符号位，在64位时符号位应在最高位64位处，因此64位会把第32位上的符号位参与到计算里）变成正数
        # mask用来把这一误算转换成32位正确的算法
        mask = 0xFFFFFFFF

        # ^ get the differences
        # & get the same
        # << move the carry
        # here, b is like carry, calculate with one bit in a in each loop
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a <= MAX else ~(a ^ mask)
            