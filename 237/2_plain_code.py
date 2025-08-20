def p(grid):
    result = [row[:] for row in grid]
    H = len(result)
    W = len(result[0])
    
    for _ in range(max(H, W)):
        for i in range(H):
            for j in range(W):
                if result[i][j] != 0 and j + 1 < W and result[i][j + 1] == 0:
                    result[i][j + 1] = result[i][j]
    
    for _ in range(max(H, W)):
        for i in range(H):
            for j in range(W):
                if (result[i][j] != 0 and 
                    (j == W - 1 or result[i][j + 1] == 0) and
                    i + 1 < H and result[i + 1][j] == 0):
                    result[i + 1][j] = result[i][j]
    
    return result