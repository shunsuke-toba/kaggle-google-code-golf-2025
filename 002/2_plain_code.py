def p(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                grid[i][j] = 4
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for loop in range(16):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 4:
                    for d in dir:
                        ni, nj = i + d[0], j + d[1]
                        if not (0 <= ni < len(grid) and 0 <= nj < len(grid[i])) or grid[ni][nj] == 0:
                            grid[i][j] = 0
    return grid