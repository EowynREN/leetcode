class Solution:
    # @param pages: a list of integers
    # @param k: an integer
    # @return: an integer
    def copyBooks(self, pages, k):
        # write your code here
        if not pages:
            return 0

        # 对于pages里的n本书,n[i]的最大值决定了至少需要多少时间
        # 最多页数决定了完成时间的下限(如果低于最多页数,则用于最多页数的这本书无法copy完, 如[1, 1, 1, 100]最少需要100 min)

        # 最长的时间(最坏情况, )
        maz = pages[0]
        for i in range(1, len(pages)):
            maz = max(maz, pages[i])

        # 用二分法枚举每一种情况(严格并不是枚举每一个,总之是搜索)
        left, right = maz, sum(pages)
        while left < right:
            mid = left + (right - left) / 2

            # 一个人copy mid页, 如果需要的工人比给定的人多,则给没人分配更多的书页(以减少copy的人数,在总量不变的情况下)
            if self.countCopier(pages, mid) > k:
                left = mid + 1
            else:
                right = mid # 否则就减少没人分配的书页(在书页总量不变的情况下, 减少每人的工作量,就会增加人数)

        return left if self.countCopier(pages, left) <= k else left - 1

    def countCopier(self, pages, limit):
        sum = pages[0]
        copier = 1

        for i in range(1, len(pages)):
            # 在'每人需要完成limit页下', 如果超过则需要多安排一个员工,因为一个人如果干这些
            if sum + pages[i] > limit:
                copier += 1
                sum = 0
            sum += pages[i]
        return copier

s = Solution()
print s.copyBooks([3,2,4], 2)