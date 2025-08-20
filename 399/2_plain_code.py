def p(grid):
    # 色付きマス（0以外）の個数を数える
    colored_count = sum(map(bool, sum(grid, [])))
    
    # 4で割って塗る個数を決める
    paint_count = colored_count // 4
    
    # 3×3の出力グリッドを初期化
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    # x座標とy座標の和が偶数のマスのリスト（チェスボード模様）
    even_positions = []
    for i in range(3):
        for j in range(3):
            if (i + j) % 2 == 0:
                even_positions.append((i, j))
    
    # paint_count個だけ1で塗る
    for k in range(min(paint_count, len(even_positions))):
        i, j = even_positions[k]
        result[i][j] = 1
    
    return result