# -*- coding: utf-8 -*-
def p(g):
    # 以下の操作を2回行う
    # - 各行をみて要素の和が8より大きい行があった場合
    #   - 列の数が偶数だった場合盤面全体を右に2つシフトする(左に追加する2列は一番右の2列)
    #   - 列の数が奇数だった場合盤面全体を右に2つシフトする(左に追加する2列は一番右の3列のうち左2列)
    # - 盤面を転置する
    
    for _ in range(2):
        # 各行の和が8より大きいかチェック
        shift_needed = False
        for row in g:
            if sum(row) > 8:
                shift_needed = True
                break
        
        # シフトが必要な場合
        if shift_needed:
            cols = len(g[0])
            new_g = []
            for row in g:
                if cols % 2 == 0:
                    # 列の数が偶数：右に2つシフト（左に追加する2列は一番右の2列）
                    new_row = row[-2:] + row[:-2]
                else:
                    # 列の数が奇数：右に2つシフト（左に追加する2列は一番右の3列のうち左2列）
                    new_row = row[-3:-1] + row[:-3] + row[-1:]
                new_g.append(new_row)
            g = new_g
        
        # 盤面を転置
        g = [[g[j][i] for j in range(len(g))] for i in range(len(g[0]))]
    
    return g