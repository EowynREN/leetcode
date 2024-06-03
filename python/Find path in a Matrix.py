def findPath(matrix, start, target):
    res = []
    start = (0, 0)
    target = (len(matrix) - 1, len(matrix[0] - 1))
    dfs(start, target, matrix, [], res, set())
    return res

def dfs(start, target, matrix, path, res, visited):
    if start == target:
        res.append(list(path))
        return

    if start in visited:
        return
    visited.add(start)

    path.append(start)
    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        x = start[0] + dx
        y = start[1] + dy

        if isValid(x, y, matrix, visited):
            dfs((x, y), target, matrix, path, res, visited)
            if len(res) != 0:
                return
    path.remove(-1)


def isValid(i, j, matrix, visited):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or (i, j) in visited or matrix[i][j] == '1':
        return False
    return True
