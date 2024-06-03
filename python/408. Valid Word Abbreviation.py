class Solution:
    """
    @param word: a non-empty string
    @param abbr: an abbreviation
    @return: true if string matches with the given abbr or false
    """
    def validWordAbbreviation(self, word, abbr):
        # write your code here
        # 用两个指针i,j分别从头开始匹配，j遇到数字，就先把数字x解析出来，然后i移动x位，继续匹配。如果不能匹配就返回false
        i = 0
        j = 0
        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isdigit() and abbr[j] != '0':
                start = j
                while j < len(abbr) and abbr[j].isdigit():
                    j += 1
                i += int(abbr[start : j])
            else:
                return False
        return i == len(word) and j == len(abbr)