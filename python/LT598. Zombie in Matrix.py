class Coordinate:
    def __init__(self, a, b):
        self.x = a
        self.y = b

class Solution:
    # @param {int[][]} grid  a 2D integer grid
    # @return {int} an integer
    def zombie(self, grid):
        # Write your code here
        if not grid or not grid[0]:
            return 0

        n, m = len(grid), len(grid[0])

        queue = []
        visited = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    queue.append(Coordinate(i, j))
                    visited.append((i, j))

        level = 0
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        days = 0

        while queue:
            level = len(queue)

            for i in range(level):
                position = queue.pop(0)

                for move in range(4):
                    x = position.x + dx[move]
                    y = position.y + dy[move]

                    if self.isSatisfied(x, y, n, m, visited, grid):
                        grid[x][y] = 1
                        queue.append(Coordinate(x, y))
                        visited.append((x, y))
            days += 1
        return days - 1 if self.check(n, m, grid) else -1

    def isSatisfied(self, x, y, n, m, visited, grid):
        if x < 0 or x >= n:
            return False

        if y < 0 or y >= m:
            return False

        if (x, y) in visited or grid[x][y] != 0:
            return False

        return True

    def check(self, n, m, grid):
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    return False
        return True

s = Solution()
print s.zombie([[0,2,0],[2,2,0],[2,0,1]])