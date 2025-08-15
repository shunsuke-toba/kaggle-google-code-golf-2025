def p(g):
    # グリッドのサイズを取得
    H=10
    
    # 結果用のグリッドを作成（元のグリッドをコピー）
    result = [row[:] for row in g]
    
    # 全てのセルを調べて0,1以外の色を探す
    for i in range(H):
        for j in range(H):
            if g[i][j] > 1:  # 0,1以外の色
                color = g[i][j]
                
                # その周囲5*5マスの0を塗る
                for di in range(-2, 3):  # -2, -1, 0, 1, 2
                    for dj in range(-2, 3):  # -2, -1, 0, 1, 2
                        ni, nj = i + di, j + dj
                        if 0 <= ni < H and 0 <= nj < H and g[ni][nj] == 0:
                            result[ni][nj] = color
                
                # 相対的に(-2,-2)のマスが1ならもう一段上も塗る
                if i-2 >= 0 and j-2 >= 0 and g[i-2][j-2] == 1:
                    # もう一段上の行の0を塗る
                    if i-3 >= 0:
                        for dj in range(-2, 3):
                            nj = j + dj
                            if 0 <= nj < H and g[i-3][nj] == 0:
                                result[i-3][nj] = color
    
    return result