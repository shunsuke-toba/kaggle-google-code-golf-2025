def p(grid):
    height = len(grid)
    width = len(grid[0])
    
    # 行ベース: 各行の中央値で埋める
    A = []
    for r in range(height):
        row_sorted = sorted(grid[r])
        median = row_sorted[width//2]
        A.append([median] * width)
    
    # 列ベース: 各列の中央値で埋める  
    B = [[0] * width for _ in range(height)]
    for c in range(width):
        col = [grid[r][c] for r in range(height)]
        col_sorted = sorted(col)
        median = col_sorted[height//2]
        for r in range(height):
            B[r][c] = median
    
    # Aの左上と右下が一致しているならBを出力、そうでないならAを出力
    if A[0][0] == A[height-1][width-1]:
        return B
    else:
        return A