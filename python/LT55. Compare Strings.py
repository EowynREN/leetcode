class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """
    def compareStrings(self, A, B):
        # write your code here
        record = {}
        for i in range(len(A)):
            if A[i] in record:
                record[A[i]] += 1
            else:
                record[A[i]] = 1

        for j in range(len(B)):
            if B[j] in record:
                record[B[j]] -= 1
            else:
                return False

        for val in record.values():
            if val < 0:
                return False
        return True