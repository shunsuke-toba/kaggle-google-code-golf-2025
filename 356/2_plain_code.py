def p(grid):
    # 日本語コメント: 解答用のグリッドを作成（入力をコピー）
    result = [row[:] for row in grid]
    
    # 各行について処理
    for i in range(len(grid)):
        # この行で8がある位置を探す
        positions = [j for j in range(len(grid[i])) if grid[i][j] == 8]
        
        # 2個以上の8がある場合、端から端まで8で埋める
        if len(positions) >= 2:
            min_pos = min(positions)
            max_pos = max(positions)
            for j in range(min_pos, max_pos + 1):
                result[i][j] = 8
    
    # 各列について処理
    for j in range(len(grid[0])):
        # この列で8がある位置を探す
        positions = [i for i in range(len(grid)) if grid[i][j] == 8]
        
        # 2個以上の8がある場合、端から端まで8で埋める
        if len(positions) >= 2:
            min_pos = min(positions)
            max_pos = max(positions)
            for i in range(min_pos, max_pos + 1):
                result[i][j] = 8
    
    return result