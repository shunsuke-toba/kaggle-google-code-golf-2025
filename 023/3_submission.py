def p(j):
    h=len(j);w=len(j[0])
    S={(r,c)for r in range(h)for c in range(w)if j[r][c]==5}
    def f(S):
        if not S:return 1
        r,c=min(S)
        t={(r,c),(r,c+1),(r+1,c),(r+1,c+1)}
        if t<=S:
            S-=t
            for a,b in t:j[a][b]=8
            if f(S):return 1
            S|=t
            for a,b in t:j[a][b]=5
        t={(r,c),(r,c+1),(r,c+2)}
        if t<=S:
            S-=t
            for a,b in t:j[a][b]=2
            if f(S):return 1
            S|=t
            for a,b in t:j[a][b]=5
        t={(r,c),(r+1,c),(r+2,c)}
        if t<=S:
            S-=t
            for a,b in t:j[a][b]=2
            if f(S):return 1
            S|=t
            for a,b in t:j[a][b]=5
        return 0
    if not f(S):
        for r,c in S:j[r][c]=8
    return j
