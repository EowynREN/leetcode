class Solution:
    """
    @param: s1: A string
    @param: s2: Another string
    @return: whether s2 is a scrambled string of s1
    """
    def isScramble(self, s1, s2):
        # write your code here
        if len(s1) != len(s2):
            return False

        if s1 == s2:
            return True

        if sorted(s1) != sorted(s2):
            return False

        n = len(s1)
        for i in xrange(1,n):
            s11 = s1[:i]
            s12 = s1[i:]

            s21 = s2[:i]
            s22 = s2[i:]

            if self.isScramble(s11, s21) and self.isScramble(s12, s22):
                return True

            s21 = s2[:n - i]
            s22 = s2[n - i:]
            if self.isScramble(s11, s22) and self.isScramble(s12, s21):
                return True

        return False

s = Solution()
print s.isScramble("abc","cab")