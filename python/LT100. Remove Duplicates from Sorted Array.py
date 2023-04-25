class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        if not A:
            return 0
        if len(A) == 1:
            return 1

        p1, p2 = 0, 1
        count = 1
        while p1 < len(A) and p2 < len(A):
            while p2 < len(A) and A[p2] == A[p1]:
                p2 += 1
            if p1 + 1 < len(A) and p2 < len(A):
                A[p1 + 1] = A[p2]
                p1 += 1
                count += 1
        return count