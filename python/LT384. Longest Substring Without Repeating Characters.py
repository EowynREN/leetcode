class Solution:
    # @param s: a string
    # @return: an integer
    def lengthOfLongestSubstring(self, s):
        # write your code here
        if s is None or s == "":
            return 0

        res = 0
        record = {}
        i, j = 0, 0
        while j < len(s):
            if s[j] in record and record[s[j]] >= i:
                i = record[s[j]] + 1

            record[s[j]] = j
            res = max(res, j - i + 1)

            if i >= len(s):
                break
            j += 1
        return res


s = Solution()
print s.lengthOfLongestSubstring("aaaa")