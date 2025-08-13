def p(g):
    n = len(g)
    h = n // 2
    # Collect ring colors from outside to inside
    rings = [g[k][k] for k in range(h)]
    out = [[0]*n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            layer = min(r, c, n-1-r, n-1-c)
            out[r][c] = rings[h-1-layer]
    return out
