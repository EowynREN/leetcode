class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        # write your code here
        record = {}
        for i in range(len(s)):
            if s[i] in record:
                record[s[i]] += 1
            else:
                record[s[i]] = 1

        for j in range(len(t)):
            if t[j] in record:
                record[t[j]] -= 1
            else:
                return False

        for val in record.values():
            if val != 0:
                return False
        return True