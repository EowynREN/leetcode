class Solution:
    def strStr(self, source, target):
        # write your code here
        if source == None or target == None:
            return -1
        if len(target) > len(source):
            return -1

        for i in range(len(source) - len(target) + 1):
            if target == source[i: i + len(target)]:
                return i
        return -1