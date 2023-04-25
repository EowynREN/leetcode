class Solution:
    # @param {string} s  an expression includes numbers, letters and brackets
    # @return {string} a string
    def expressionExpand(self, s):
        # Write your code here
        stack = []
        num = 0

        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i].isalpha():
                stack.append(s[i])
            elif s[i] == '[':
                stack.append(str(num))
                num = 0
            else:
                letters = self.popStack(stack)
                times = int(stack.pop())

                for i in range(times):
                    stack.append(letters)

        return self.popStack(stack)

    def popStack(self, stack):
        letters = ""

        while stack:
            if stack[-1].isalpha():
                letters = stack.pop() + letters
            else:
                break

        return letters


# stack