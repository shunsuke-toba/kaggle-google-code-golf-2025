def p(j):
    result = []
    for r in range(9):
        row = []
        for c in range(9):
            # Get the corresponding positions in the 3x3 grid
            block_r = r // 3
            block_c = c // 3
            pattern_r = r % 3
            pattern_c = c % 3
            
            # If both the block position and pattern position are non-zero in original grid
            if j[block_r][block_c] != 0 and j[pattern_r][pattern_c] != 0:
                row.append(j[pattern_r][pattern_c])
            else:
                row.append(0)
        result.append(row)
    return result