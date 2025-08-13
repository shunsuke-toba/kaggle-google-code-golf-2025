def p(g):
    h, w = len(g), len(g[0])

    # 色ごとの統計
    INF = 10**9
    cnt  = [0]*10
    minr = [INF]*10
    maxr = [-1]*10
    minc = [INF]*10
    maxc = [-1]*10

    for r in range(h):
        row = g[r]
        for c in range(w):
            v = row[c]
            if v == 0:
                continue
            cnt[v] += 1
            if r < minr[v]: minr[v] = r
            if r > maxr[v]: maxr[v] = r
            if c < minc[v]: minc[v] = c
            if c > maxc[v]: maxc[v] = c

    # 最大サイズの色を選択（同数なら色番号が小さい方）
    best_color = max(range(1, 10), key=lambda x: (cnt[x], -x))
    if cnt[best_color] == 0:
        return []

    r0, r1 = minr[best_color], maxr[best_color]
    c0, c1 = minc[best_color], maxc[best_color]

    # 最小外接矩形を切り出し、該当色のみ残す
    out_h = r1 - r0 + 1
    out_w = c1 - c0 + 1
    out = [[0]*out_w for _ in range(out_h)]
    bc = best_color
    for r in range(r0, r1 + 1):
        gr = g[r]
        orow = out[r - r0]
        for c in range(c0, c1 + 1):
            if gr[c] == bc:
                orow[c - c0] = bc
    return out