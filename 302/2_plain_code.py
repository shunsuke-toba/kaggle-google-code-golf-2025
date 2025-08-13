def p(g):
    h=len(g); w=len(g[0]) if g else 0
    a=[r[:] for r in g]
    for s,col in ((3,6),(4,7),(5,8)):
        f=0
        for i in range(h-s+1):
            if f: break
            for j in range(w-s+1):
                ok=1
                # 上下辺
                for x in range(j,j+s):
                    if g[i][x]!=5 or g[i+s-1][x]!=5: ok=0; break
                if not ok: continue
                # 左右辺
                for y in range(i,i+s):
                    if g[y][j]!=5 or g[y][j+s-1]!=5: ok=0; break
                if not ok: continue
                # 内側を塗る
                for y in range(i+1,i+s-1):
                    for x in range(j+1,j+s-1):
                        a[y][x]=col
                f=1; break
    return a