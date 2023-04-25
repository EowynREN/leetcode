class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp = list(s)
        return self.helper(temp)

    #backtracing
    # O(2^n)
    def helper(self, list):
        for i in range(len(list) - 1):
            if list[i] == list[i + 1] == '+':
                list[i] = '-'
                list[i + 1] = '-'

                # determine my winnese according to opponent's status
                # if opponent win, I lose
                # if opponent lose, I win
                win = not self.helper(list)

                list[i] = '+'
                list[i + 1] = '+'

                if win:
                    return True
        #there is no valid move -> lose
        return False



s = Solution()
print s.canWin("++++-++++++")