class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # 两个指针分别初始化在两个数组的最后一个元素（类似拉链两端的锯齿）
        i, j = m - 1, n - 1
        p = len(nums1) - 1

        # 从后向前生成结果数组，类似合并两个有序链表的逻辑
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[p] = nums1[i]
                i -= 1
            else:
                nums1[p] = nums2[j]
                j -= 1
            p -= 1

        # 可能其中一个数组的指针走到尽头了，而另一个还没走完
        # 因为我们本身就是在往 nums1 中放元素，所以只需考虑 nums2 是否剩元素即可
        if j >= 0:
            nums1[:p + 1] = nums2[:j + 1]