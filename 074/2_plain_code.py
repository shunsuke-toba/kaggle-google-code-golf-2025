def p(grid):
    n=30
    for _ in range(9):
        for i in range(n):
            for j in range(n):
                if 31-i<n and grid[31-i][j] != 9:
                    grid[i][j] = grid[31-i][j]
                if 31-j<n and grid[i][31-j] != 9:
                    grid[i][j] = grid[i][31-j]
                if grid[j][i] != 9:
                    grid[i][j] = grid[j][i]
    return grid