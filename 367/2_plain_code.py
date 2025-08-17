# -*- coding: utf-8 -*-
def p(grid):
    import copy
    g = copy.deepcopy(grid)
    H, W = len(g), len(g[0])
    
    # 1. 全ての5のマスで隣接する4マスが時計回りに(5,5,0,0)のパターンを見つける
    # そのマスについて5で挟まれた斜めのマスを4に変える
    for r in range(H):
        for c in range(W):
            if g[r][c] == 5:
                # 隣接する4マス（上、右、下、左）を時計回りでチェック
                directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 上、右、下、左
                neighbors = []
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < H and 0 <= nc < W:
                        neighbors.append(g[nr][nc])
                    else:
                        neighbors.append(-1)  # 境界外
                
                # 時計回りに(5,5,0,0)のパターンを探す
                # 各パターンと対応する斜めの方向
                patterns_and_diagonals = [
                    ([5, 5, 0, 0], -1, 1),   # 上と右が5、下と左が0 → 右上斜め
                    ([5, 0, 0, 5], -1, -1),  # 右と下が5、左と上が0 → 左上斜め  
                    ([0, 0, 5, 5], 1, -1),   # 下と左が5、上と右が0 → 左下斜め
                    ([0, 5, 5, 0], 1, 1)     # 左と上が5、右と下が0 → 右下斜め
                ]
                
                for pattern, dr, dc in patterns_and_diagonals:
                    if neighbors == pattern:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < H and 0 <= nc < W:
                            g[nr][nc] = 4
    
    # 2. 4に隣接している0のマスを4に変えることを99回繰り返す
    for iteration in range(99):
        changed = False
        new_g = copy.deepcopy(g)
        
        for r in range(H):
            for c in range(W):
                if g[r][c] == 0:
                    # 隣接に4があるかチェック
                    has_4_neighbor = False
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < H and 0 <= nc < W and g[nr][nc] == 4:
                            has_4_neighbor = True
                            break
                    
                    if has_4_neighbor:
                        new_g[r][c] = 4
                        changed = True
        
        g = new_g
        if not changed:
            break
    
    return g