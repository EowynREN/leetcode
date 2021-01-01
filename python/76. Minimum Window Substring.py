#-*- coding:utf8 -*-
#coding=utf-8

import sys
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t:
            return ""

        start, length = 0,  sys.maxsize # 结果字符串的开始与长度
        left, right = 0, 0 # 用于编辑window大小的左右指针
        window, need = {}, {} # 记录当前窗口含有字符与需求字符的map
        valid = 0 # 记录当前窗口中的字符是否match需求need中的字符（包括个数）

        # 初始化需求字符的map
        for c in t:
            if c in need:
                need[c] += 1
            else:
                need[c] = 1

            window[c] = 0

        # 滑动窗口结束条件：右指针达到最末端
        while right < len(s):
            # c 是即将移入窗口的字符
            c = s[right]

            # 右移窗口
            right +=1

            # 如果当前字符是需求字符，进行窗口内数据的一系列更新
            if c in need:
                window[c] += 1

                if window[c] == need[c]:
                    valid += 1

            # 判断左侧窗口是否要收缩
            while valid == len(need):
                # 在这里更新最小覆盖子串
                if right - left < length:
                    start = left
                    length = right - left

                # d 是即将移出窗口的字符
                d = s[left]

                # 左移收缩窗口
                left +=1

                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return s[start: start + length] if length != sys.maxsize else ""

s = Solution()
print s.minWindow("ADOBECODEBANC", "ABC")