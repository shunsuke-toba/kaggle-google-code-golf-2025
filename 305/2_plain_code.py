def p(g):
    h,w=len(g),len(g[0])
    c=max(max(r) for r in g)
    if c==0: return g
    i0=j0=v0=0
    for i in range(h):
        for j in range(w):
            if g[i][j]: i0,j0,v0=i,j,g[i][j]; break
        if v0: break
    off=(v0-1-(i0+j0))%c
    return [[(i+j+off)%c+1 for j in range(w)] for i in range(h)]