# 思路: 如果一个数字为正数,但不在自己的位置上(1在1上,2在2上,因为是0-based, 所以1在0上, 2在1上),则为不属于这个位置
# 当前这个数如果不属于这个位置,那么把他换到自己的位置上去
# 一直交换,直到这个数超出数组的下标,或者这个数与要交换的那个位置上的数一样(不判断这个会死循环), 或者当前i已经是对的位置了

class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        # write your code here
        if not A:
            return 1

        n = len(A)
        for i in range(n):
            # A[i] > 0 and A[i] <= n ---- make sure in range
            # A[i] != i + 1 ------------- already on the right position
            # A[i] != A[A[i] - 1] ------- two candidate (waiting for swithing) are not the same
            while A[i] != i + 1 and A[i] > 0 and A[i] <= n  and A[i] != A[A[i] - 1]:
                tmp = A[i]
                A[i] = A[A[i] - 1]
                A[tmp - 1] = tmp

        for i in xrange(n):
            if A[i] != i + 1:
                return i + 1
        return n + 1

s = Solution()
print s.firstMissingPositive([1, 2])