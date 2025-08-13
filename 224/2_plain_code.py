def p(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    # Create copy of grid for result
    result = [row[:] for row in grid]
    
    # Find all positions of 5s (markers)
    markers = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 5:
                markers.append((r, c))
    
    # Find non-zero pattern value (not 0 or 5)
    pattern_value = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 0 and grid[r][c] != 5:
                pattern_value = grid[r][c]
                break
        if pattern_value:
            break
    
    if not markers or not pattern_value:
        return result
    
    # Calculate bounding rectangle from markers, extending inward by 1
    min_row = min(r for r, c in markers)
    max_row = max(r for r, c in markers)
    min_col = min(c for r, c in markers)
    max_col = max(c for r, c in markers)
    
    # Adjust bounds - find the enclosed rectangle
    # From the examples, it seems to find the rectangle one step inward from markers
    min_row = min_row + 1
    max_row = max_row - 1
    min_col = min_col + 1
    max_col = max_col - 1
    
    # Ensure valid bounds
    if min_row > max_row or min_col > max_col:
        return result
    
    # Draw rectangular frame using pattern value
    # Top and bottom edges
    for c in range(min_col, max_col + 1):
        if result[min_row][c] == 0:
            result[min_row][c] = pattern_value
        if result[max_row][c] == 0:
            result[max_row][c] = pattern_value
    
    # Left and right edges
    for r in range(min_row, max_row + 1):
        if result[r][min_col] == 0:
            result[r][min_col] = pattern_value
        if result[r][max_col] == 0:
            result[r][max_col] = pattern_value
    
    return result