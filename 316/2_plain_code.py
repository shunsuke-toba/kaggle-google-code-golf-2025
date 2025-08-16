def p(grid):
    h = len(grid)
    w = len(grid[0]) if h else 0

    # 各列を左から走査して最上の非ゼロ値を集める（最大9個）
    vals = []
    for x in range(w):
        for y in range(h):
            v = grid[y][x]
            if v:
                vals.append(v)
                break
        if len(vals) == 9:
            break

    # 足りない分は 0 で埋める
    vals += [0] * (9 - len(vals))

    # Z字に配置：1行目→、2行目←、3行目→
    return [vals[0:3], list(reversed(vals[3:6])), vals[6:9]]