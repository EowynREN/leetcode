class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 双指针, 从两头走到中间，发现第一对不一样的字符之后
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                break
            left += 1
            right -= 1

        # 要么删左边的，要么删右边的
        return self.isPalindrome(left + 1, right, s) or self.isPalindrome(left, right - 1, s)

    def isPalindrome(self, left, right, s):
        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1
        return True
