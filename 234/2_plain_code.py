# -*- coding: utf-8 -*-
# 0が上下または左右に隣接している数字について、その数字から成る長方形が
# もう片方の長方形に接するまで移動している

def p(grid):
    # 入力をコピー
    g = [row[:] for row in grid]
    
    # 4回繰り返し
    for _ in range(4):
        # 新しいグリッドを構築
        new_g = []
        zero_rows = []
        
        # 今までの行で出てきた色の種類数をカウント
        all_colors = set()
        
        for r in g:
            # 現在の行の0以外の色を追加
            row_colors = set(x for x in r if x != 0)
            all_colors.update(row_colors)
            
            # 今までの行で出てきた色が2色かつsum(map(bool,r))==1なら削除
            if len(all_colors) == 2 and sum(map(bool, r)) == 1:
                zero_rows.append([0] * len(r))
            else:
                new_g.append(r[:])
        
        # 削除した分だけ末尾に0で構成された行を追加
        g = new_g + zero_rows
        
        # [*map(list,zip(*a[::-1]))]で回転（90度時計回り）
        g = [*map(list, zip(*g[::-1]))]
    
    return g