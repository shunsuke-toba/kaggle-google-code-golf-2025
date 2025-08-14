def p(grid):
    n=19
    # Check for two numbers and their positions
    num_count = [0] * 10
    for j2 in range(n//2):
        for i in range(n):
            for j in [j2, n-j2-1]:
                if grid[i][j] > 0:
                    num_count[grid[i][j]] += 1
                    if num_count[grid[i][j]] == 2:
                        k = j2
                        while k <= n-j2-1:
                            grid[i][k] = grid[i][j]
                            k += 2
    for _ in range(3):
        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    grid[j][n-i-1] = grid[i][j]
    return grid