class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #思路: 基本接近于快排,只是不需要整个数组有序,因此减少了许多操作
        #     选定一个pivot值,对其进行梳理 -- 讲比pivot大的值放在pivot右边,比pivot值小的放在左边
        #     返回这个pivot值的index

        #     因为所有pivot左边的数,都比它小,右边的数都比它大
        #     所以pivot的index就表示它是第几大的数

        #     如果k大于pivot的index,则表示,当前的pivot是第k - x大的数(0 < x < k)
        #     那么第k大的数一定在[piovot' index, right]的区间里

        #     如果k小于pivot的index,则表示,当前的pivot是第k + x大的数(0 < x < k)
        #     那么第k大的数一定在[left, piovot' index]的区间里

        #     如果当前pivot's index等于k,则表示这个pivot就是第k大的数
        #     因此返回pivot


        #time: O(n) space: O(1)
        if not nums:
            return 0

        if k <= 0:
            return 0

        return self.quickSelect(nums, 0, len(nums) - 1, len(nums) - k + 1)

    def quickSelect(self, nums, left, right, k):
        # 如果找完了nums数组还是没是没找到，就返回最接近的一个（数组的最开头或者最末尾）
        if left == right:
            return nums[left]

        position = self.partition(nums, left, right)

        # +1是因为数组是zero-based
        if position + 1 == k:
            return nums[position]
        elif position + 1 < k:
            return self.quickSelect(nums, position + 1, right, k) # 不需要对当前的这个position再计算了,因为他不已经是第k大值了, 所以 + 1
        else:
            return self.quickSelect(nums, left, position - 1, k)  # 不需要对当前的这个position再计算了,因为他不已经是第k大值了, 所以 - 1

    def partition(self, nums, left, right):
        pivot = nums[left]

        # 因为不是取中间值作为pivot,不能够再从左右两边向里挪指针
        # 需要下面这种处理方法,将小于pivot的数挪到pivot左边,讲大于的数挪到右边

        # 为什么是 left < right 而不是 <= ,
        # 因为当跳出while循环的时候left = right
        # 两个指针正好一起直到pivot的地方
        while left < right:

            # 在最右面找到第一个比pivot小的数
            while left < right and nums[right] >= pivot:
                right -= 1

            nums[left] = nums[right]

            # 在最左面找到第一个比pivot大的数
            while left < right and nums[left] <= pivot:
                left += 1

            nums[right] = nums[left]

        # 最后把pivot放在一个位置
        # 这是left = right,指向同一个位置
        # 左边的值逗比它小， 右边的值都比它大
        # 这里正好放置pivot
        nums[left] = pivot

        return left

s = Solution()
print s.findKthLargest([3, 2, 1, 5, 6, 4], 3)
