class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        if not s:
            return []

        res = []
        queue = [s]
        found = False
        visited = set()
        visited.add(s)

        while queue:
            modified = queue.pop(0)
            if self.isValid(modified):
                res.append(modified)
                found = True

            if found:
                continue

            for i in xrange(len(modified)):
                if modified[i] != "(" and modified[i] != ")":
                    continue

                next = modified[:i] + modified[i + 1:]

                if next not in visited:
                    queue.append(next)
                    visited.add(next)
        return res

    def isValid(self, s):
        count = 0
        for c in s:
            if c == "(":
                count += 1
            else:
                count -= 1

            if count < 0:
                return False

        return count == 0

s = Solution()
print s.removeInvalidParentheses("()())()")