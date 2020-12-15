#-*- coding:utf8 -*-
#coding=utf-8

# stack 解法
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        start, longest = 0, 0
        stack = []

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if not stack: # 空栈
                    # 把当前的")"当做下个potential result的起始位置
                    start = i + 1
                else:
                    # 把对应的"("pop出来
                    stack.pop()
                    if not stack:
                        # 空栈了的话，利用start来计算长度
                        longest = max(longest, i - start + 1)
                    else:
                        # 用最近的"("计算长度
                        longest = max(longest, i - stack[-1])
        return longest


s = Solution()
print s.longestValidParentheses(")()())")