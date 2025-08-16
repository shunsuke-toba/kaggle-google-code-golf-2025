# -*- coding: utf-8 -*-
def p(grid):
    import copy
    g = copy.deepcopy(grid)
    H, W = len(g), len(g[0])
    
    # 0の連結成分を見つけて、各成分が長方形かつ条件を満たすかチェック
    visited = [[False] * W for _ in range(H)]
    
    for r in range(H):
        for c in range(W):
            if g[r][c] == 0 and not visited[r][c]:
                # 連結成分を見つける
                component = []
                stack = [(r, c)]
                while stack:
                    cr, cc = stack.pop()
                    if visited[cr][cc]:
                        continue
                    visited[cr][cc] = True
                    component.append((cr, cc))
                    
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = cr + dr, cc + dc
                        if (0 <= nr < H and 0 <= nc < W and 
                            g[nr][nc] == 0 and not visited[nr][nc]):
                            stack.append((nr, nc))
                
                # この連結成分が長方形かどうかチェック（1マスも含む）
                if len(component) > 0:
                    min_r = min(pos[0] for pos in component)
                    max_r = max(pos[0] for pos in component)
                    min_c = min(pos[1] for pos in component)
                    max_c = max(pos[1] for pos in component)
                    
                    # 長方形の場合、面積が一致するはず
                    expected_area = (max_r - min_r + 1) * (max_c - min_c + 1)
                    if len(component) == expected_area:
                        # 各隅の特定の斜め隣接マスが5で、その5のマスの隣接する5のマスが2つかチェック
                        should_convert = False
                        
                        # 各隅に対応する斜め方向のみをチェック
                        diagonal_checks = [
                            (min_r, min_c, -1, -1),  # 左上の隅の左上斜め
                            (min_r, max_c, -1, 1),   # 右上の隅の右上斜め
                            (max_r, min_c, 1, -1),   # 左下の隅の左下斜め
                            (max_r, max_c, 1, 1)     # 右下の隅の右下斜め
                        ]
                        
                        for corner_r, corner_c, dr, dc in diagonal_checks:
                            nr, nc = corner_r + dr, corner_c + dc
                            if (0 <= nr < H and 0 <= nc < W and g[nr][nc] == 5):
                                # この5のマスの隣接する5のマスの数をカウント
                                adjacent_5_count = 0
                                for adr, adc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                                    anr, anc = nr + adr, nc + adc
                                    if (0 <= anr < H and 0 <= anc < W and g[anr][anc] == 5):
                                        adjacent_5_count += 1
                                
                                if adjacent_5_count == 2:
                                    should_convert = True
                                    break
                        
                        if should_convert:
                            # この長方形領域を4に変更
                            for cr, cc in component:
                                g[cr][cc] = 4
    
    return g