class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        needLeft = 0
        needRight = 0

        for i in range(len(s)):
            if s[i] == '(':
                # 对右括号的需求 + 1
                needRight += 1

            if s[i] == ')':
                # 对右括号的需求 - 1
                needRight -= 1

                if needRight == -1:
                    needRight = 0

                    # 需插入一个左括号
                    needLeft += 1
        return needLeft + needRight