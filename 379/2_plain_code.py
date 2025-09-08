def p(g):
    for _ in range(4):
        # 元から存在する赤セルの位置を記録
        red_positions = []
        for row_idx in range(len(g)):
            for col_idx in range(len(g[row_idx])):
                if g[row_idx][col_idx] == 2:
                    red_positions.append((row_idx, col_idx))
        
        # 記録された赤セルから処理
        for row_idx, col_idx in red_positions:
            # 2のマスの1つ右が0かチェック
            if col_idx + 1 < len(g[row_idx]) and g[row_idx][col_idx + 1] == 0:
                # 右方向に8を探す
                for j in range(col_idx + 1, len(g[row_idx])):
                    if g[row_idx][j] == 8:
                        # col_idx から j までを赤(2)で塗りつぶす
                        for k in range(col_idx, j + 1):
                            g[row_idx][k] = 2
                        
                        # 水色セル(row_idx, j)の周囲8マスを水色(8)にする
                        for di in range(-1, 2):
                            for dj in range(-1, 2):
                                if di == 0 and dj == 0:
                                    continue  # 中心は除く
                                ni, nj = row_idx + di, j + dj
                                if 0 <= ni < len(g) and 0 <= nj < len(g[0]):
                                    g[ni][nj] = 8
                        break  # この赤セルからは最初の水色セルのみ処理
        
        # 90度回転
        g = [list(row) for row in zip(*g[::-1])]
    
    return g