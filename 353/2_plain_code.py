def p(grid):
    # Find 3s and move them one step closer to 4s
    result = [row[:] for row in grid]
    
    height = len(grid)
    width = len(grid[0])
    
    # Find position of 3 and 4
    pos_3 = None
    pos_4 = None
    
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 3:
                pos_3 = (i, j)
            elif grid[i][j] == 4:
                pos_4 = (i, j)
    
    if pos_3 and pos_4:
        i3, j3 = pos_3
        i4, j4 = pos_4
        
        # Calculate direction to move 3 towards 4
        di = 0 if i3 == i4 else (1 if i4 > i3 else -1)
        dj = 0 if j3 == j4 else (1 if j4 > j3 else -1)
        
        # Move 3 one step towards 4
        new_i = i3 + di
        new_j = j3 + dj
        
        # Clear original position and place 3 at new position
        result[i3][j3] = 0
        result[new_i][new_j] = 3
    
    return result