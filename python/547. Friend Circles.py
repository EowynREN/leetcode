#-*- coding:utf8 -*-
#coding=utf-8
class UnionFind:
    def __init__(self, n):
        self.father = {}

        for i in xrange(n):
            self.father[i] = i

    def compressed_find(self, x):
        ancestor = self.father[x]

        while ancestor != self.father[ancestor]:
            ancestor = self.father[ancestor]

        while x != self.father[x]:
            next = self.father[x]
            self.father[x] = ancestor
            x = next

        return ancestor

    def union(self, x, y):
        fa_x = self.compressed_find(x)
        fa_y = self.compressed_find(y)

        if fa_x != fa_y:
            self.father[fa_y] = fa_x

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M or not M[0]:
            return 0

        n = len(M)

        uf = UnionFind(n)

        for i in xrange(n):
            for j in xrange(n):
                if M[i][j] == 1:
                    uf.union(i, j)

        res = set()
        for i in xrange(n):
            for j in xrange(n):
                if M[i][j] == 0:
                    continue

                uf.compressed_find(j)
                res.add(uf.father[j])
        return len(res)

s = Solution()
print s.findCircleNum([[1,1,0],
 [1,1,0],
 [0,0,1]])