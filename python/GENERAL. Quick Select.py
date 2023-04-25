#-*- coding:utf8 -*-
#coding=utf-8

class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        # 时间复杂度: 平均O(n)
        # 记忆:快排平均是O(nlogn),quick select算法不需要保持整体有序,只保持了部分有序(问题减小的规模是一半一半减小的 -> 因为每次只需看左半边或右半边,不用全看)
        if not nums or n > len(nums):
            return -1

        return self.quickSelect(0, len(nums) - 1, n, nums)

    def quickSelect(self, start, end, k, nums):
        if start == end:
            return nums[start]

        pivot = nums[(start + end) / 2]
        i, j = start, end

        while i <= j:
            #如果左半部分当前值比pivot大,跳过它寻找下一个可交换candidate
            while i <= j and nums[i] > pivot:
                i += 1

            #如果右版部分当前值比pivot大,跳过它寻找下一个可交换candidate
            while i <= j and nums[j] < pivot:
                j -= 1

            # 交换两个candidate
            if i <= j:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1
                j -= 1

        # 如果左半部分已经超出k个数了,那第k大的数一定在这一侧,进入左半边继续找第k大
        if start + k - 1 <= j:
            return self.quickSelect(start, j, k, nums)

        # 如果左半部分不够k个数了,那第k大的数一定在右半边,进入右半边, 刨去左边已有的几个数,找第k - (i- start)大的数
        if start + k - 1 >= i:
            return self.quickSelect(i, end, k - (i - start), nums)

        return nums[j + 1]

s = Solution()
print (s.kthLargestElement(10, [1,2,3,4,5,6,8,9,10,7]))