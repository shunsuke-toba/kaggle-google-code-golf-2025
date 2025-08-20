def p(g):
    h,w=len(g),len(g[0])
    corners=[(0,0),(0,w-1),(h-1,0),(h-1,w-1)]
    P=[(i,j,g[i][j]) for i,j in corners if g[i][j]]

    out=[[0]*w for _ in range(h)]
    if not P: return out

    INF=10**9
    mind=[[INF]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            mind[i][j]=min(max(abs(i-x),abs(j-y)) for x,y,_ in P)

    R=max(h-1,w-1)
    for r in range(0,R+1,2):
        cells={}  # (i,j) -> [(t,color),...]
        for x,y,c in P:
            sx = 1 if x==0 else -1
            sy = 1 if y==0 else -1

            I = x + sx*r
            if 0 <= I < h:
                for t in range(r+1):
                    J = y + sy*t
                    if 0 <= J < w and mind[I][J] >= r:
                        cells.setdefault((I,J),[]).append((t,c))
            J = y + sy*r
            if 0 <= J < w:
                for t in range(r+1):
                    I = x + sx*t
                    if 0 <= I < h and mind[I][J] >= r:
                        cells.setdefault((I,J),[]).append((t,c))

        for (i,j), lst in cells.items():
            best_t=None; best_c=None; ties=0
            per_color={}
            for t,c in lst:
                per_color[c]=min(per_color.get(c,INF),t)
            for c,t in per_color.items():
                if best_t is None or t<best_t:
                    best_t=t; best_c=c; ties=1
                elif t==best_t:
                    ties+=1
            if ties==1:
                out[i][j]=best_c
    return out