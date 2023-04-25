class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    # 思路: 二分法
    #      讲rotated array首先分成两部分 ----> 规则部分和不规则部分
    #      规则部分为, 其中的数是升序的
    #      不规则部分, 其中有一个peak点, 两段升序,且第二段升序比第一段小
    def search(self, A, target):
        # write your code here
        if not A:
            return -1

        left, right = 0, len(A) - 1
        while left < right:
            mid = left + (right - left) / 2
            if A[mid] == target:
                return mid
            # 说明[mid, right]之间是升序的
            if A[mid] <= A[right]:
                # normal binary search
                # 如果target存在在这段升序当中, 否则就应该在[left, mid]区间里
                if A[mid] < target <= A[right]:
                    left = mid + 1
                else:
                    right = mid
            # 说明 [left, mid]之间是升序的
            else:
                # normal binary search
                # 如果target存在在这段升序当中, 否则就应该在[mid, right]区间里
                if A[left] <= target < A[mid]:
                    right = mid
                else:
                    left = mid + 1
        return left if A[left] == target else -1