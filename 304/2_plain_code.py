def p(g):
    # 最頻色（0は除外）
    cnt=[0]*10
    for r in g:
        for v in r:
            if v: cnt[v]+=1
    c=max(range(1,10), key=cnt.__getitem__)

    # 9x9を作成し、最頻色の位置に g を貼る
    out=[[0]*9 for _ in range(9)]
    for bi in range(3):
        for bj in range(3):
            if g[bi][bj]==c:
                for di in range(3):
                    for dj in range(3):
                        out[3*bi+di][3*bj+dj]=g[di][dj]
    return out