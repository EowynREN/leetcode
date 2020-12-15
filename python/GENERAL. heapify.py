class Solution:
    # @param {integer[]} nums
    # @return {integer[]} nums

    def heapify(self, nums):
        for i in range(len(nums) / 2 - 1, - 1, -1 ):
            self.siftDown(nums, i)
        return nums

    def siftDown(self, nums, parent):
        n = len(nums)
        smallest = parent

        while parent < n:
            #left child, 此时smallest为parent
            if 2 * parent + 1 < n and nums[smallest] > nums[2 * parent + 1] :
                smallest = 2 * parent + 1

            #right child,此时smallest为parent,或者left child(如果进入上面一个循环的话)
            if 2 * parent + 2 < n and nums[smallest] > nums[2 * parent + 2] :
                smallest = 2 * parent + 2

            #both children are great than parent
            if smallest == parent:
                break

            #either of children is less than parent, swap parent and the child
            nums[smallest], nums[parent] = nums[parent], nums[smallest]
            #move pointer to the child
            parent = smallest


s = Solution()
print s.heapify([0, 9, 8, 6, 2, 4, 5])