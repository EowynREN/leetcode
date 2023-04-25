class Solution:
    # @param {int[][]} arrays a list of array
    # @param {int} k an integer
    # @return {int} an integer, K-th largest element in N arrays
    def KthInArrays(self, arrays, k):
        # Write your code here
        if not arrays:
            return 0

        if k <= 0:
            return 0

        n = len(arrays) * len(arrays[0])
        return self.quickSelect(arrays, 0, n - 1, n - k + 1)


    def quickSelect(self, arrays, left, right, k):
        n = len(arrays[0])

        if left == right:
            return arrays[left / n][left % n]

        position = self.partition(arrays, left, right)

        if position + 1 == k:
            return arrays[position / n][position % n]
        elif position + 1 > k:
            return self.quickSelect(arrays, left, position - 1, k)
        else:
            return self.quickSelect(arrays, position + 1, right, k)

    def partition(self, arrays, left, right):
        n = len(arrays[0])
        pivot = arrays[left / n][left % n]

        while left < right:
            while left < right and arrays[right / n][right % n] >= pivot:
                right -= 1
            arrays[left / n][left % n] = arrays[right / n][right % n]

            while left < right and arrays[left / n][left % n] <= pivot:
                left += 1
            arrays[right / n][right % n] = arrays[left / n][left % n]

        arrays[left / n][left % n] = pivot
        return left

