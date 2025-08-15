def p(g):
    R=range
    h,w=len(g),len(g[0])

    # 背景2色＝単純に出現数トップ2（点は少数なので安定）
    cnt=[0]*10
    for r in g:
        for v in r: cnt[v]+=1
    b1,b2=sorted(range(10), key=cnt.__getitem__, reverse=True)[:2]
    BG={b1,b2}

    # 点色の収集＆隣接投票: votes[bg][point_color]
    votes=[[0]*10 for _ in R(10)]
    pts=[]; seen=[0]*10
    for i in R(h):
        for j in R(w):
            v=g[i][j]
            if v in BG: continue
            pts.append((i,j))
            seen[v]=1
            for di in (-1,0,1):
                for dj in (-1,0,1):
                    if di or dj:
                        x=i+di; y=j+dj
                        if 0<=x<h and 0<=y<w:
                            b=g[x][y]
                            if b in BG: votes[b][v]+=1

    # 点は2色想定
    ps=[c for c in R(10) if seen[c]]
    p1,p2=ps[0],ps[1]

    # 2通りの割当を比較（総票が大きい方）。同点は色番号で安定化
    s12=votes[b1][p1]+votes[b2][p2]
    s21=votes[b1][p2]+votes[b2][p1]
    if s21>s12 or (s21==s12 and sorted((b1,b2))!=[b1,b2] and sorted((p1,p2))==[p1,p2]): 
        mp={b1:p2,b2:p1}
    else:
        mp={b1:p1,b2:p2}

    # 斜め2本を背景セルにのみ上書き
    o=[r[:] for r in g]
    for i,j in pts:
        s=i+j; d=i-j
        for r in R(h):
            c=s-r
            if 0<=c<w:
                vb=g[r][c]
                if vb in BG: o[r][c]=mp[vb]
            c=r-d
            if 0<=c<w:
                vb=g[r][c]
                if vb in BG: o[r][c]=mp[vb]
    return o