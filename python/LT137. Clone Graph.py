# 思路: BFS + 2个queue
#      q1 --- 用来放原图的节点, 同时这个queue也被用来遍历
#      q2 --- 用来放新的呗copy出来的节点, pop和push都和q1保持一致


# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        # 1. 用hashmap来保证每个被copy的节点,只会被创建出来一次 ----> (查重)
        # 2. 当发现这个节点已经被创建了以后,通过key获取这个节点,再进行进一步操作
        self.dict = {}

    def cloneGraph(self, node):
        # write your code here
        if not node:
            return None

        res = UndirectedGraphNode(node.label)
        self.dict[node.label] = res
        q1 = [node]
        q2 = [res]

        while q1:
            n = q1.pop(0)
            cur = q2.pop(0)

            for neighbor in n.neighbors:
                # self connected
                if neighbor == n:
                    cur.neighbors.append(cur)
                    continue

                #if the node hasn't been copied
                if neighbor.label not in self.dict:
                    # copy the current node
                    new_node = UndirectedGraphNode(neighbor.label)
                    self.dict[neighbor.label] = new_node

                    q1.append(neighbor)
                    q2.append(new_node)

                    # add edge
                    cur.neighbors.append(new_node)
                else:
                    # add edge
                    cur.neighbors.append(self.dict[neighbor.label])
        return res