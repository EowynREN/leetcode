# What is a grid - graph?
# Grid - graph are planar graphs with 4 - neighborhood connectivity, see examples of grid graphs below grid graph examples:
#
# 2 x 3 grid graph:
# 1 - 2 - 3
# |   |   |
# 4 - 0 - 5
#
# 3 x 3 grid graph:
# 7 - 8 - 4
# |   |   |
# 0 - 1 - 3
# |   |   |
# 5 - 2 - 6
#
# none - grid graph example:
# 1 - 3 - 6
# |   |   |
# 4 - 2   5
#
# Write a function that takes two integers n_rows and m_cols, and returns an n_rows x m_cols grid graph


# Returns a grid graph. The graph should be a data structure encapsulating its nodes and edges.
# are_connected(data_struct, node1_id, node2_id) -> bool ?
# convert_row_col_to_id(i, j, n_rows, m_cols) -> int ?
# convert_id_to_row_col(id, n_rows, m_cols) -> Tuple[int, int] ?
def build_grid_graph(n_rows, m_cols):  # graph

    # 4 nodes has degree of 2
    # edge nodes, degree of 3
    # rest of nodes, degree of 4

    grid = []
    for i in range(n_rows):
        for j in range(m_cols):
            grid[i][j] = i + j

    isConnected = [[False] * m_cols * n_rows for _ in range(n_rows * m_cols)]
    for i in range(m_cols * n_rows):
        ri, ci = convert_id_to_row_col(i, n_rows, m_cols)
        # Using ri and ci, how to find i's neighbours?
        # up: x, y = [(ri - 1, ci), (r1 + 1, ci), (ri, ci - 1), (r1, ci + 1)]
        # id = grid[x][y]

        # neighbours
        for x, y in [[ri - 1, ci], [r1 + 1, ci], [ri, ci - 1], [r1, ci + 1]]:
            if x < 0 or x >= m_cols * n_rows or y < 0 or y >= m_cols * n_rows:
                continue
            #
            nid = grid[x][y]
            isConnected[i][nid] = True
    return grid, isConnected


# what is the size of isConnected ?
# (m_cols *  n_rows) * (m_cols *  n_rows)
# Is there away to improve this?
# 0 -> [1, 3]
# 1 -> [0, 4, 2] # max 4 out degree
# are_connected is going to be O(1) per check

def convert_id_to_row_col(id, n_rows, m_cols):
    row = id / n_rows
    col = id % m_cols
    return (row, col)


def are_connected(isConnected, id1, id2):
    return isConnected[id1, id2]


# Testing
# 0 - 1 - 2
# |   |   |
# 3 - 4 - 5
# |   |   |
# 6 - 7 - 8

# grid
[[0, 1, 2],
 [3, 4, 5],
 [6, 7, 8]]

# isConnected
[[False, False, False, True, False, False, False, False, False],
 [False, False, False, False, False, False, False, False, False],
 [False, False, False, False, False, False, False, False, False],
 [False, False, False, False, False, False, False, False, False],
 [False, False, False, False, False, False, False, False, False],
 [False, False, False, False, False, False, False, False, False],
 [False, False, False, False, False, False, False, False, False],
 [False, False, False, False, False, False, False, False, False],
 [False, False, False, False, False, False, False, False, False],
 [False, False, False, False, False, False, False, False, False],
 ]

i = 0
ri, ci = [1, 0]
nid = 3

ri, ci = [0, 1]
nid = 1
