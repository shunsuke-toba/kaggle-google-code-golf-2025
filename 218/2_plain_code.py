def p(grid):
    # 各行で異なる色のブロックが変わる境界列を特定
    boundary_cols = set()
    boundary_rows = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if r == 0 or grid[r-1][c] != grid[r][c]:
                boundary_rows.add(r)
            if c == 0 or grid[r][c-1] != grid[r][c]:
                boundary_cols.add(c)
    rows = sorted(boundary_rows)
    cols = sorted(boundary_cols)
    
    # 結果を構築
    result = []
    for r in rows:
        row = []
        for c in cols:
            if grid[r][c] != 0:  # 0以外の数字のみを追加
                row.append(grid[r][c])
        if len(row) > 0:
            result.append(row)
    return result