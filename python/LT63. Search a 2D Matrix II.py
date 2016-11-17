class Solution:
    """
    @param matrix: An list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicates the total occurrence of target in the given matrix
    """
    # time: O(n + m)
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix or not matrix[0]:
            return 0

        n, m = len(matrix), len(matrix[0])
        x, y = n - 1, 0
        count = 0

        while x >= 0 and y < m:
            if matrix[x][y] < target:
                y += 1
            elif matrix[x][y] > target:
                x -= 1
            else:
                count += 1
                x -= 1
                y += 1
        return count
