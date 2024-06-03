class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """

        # 用stack销掉所有成对的()， 最后生在stack里的就是单独的(，剩在remove里的就是落单的)
        left, right = 0, 0
        stack = []
        remove = set() # record the index of invalid paranthesis that needed to be removed

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if stack:
                    stack.pop()
                else:
                    remove.add(i)

        stack = set(stack)
        res = ""
        for i, char in enumerate(s):
            if i not in stack and i not in remove:
                res += char
        return i

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = ""
        left = 0
        right = 0
        for c in s:
            if c == ')':
                right += 1
        for c in s:
            if c == '(':
                if left == right:
                    continue
                left += 1
            elif c == ')':
                right -= 1
                if left == 0:
                    continue
                left -= 1
            res += c
        return res

