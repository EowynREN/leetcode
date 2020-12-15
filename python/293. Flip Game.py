class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        i, n = 0, len(s)

        while(i < n - 1):
            temp = list(s)
            if s[i] == s[i + 1] == '+':
                temp[i] = '-'
                temp[i + 1] = '-'
                res.append("".join(temp))
            i += 1
        return res

s = Solution()
print s.generatePossibleNextMoves("--")