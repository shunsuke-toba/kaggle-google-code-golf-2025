def p(grid):
    n = len(grid)

    for r in range(n):
        for c in range(n):
            for sz in range(3, n):
                if r + sz - 1 < n and c + sz - 1 < n:
                    # Check if the square is surrounded by 1s
                    ok = True
                    for i in range(sz):
                        if grid[r][c + i] != 1 or grid[r + sz - 1][c + i] != 1 or grid[r + i][c] != 1 or grid[r + i][c + sz - 1] != 1:
                            ok = False
                    if ok:
                        # Fill the inner square with the appropriate color
                        for i in range(r + 1, r + sz - 1):
                            for j in range(c + 1, c + sz - 1):
                                if sz % 2 == 0:
                                    grid[i][j] = 2
                                else:
                                    grid[i][j] = 7
    return grid