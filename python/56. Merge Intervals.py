"""
Intuition
    brute force: O(n^2)
    - Is O(n) possible? -> No
    - Then consider O(nlogn) -> needs to sort
    Sort by start or end?
    - sort by end? -> No meaning
    => sort by start

Approach
    将区间按起点从小到大排序，然后从左到右扫一遍找最远的右端点。 交错或包含的区间就合并

Complexity
Time complexity:
    O(nlogn)
    - sorting -> O(nlogn)
    - merge sorted intervals -> O(n)

Space complexity:
    O(1)
"""


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # sort interval by its start
        intervals = sorted(intervals, key=lambda x: x[0])

        res = []
        for interval in intervals:
            #                 res[-1].end   interval.start
            if len(res) == 0 or res[-1][1] < interval[0]:  # compare if the res overlap with the current interval
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res