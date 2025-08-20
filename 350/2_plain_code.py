def p(grid):
    # 356風解法：各行と列で端の1の間を8で埋める
    result = [row[:] for row in grid]
    
    # 各行について処理
    for i in range(len(grid)):
        # この行で1がある位置を探す
        positions = [j for j in range(len(grid[0])) if grid[i][j] == 1]
        
        # 2個以上の1がある場合、端から端まで8で埋める（1以外の場所を）
        if len(positions) >= 2:
            min_pos = min(positions)
            max_pos = max(positions)
            for j in range(min_pos, max_pos + 1):
                if result[i][j] != 1:  # 1でない場合のみ8に変更
                    result[i][j] = 8
    
    # 各列について処理
    for j in range(len(grid[0])):
        # この列で1がある位置を探す
        positions = [i for i in range(len(grid)) if grid[i][j] == 1]
        
        # 2個以上の1がある場合、端から端まで8で埋める（1以外の場所を）
        if len(positions) >= 2:
            min_pos = min(positions)
            max_pos = max(positions)
            for i in range(min_pos, max_pos + 1):
                if result[i][j] != 1:  # 1でない場合のみ8に変更
                    result[i][j] = 8
    
    return result