class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class UnionFind():
    def __init__(self, hashset):
        self.father = {}
        for label in hashset:
            self.father[label] = label

    def compressed_find(self, label):
        ancestor = self.father[label]
        while ancestor != self.father[ancestor]:
            ancestor = self.father[ancestor]

        while label != self.father[label]:
            next = self.father[label]
            self.father[label] = ancestor
            label = next
        return ancestor

    def union(self, x, y):
        fa_x = self.compressed_find(x)
        fa_y = self.compressed_find(y)

        if fa_x != fa_y:
            self.father[fa_y] = fa_x


class Solution:
    # @param {DirectedGraphNode[]} nodes a array of directed graph node
    # @return {int[][]} a connected set of a directed graph
    def connectedSet2(self, nodes):
        # remove the dupliactes
        hashset = set()
        for node in nodes:
            hashset.add(node.label)
            for neighbor in node.neighbors:
                hashset.add(neighbor.label)

        # init the set
        uf = UnionFind(hashset)

        # union the sets
        for node in nodes:
            for neighbor in node.neighbors:
                uf.union(node.label, neighbor.label)

        # drag the res
        res = {}
        for item in hashset:
            # 此处注意: 一定要再找一次ancestor

            #         e.g., [1,2,4#3, 5#4#5#6, 5 ]
            #         1 -> 2 -> 4
            #         3 -> 5 <- 6
            #         -------------------------------------     fa : child
            #         |  1  |  2  |  3  |  4  |  5  |  6  |      1 : 2
            #         -------------------------------------      2 : 4
            #         |  1  |  1  |  6  |  1  |  3  |  6  |      4 : []
            #         -------------------------------------      5 : []
            #                                                    6 : 5
            #         3的father一开始是3,但是当6被扫描后,会查找6与5的关系
            #         进而, 找到6与3的关系
            #         最后添加: 6 : 3 (即3的father是6)

            # 如果直接在此处不再compressed_find一次,那么结果就会变成[[1, 2, 4], [3, 6], [5]]
            # 5被单独放出来了
            fa = uf.compressed_find(item)
            if fa in res:
                res[fa].append(item)
                res[fa] = sorted(res[fa])
            else:
                res[fa] = [item]

        return res.values()


n1 = DirectedGraphNode(1)
n2 = DirectedGraphNode(2)
n3 = DirectedGraphNode(3)
n4 = DirectedGraphNode(4)
n5 = DirectedGraphNode(5)
n6 = DirectedGraphNode(6)
n1.neighbors = [n2]
n2.neighbors = [n4]
n3.neighbors = [n5]
n6.neighbors = [n5]

nodes = [n1, n2, n3, n4, n5, n6]
s = Solution()
print s.connectedSet2(nodes)