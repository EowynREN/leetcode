# 思路:

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        # write your code here
        ladder = []
        graph = {}
        distance = {}

        # 依然是一个小trick
        # 把start 和 end都加进去,可以省去很多edge case(比如:start在dict里end不在, end在start不在, start end都不在, start end都在 ...)
        dict.append(start)
        dict.append(end)
        dict = set(dict)

        # 这里非常重要的两个数据结构
        # hashmap -- graph: 建图
        # hashmap -- distance: 按照只差一个字母的规矩,来算level,存储{node: level should on}
        #                      这样就得到了一副有level order的图了
        #                      这里有个小trick,在见图的和算distance的时候,把neighbor作为key,让它指向他的origin
        #                      这样start会变成终点,end会变成起点,因为是反向建的图(所有的direction都是反向的)
        self.bfs(graph, distance, start, end, dict)

        # 从后到前dfs遍历,把每个path都加进结果集
        self.dfs(graph, distance, end, start, dict, [end], ladder)

        return ladder

    def bfs(self, graph, distance, start, end, dict):
        queue = [start]
        distance[start] = 0

        for word in dict:
            graph[word] = []

        while queue:
            cur = queue.pop(0)

            neighbors = self.getNeighbors(cur, dict)
            for neighbor in neighbors:
                graph[neighbor].append(cur)

                if neighbor not in distance:
                    distance[neighbor] = distance[cur] + 1
                    queue.append(neighbor)


    def getNeighbors(self, word, dict):
        next_words = []
        for i in range(len(word)):
            next_word = list(word)
            for j in range(ord('a'), ord('z') + 1):
                next_word[i] = chr(j)

                t = ''.join(next_word)
                if t != word and t in dict:
                    next_words.append(t)
        return next_words

    # 标准dfs模板:加一个,删一个
    def dfs(self, graph, distance, cur, start, dict, tmp, ladder):

        # 递归出口: 到达start,表示一条路径(从end到start)已经得到了
        if cur == start:
            # 因为是反向建的图,加入的时候记得把结果reverse一下
            ladder.append(list(tmp[::-1]))
            return

        for neighbor in graph[cur]:
            # is neighbor
            if neighbor in distance and distance[neighbor] + 1 == distance[cur]:
                tmp.append(neighbor)
                self.dfs(graph, distance, neighbor, start, dict, tmp, ladder)
                del tmp[-1]

s = Solution()
print s.findLadders("hit","cog",["hot","dot","dog","lot","log"])