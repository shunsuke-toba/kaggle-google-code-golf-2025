# -*- coding: utf-8 -*-

def p(grid):
    """
    問題205: 長方形内の2色のうち少ない方の色のパターンを出力する
    
    解法:
    1. 各色の二次元累積和を事前に計算して高速化
    2. 全ての長方形を全探索
    3. 長方形内で色が2種類のものを見つける
    4. 2色のうち多い方の色の個数が最多となる長方形を選択
    5. その長方形の少ない方の色のマスについて、縦横に引き伸ばしたものを出力
    """
    rows = len(grid)
    cols = len(grid[0])
    
    # グリッド内の全ての色を取得
    all_colors = set()
    for r in range(rows):
        for c in range(cols):
            all_colors.add(grid[r][c])
    
    # 各色の二次元累積和を計算
    cumsum = {}
    for color in all_colors:
        cumsum[color] = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows):
            for c in range(cols):
                cumsum[color][r + 1][c + 1] = (
                    cumsum[color][r][c + 1] + 
                    cumsum[color][r + 1][c] - 
                    cumsum[color][r][c] + 
                    (1 if grid[r][c] == color else 0)
                )
    
    def get_count(color, top, left, bottom, right):
        """長方形内の指定色の個数を累積和を使って高速計算"""
        return (cumsum[color][bottom + 1][right + 1] - 
                cumsum[color][top][right + 1] - 
                cumsum[color][bottom + 1][left] + 
                cumsum[color][top][left])
    
    best_rect = None
    max_major_count = 0
    
    # 全ての長方形を全探索
    for top in range(rows):
        for left in range(cols):
            for bottom in range(top, rows):
                for right in range(left, cols):
                    # 長方形内の各色の個数をカウント
                    color_count = {}
                    for color in all_colors:
                        count = get_count(color, top, left, bottom, right)
                        if count > 0:
                            color_count[color] = count
                    
                    # 色が2種類の場合のみ考慮
                    if len(color_count) == 2:
                        colors = list(color_count.keys())
                        count1, count2 = color_count[colors[0]], color_count[colors[1]]
                        
                        # 多い方の色の個数を取得
                        major_count = max(count1, count2)
                        
                        # 現在の最大値より多い場合、更新
                        if major_count > max_major_count:
                            max_major_count = major_count
                            # 少ない方の色を特定
                            if count1 < count2:
                                minor_color = colors[0]
                            else:
                                minor_color = colors[1]
                            
                            best_rect = (top, left, bottom, right, minor_color)
    
    # 最適な長方形が見つからない場合（エラーハンドリング）
    if best_rect is None:
        return [[]]
    
    top, left, bottom, right, minor_color = best_rect
    
    # 長方形内の多数色を特定
    major_color = None
    for r in range(top, bottom + 1):
        for c in range(left, right + 1):
            if grid[r][c] != minor_color:
                major_color = grid[r][c]
                break
        if major_color is not None:
            break
    
    # 少ない方の色のマスの位置を記録
    minor_positions = []
    for r in range(top, bottom + 1):
        for c in range(left, right + 1):
            if grid[r][c] == minor_color:
                minor_positions.append((r - top, c - left))
    
    # 出力グリッドのサイズ
    out_rows = bottom - top + 1
    out_cols = right - left + 1
    
    # 少数色がある行と列を特定
    minor_rows = set(pos[0] for pos in minor_positions)
    minor_cols = set(pos[1] for pos in minor_positions)
    
    # 出力グリッドを作成：少数色の行または列にある場合は少数色、そうでなければ多数色
    result = []
    for r in range(out_rows):
        row = []
        for c in range(out_cols):
            if r in minor_rows or c in minor_cols:
                row.append(minor_color)
            else:
                row.append(major_color)
        result.append(row)
    
    return result