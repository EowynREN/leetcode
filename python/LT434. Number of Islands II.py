class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b


class UnionFind:
    def __init__(self, n, m):
        self.father = {}
        for i in range(n):
            for j in range(m):
                self.father[(i, j)] = (i, j)

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


class Solution:
    # @param {int} n an integer
    # @param {int} m an integer
    # @param {Pint[]} operators an array of point
    # @return {int[]} an integer array

    # 思路: 对operate的点的上下左右扫面一次
    #      如果是0,就停止;
    #      如果是1,union进1的那个集合里
    def valid(self, islands, x, y):
        if x < 0 or x >= len(islands) or y < 0 or y >= len(islands[0]) or islands[x][y] == 0:
            return False
        return True

    def numIslands2(self, n, m, operators):

        res = []
        count = 0
        uf = UnionFind(n, m)
        islands  = [[0 for j in range(m)] for i in range(n)]

        for opr in operators:
            # 如果这块陆地已经被翻过一次(0 -> 1)不需要再翻
            if islands[opr.x][opr.y] == 1:
                continue

            # 创建一个岛屿,先+1
            islands[opr.x][opr.y] = 1
            count += 1
            for pos in [[0,1],[0,-1],[1,0],[-1,0]]:
                x = opr.x + pos[0]
                y = opr.y + pos[1]
                # check边界条件
                if self.valid(islands, x, y):
                    # 此处注意: 一定要check当前的(i, j)和即将扫描的上下左右,是否在一个集合里
                    #          如果不在, 把  新翻的这个岛  和  上下左右为1的岛屿  ""添加""  到一个集合里
                    #          因为这个新的岛屿归并到以前岛屿的集合里 ----> 减少岛屿个数
                    #          如果这个岛屿和上下左右任意一个方向在一个集合里 ----> 不能减少岛屿这个
                    #          这里设置这个条件 ----> 就是为了count

                    # e.g., 2, 2, [[0,0],[1,1],[1,0],[0,1]]
                    #
                    #       0 0  ->  1 0  ->  1 0  ->  1 x
                    #       0 0      0 1      1 1      1 1
                    #       这里的x,当扫面完向左(0, 0)位置后,x已经被加入了其集合中
                    #       再向下扫描的时候, x已经和(1, 1)在一个集合里
                    #       因为这个if条件,count不会被再次-1
                    if uf.compressed_find((opr.x, opr.y)) != uf.compressed_find((x, y)):
                        count -=1
                        uf.union((opr.x, opr.y), (x, y))
            res.append(count)
        return res


s = Solution()
o1 = Point(0, 0)
o2 = Point(1, 1)
o3 = Point(1, 0)
o4 = Point(0, 1)
print s.numIslands2(2, 2, [o1, o2, o3, o4])