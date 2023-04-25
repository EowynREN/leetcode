class Solution:
    """
    Get all distinct N-Queen solutions
    @param n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        res = []
        if n > 0:
            self.dfs(n, [], res)
        return res
    
    def dfs(self, n, sol, res):
        if len(sol) == n:
            res.append(self.drawChessboard(sol))
            return
        
        for colIndex in range(n):
            if self.attack(sol, colIndex):
                continue
            sol.append(colIndex)
            self.dfs(n, sol, res)
            del sol[-1]
        

    # 根据sol这个一维数组所表示的:
    #                         1. sol的index表示第几row
    #                         2. sol[i]表示第irow的第几个col
    def drawChessboard(self, sol):
        chessboard = []
        for i in range(len(sol)):
            s = ""
            for j in range(len(sol)):
                s += 'Q' if j == sol[i] else '.'
            chessboard.append(s)
        return chessboard
        
    def attack(self, sol, col):
        # 一个sol是一行, 因为行列的个数相等,所以乐意通过列数求行数

        row = len(sol)
        for rowIndex in range(len(sol)):
            # 是否在同一列上
            if sol[rowIndex] == col:
                return True

            # 是否在'右-左'对角线上
            if rowIndex + sol[rowIndex]== row + col:
                return True

            # 是否在'左-右'对角线上
            if rowIndex - sol[rowIndex]== row - col:
                return True
        return False

s = Solution()
print s.solveNQueens(8)