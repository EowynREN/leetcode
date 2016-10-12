class Solution:
    # @param A: Given an integer array
    # @return: void
    def heapify(self, A):
        # write your code here
        for i in range(len(A) / 2 - 1, -1, -1):
            self.siftDown(A, i)

    def siftDown(self, A, parent):
        n = len(A)

        tmp = parent
        while parent < n:
            #                 此处注意:是tmp不是parent
            #                 这样parent和lchild, rchild三者之间相互比较出最小的,但在parent上
            if parent * 2 + 1 < n and A[tmp] > A[parent * 2 + 1]:
                tmp = parent * 2 + 1

            #                 此处注意:是tmp不是parent
            #                 这样parent和lchild, rchild三者之间相互比较出最小的,但在parent上
            if parent * 2 + 2 < n and A[tmp] > A[parent * 2 + 2]:
                tmp = parent * 2 + 2

            if parent == tmp:
                break
            A[tmp], A[parent] = A[parent], A[tmp]
            parent = tmp

s = Solution()
print s.heapify([45,39,32,11])