class Solution:
    # @param strs: A list of strings
    # @return: A list of strings
    def anagrams(self, strs):
        # write your code here
        if not strs:
            return []

        record = {}
        res = []
        for s in strs:
            t = ''.join(sorted(s))
            if t in record:
                record[t].append(s)
            else:
                record[t] = [s]

        for val in record.values():
            if len(val) > 1:
                res += val
        return res