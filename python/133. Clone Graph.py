"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        root = node
        nodes = self.getDistinctNodes(node)

        # 克隆所有的node
        originToClone = {}
        for node in nodes:
            originToClone[node] = Node(node.val)

        # 再建立连接
        for node in nodes:
            new_node = originToClone[node]
            for neighbor in node.neighbors:
                new_neighbor = originToClone[neighbor]
                new_node.neighbors.append(new_neighbor)
        return originToClone[root]

    # bfs
    def getDistinctNodes(self, node):
        queue = [node]
        res = set()
        res.add(node)

        while queue:
            node = queue.pop(0)

            for neighbor in node.neighbors:
                if neighbor not in res:
                    queue.append(neighbor)
                    res.add(neighbor)
        return res
