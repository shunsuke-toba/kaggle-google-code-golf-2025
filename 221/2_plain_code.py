def p(grid):
    # Count zeros and non-zeros
    zero_count = 0
    non_zero_count = 0
    for r in range(3):
        for c in range(3):
            if grid[r][c] == 0:
                zero_count += 1
            else:
                non_zero_count += 1
    
    # Output size is zero_count * 3
    output_size = zero_count * 3
    
    # Initialize result grid
    result = [[0 for _ in range(output_size)] for _ in range(output_size)]
    
    # Place non_zero_count patterns from left to right, top to bottom
    patterns_placed = 0
    for block_row in range(output_size // 3):
        if patterns_placed >= non_zero_count:
            break
        for block_col in range(output_size // 3):
            if patterns_placed >= non_zero_count:
                break
            # Place 3x3 pattern at this block position
            for r in range(3):
                for c in range(3):
                    result[block_row * 3 + r][block_col * 3 + c] = grid[r][c]
            patterns_placed += 1
    
    return result