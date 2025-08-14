def p(g):
    h,w=len(g),len(g[0])
    out=[r[:] for r in g]
    for r in range(h):
        if r%3==2: continue          # 区切り行は飛ばす
        for c in range(w):
            if c%3==2: continue       # 区切り列は飛ばす
            v=0
            # 左右の隣領域が同じ非背景色なら採用
            if c>=3 and c+3<w:
                a,b=g[r][c-3],g[r][c+3]
                if a>1 and a==b: v=a
            # まだ未決&上下の隣領域が同じ非背景色なら採用
            if not v and r>=3 and r+3<h:
                a,b=g[r-3][c],g[r+3][c]
                if a>1 and a==b: v=a
            if v: out[r][c]=v
    return out