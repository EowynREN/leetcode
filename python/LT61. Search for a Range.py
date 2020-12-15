class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        if not A:
            return [-1, -1]

        res = [-1, -1]
        left, right = 0, len(A) - 1
        while left < right:
            mid = left + (right - left) / 2

            if A[mid] >= target:
                right = mid
            else:
                left = mid + 1

        if A[left] == target:
            res[0] = left

        left, right = 0, len(A) - 1
        while left < right:
            mid = left + (right - left) / 2

            if A[mid] <= target:
                left = mid + 1
            else:
                right = mid

        if A[left - 1] == target:
            res[1] = left - 1
        if A[left] == target:
            res[1] = left
        return res