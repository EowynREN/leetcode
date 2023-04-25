#-*- coding:utf8 -*-
#coding=utf-8

class Solution(object):
    # 与76一样,用滑动窗口的解法
    # 联系76,可以看出算法框架基本没变,唯二改变的地方:
    #       1. 收缩窗口的时机为当window size大于等于s1时,因为是排列,所以长度必须一样(防止中间夹其他不在need中的字符)
    #       2. 当发现 valid == need size 时，就说明窗口中就是一个合法的排列，所以立即返回 true
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        left, right = 0, 0 # 用于编辑window大小的左右指针
        window, need = {}, {} # 记录当前窗口含有字符与需求字符的map
        valid = 0 # 判断当前window内的字符是不是已经满足need要求了

        # init
        for c in s1:
            if c in need:
                need[c] += 1
            else:
                need[c] = 1
            window[c] = 0

        # 开始滑动,窗口向右延伸
        while right < len(s2):
            c = s2[right]

            right += 1

            # -- 对称代码 --
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            # 收缩窗口
            while right - left >= len(s1):
                if valid == len(need):
                    return True

                d = s2[left]

                left += 1

                # -- 对称代码 --
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return False
