class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # edge case
        if not matrix or not matrix[0]:
            return False

        # find the row the target in
        left, right = 0, len(matrix) - 1
        while left < right:
            mid = left + (right - left) / 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                right = mid
            elif matrix[mid][0] < target:
                left  = mid + 1

        # record the row
        if target < matrix[left][0]:
             left -= 1
        i = left

        # find the column target at
        left, right = 0, len(matrix[0]) - 1
        while left < right:
            mid = left + (right - left) / 2
            if matrix[i][mid] == target:
                return True
            elif matrix[i][mid] > target:
                right = mid
            elif matrix[i][mid] < target:
                left = mid + 1

        # edge cases for the:
        #                    matrix only have one row                              e.g., [[1, 2,3]],
        #                    matrix only have one row & one column                 e.g., [[1]] ...
        #                    for a row, target is at the last (m - 1) position     e.g., [[ 1,  3,  5,  7],
        #                                                                                 [10, 11, 16, 20],
        #                                                 target = 7                      [23, 30, 34, 50]]
        # 这些 edge case 都是因为 while left < right, 左右指针在相等时候跳出循环(或者初始值就相等,不能进入循环)
        if matrix[i][left] == target:
            return True
        if matrix[i][right] == target:
            return True
        return False