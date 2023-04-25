import heapq

class Type:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __cmp__(self, other):
        if self.freq != other.freq:
            return self.freq - other.freq

        # 这里如果freq是一样的话,就比较字符串
        # 把字母顺序靠后的放在前面,这样字母顺序靠后的就会被首先pop出去
        # 或者在最后放进res的时候,字母顺序靠后的会被先pop出放在较后的位置
        a = min(self.word, other.word)
        if self.word == other.word:
            return 0
        if a == self.word:
            return 1
        if a == other.word:
            return -1


    def add(self):
        self.freq += 1


class Solution:
    # @param {string[]} words a list of string
    # @param {int} k an integer
    # @return {string[]} a list of string
    def topKFrequentWords(self, words, k):
        # Write your code here
        map = {}

        for word in words:
            if word in map:
                map[word].add()
            else:
                map[word] = Type(word, 1)

        minHeap = []
        for word in map:
            heapq.heappush(minHeap, map[word])

            if len(minHeap) > k:
                heapq.heappop(minHeap)

        res = [''] * k
        for i in range(k - 1, -1, -1):
            res[i] = heapq.heappop(minHeap).word
        return res

s =Solution()
print s.topKFrequentWords(["yes","lint","code","yes","code","baby","you","baby","chrome","safari","lint","code","body","lint","code"], 3
)