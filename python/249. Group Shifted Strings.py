class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        map = {}
        for s in strings:
            key = self.encode(s)
            if key in map.keys():
                values = map[key]
                values.append(s)
                map[key] = sorted(values)
            elif key != "not":
                map[key] = [s]
        return map.values()

    def encode(self, string):
        if not string.isalpha():
            return "not"

        n = len(string)
        if n == 1:
            return n

        res = "a"
        for i in range(n - 1):
            code = ord(string[i + 1]) - ord(string[i])
            if code < 0:
                code += 26
            res += chr(code)
        return res

