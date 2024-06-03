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

# 03/27/2024
class Solution(object):
    from typing import List

    def merge(intervals: List[List[int]]) -> List[List[int]]:
        # 如果输入为空的情况，直接返回空列表
        if not intervals:
            return []
        # 按区间的 start 升序排列
        intervals.sort(key=lambda x: x[0])
        # 存储合并后的区间
        res = [intervals[0]]

        # 合并区间
        for interval in intervals[1:]:
            # 找到最后一个区间
            last = res[-1]

            # last.end >= interval.start
            if last[1] >= interval[0]:
                # 合并，并更新最大的 end
                last[1] = max(last[1], interval[1])
            else:
                # 处理下一个待合并区间
                res.append(interval)

        return res