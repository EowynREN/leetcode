# 思路: 此题的题眼是,如果是图一定成环
#      也就是说: 在这个环里的任意两个node会拥有相同的ancestor
#      也就是说: 需要在edges集合中找出是否有两个点,拥有同样的father
#      ----> union find


class UnionFind():
    def __init__(self, n):
        self.father = {}
        for i in range(n):
            self.father[i] = i

    def compressed_find(self, x):
        parent = self.father[x]
        while parent != self.father[parent]:
            parent = self.father[parent]  # move to next node

        cur = self.father[x]
        while cur != self.father[cur]:
            temp = self.father[cur]
            self.father[cur] = parent
            cur = temp  # move to next node

        return parent

    def union(self, x, y):
        fa_x = self.compressed_find(x)
        fa_y = self.compressed_find(y)

        if fa_x != fa_y:
            self.father[fa_x] = fa_y


class Solution:
    # @param {int} n an integer
    # @param {int[][]} edges a list of undirected edges
    # @return {boolean} true if it's a valid tree, or false
    def validTree(self, n, edges):
        # 树必须满足n个节点，n - 1条边
        # 离散的点不算树
        if n - 1 != len(edges):
            return False

        uf = UnionFind(n)
        # 如果两个边里的node有同一个祖先  --> 成环，graph
        for i in range(len(edges)):
            if uf.compressed_find(edges[i][0]) == uf.compressed_find(edges[i][1]):
                return False
            uf.union(edges[i][0], edges[i][1])
        return True
