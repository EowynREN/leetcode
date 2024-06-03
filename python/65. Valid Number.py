class Solution:
    """
    @param s: the string that represents a number
    @return: whether the string is a valid number
    """
    """
    1. 整数, 例如 "122", "114"
    2. 浮点数, 例如 "1.2", "2.", ".5", "1e10", "1E10"
    3. 上面两种数加上符号, 即 "+" 或 "-"
       "2.", ".5" 这两种形式可能让你有点迷惑, 你可以试一试, 在大多数编程语言中它们都是合法的字面量.
    """
    def isNumber(self, s):

        # 先处理掉首尾的空白字符
        space = ' \t'
        l, r = 0, len(s) - 1
        while l <= r and s[l] in space:
            l += 1
        while l <= r and s[l] in space:
            r -= 1
        if l > r:
            return False

        # 再判断第一个是否符号, 如果是也过滤掉
        if s[l] in '+-':
            l += 1
        if l > r:
            return False

        # 然后, 剩下的字符串就只能包含 0-9, ., e/E 这三类字符了, 如果含有这三类之外的, 直接返回 false 即可. 然后根据以下原则判断即可:
        #     1. 小数点和 e/E 都至多只能出现 1 次
        #     2. 如果含有小数点, 则小数点前后至少有一个数字, 一个孤立的小数点是非法的.
        #     3. 如果含有 e/E, 则它的前后必须有数字.
        dot, ex = -1, -1
        for i in range(l, r + 1):
            if s[i] in '1234567890':
                continue

            if s[i] == '.':
                if dot >= 0:
                    return False
                else:
                    dot = i
            elif s[i] in 'eE':
                if ex >= 0:
                    return False
                else:
                    ex = i
            else:
                return False

        # e/E 前后必须有数字.
        if ex == l or ex == r:
            return False
        # 小数点前后至少有一个数字
        if dot == l:
            return dot < r and s[dot + 1] in '1234567890'
        if dot == r:
            return l < dot and s[dot - 1] in '1234567890'
        return True