def p(grid):
    height = len(grid)
    width = len(grid[0])
    
    result = [row[:] for row in grid]
    
    # 各行について処理
    for r in range(height):
        non_zero_count = sum(1 for val in grid[r] if val != 0)
        if non_zero_count >= 2:
            a = non_zero_count
            
            # 左から右に見る
            for c in range(width):
                if c >= a and result[r][c - a] != 0:
                    result[r][c] = result[r][c - a]
            
            # 右から左に見る
            for c in range(width - 1, -1, -1):
                if c + a < width and result[r][c + a] != 0:
                    result[r][c] = result[r][c + a]
    
    # 各列について処理
    for c in range(width):
        column = [grid[r][c] for r in range(height)]
        non_zero_count = sum(1 for val in column if val != 0)
        if non_zero_count >= 2:
            a = non_zero_count
            
            # 上から下に見る
            for r in range(height):
                if r >= a and result[r - a][c] != 0:
                    result[r][c] = result[r - a][c]
            
            # 下から上に見る
            for r in range(height - 1, -1, -1):
                if r + a < height and result[r + a][c] != 0:
                    result[r][c] = result[r + a][c]
    
    return result