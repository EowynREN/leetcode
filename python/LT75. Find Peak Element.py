class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.

    # 思路: 当找到一个下坡，我们往左移动，当找到一个上坡，我们往右移动，这样我们就可以达到顶峰。
    # 如果找到一个山谷，则向任意方向移动即可
    def findPeak(self, A):
        # write your code here
        if not A:
            return -1

        left, right = 0, len(A) - 1

        while left < right:
            mid = left + (right - left) / 2
            if mid + 1 < len(A) and A[mid] < A[mid + 1]:
                left = mid + 1
            elif mid - 1 >= 0 and A[mid] < A[mid - 1]:
                right = mid
            else:
                right = mid
        return left