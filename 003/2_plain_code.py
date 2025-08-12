def p(grid):
    # 2行目と5行目を比較
    if grid[1] == grid[4]:  # 2行目と5行目が同じ場合
        # 最初の3行(0,1,2行目)を使用
        pattern_rows = grid[0:3]
    else:  # 2行目と5行目が異なる場合
        # 2~4行目(1,2,3行目)を使用
        pattern_rows = grid[2:5]
    
    # 9行の出力を生成
    result = []
    
    # まず最初の6行をそのまま追加（1を2に変換）
    for row in grid:
        new_row = []
        for cell in row:
            new_row.append(cell * 2)  # 1を2に、0を0にする
        result.append(new_row)
    
    # 次に3行を追加（パターンに基づく）
    for i in range(3):
        row = pattern_rows[i]
        new_row = []
        for cell in row:
            new_row.append(cell * 2)  # 1を2に、0を0にする
        result.append(new_row)
    
    return result