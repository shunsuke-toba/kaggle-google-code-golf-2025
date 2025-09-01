def p(g,e=enumerate):
 for r,a in e(g,-1):
  for c,v in e(a):
   if v>4:T=g[r][c]%3;u=a[c-1]>4;g[r+T][c+2*u-1]=T-~u
 return g