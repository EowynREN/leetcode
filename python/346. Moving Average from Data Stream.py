"""
前缀和的解法
"""
class MovingAverage(object):
    def __init__(self, size):
        self.prefixSum = [0] * 100000
        self.size = size
        self.index = 0

    def next(self, val):
        self.index += 1
        self.prefixSum[self.index] = self.prefixSum[self.index - 1] + val
        if self.index - self.size >= 0:
            return (self.prefixSum[self.index] - self.prefixSum[self.index - self.size]) / self.size
        else:
            return self.prefixSum[self.index] / self.index


"""
follow-up: 优化空间，滚动数组(rolling array)
"""
class MovingAverage(object):
    def __init__(self, size):
        self.prefixSum = [0] * (size + 1)
        self.size = size
        self.index = 0

    def next(self, val):
        self.index += 1
        self.prefixSum[self.mod(self.index)] = self.prefixSum[self.mod(self.index - 1)] + val
        if self.index - self.size >= 0:
            return (self.prefixSum[self.mod(self.index)] - self.prefixSum[self.mod(self.index - self.size)]) / self.size
        else:
            return self.prefixSum[self.index] / self.index

    def mod(self, x):
        return x % (self.size + 1)
