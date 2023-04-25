#-*- coding:utf8 -*-
#coding=utf-8

class Solution(object):
    # 依然是一道滑动窗口的题 (与76, 567, 438类似,同一套算法框架)
    # 在这道题里,问题被简化了,不需要用到need = {}和valid = 0
    #       按题目要求找到最长不含重复字符的substring, 那么每个字符就只能出现一次,因此不需要记录次数, 因此不再需要valid来判断次数/进行收缩
    #       因为字符都只出现一次,那么window和need的数据只有0和1的差别,因此只用window来判断就可以了
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right = 0, 0
        window = {}
        res = 0

        # init
        for c in s:
            window[c] = 0

        # start sliding to right
        while right < len(s):
            c = s[right]

            right += 1

            window[c] += 1

            # if same char appears twice, tight up the window from left
            while window[c] > 1:
                d = s[left]

                left += 1

                window[d] -= 1

            res = max(res, right - left) # 此处因为是左闭右开，所以不需要+1
        return res