def p(grid):
    N = len(grid)
    M = len(grid[0])
    d = 1, -1, -1, 1, 1
    for r in range(N - 1):
        for c in range(M - 1):
            # Check if the 2x2 square has all different numbers
            if (grid[r][c] != grid[r][c + 1] and
                grid[r][c] != grid[r + 1][c] and
                grid[r][c] != grid[r + 1][c + 1]):
                center_r, center_c = r+0.7, c+0.7
                for dir in range(4):
                    nr = int(center_r + d[dir]*0.5)
                    nc = int(center_c + d[dir + 1]*0.5)
                    for x in range(2):
                        for y in range(2):
                            nnr = int(center_r - d[dir]*(1.5 + x))
                            nnc = int(center_c - d[dir + 1]*(1.5 + y))
                            if 0 <= nnr < N and 0 <= nnc < M:
                                grid[nnr][nnc] = grid[nr][nc]
                return grid