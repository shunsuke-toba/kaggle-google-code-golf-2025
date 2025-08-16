def p(grid):
    height = len(grid)
    width = len(grid[0])
    
    # 結果グリッドを作成（元の内容をコピー）
    result = [row[:] for row in grid]
    
    # 3x3の0を含まない正方形領域を探す
    for start_row in range(height - 2):
        for start_col in range(width - 2):
            # 3x3領域をチェック
            has_zero = False
            for r in range(start_row, start_row + 3):
                for c in range(start_col, start_col + 3):
                    if grid[r][c] == 0:
                        has_zero = True
                        break
                if has_zero:
                    break
            
            if not has_zero:
                # 3x3の中心を基準にして90度回転対称になるように拡張
                center_row = start_row + 1
                center_col = start_col + 1
                
                # 盤面全体の各点について90度回転を適用
                for r in range(height):
                    for c in range(width):
                        value = grid[r][c]
                        if value == 0:
                            continue
                        # 相対座標
                        rel_r = r - center_row
                        rel_c = c - center_col
                        
                        # 90度回転: (rel_r,rel_c) -> (-rel_c,rel_r)
                        new_r1 = center_row + (-rel_c)
                        new_c1 = center_col + rel_r
                        if 0 <= new_r1 < height and 0 <= new_c1 < width:
                            result[new_r1][new_c1] = value
                        
                        # 180度回転: (rel_r,rel_c) -> (-rel_r,-rel_c)
                        new_r2 = center_row + (-rel_r)
                        new_c2 = center_col + (-rel_c)
                        if 0 <= new_r2 < height and 0 <= new_c2 < width:
                            result[new_r2][new_c2] = value
                        
                        # 270度回転: (rel_r,rel_c) -> (rel_c,-rel_r)
                        new_r3 = center_row + rel_c
                        new_c3 = center_col + (-rel_r)
                        if 0 <= new_r3 < height and 0 <= new_c3 < width:
                            result[new_r3][new_c3] = value
                
                return result
    
    # 3x3が見つからない場合、2x2の0を含まない正方形領域を探す
    for start_row in range(height - 1):
        for start_col in range(width - 1):
            # 2x2領域をチェック
            has_zero = False
            for r in range(start_row, start_row + 2):
                for c in range(start_col, start_col + 2):
                    if grid[r][c] == 0:
                        has_zero = True
                        break
                if has_zero:
                    break
            
            if not has_zero:
                # 2x2の中心を基準にして90度回転対称になるように拡張
                center_row = start_row + 0.5
                center_col = start_col + 0.5
                
                # 結果グリッドを作成（元の内容をコピー）
                result = [row[:] for row in grid]
                
                # 盤面全体の各点について90度回転を適用
                for r in range(height):
                    for c in range(width):
                        value = grid[r][c]
                        if value == 0:
                            continue
                        # 相対座標
                        rel_r = r - center_row
                        rel_c = c - center_col
                        
                        # 90度回転
                        new_r1 = center_row + (-rel_c)
                        new_c1 = center_col + rel_r
                        if 0 <= new_r1 < height and 0 <= new_c1 < width:
                            result[int(new_r1)][int(new_c1)] = value
                        
                        # 180度回転
                        new_r2 = center_row + (-rel_r)
                        new_c2 = center_col + (-rel_c)
                        if 0 <= new_r2 < height and 0 <= new_c2 < width:
                            result[int(new_r2)][int(new_c2)] = value
                        
                        # 270度回転
                        new_r3 = center_row + rel_c
                        new_c3 = center_col + (-rel_r)
                        if 0 <= new_r3 < height and 0 <= new_c3 < width:
                            result[int(new_r3)][int(new_c3)] = value
                
                return result
    
    # どちらも見つからない場合、元のグリッドを返す
    return grid