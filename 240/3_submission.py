def p(g):
 c=[0]*10
 for d in range(9):
  for r in g:
   for v in r[d],r[~d]:
    c[v]+=v>0
    if c[v]>1:r[d:-d or 19:2]=[v]*(10-d)
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v:g[j][~i]=g[~i][~j]=g[~j][i]=v
 return g
