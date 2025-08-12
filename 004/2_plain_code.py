def p(grid):
    rows = len(grid)
    cols = len(grid[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # 各色の図形を処理
    for color in range(1, 10):
        # この色の全てのセルを取得
        colored_cells = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == color:
                    colored_cells.append((r, c))
        
        if not colored_cells:
            continue
        
        # 底部（最下行）の水平線を見つける
        bottom_row = max(pos[0] for pos in colored_cells)
        bottom_cells = [pos for pos in colored_cells if pos[0] == bottom_row]
        
        if not bottom_cells:
            continue
        
        # 底部の右端を特定
        right_edge_col = max(pos[1] for pos in bottom_cells)
        
        # 固定する部分：底部 + 右端から上に伸びる垂直線
        fixed_cells = set(bottom_cells)  # 底部
        
        # 右端から上に伸びる垂直線を追加
        for r in range(bottom_row):
            if (r, right_edge_col) in colored_cells:
                fixed_cells.add((r, right_edge_col))
        
        # 残りのセルを右に1つ移動
        for r, c in colored_cells:
            if (r, c) in fixed_cells:
                # 固定部分はそのまま
                result[r][c] = color
            else:
                # 右に1つ移動（境界チェック）
                if c + 1 < cols:
                    result[r][c + 1] = color
    
    return result