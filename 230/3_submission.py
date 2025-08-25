def p(g):
 for r,a in enumerate(g):
  for c,v in enumerate(a):
   if v>4>g[r-1][c]+a[c-1]:g[r-1][c-1:c+3:3]=1,2;g[r+2][c-1:c+3:3]=3,4
 return g
