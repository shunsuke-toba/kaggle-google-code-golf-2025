def p(g):
    if not g or not g[0]: return g
    h,w=len(g),len(g[0])
    rz=[all(x==0 for x in r) for r in g]              # 全要素0の行
    cz=[all(g[i][j]==0 for i in range(h)) for j in range(w)]  # 全要素0の列
    return [[2 if rz[i] or cz[j] else g[i][j] for j in range(w)] for i in range(h)]