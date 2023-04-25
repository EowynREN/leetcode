# 思路：从外围向里bfs search，只添加'O'的点进队
#       如果存在Surrounded Regions，那么一定存在一个围墙
#       使得从外向内的搜索碰到墙以后就停止了（因为只添加'O'的点，围墙是'X'）
#       将已经搜索过的外围的'O'点标为'已访问'
#       这时全棋盘剩下的'O'就是墙里的'O'点了
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Solution:
    # @param {list[list[str]]} board a 2D board containing 'X' and 'O'
    # @return nothing
    def surroundedRegions(self, board):
        # Write your code here
        if len(board) == 0:
            return

        n, m = len(board), len(board[0])

        # 添加最左列和最右列为'O'的点，开始搜索
        for i in range(n):
            self.bfs(board, i, 0)
            self.bfs(board, i, m - 1)

        # 添加最上列和最下列为'O'的点，开始搜索
        for j in range(1, m - 1):
            self.bfs(board, 0, j)
            self.bfs(board, n - 1, j)

        for i in range(n):
            for j in range(m):
                # 将'已访问'的'O'点，变回原来的'O'点
                if board[i][j] == 'F':
                    board[i][j] = 'O'
                # 将围墙里的'O'点，翻转为'X'点
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

    def bfs(self, board, i, j):
        if board[i][j] != 'O':
            return

        queue = [Node(i, j)]

        while queue:
            cur = queue.pop(0)
             # 'F' means free
            board[cur.x][cur.y] = 'F'

            self.enqueue(board, cur, queue)


    def enqueue(self, board, node, queue):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        n, m = len(board), len(board[0])

        for i in range(4):
            x = node.x + dx[i]
            y = node.y + dy[i]

            # check validity
            if x < 0 or x >= n or y < 0 or y >= m or board[x][y] != 'O':
                continue

            # 'V' means visited
            board[x][y] = 'V'
            queue.append(Node(x, y))



s = Solution()
print s.surroundedRegions(["XXXX","XOOX","XXOX","XOXX"])
