# -*- coding: utf-8 -*-
def p(g):
    # 新しい解法: 以下を4回行う
    # - 全部のマスに対し(g[i][j-1]!=g[i][j]かつg[i][j]!=g[i][j+1])または(g[i][j-1]!=g[i][j]かつg[i][j]!=g[i-1][j]かつg[i][j]!=g[i][j+2]かつg[i][j]!=g[i+2][j])なら0にする
    # - 盤面全体を転置する
    
    # 4回処理を行う
    for _ in range(4):
        # 新しいグリッドを作成
        new_g = [[g[i][j] for j in range(len(g[0]))] for i in range(len(g))]
        
        # 全てのマスについて条件をチェック
        for i in range(len(g)):
            for j in range(len(g[0])):
                if g[i][j] == 0:
                    continue
                
                # 隣接する値を取得
                left = g[i][j-1] if j > 0 else 0
                right = g[i][j+1] if j < len(g[0])-1 else 0
                up = g[i-1][j] if i > 0 else 0
                down = g[i+2][j] if i+2 < len(g) else 0
                right2 = g[i][j+2] if j+2 < len(g[0]) else 0
                
                # 条件1: 左右が異なる
                condition1 = (left != g[i][j] and right != g[i][j])
                
                # 条件2: 4方向すべてが異なる
                condition2 = (left != g[i][j] and up != g[i][j] and 
                             right2 != g[i][j] and down != g[i][j])
                
                # いずれかの条件が満たされたら0にする
                if condition1 or condition2:
                    new_g[i][j] = 0
        
        # 盤面全体を転置する
        g = [[new_g[j][i] for j in range(len(new_g))] for i in range(len(new_g[0]))]
    
    return g