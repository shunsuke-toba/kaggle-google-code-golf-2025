def p(grid):
    rows, cols = len(grid), len(grid[0])
    
    # Find center 3x3 block (has numbers in all rows and columns)
    center_r, center_c = -1, -1
    for r in range(0, rows):
        for c in range(0, cols):
            if r + 2 < rows and c + 2 < cols:
                # Check if this 3x3 block has numbers in all 3 rows and all 3 columns
                has_all_rows = True
                has_all_cols = True
                
                for i in range(3):
                    row_has_number = False
                    for j in range(3):
                        if grid[r + i][c + j] > 0:
                            row_has_number = True
                            break
                    if not row_has_number:
                        has_all_rows = False
                        break
                
                for j in range(3):
                    col_has_number = False
                    for i in range(3):
                        if grid[r + i][c + j] > 0:
                            col_has_number = True
                            break
                    if not col_has_number:
                        has_all_cols = False
                        break
                
                if has_all_rows and has_all_cols:
                    center_r, center_c = r, c
                    break
        if center_r != -1:
            break
    
    # Check 8 directions from center
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    for dr, dc in directions:
        # Check 3x3 block one step away in this direction (with 1 cell gap)
        check_r = center_r + dr * 4
        check_c = center_c + dc * 4
        
        if (check_r >= 0 and check_r + 2 < rows and 
            check_c >= 0 and check_c + 2 < cols):
            # Check if this block has any pattern
            color = -1
            for i in range(3):
                for j in range(3):
                    if grid[check_r + i][check_c + j] > 0:
                        color = grid[check_r + i][check_c + j]
                        break
                if color != -1:
                    break

            if color != -1:
                # Propagate the pattern repeatedly from center in this direction (with 1 cell gap)
                step = 1
                while True:
                    target_r = center_r + dr * 4 * step
                    target_c = center_c + dc * 4 * step
                    
                    # Copy the pattern from the seed block to the target block
                    for i in range(3):
                        for j in range(3):
                            target_i = target_r + i
                            target_j = target_c + j
                            if 0 <= target_i < rows and 0 <= target_j < cols and grid[center_r + i][center_c + j] > 0:
                                grid[target_i][target_j] = color

                    if (target_r < 0 or target_r + 2 >= rows or 
                        target_c < 0 or target_c + 2 >= cols):
                        break
                    
                    step += 1

    return grid