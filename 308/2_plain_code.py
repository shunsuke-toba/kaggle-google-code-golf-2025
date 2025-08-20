def p(g):
    h,w=len(g),len(g[0])
    # 背景色 = 最多出現色
    cnt=[0]*10
    for r in g:
        for v in r: cnt[v]+=1
    bg=max(range(10),key=cnt.__getitem__)

    # 色ごとの点・外接矩形
    pts=[[] for _ in range(10)]
    mi=[10**9]*10; mj=[10**9]*10
    Mi=[-10**9]*10; Mj=[-10**9]*10
    for i,row in enumerate(g):
        for j,v in enumerate(row):
            if v!=bg:
                pts[v].append((i,j))
                if i<mi[v]: mi[v]=i
                if i>Mi[v]: Mi[v]=i
                if j<mj[v]: mj[v]=j
                if j>Mj[v]: Mj[v]=j

    cols=[c for c in range(10) if c!=bg and pts[c]]

    # 一辺 s は色ごとの外接幅の最大 + 1
    s=max(max(Mi[c]-mi[c], Mj[c]-mj[c]) for c in cols)+1
    k=(s-1)//2
    # 復元（背景で初期化し、各色の点を中心基準に配置）
    out=[[bg]*s for _ in range(s)]
    for c in cols:
        cx=(mi[c]+Mi[c])//2; cy=(mj[c]+Mj[c])//2
        for i,j in pts[c]:
            out[i-cx+k][j-cy+k]=c
    return out