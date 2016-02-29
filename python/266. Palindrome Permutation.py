class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        map = {}
        for i in range(len(s)):
            if s[i] in map.keys():
                map[s[i]] += 1
            else:
                map[s[i]] = 1

        count = 0
        for val in map.values():
            if val % 2 != 0:
                count += 1

        if count > 1:
            return False
        return True
            