"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
def sorter(x, y):
        if x[0] != y[0]:
            return x[0] - y[0]
        return x[1] - y[1]  # 多架飞机降落和起飞在同一时刻，降落比起飞有优先权
                            # 也就是说在,比大小的时候,start应该比end大,这样<<起飞>>会被排在<<降落>>的后面


class Solution:
    # @param airplanes, a list of Interval
    # @return an integer

    # 思路: sweap line揭发
    #      先把airplanes的interval, 拆开标成 - [start, 1] [end, 0] (1表示起飞,0表示降落)
    #      然后按时间排序
    def preProcess(self, airplanes):
        res = []
        for i in range(len(airplanes)):
            res.append([airplanes[i].start, 1])
            res.append([airplanes[i].end, 0])
        return res

    def countOfAirplanes(self, airplanes):
        maxCount = 0
        count = 0
        planes = sorted(self.preProcess(airplanes), cmp = sorter)

        for i in range(len(planes)):
            if planes[i][1]:
                count += 1
            else:
                count -= 1
            maxCount = max(maxCount, count)
        return maxCount