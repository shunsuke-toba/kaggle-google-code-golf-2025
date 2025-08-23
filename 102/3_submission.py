def p(g):
 n=len(g);R=range
 for s in R(2,n):
  for y in R(n-s):
   for x in R(n-s):
    if all(g[y][x+i]==g[y+s][x+i]==g[y+i][x]==g[y+i][x+s]==5 for i in R(s+1))>max(max(m[x+1:x+s])for m in g[y+1:y+s]):
     for m in g[y+1:y+s]:m[x+1:x+s]=[2]*(s-1)
 return g
