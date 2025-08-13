def p(grid):
    # Find the largest rectangular region of the same non-zero value
    rows = len(grid)
    cols = len(grid[0])
    
    # Initialize result grid with zeros
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for r in range(rows):
        # Update heights for current row
        for c in range(cols):
            for r2 in reversed(range(r+1, rows)):
                for c2 in reversed(range(c+1, cols)):
                    area = (r2 - r + 1) * (c2 - c + 1)
                    if area < 6:
                        continue
                    ok = True
                    for i in range(r, r2 + 1):
                        for j in range(c, c2 + 1):
                            if grid[i][j] != grid[r][c] or grid[i][j] == 0:
                                ok = False
                                break
                    if not ok:
                        continue
                    # If a valid rectangle is found, fill it in the result grid
                    for i in range(r, r2 + 1):
                        for j in range(c, c2 + 1):
                            result[i][j] = grid[r][c]
                    return result
    return None