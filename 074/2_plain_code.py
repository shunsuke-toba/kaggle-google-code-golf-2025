# -*- coding: utf-8 -*-
def p(grid):
    """
    32*32の90度対称な図形の左上30*30である。
    一部は9によって隠されている。9を復元せよ。
    32*32のgridで考える。
    x番目の行と31-x番目の行をその最小値で更新する。列も同様。
    最後にclipして出力。
    """
    h, w = len(grid), len(grid[0])
    
    # 32x32のグリッドに拡張（右端と下端に9を追加）
    extended = [[9] * 32 for _ in range(32)]
    for r in range(h):
        for c in range(w):
            extended[r][c] = grid[r][c]
    
    # 収束するまで繰り返す
    for _ in range(2):  # 最大2回
        changed = False
        new_result = [row[:] for row in extended]
        
        # 行の対称性：x番目の行と31-x番目の行を最小値で更新
        for r in range(32):
            mirror_r = 31 - r
            for c in range(32):
                if extended[r][c] != extended[mirror_r][c]:
                    # 最小値を適用
                    min_val = min(extended[r][c], extended[mirror_r][c])
                    if new_result[r][c] != min_val:
                        new_result[r][c] = min_val
                        changed = True
                    if new_result[mirror_r][c] != min_val:
                        new_result[mirror_r][c] = min_val
                        changed = True
    
        extended = new_result
        new_result = [row[:] for row in extended]
        
        # 対角線の対称性：r,cとc,rを最小値で更新
        for r in range(32):
            for c in range(r + 1, 32):
                if extended[r][c] != extended[c][r]:
                    # 最小値を適用
                    min_val = min(extended[r][c], extended[c][r])
                    if new_result[r][c] != min_val:
                        new_result[r][c] = min_val
                        changed = True
                    if new_result[c][r] != min_val:
                        new_result[c][r] = min_val
                        changed = True
        
        extended = new_result
        
        if not changed:
            break
    
    # 元のサイズにクリップして返す
    result = []
    for r in range(h):
        result.append(extended[r][:w])
    
    return result