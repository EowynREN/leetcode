class Solution:
    # @param {int[]} nums1 an integer array
    # @param {int[]} nums2 an integer array
    # @return {int[]} an integer array
    def intersection(self, nums1, nums2):
        # Write your code here
        if not nums1 or not nums2:
            return set()

        res = set()
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        n, m = len(nums1), len(nums2)
        i, j = 0, 0

        while i < n and j < m:
            if nums1[i] == nums2[j]:
                res.add(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return list(res)

s = Solution()
print s.intersection([1,2,2,1], [2,2])