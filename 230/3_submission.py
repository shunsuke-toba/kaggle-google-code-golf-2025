def p(g,e=enumerate):
 for r,a in e(g,-1):
  for c,v in e(a):
   if v>4:t,u=g[r][c]>4,a[c-1]>4;g[r+2*t][c+2*u-1]=t*2-~u
 return g