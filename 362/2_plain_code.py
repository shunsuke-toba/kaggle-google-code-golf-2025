def p(grid):
    # 5の数をカウント
    count_5 = 0
    for row in range(10):
        for col in range(10):
            if grid[row][col] == 5:
                count_5 += 1
    
    a = count_5
    
    # 結果グリッドを初期化
    result = [[0 for _ in range(10)] for _ in range(10)]
    
    # range(a, 10+a)行、range(-a, 10-a)列の範囲で出力
    # -aはmod10で処理
    for i in range(a, 10 + a):
        for j in range(-a, 10 - a):
            result_i = i % 10
            result_j = j % 10
            if 0 <= result_i < 10 and 0 <= result_j < 10:
                # 元のグリッドから対応する位置の値を取得
                orig_i = (i - a) % 10
                orig_j = (j + a) % 10
                if grid[orig_i][orig_j] != 5:  # 5以外の値をコピー
                    result[result_i][result_j] = grid[orig_i][orig_j]
    
    return result