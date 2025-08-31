def p(g):
 for r in g[1:-1]:
  j=1
  for c in r[2:-2]:
   j+=1;r[j]=0
   for a in-2,1:r[a]+=c*(c==r[a//2]);g[a][j]+=c*(c==g[a//2][j])
 return g