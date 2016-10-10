class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class UnionFind:
    def __init__(self, set):
        self.father = {}
        for label in set:
            self.father[label] = label

    def find(self, label):
        ancestor = self.father[label]
        while ancestor != self.father[ancestor]:
            ancestor = self.father[ancestor]
        return ancestor

    def compressed_find(self, label):
        # find big brother/ancestor
        ancestor = self.father[label]
        while ancestor != self.father[ancestor]:
            ancestor = self.father[ancestor]

        # compress the path
        while label != self.father[label]:
            next = self.father[label]  # keep the next node for record
            self.father[label] = ancestor
            label = next  # move the cur pointer to next node

    def union(self, x, y):
        fa_x = self.compressed_find(x)
        fa_y = self.compressed_find(y)

        if fa_x != fa_y:
            self.father[fa_y] = fa_x


class Solution:
    # @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    # @return {int[][]} a connected set of a undirected graph
    def connectedSet(self, nodes):
        # Write your code here
        if not nodes:
            return 0

        # remove the duplicates
        # 因为此处可能出现{1,2,4 # 2,1,4 # 3,5 # 4,1,2 # 5,3}的情况(#表示分隔)
        # 这个case中(图): 1-2-4  3-5
        #                |___|
        # 但是在nodes和its neighbors有很多重复出现的值
        # 因此要去掉
        hashset = set()
        for node in nodes:
            hashset.add(node.label)
            for neighbour in node.neighbors:
                hashset.add(neighbour.label)

        # init the set
        uf = UnionFind(hashset)

        # O(n^2)
        for node in nodes:
            for neighbour in node.neighbors:
                fnode = uf.compressed_find(node.label)
                fneighbour = uf.compressed_find(neighbour.label)
                if fnode != fneighbour:
                    uf.union(node.label, neighbour.label)

        # 此处注意: 一定要从hashset里遍历所有的node,然后用compressed_find查找他们的ancestor
        #          不能直接从uf.father里遍历
        #          因为在不断union node到同一个set中的时候,后出现的node有可能成为super ancestor
        #          如果直接从uf.father通过key,val来遍历,有可能会将同一个ancestor下的set分成好几个subset
        #          这是因为后出现的node成为super ancestor,而之前的node在uf.father未被更新(因为已经遍历/扫描过它),还是属于ancestor的集合

        # O(nlogn)
        res = {}
        for item in hashset:
            fa = uf.compressed_find(item)
            if fa in res.keys():
                res[fa].append(item)
                # 排序输出结果
                res[fa] = sorted(res[fa])
            else:
                res[fa] = [item]
        return res.values()


n1 = UndirectedGraphNode(1)
n2 = UndirectedGraphNode(2)
n3 = UndirectedGraphNode(3)
n4 = UndirectedGraphNode(4)
n5 = UndirectedGraphNode(5)
n1.neighbors = [n2, n4]
n2.neighbors = [n1, n4]
n3.neighbors = [n5]
n4.neighbors = [n1]
n5.neighbors = [n3]

nodes = [n1, n2, n3, n4, n5]
s = Solution()
print s.connectedSet(nodes)