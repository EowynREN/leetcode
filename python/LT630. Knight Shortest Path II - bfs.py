class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

# 思路: bfs by level order
class Solution:
    # @param {boolean[][]} grid a chessboard included 0 and 1
    # @return {int} the shortest path
    def shortestPath2(self, grid):
        # Write your code here
        if not grid or not grid[0]:
            return -1

        n, m = len(grid), len(grid[0])

        shortest = 0
        queue = [Point(0, 0)]
        visited = set([(0, 0)])
        level = 0

        while queue:
            level = len(queue)

            for i in range(level):
                point = queue.pop(0)

                # meet barrier, cannot pass through
                if grid[point.x][point.y] == 1:
                    continue

                if point.x == n - 1 and point.y == m - 1:
                    return shortest

                self.enqueue(queue, point, grid, visited)

            shortest += 1

        return -1

    def enqueue(self, queue, point, grid, visited):
        dx = [-1, 1,-2, 2]
        dy = [ 2, 2, 1, 1]

        n, m = len(grid), len(grid[0])

        for i in range(4):
            x = point.x + dx[i]
            y = point.y + dy[i]

            if x < 0 or x >= n or y < 0 or y >= m or (x, y) in visited:
                continue

            queue.append(Point(x, y))
            visited.add((x, y))

