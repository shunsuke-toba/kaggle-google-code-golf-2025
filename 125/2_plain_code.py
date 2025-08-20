def p(g):
    h, w = len(g), len(g[0])
    
    result = [row[:] for row in g]
    
    # 8のマスを全部4にする
    for i in range(h):
        for j in range(w):
            if result[i][j] == 8:
                result[i][j] = 4
    
    # g[0][0]を8にする
    result[0][0] = 8
    
    # 全部のマスをみて変換処理
    changed = True
    while changed:
        changed = False
        new_result = [row[:] for row in result]
        
        for i in range(h):
            for j in range(w):
                # 4,6のマスでないかつ周囲8マスに6のマスがあるなら3にする
                if result[i][j] not in [4, 6]:
                    has_pink_neighbor = False
                    for di in [-1, 0, 1]:
                        for dj in [-1, 0, 1]:
                            if di == 0 and dj == 0:
                                continue
                            ni, nj = i + di, j + dj
                            if 0 <= ni < h and 0 <= nj < w and result[ni][nj] == 6:
                                has_pink_neighbor = True
                                break
                        if has_pink_neighbor:
                            break
                    
                    if has_pink_neighbor and result[i][j] != 3:
                        new_result[i][j] = 3
                        changed = True
                
                # 3,6のマスでないかつ周囲8マスに8のマスがあるなら8にする
                if result[i][j] not in [3, 6]:
                    has_eight_neighbor = False
                    for di in [-1, 0, 1]:
                        for dj in [-1, 0, 1]:
                            if di == 0 and dj == 0:
                                continue
                            ni, nj = i + di, j + dj
                            if 0 <= ni < h and 0 <= nj < w and result[ni][nj] == 8:
                                has_eight_neighbor = True
                                break
                        if has_eight_neighbor:
                            break
                    
                    if has_eight_neighbor and result[i][j] != 8:
                        new_result[i][j] = 8
                        changed = True
        
        result = new_result
    
    return result