# -*- coding: utf-8 -*-
def p(g):
    for _ in range(96):
        n, m = len(g), len(g[0])
        new_g = []
        
        for i in range(n):
            row = []
            for j in range(m):
                # g[i-1][j]が4の場合、または
                # g[i-2][j-1],g[i-1][j-2],g[i-1][j],g[i][j-1]=[0,0,5,5]の場合はg[i][j]|4
                # それ以外はg[i][j]
                
                # 範囲外は0で処理
                v1 = g[i-2][j-1] if i >= 2 and j >= 1 else 0
                v2 = g[i-1][j-2] if i >= 1 and j >= 2 else 0
                v3 = g[i-1][j] if i >= 1 else 0
                v4 = g[i][j-1] if j >= 1 else 0
                
                if v3 == 4 or [v1, v2, v3, v4] == [0, 0, 5, 5]:
                    row.append(g[i][j] | 4)
                else:
                    row.append(g[i][j])
            new_g.append(row)
        
        # 90度回転
        g = [list(row) for row in zip(*new_g[::-1])]
    
    return g