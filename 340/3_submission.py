def p(g):
 for r in g[1:-1]:
  j=1
  for c in r[2:-2]:
   j+=1
   r[j]=0
   for a,b in(1,0),(-2,-1):r[a]+=c*(c==r[b]);g[a][j]+=c*(c==g[b][j])
 return g