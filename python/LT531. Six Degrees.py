# Definition for Undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

# 思路：BFS

class Solution:
    '''
    @param {UndirectedGraphNode[]} graph a list of Undirected graph node
    @param {UndirectedGraphNode} s, t two Undirected graph nodes
    @return {int} an integer
    '''

    def sixDegrees(self, graph, s, t):
        # Write your code here
        if not s or not t:
            return -1

        # corner case
        # 如果是自己和自己
        if s == t:
            return 0

        queue = [s]
        degree = 0
        pool = set()
        pool.add(s)

        while queue:
           count = len(queue)
           degree += 1

           for i in range(count):
               node = queue.pop(0)

               for neighbor in node.neighbors:
                   if neighbor == t:
                       return degree
                   if neighbor in pool:
                       continue
                   queue.append(neighbor)
        return -1


n1 = UndirectedGraphNode(1)
n21 = UndirectedGraphNode(2)
n22 = UndirectedGraphNode(2)
n31 = UndirectedGraphNode(3)
n32 = UndirectedGraphNode(3)
n4 = UndirectedGraphNode(4)

n1.neighbors.append(n21)
n21.neighbors.append(n1)

n4.neighbors.append(n4)
n4.neighbors.append(n31)
n31.neighbors.append(n4)

graph = [n1, n21, n22, n31, n32, n4]

s = Solution()
s.sixDegrees(graph, n21, n22)
