class Solution:
    # @param strs: A list of strings
    # @return: The longest common prefix
    def longestCommonPrefix(self, strs):
        # write your code here
        if not strs:
            return ""

        i, j = 0, 0
        while j < len(strs[0]):
            i = 0
            tmp = strs[0][j]
            while i < len(strs):
                if j >= len(strs[i]) or tmp != strs[i][j]:
                    return strs[i][0:j] if j > 0 else ""
                i +=1
            j += 1
        return strs[0][0:j] if j > 0 else ""