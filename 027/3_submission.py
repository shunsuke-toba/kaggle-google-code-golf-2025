def p(g):
 x=[(r,c)for r in range(1,10)for c in range(9)if g[r][c]];k=min(9,10,key=lambda k:sum(g[c][k-r]<1 for r,c in x))
 for r,c in x:g[c][k-r]=g[c][k-r]or 2
 return g