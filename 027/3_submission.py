def p(g):
 x=[(r,c)for r in range(10)for c in range(10)if g[r][c]];k=min((9,10),key=lambda k:sum(-1<k-r<10 and g[c][k-r]<1 for r,c in x))
 for r,c in x:
  if -1<k-r<10:g[c][k-r]=g[c][k-r]or 2
 return g
