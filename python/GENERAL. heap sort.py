#-*- coding:utf8 -*-
#coding=utf-8
class Solution:
    # @param {integer[]} nums
    # @return {integer[]} nums

    #升序排序需要用大顶堆
    #降序排序需要用小顶堆
    def sortIntegers(self, nums):
        #首先,构建一个大顶堆
        for i in range(len(nums)):
            self.heapify(nums, i)

        #然后不定的把最大的一个数放到n - 1, n - 2, ..., 2, 1, 0, 以此得到升序数列
        for i in range(len(nums) - 1, -1, -1): #此处i从n - 1开始,一直到0

            #第一个数是整个堆中最大数, 第一个数与最后一个数交换
            nums[0], nums[i] = nums[i], nums[0]

            #注意这里是，不是i- 1,因为heapifyDown当中用的是 < n,而不是<=n
            #这里是[0, n), [0, n - 1), ...
            self.siftDown(nums, 0, i)

        return nums

    def heapify(self, nums, child):
        parent = (child - 1) / 2

        while child != 0 and nums[parent] < nums[child]:
            nums[child], nums[parent] = nums[parent], nums[child]

            child = parent
            parent = (child - 1) / 2

    def siftDown(self, nums, parent, n):
        lchild = 2 * parent + 1 #left child
        rchild = 2 * parent + 2 #right child

        #在两个孩子中,至少有一个比parent大,parent需要被heapifyDown
        while lchild < n and rchild < n and nums[parent] < max(nums[lchild], nums[rchild]):
            if nums[lchild] > nums[rchild]:
                nums[parent], nums[lchild] = nums[lchild], nums[parent]
                parent = lchild
            else:
                nums[parent], nums[rchild] = nums[rchild], nums[parent]
                parent = rchild

            lchild = 2 * parent + 1
            rchild = 2 * parent + 2

        if lchild < n and nums[parent] < nums[lchild]:
            nums[parent], nums[lchild] = nums[lchild], nums[parent]


s = Solution()
print s.sortIntegers([0, 9 , 6 , 8 , 3 , 5 , 2 , 1])