def p(grid):
    height = len(grid)
    width = len(grid[0])
    
    # グリッドをコピー
    result = [row[:] for row in grid]
    
    # 各マスについて処理
    for r in range(height):
        for c in range(width):
            # 同じ行と同じ列のマスをすべて取得
            row_vals = result[r]
            col_vals = [result[i][c] for i in range(height)]
            
            # 行と列の値を合わせて最も多い数字を取得
            all_vals = row_vals + col_vals
            most_common = max(all_vals, key=all_vals.count)
            
            # そのマスを最も多い数字に変える
            result[r][c] = most_common
    
    return result