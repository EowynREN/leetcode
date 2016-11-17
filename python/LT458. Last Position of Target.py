class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def lastPosition(self, A, target):
        # Write your code here
        if not A:
            return -1

        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if A[mid] == target:
                left = mid
            elif A[mid] < target:
                left = mid
            else:
                right = mid

        if A[right] == target:
            return right
        if A[left] == target:
            return left
        return -1

s = Solution()
print s.lastPosition([1,1,1,1,1,1,1,1,1,1,1], 1)