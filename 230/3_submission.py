def p(g,u=0,e=enumerate):
 for r,a in e(g,-1):
  for c,v in e(a):
   if v>4:T=g[r][c]%3;g[r+T][c+2*u-1]=T-~u;u^=1
 return g