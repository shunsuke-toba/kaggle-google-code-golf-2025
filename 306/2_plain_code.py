def p(g):
    H,W=len(g),len(g[0]);A=(H+1)//10;B=(W+1)//10
    for i in range(A):
        for j in range(B):
            P=[r[j*10:j*10+9] for r in g[i*10:i*10+9]]
            if any(map(any,P)):
                for x in range(A):
                    for y in range(B):
                        s=x*10;t=y*10
                        for u in range(9): g[s+u][t:t+9]=P[u]
                return g
    return g