def p(g):
 n=len(g)
 for s in range(1,n):
  for y in range(n-s):
   for x in range(n-s):
    if all(g[y][x+i]==g[y+s][x+i]==g[y+i][x]==g[y+i][x+s]==5 for i in range(s+1))and not sum(sum(r[x+1:x+s])for r in g[y+1:y+s]):
     for i in range(1,s):g[y+i][x+1:x+s]=[2]*(s-1)
 return g
