#-*- coding:utf8 -*-
#coding=utf-8
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # 思路:这道题利用了max area in histogram这道理的思路
        #     想象在matrix这个矩阵中,每一行划一条线,那么在这条线之上的矩阵可以看做是一个条形图
        #     1的地方累积成一个条形
        #     那么这道题就转化成了n个maxAreaInHist
        #     最好再在这n个maxAreaInHist中找到最大的即可

        if not matrix or not matrix[0]:
            return 0

        n, m = len(matrix), len(matrix[0])
        heights = [[0 for j in xrange(m + 1)] for i in xrange(n)] # 这里m + 1是为了maxAreaInHist函数中所有的height都能pop出来
        for i in xrange(n):
            for j in xrange(m):
                if matrix[i][j] == '0':
                    heights[i][j] = 0
                else:
                    heights[i][j] = 1 if i == 0 else heights[i - 1][j] + 1

        res = 0
        for i in xrange(n):
            res = max(res, self.maxAreaInHist(heights[i]))
        return res

    def maxAreaInHist(self, height):
        # 维护一个单调递增栈
        stack = []

        maxArea, i = 0, 0
        while i < len(height):
            if not stack or height[stack[-1]] <= height[i]:
                stack.append(i)
                i += 1
            else:
                h = height[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, h * w)
        return maxArea
