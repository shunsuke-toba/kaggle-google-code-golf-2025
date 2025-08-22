def p(g):
 for r in g[1:-1]:
  for j in range(1,len(r)-1):
   c=r[j];r[j]=0
   if c==r[0]:r[1]=c
   if c==r[-1]:r[-2]=c
   if c==g[0][j]:g[1][j]=c
   if c==g[-1][j]:g[-2][j]=c
 return g
