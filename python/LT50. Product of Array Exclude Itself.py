# class Solution:
#     """
#     @param A: Given an integers array A
#     @return: An integer array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
#     """
#     def productExcludeItself(self, A):
#         # write your code here
#         n = len(A)
#         forward = [1] * n
#         backward = [1] * n
#
#         forward[0] = A[0]
#         for i in range(1, n):
#             forward[i] = forward[i - 1] * A[i]
#
#         backward[n - 1] = A[n - 1]
#         for i in range(n - 2, -1, -1):
#             backward[i] = backward[i + 1] * A[i]
#
#         res = []
#         for i in range(n):
#             product = 1
#
#             if i - 1 >= 0:
#                 product *= A[i - 1]
#             if i + 1 < n:
#                 product *= backward[i + 1]
#
#             res.append(product)
#         return res
class Solution:
    """
    @param A: Given an integers array A
    @return: An integer array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, A):
        # write your code here
        n = len(A)
        backward = [1] * n

        backward[n - 1] = A[n - 1]
        for i in range(n - 2, -1, -1):
            backward[i] = backward[i + 1] * A[i]

        res = []
        product = 1
        for i in range(n):
            if i - 1 >= 0:
                product *= A[i - 1]
            if i + 1 < n:
                res.append(product * backward[i + 1])
            else:
                res.append(product)
        return res

s = Solution()
print s.productExcludeItself([1, 2, 3])