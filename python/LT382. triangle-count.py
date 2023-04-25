class Solution:
    # @param S: a list of integers
    # @return: a integer
    def triangleCount(self, S):

        # index: left < right < i

        # sort array first, and we get:
        #         (triangle rule: a + b > c)

        #         S[left] + S[right] > S[i]
        #         S[left] + S[i] > S[right] ---- always true after sort
        #         S[i] + S[right] > S[left] ---- always true after sort

        # so we only have to compute on condition: S[left] + S[right] > S[i]
        # This is similar to the Two Sum problem

        if len(S) < 3:
            return 0

        count = 0
        S = sorted(S)

        for i in range(2, len(S)):
            left, right = 0, i - 1
            while left < right:
                if S[left] + S[right] > S[i]:
                    count += right - left
                    right -= 1
                else:
                    left += 1
        return count
