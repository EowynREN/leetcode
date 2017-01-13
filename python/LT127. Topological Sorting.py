# Definition for a Directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    """
    @param graph: A list of Directed graph node
    @return: A list of graph nodes in topological order.
    """
    def topSort(self, graph):
        # write your code here
        res = []

        # count indegree on each node
        map = {}
        for node in graph:
            for neighbor in node.neighbors:
                if neighbor in map:
                    map[neighbor] += 1
                else:
                    map[neighbor] = 1

        # inqueue the nodes with 0 indegree
        queue = []
        for node in graph:
            if node not in map:
                queue.append(node)
                res.append(node)

        # topological sorting
        while queue:
            node = queue.pop(0)
            for neighbor in node.neighbors:
                # decrease the node eith dependency
                map[neighbor] -= 1

                # inqueue   the node with 0 indegree
                if map[neighbor] == 0:
                    queue.append(neighbor)
                    res.append(neighbor)
        return res