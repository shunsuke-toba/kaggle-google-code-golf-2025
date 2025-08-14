def p(grid):
    # Find positions where the grid has value 3 and output the corresponding 180-degree rotated values
    result = []
    
    for i in range(16):
        if 3 in grid[i]:  # Only process rows that contain 3
            row = []
            for j in range(16):
                if grid[i][j] == 3:
                    # For 180-degree rotation: (i,j) -> (15-i, 15-j)
                    rotated_value = grid[15-i][15-j]
                    row.append(rotated_value)
            if row:  # Only add non-empty rows
                result.append(row)
    
    return result