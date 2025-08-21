def p(grid):
    x = 1

    for i in range(9, 1, -1):
        # 行を検索
        for r in range(10):
            for c in range(10):
                if c + i <= 10 and all(grid[r][c + j] == 5 for j in range(i)):
                    for j in range(i):
                        grid[r][c + j] = x
                    x = x * 4 % 7

        # 列を検索
        for r in range(10):
            for c in range(10):
                if r + i <= 10 and all(grid[r + j][c] == 5 for j in range(i)):
                    for j in range(i):
                        grid[r + j][c] = x
                    x = x * 4 % 7

    return grid
