def p(grid):
    # 3つの3x3ブロックに分割されたグリッドを処理
    # 左のブロック（0-2列）を時計回りに90度回転して中央のブロック（4-6列）にコピー
    # 中央のブロック（4-6列）を時計回りに90度回転して右のブロック（8-10列）にコピー
    
    rows = len(grid)
    cols = len(grid[0])
    
    # 左のブロック（0-2列）を時計回りに90度回転して中央のブロック（4-6列）に
    for r in range(rows):
        for c in range(3):
            # 時計回りに90度回転: (r, c) -> (c, 2-r)
            new_r = c
            new_c = 2 - r
            grid[new_r][4 + new_c] = grid[r][c]
    
    # 中央のブロック（4-6列）を時計回りに90度回転して右のブロック（8-10列）に
    for r in range(rows):
        for c in range(3):
            # 時計回りに90度回転: (r, c) -> (c, 2-r)
            new_r = c
            new_c = 2 - r
            grid[new_r][8 + new_c] = grid[r][4 + c]
    
    return grid