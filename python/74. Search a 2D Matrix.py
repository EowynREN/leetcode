class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        n, m = len(matrix), len(matrix[0])
        l = n * m

        left, right = 0, l - 1
        while left < right:
            mid = left + (right - left) / 2
            grid = matrix[mid / m][mid % m]

            if grid == target:
                return True
            elif grid < target:
                left = mid + 1
            elif grid > target:
                right = mid

        # edge cases for the:
        #                    matrix only have one row                              e.g., [[1, 2,3]],
        #                    matrix only have one row & one column                 e.g., [[1]] ...
        #                    for a row, target is at the last (m - 1) position     e.g., [[ 1,  3,  5,  7],
        #                                                                                 [10, 11, 16, 20],
        #                                                 target = 7                      [23, 30, 34, 50]]
        # 这些 edge case 都是因为 while left < right, 左右指针在相等时候跳出循环(或者初始值就相等,不能进入循环)
        # remind: left / m, not left / n
        #         right / m, not right / n
        if matrix[left / m][left % m] == target:
            return True
        if matrix[right / m][right % m] == target:
            return True
        return False