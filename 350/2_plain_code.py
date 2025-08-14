def p(grid):
    # Get grid dimensions
    rows = len(grid)
    cols = len(grid[0])
    
    # Direction vectors: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Search all cells
    for r in range(rows):
        for c in range(cols):
            # If current cell is 1
            if grid[r][c] == 1:
                # Search in each direction
                for dr, dc in directions:
                    # Move one step from current position
                    nr, nc = r + dr, c + dc
                    path = []  # Record cells on the path
                    
                    # Continue until hitting boundary or 1
                    while 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == 1:
                            # If hit 1, change all cells on path to 8
                            for pr, pc in path:
                                grid[pr][pc] = 8
                            break
                        else:
                            # If not 1, add to path and continue
                            path.append((nr, nc))
                        
                        # Move to next position
                        nr += dr
                        nc += dc
    
    return grid