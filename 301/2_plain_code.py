def p(g):
    if not g or not g[0]:
        return g
    h, w = len(g), len(g[0])

    # 各色の長さ（出現数）をカウント
    cnt = [0]*10
    for r in g:
        for v in r:
            if v: cnt[v] += 1

    # 出現した色だけ取り出し、(長さ, 色) を長さ昇順でソート
    lines = [(cnt[c], c) for c in range(1, 10) if cnt[c] > 0]
    lines.sort()  # 長さが同じ場合は色番号の小さい順になる

    k = len(lines)
    out = [[0]*w for _ in range(h)]

    # 下から順に長いものを配置（右詰め）
    for i, (L, c) in enumerate(lines):
        r = h - k + i
        start = w - L
        if start < 0:  # 念のため幅超過の安全策
            start = 0
            L = w
        for j in range(start, start + L):
            out[r][j] = c
    return out