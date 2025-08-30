def p(g,e=enumerate):
 for r,a in e(g):
  for c,v in e(a):
   if v>4:t,u=g[r-1][c]>4,a[c-1]>4;g[r+2*t-1][c+2*u-1]=t*2-~u
 return g