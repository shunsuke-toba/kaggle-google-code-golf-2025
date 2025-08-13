def p(grid):
    rows = len(grid)
    cols = len(grid[0])

    # Find the horizontal line of 5s
    line_row = -1
    for r in range(rows):
        if grid[r][0] == 5:
            line_row = r
    
    # For each column, extend 1s away from line and 2s toward line
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in [0, 5]:
                continue
            if (grid[r][c] == 1) == (r < line_row): d = -1
            else: d = 1
            i = r
            while 0 <= i < rows and i != line_row:
                grid[i][c] = grid[r][c]
                i += d
    return grid