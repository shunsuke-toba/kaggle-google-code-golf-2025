def p(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            for k in range(i+2, len(grid)):
                for l in range(j+2, len(grid[i])):
                    ok = 1
                    for x in range(i+1, k):
                        ok = ok and not(grid[x][j] != 3 or grid[x][l] != 3)
                    for y in range(j+1, l):
                        ok = ok and not(grid[i][y] != 3 or grid[k][y] != 3)
                    if ok:
                        for x in range(i+1, k):
                            for y in range(j+1, l):
                                grid[x][y] = grid[x][y] or 4
    return grid