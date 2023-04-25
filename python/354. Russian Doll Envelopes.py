#-*- coding:utf8 -*-
#coding=utf-8

import functools

# 这道题的关键在于:要先对envelopes[i][0]进行升序排序,然后当envelopes[a][0] == envelopes[b][0]的时候,再对envelopes[i][1]进行降序牌数
# 因为宽度相同的信封无法互相包含,以上做法可以保证在信封宽度相同时,只有高度最高的会被包容进来,高度较矮的会被跳过,避免错误计算
# 总体思路是,在两次排序后,在envelopes[i][1]上找LIS

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        # variant for Longest Increasing Subsequence(No.300)
        # dp 解法

        envelopes.sort(key = functools.cmp_to_key(self.cmp))
        dp = [1 for i in range(len(envelopes))]

        # LIS
        for i in range(len(envelopes)):
            for j in range(i):
                if envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        LIS = 0
        for i in range(len(dp)):
            LIS = max(LIS, dp[i])
        return LIS

    def cmp(self, item1, item2):
            if item1[0] == item2[0]:
                return item2[1] - item1[1]
            else:
                return item1[0] - item2[0]

# LIS patience sort 的解法
class Solution2(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        # variant for Longest Increasing Subsequence(No.300)
        envelopes.sort(key = functools.cmp_to_key(self.cmp))

        # LIS
        top = [0 for i in range(len(envelopes))]
        piles = 0

        for i in range(len(envelopes)):

            poker = envelopes[i][1]
            left, right = 0, piles
            while left < right:
                mid = left + (right - left) / 2

                if top[mid] < poker:
                    left = mid + 1
                else:
                    right = mid

            top[left] = poker
            if left == piles:
                piles += 1

        return piles

    def cmp(self, item1, item2):
            if item1[0] == item2[0]:
                return item2[1] - item1[1]
            else:
                return item1[0] - item2[0]


s = Solution2()
print(s.maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1]]))