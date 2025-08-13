def p(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    result = [row[:] for row in grid]
    
    marker_pos = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 5:
                marker_pos = (r, c)
                break
        if marker_pos:
            break
    
    if not marker_pos:
        return result
    
    marker_r, marker_c = marker_pos
    
    best_pattern = None
    max_non_zero = 0
    
    for top in range(rows - 2):
        for left in range(cols - 2):
            pattern = []
            non_zero_count = 0
            
            for r in range(top, top + 3):
                row = []
                for c in range(left, left + 3):
                    value = grid[r][c]
                    row.append(value)
                    if value != 0:
                        non_zero_count += 1
                pattern.append(row)
            
            if non_zero_count > max_non_zero:
                max_non_zero = non_zero_count
                best_pattern = pattern
    
    if best_pattern:
        start_r = marker_r - 1
        start_c = marker_c - 1
        
        for dr in range(3):
            for dc in range(3):
                new_r = start_r + dr
                new_c = start_c + dc
                
                if 0 <= new_r < rows and 0 <= new_c < cols:
                    result[new_r][new_c] = best_pattern[dr][dc]
    
    return result