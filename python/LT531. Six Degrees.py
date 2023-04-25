# Definition for Undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

# 思路：BFS + count node for each level

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