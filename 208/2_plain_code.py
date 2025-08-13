def p(grid):
    max_area = 0
    max_r = max_c = 0
    max_h = max_w = 0
    rows = len(grid)
    cols = len(grid[0])
    for r1 in range(rows):
        for c1 in range(cols):
            for r2 in range(r1+2, rows):
                for c2 in range(c1+2, cols):
                    if all(grid[r][c1] == grid[r1][c1] for r in range(r1, r2 + 1)) and \
                       all(grid[r1][c] == grid[r1][c1] for c in range(c1, c2 + 1)) and \
                       all(grid[r][c] == 0 for r in range(r1+1, r2) for c in range(c1+1, c2)):
                        area = (r2 - r1 + 1) * (c2 - c1 + 1)
                        if area > max_area:
                            max_area = area
                            max_r, max_c = r1, c1
                            max_h, max_w = r2 - r1 + 1, c2 - c1 + 1
    for r1 in range(rows-max_h+1):
        for c1 in range(cols-max_w+1):
            ok = True
            for x in range(r1+1, r1+max_h-1):
                for y in range(c1+1, c1+max_w-1):
                    ok = ok and grid[x][y] == 0
            if ok:
                for i in range(max_h):
                    for j in range(max_w):
                        grid[r1+i][c1+j] = grid[max_r+i][max_c+j]
    return grid