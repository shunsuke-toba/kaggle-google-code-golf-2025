def p(grid):
    # Find cells with value 2 and place 1s in the 8 surrounding cells
    # Create a copy of the grid for the result
    result = [row[:] for row in grid]
    
    height = len(grid)
    width = len(grid[0])
    
    # 8 directions (Moore neighborhood)
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    
    # Scan all cells to find 2s
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 2:
                # Place 1s around the 2 (only if the cell is currently 0)
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    # Check bounds
                    if 0 <= ni < height and 0 <= nj < width:
                        if result[ni][nj] == 0:
                            result[ni][nj] = 1
    
    return result