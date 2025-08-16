def p(grid):
    # Fill connected 5s with values from top row
    result = [row[:] for row in grid]
    
    def flood_fill(row, col, fill_value):
        # Bounds check and value check
        if 0 <= row < 10 and 0 <= col < 10 and result[row][col] == 5:
            result[row][col] = fill_value
            # Fill in 4 directions
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                flood_fill(row + dr, col + dc, fill_value)
    
    # For each column, if top row has a value, flood fill connected 5s
    for col in range(10):
        if grid[0][col] != 0:  # Non-zero value in top row
            fill_value = grid[0][col]
            # Start flood fill from rows 1-9 in this column
            for row in range(1, 10):
                if result[row][col] == 5:
                    flood_fill(row, col, fill_value)
    
    return result