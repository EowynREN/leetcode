#-*- coding:utf8 -*-
#coding=utf-8

class Solution(object):
    # 解法: 滑动窗口
    # 与76,567一样的算法框架
    # 相比567, 唯一改动的地方就是添加了res变量,按题目要求,用来记录所有出Anagrams的first index,
    #       因此,在567中返回true的地方,改成res.append左指针就可以了

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        left, right = 0, 0
        window, need = {}, {}
        valid = 0
        res = []

        # init
        for c in p:
            if c in need:
                need[c] += 1
            else:
                need[c] = 1
            window[c] = 0

        # start sliding
        while right < len(s):
            c = s[right]

            right += 1

            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            while right - left >= len(p):
                if valid == len(need):
                    res.append(left)

                d = s[left]

                left += 1

                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return res