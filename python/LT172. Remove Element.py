class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        isElem, notElem = 0, len(A) - 1
        count = 0

        while isElem < notElem:
            while isElem < notElem and A[isElem] != elem:
                isElem += 1

            if A[isElem] == elem:
                count += 1

            while isElem < notElem and A[notElem] == elem:
                notElem -= 1
                count +=1

            A[isElem], A[notElem] = A[notElem], A[isElem]
            isElem += 1
            notElem -= 1
        return len(A) - count

s = Solution()
print s.removeElement([0,4,4,0,4,4,4,0,2], 4)