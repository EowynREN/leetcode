class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        # 26的变种
        # 题目让你原地删除，不允许 new 新数组，只能在原数组上操作，然后返回一个长度
        #
        # 由于数组已经排序，所以重复的元素一定连在一起，找出它们并不难。但如果毎找到一个重复元素就立即原地删除它，由于数组中删除元素涉及数据搬移，整个时间复杂度是会达到 O(N^2)。
        #
        # 高效解决这道题就要用到快慢指针技巧：
        # 我们让慢指针 slow 走在后面，快指针 fast 走在前面探路，找到一个不重复的元素就赋值给 slow 并让 slow 前进一步。
        # 这样，就保证了 nums[0..slow] 都是无重复的元素，当 fast 指针遍历完整个数组 nums 后，nums[0..slow] 就是整个数组去重之后的结果
        if not nums:
            return 0

        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        # 先给 nums[slow] 赋值然后再给 slow++
        # 这样可以保证 nums[0..slow-1] 是不包含值为 val 的元素的
        # 最后的结果数组长度就是 slow
        return slow