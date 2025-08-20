def p(g):
 for i in range(len(g[0])):
  for r,m in zip(g,(224,65,2051)):
   if m>>i%12&1:r[i]=4
 return g
