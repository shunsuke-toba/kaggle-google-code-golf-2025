def p(grid):
    from collections import Counter
    import copy
    
    # グリッドのコピーを作成（元のグリッドを変更しないため）
    g = copy.deepcopy(grid)
    h, w = len(g), len(g[0])
    
    # 最頻出でない色（レアな色）を見つける
    flat = sum(g, [])
    counts = Counter(flat)
    target_color = min(counts, key=counts.get)
    
    # 各色のカウンター
    color_counts = {}
    
    # 全てのマスについて複数回処理（submission codeのように）
    for k in range(9 * h * w):  # 十分な回数実行
        i, j = k // w % h, k % w
        
        if g[i][j] == target_color:
            # 周囲4マスの色を取得
            neighbors = []
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < h and 0 <= nj < w and g[ni][nj] != target_color:
                    neighbors.append(g[ni][nj])
            
            if neighbors:
                # 周囲の色の出現回数をカウント
                neighbor_counts = Counter(neighbors)
                # 最も多く出現する色を取得
                most_common_color = max(neighbor_counts, key=neighbor_counts.get)
                
                # 2回以上出現する場合
                if neighbor_counts[most_common_color] >= 2:
                    # グリッドの値を変更
                    g[i][j] = most_common_color
                    # カウンターを更新
                    color_counts[most_common_color] = color_counts.get(most_common_color, 0) + 1
    
    # 最も多くカウントされた色を返す
    if color_counts:
        result = max(color_counts, key=color_counts.get)
        return [[result]]
    else:
        return [[target_color]]