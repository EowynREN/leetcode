# 思路: 主要还是BFS by level order
# 关键是如何构建图,方法一(被注释的,自己写的)用的方法太过复杂,会超时
#    因为是string,可以完全把每个word里的char换了字母这样的复杂度是O(26n)




# class Node:
#     def __init__(self, label):
#         self.label = label
#         self.neighbors = []
#
#
# class Solution:
#     # @param start, a string
#     # @param end, a string
#     # @param dict, a set of string
#     # @return an integer
#     def ladderLength(self, start, end, dict):
#         # write your code here
#         if not dict:
#             return 2147483647
#
#         if start == end:
#             return 1
#
#         dict.add(start)  # 在ide里要用append才能过,不知道为什么,在lintcode上add就可以,可能是用了关键字做变量的原因
#         dict.add(end)
#         dic = list(set(dict))
#
#         # init
#         map = self.drawGraph(dic)
#
#         first = map[start]
#
#         queue = [first]
#         visited = set([first])
#         ladder = 1
#         count = 0
#         flag = False
#
#         while queue:
#             count = len(queue)
#             ladder += 1
#
#             for i in range(count):
#                 node = queue.pop(0)
#                 for neighbor in node.neighbors:
#                     if neighbor in visited:
#                         continue
#
#                     if neighbor.label == end:
#                         return ladder
#                     queue.append(neighbor)
#                     visited.add(neighbor)
#
#         return 2147483647
#
#     def drawGraph(self, dic):
#         map = {}
#         for i in range(len(dic)):
#             if dic[i] in map:
#                 node = map[dic[i]]
#             else:
#                 node = Node(dic[i])
#                 map[node.label] = node
#
#             for j in range(len(dic)):
#                 if i == j:
#                     continue
#                 if self.isNeighbor(dic[i], dic[j]):
#                     if dic[j] in map:
#                         node.neighbors.append(map[dic[j]])
#                     else:
#                         neighbor = Node(dic[j])
#                         node.neighbors.append(neighbor)
#                         map[dic[j]] = neighbor
#         return map
#
#
#     def isNeighbor(self, word1, word2):
#         diff = 0
#
#         for i in range(len(word1)):
#             if word1[i] != word2[i]:
#                 diff += 1
#
#         return diff == 1 or len(word1) == 1

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        # write your code here
        if not dict:
            return 0

        if start == end:
            return 1

        # 这里是一个关键
        # 把start 和 end都加进去,可以省去很多edge case(比如:start在dict里end不在, end在start不在, start end都不在, start end都在 ...)
        dict.add(start)  # 在ide里要用append才能过,不知道为什么,在lintcode上add就可以,可能是用了关键字做变量的原因
        dict.add(end)

        queue = [start]
        visited = set([start])
        ladder = 1
        count = 0

        # BFS by level order
        while queue:
            ladder += 1
            count = len(queue)

            for i in range(count):
                word = queue.pop(0)
                for neighbor in self.getNext(word, end, dict):
                    if neighbor in visited:
                        continue

                    if neighbor == end:
                        return ladder

                    queue.append(neighbor)
                    visited.add(neighbor)
        return 2147683647


    def getNext(self, word, end, dict):
        next_words = []

        for i in range(len(word)):
            next_word = list(word)
            for j in range(ord('a'), ord('z') + 1):
                next_word[i] = chr(j)

                t = ''.join(next_word)
                if t in dict:
                    next_words.append(t)
        return next_words

s = Solution()
print s.ladderLength("game", "thee", ["frye","heat","tree","thee","game","free","hell","fame","faye"])