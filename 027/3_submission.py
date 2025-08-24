def p(g):
 x=[(r,c)for r in range(1,10)for c in range(9)if g[r][c]];k=9+(sum(g[c][10-r]-g[c][9-r]for r,c in x)>0)
 for r,c in x:g[c][k-r]=g[c][k-r]or 2
 return g
