#-*- coding:utf8 -*-
#coding=utf-8

# 动态规划的解法: dp[i][j表示子串i到j是不是palindrome
#               dp[i][j] = dp[i + 1][j - 1] and s[i - 1] == s[j - 1]
#               这里由于地推公式,i + 1要比i先算出来,所以这道题要从右到左扫
# 时间复杂度: O(n^2)
# 空间度咋读: O(n^2)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        n = len(s)
        dp = [[False for j in xrange(n + 1)] for i in xrange(n + 1)]

        # init:
        for i in xrange(n + 1):
            dp[i][i] = True

        max_len = 0
        start, end = 0, 0

        # 倒着从串为开始找子串(从右到左),i指针在左边,j指针在右边,一直扩大到整个string
        for i in xrange(n, 0, -1):
            for j in xrange(i + 1, n + 1):
                # 单个字符
                if s[i - 1] == s[j - 1] and j - i < 2:
                    dp[i][j] = True

                # 当前subtring的最大子串是回文,且左右边缘的字符相同->也是回文
                if s[i - 1] == s[j - 1] and dp[i + 1][j - 1]:
                    dp[i][j] = True

                # 更新最大回文子串开头结尾的指针
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    start = i - 1
                    end = j - 1
        return s[start: end + 1]

# 基于中心线枚举的方法
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        longest = ""
        for mid in xrange(len(s)):
            # 针对奇数长度的字符数
            potential = self.isPalindormic(s, mid, mid)
            if len(potential) > len(longest):
                longest = potential

            # 针对偶数长度的字符串
            potential = self.isPalindormic(s, mid, mid + 1)
            if len(potential) > len(longest):
                longest = potential

        return longest

    # 已mid为基准心，像两边延伸
    def isPalindormic(self, s, left, right):
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break

            left -= 1
            right += 1

        # 因为循环结束，必然是因为
        # 1.整个串已扫完，left现在是-1，而right超过length
        # 2. s[left] != s[right], 此时需要把s[left]yu s[right]刨去，因为python的api不取最右的值，所以只许left+1即可
        return s[left + 1: right]

s = Solution()
print s.longestPalindrome("cbbd")