#-*- coding:utf8 -*-
#coding=utf-8
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        # 想一想，当一个数为2的整数幂的时候，'1'的个数为1，比如2（10) 和4(100)，8(1000)都只有一个1
        #
        # 每一个2的整数幂就像一个台阶，在这个台阶到下一个台阶之间的数，就是当前台阶之前的所有数加上当前台阶的值
        # 比如[8, 15]的区间中，8是2的整数幂因此'1'的个数只有一个
        #     9(1001) = 8(1个1) + 1(1个1) = 2个1
        #     10(1001) = 8(1个1) + 2(1个1) = 2个1
        #     11(1001) = 8(1个1) + 3(2个1) = 3个1
        #                 .
        #                 .
        #     15(1001) = 8(1个1) + 7(3个1) = 4个1
        # 在这个例子里，8就是那个台阶(2的整数幂)，1 ~ 7在计算区间[0], [1], [2, 3], [4, 7]已经计算过了
        # 因此'1'的个数 =
        #                 res[i] = 1 + res[before]
        #                 (before: 1 ~ 7, 1表示8里的1的个数)
        res = [0] * (num + 1)

        pow2, before = 1, 1
        for i in xrange(1, num + 1):
            if i == pow2:
                res[i] = before = 1
                pow2 <<= 1
            else:
                res[i] = res[before] + 1
                before += 1
        return res

    # version 2
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        # 倒过来想，一个数 * 2 就是把它的二进制全部左移一位，也就是说 1的个数是相等的
        # 那么对一个数右移的话，只需要记录下低位那个被挤掉的bit是1是0，再加上右移后(就是除以2后)的数里'1'的个数，就是答案
        # res[i] = res[i  >> 1] + (i & 1)

        res = [0] * (num + 1)

        for i in xrange(1, num + 1):
            res[i] = res[i >> 1] + (i & 1)
        return res

s = Solution()
print s.countBits(15)