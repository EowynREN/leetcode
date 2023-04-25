class Solution:
    # @param s : A string
    # @return : An integer
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        if s is None or s == "":
            return 0

        i, j = 0, 0
        has = {}
        res = 0
        while j < len(s):
            if s[j] in has:
                has[s[j]] += 1
            else:
                has[s[j]] = 1

            while len(has) > k:
                has[s[i]] -= 1
                if has[s[i]] == 0:
                    del has[s[i]]
                i += 1
            res = max(res, j - i + 1)
            j += 1
        return res
s =Solution()
print s.lengthOfLongestSubstringKDistinct("eqgkcwGFvjjmxutystqdfhuMblWbylgjxsxgnoh", 16)