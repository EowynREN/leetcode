class Solution:
    """
    @param A: sorted integer array A which has m elements,
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """

    # 思路: 从后往前
    #      三个指针,分别从m - 1, n - 1, m + n -1开始
    #      index指针记录的移动记录的是最终结果
    #      i和j分别是A与B的指针
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        i, j, index = m - 1, n - 1, m + n -1

        while i >=0 and j >= 0:
            if A[i] > B[j]:
                A[index] = A[i]
                i -= 1
            else:
                A[index] = B[j]
                j -= 1
            index -= 1

        while j >= 0:
            A[index] = B[j]
            index -= 1
            j -=1