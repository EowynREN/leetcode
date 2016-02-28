class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        dict = {"0":"0", "1":"1", "8":"8", "6":"9", "9":"6"}
        left, right = 0, n - 1

        while left <= right:
            if num[right] in dict.keys() and num[left] == dict[num[right]]:
                left += 1
                right -= 1
            else:
                return False
        return True